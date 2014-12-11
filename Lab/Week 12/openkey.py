import ecb
import base64

def openkeyinner(fname,keyfname):
    keyfile = open(keyfname)
    messagefile = open(fname)

    key = int(base64.b64decode(keyfile.read()))
    message = base64.b64decode(messagefile.read())

    f = open('temp','w')
    f.write(message)
    f.close()
    ecb.ecb("temp","temp_d",key,'d')

    f = open('temp_d')
    r = f.read()

    ts, l, kab, a = r.split("$$")

    return ts,l,kab,a

def openkeyouter(fname,keyfname):
    keyfile = open(keyfname)
    messagefile = open(fname)
    key = int(base64.b64decode(keyfile.read()))
    message = base64.b64decode(messagefile.read())

    f = open('temp','w')
    f.write(message)
    f.close()
    ecb.ecb("temp","temp_d",key,'d')

    f = open('temp_d')
    r = f.read()
    print r
    ts, l, kab, b, msgforb = r.split("$$")

    return (ts,l,kab,b),msgforb

if __name__=="__main__":

    fname = "message"
    keyfname = "Kas"

    mykey,othermsg=openkeyouter(fname,keyfname)
    print '========================================'
    print 'Timestamp in second: ',mykey[0]
    print 'Lifetime in second: ',mykey[1]
    print 'Shared key with B in PEM: ',mykey[2]
    print 'B username: ',mykey[3]
    f = open("othermsg.txt",'w')
    f.write(othermsg)
    f.close()

    # parse the inner message from A
    keyfname = "Kbs"
    otherkey=openkeyinner('othermsg.txt',keyfname)
    print '========================================'
    print 'Timestamp in second: ',otherkey[0]
    print 'Lifetime in second: ',otherkey[1]
    print 'Shared key with A in PEM: ',otherkey[2]
    print 'A username: ',otherkey[3]

