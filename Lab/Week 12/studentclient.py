import ssl, socket, pprint

server="localhost"
port=10023

buffsize = 1024*16

# bind to localhost and port
HOST = ("",10023)
PORT = 10023

# create socket.socket() object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sslsocket = ssl.wrap_socket(s, ca_certs="ca.crt",cert_reqs=ssl.CERT_REQUIRED)

# FOR LATTER PART: wrap socket with ssl
s = sslsocket
# connection requires certificate and specify CA certificate location
s.connect((server,port))

# connect to server and port using ssl
pass
# Check certificate from server
pass
# Read message from server and reply

while True:
  message = s.recv(buffsize)
  print message
  if len(message) > 0 and message[-1] == "%":
    print "Exit"
    break
  if len(message) > 0 and message == "<SHARED KEY>":
    f = open("message",'w')
    message = s.recv(buffsize)
    print message
    # message = message[:message.find('%')]
    print "Shared Key: ", message
    f.write(message)
    f.close()
    break
  if len(message) > 0 and message == "<SERVER - CLIENT KEY>":
    f = open("server_client",'w')
    message = s.recv(buffsize)
    print message
    message = message[:message.find('%')]
    print "Server Client Key: ", message
    f.write(message)
    f.close()
    break
  send_msg = ""
  while send_msg == "":
    send_msg = raw_input()

  s.send(send_msg)


# close ssl connection

