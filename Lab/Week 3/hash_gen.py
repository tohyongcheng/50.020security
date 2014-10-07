# Import libraries
import sys
import argparse
import md5

def generate_hash(filein, fileout):

  fin  = open(filein)       # by default, read mode
  fout = open(fileout,'w')  # write mode
  c    = fin.read()         # read in file into c


  passwords = c.split("\n")
  encrypted = []
  for p in passwords:
    e = md5.new(p).hexdigest()
    encrypted.append(e)

  for p in encrypted:
    fout.write(p)
    fout.write("\n")




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

  generate_hash(filein, fileout)

  # all done


