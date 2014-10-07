# Import libraries
import sys
import argparse
import md5
import string
import random

def generate_hash(filein, fileout,saltout):

  fin  = open(filein)       # by default, read mode
  fout = open(fileout,'w')  # write mode
  sout = open(saltout,'w')
  c    = fin.read()         # read in file into c


  passwords = c.split("\n")
  salts = []
  encrypted = []


  for p in passwords:
    s = random.choice(string.ascii_lowercase)
    salts.append(s)
    e = md5.new(p+s).hexdigest()
    encrypted.append(e)

  for p in encrypted:
    fout.write(p)
    fout.write("\n")

  for s in salts:
    sout.write(s)
    sout.write("\n")



# our main function
if __name__=="__main__":
  # set up the argument parser
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', dest='filein', help='input file')
  parser.add_argument('-o', dest='fileout', help='output file')
  parser.add_argument('-s', dest='saltfile', help='salt file')


  # parse our arguments
  args = parser.parse_args()
  filein=args.filein
  fileout=args.fileout
  saltout=args.saltfile

  generate_hash(filein, fileout,saltout)

  # all done


