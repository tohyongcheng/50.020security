import argparse
import string
import md5
import itertools
import sys

def brute(infile,dictfile,outfile):
    fin  = open(infile)       # by default, read mode
    din = open(dictfile)
    fout = open(outfile,'w')  # write mode
    hashed_passwords = fin.read().split("\n")

    words = din.read().split("\n")
    words_4 = []
    for word in words:
        if len(word) <= 4:
            words_4.append(word)

    decrypted = []
    for h in hashed_passwords:
        found = False
        for word in words_4:
            if md5.new(word).hexdigest() == h:
                decrypted.append(word)
                found = True
                break

        if not found:
            permutate(h,decrypted)

    print decrypted

    for d in decrypted:
        fout.write(d+"\n")


def permutate(h,decrypted):
    string = "abcdefghijklmnopqrstuvwxyz"
    for i in xrange(26):
        for j in xrange(26):
            for x in xrange(26):
                for y in xrange(26):
                    word = string[i]+string[j]+string[x]+string[y]
                    e = md5.new(word).hexdigest()
                    if e == h:
                        decrypted.append(word)





if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Brute force.')
    parser.add_argument('-i', dest='infile',help='Input file')
    parser.add_argument('-d', dest='dictfile',help='Dictionary file')
    parser.add_argument('-o', dest='outfile',help='Output file')

    args=parser.parse_args()
    infile=args.infile
    dictfile=args.dictfile
    outfile=args.outfile

    if infile==None or outfile==None or dictfile==None:
        print 'Missing infile, outfile, or dictfile'
        printusage();
        sys.exit(1)

    print 'Reading from: ',infile
    print 'Dictionary from: ',dictfile
    print 'Writing to: ',outfile

    brute(infile,dictfile,outfile)
