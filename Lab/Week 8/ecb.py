from present import *
import argparse
import binascii

nokeybits=80
blocksize=64


def ecb(infile,outfile,key,mode):
    f = open(infile, 'rb')
    o = open(outfile, 'w')
    inputs = []
    out = []

    k = open(key, 'rb')
    key = k.read(nokeybits/8)
    key = int(key,2)
    print "Key is: %064b" % key
    k.close()

    try:
        plain = f.read(8)
        
        while plain != "":
            block = ""
            for ch in plain:
                block += format(ord(ch),"08b")
            block = int(block,2)

            if mode == "e":
                c = present(block,key)
            elif mode == "d":
                c = present_inv(block,key)
            out.append(binascii.unhexlify('%016x' % c))
            plain = f.read(8)

    finally:
        f.close()

    out = "".join(out)
    print out
    
    o.write("".join(out))
    o.close()

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Block cipher using ECB mode.')
    parser.add_argument('-i', dest='infile',help='input file')
    parser.add_argument('-o', dest='outfile',help='output file')
    parser.add_argument('-k', dest='keyfile',help='key file')
    parser.add_argument('-m', dest='mode',help='mode')

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    keyfile=args.keyfile
    mode=args.mode
    ecb(infile,outfile,keyfile,mode)



