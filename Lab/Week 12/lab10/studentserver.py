import socket,ssl
import md5
import random
import base64
import time, datetime
import ecb
import sys

buffsize = 1024*16

# create socket object to bind
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind to localhost and port
HOST = ("localhost",10023)
PORT = 10023
try:
    s.bind(HOST)
except socket.error as msg:
    print "Bind failed..."
    sys.exit()

# listen to port
s.listen(PORT)

# create new account
def create_account(connstream):
    username = ""
    while username == "":
        connstream.sendall('enter your username')
        username = connstream.recv(buffsize)
    passwd = ""
    while passwd == "":
        connstream.sendall('enter your password')
        passwd = connstream.recv(buffsize)
    passwd2 = ""
    while passwd2 == "":
        connstream.sendall('enter your password again')
        passwd2 = connstream.recv(buffsize)

    f = open('passwd','r')
    for line in f.readlines():
        if line != "\n":
            line = line.strip()
            stored_username, stored_password, stored_key = line.split(" ")
            if stored_username == username:
                connstream.sendall('username exists!%')
                f.close()
                return
    f.close()

    f = open('passwd','a')
    if passwd == passwd2:
        hashed_pw = (md5.new(passwd)).hexdigest()
        shared_key = requestKey(connstream)
        packed_shared_key = base64.b64encode(str(shared_key))
        connstream.sendall("<SERVER - CLIENT KEY>")
        connstream.sendall(packed_shared_key)
        f.write("%s %s %s" %(username, hashed_pw, shared_key))
        f.write("\n")
        connstream.sendall("%")
        print "Account created"
    else:
        connstream.sendall("passwords do not match")
    f.close()
    return

def step2(connstream):
    Kab = requestKey(connstream)

    username = ""
    while username == "":
        connstream.sendall('enter your username')
        username = connstream.recv(buffsize)
    passwd = ""
    while passwd == "":
        connstream.sendall('enter your password')
        passwd = connstream.recv(buffsize)

    hashed_p = (md5.new(passwd)).hexdigest()
    found_username = False
    f = open('passwd','r')
    for line in f.readlines():
        if line != "\n":
            line = line.strip()
            u, p, s = line.split(" ")
            if username == u and p == hashed_p:
                found_username = True
                f.close()
                break
    f.close()

    client_username = u
    Kas = int(s)
    print Kas

    if found_username == False:
        connstream.sendall('username/password combination does not exist')
        connstream.sendall('%')
        return

    destination_username = ""
    while destination_username == "":
        connstream.sendall('enter your destination username')
        destination_username = connstream.recv(buffsize)

    found_username = False
    f = open('passwd','r')
    for line in f.readlines():
        if line != "\n":
            line = line.strip()
            u, p, s = line.split(" ")
            if destination_username == u:
                found_username = True
                break
    f.close()

    if found_username == False:
        connstream.sendall('destination username does not exist')
        connstream.sendall('%')
        return

    destination_username = u
    Kbs = int(s)
    print Kbs
    # found username

    current_timestamp = time.time()
    lifetime = 5000

    #encrypt inner
    inner = str(current_timestamp)+"$$"+str(lifetime)+"$$"+str(Kab)+"$$"+str(client_username)
    f = open('inner','w')
    f.write(inner)
    f.close()
    ecb.ecb("inner","inner_e",Kbs,'e')

    f = open('inner_e','r')
    inner_e = base64.b64encode(f.read())
    f.close()

    #encrypt_outer
    new_timestamp = time.time()
    outer = str(new_timestamp)+"$$"+str(lifetime)+"$$"+str(Kab)+"$$"+str(destination_username)+"$$"+str(inner_e)
    f = open('outer','w')
    f.write(outer)
    f.close()
    ecb.ecb("outer","outer_e",Kas,'e')

    f = open('outer_e','r')
    outer_e = base64.b64encode(f.read())
    f.close()

    connstream.sendall("<SHARED KEY>")
    connstream.sendall(outer_e)
    connstream.sendall("%")

    return







# generate shared key request
def requestKey(connstream):
    key = "".join([str(random.randint(0,1)) for b in range(80)])
    key = int(key,2)
    return key

# if client enter something, then do something here
def do_something(connstream, data):
    pass

# prompt menu, read client reply, etc
# if valid reply from client, then call do_something()
def deal_with_client(connstream):
    s = "0) Exit \n1) Create user account \n2) Request Keys.\n"
    connstream.sendall(s)
    r = connstream.recv(buffsize)
    print r
    if r == "0":
        connstream.sendall("%")
    elif r == "1":
        # create user account
        create_account(connstream)
    elif r == "2":
        # create keys and sendall to users
        step2(connstream)
    # connstream.close()


def square_multiply(m,k,n):
    res = 1
    for i in bin(k)[2:]:
        res = res * res % n
        if i == '1':
            res = res * m % n
    return res


# infinite loop to accept connection and deal with client
while True:
    # accept connection
    connection,address = s.accept()
    conn = ssl.wrap_socket(connection,
        server_side=True,
        certfile="SignedChin Jia Kai Samuel ._req_66.pem",
        keyfile="private.pem"
        )

    # FOR LATTER PART:
    # - wrap socket in ssl
    # - specify server side to True, location for server certificate,
    #   and location to private key
    # pass

    # call deal_with_client()
    deal_with_client(conn)

