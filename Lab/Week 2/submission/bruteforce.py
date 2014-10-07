# Import libraries
import sys
import argparse

def decrypt(filein,fileout):
  # open file handles to both files
  fin  = open(filein)       # by default, read mode
  fout = open(fileout,'w')  # write mode
  c    = fin.read()         # read in file into c
  string = ""
  for shift in xrange(256):
    string += ("For shift %d" % (shift) )
    string += "\n-------------------------\n"

    for i in xrange(100):
      string += chr((ord(c[i]) - shift)%256)

    string += "\n-------------------------\n"

  # and write to fileout
  fout.write(string)

# our main function
if __name__=="__main__":
  # set up the argument parser
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', dest='filein', help='input file')
  parser.add_argument('-o', dest='fileout', help='output file')

  # parse our arguments
  args = parser.parse_args()
  filein=args.filein
  fileout=args.fileout

  decrypt(filein, fileout)

  # all done


