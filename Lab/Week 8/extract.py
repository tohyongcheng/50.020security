import argparse
import binascii
import operator
from present import *

def getInfo(headerfile):
    f = open(headerfile, 'rb')
    plain = f.read()

    return plain


def analyse(infile):
    f = open(infile, 'rb')
    plain = f.read(8)
    d = dict()
    while plain != "":
        if plain in d:
            d[plain] += 1
        else:
            d[plain] = 0
        plain = f.read(8)

    s = sorted(d.items(), key=operator.itemgetter(1))
    s.reverse()
    f.close()
    return s[0][0], s[0][1]



def extract(infile,outfile,headerfile):
    white, count = analyse(infile)
    print white, count

    f = open(infile, 'rb')
    o = open(outfile, 'w')
    out = []

    h = getInfo(headerfile)

    len_h = len(h)

    try:
        plain = f.read(len_h)
        plain = f.read(8)
        while plain != "":
            if plain == white:
                out.append("00000000")
            else:
                out.append("11111111")
            plain = f.read(8)

    finally:
        f.close()

    out = "".join(out)
    out = h + "\n" + out

    o.write(out)
    o.close()

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Extract PBM pattern.')
    parser.add_argument('-i', dest='infile',help='input file, PBM encrypted format')
    parser.add_argument('-o', dest='outfile',help='output PBM file')
    parser.add_argument('-hh', dest='headerfile',help='known header file')

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    headerfile=args.headerfile

    print 'Reading from: ',infile
    print 'Reading header file from: ',headerfile
    print 'Writing to: ',outfile

    success=extract(infile,outfile,headerfile)


