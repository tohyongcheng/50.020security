# Import libraries
import sys
import argparse

def shiftcipher(filein,fileout, key, mode):
  # open file handles to both files
  fin  = open(filein)       # by default, read mode
  fout = open(fileout,'w')  # write mode
  c    = fin.read()         # read in file into c

  shift = 0
  if mode == "e":
    shift = key
  elif mode == "d":
    shift = -key

  string = ""
  for i in xrange(len(c)):
    string += chr(ord(c[i]) + shift)

  # and write to fileout
  fout.write(string)


# our main function
if __name__=="__main__":
  # set up the argument parser
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', dest='filein', help='input file')
  parser.add_argument('-o', dest='fileout', help='output file')
  parser.add_argument('-k', dest='key', help='key string')
  parser.add_argument('-m', dest='mode', help='d or e')

  # parse our arguments
  args = parser.parse_args()
  filein=args.filein
  fileout=args.fileout
  key = int(args.key)
  mode = args.mode

  if key > 255:
    raise "Error! Key length must be between 0 and 255"
  if mode != 'd' and mode != 'e':
    raise "Error! Mode can only be 'e' or 'd'."
  shiftcipher(filein, fileout, key, mode)

  # all done


