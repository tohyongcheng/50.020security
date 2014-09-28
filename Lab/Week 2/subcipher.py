# Import libraries
import sys
import argparse

def subcipher(filein,fileout, filekey, mode):
  # load keyfile
  keyin = open(filekey)
  plain = keyin.readline()
  cipher = keyin.readline()

  # open file handles to both files
  fin  = open(filein)       # by default, read mode
  fout = open(fileout,'w')  # write mode
  c    = fin.read()         # read in file into c

  string = ""
  for i in xrange(len(c)):
    char = c[i]
    upper = False

    if char.isupper():
      upper = True
      char = char.lower()

    res = char
    try:
      idx = plain.index(char)
      if mode == "e":
        res = cipher[idx]
      elif mode == "d":
        res = plain[idx]

      if upper:
        res = res.upper()
      string += res
    except ValueError:
      string += char


  # and write to fileout
  fout.write(string)


# our main function
if __name__=="__main__":
  # set up the argument parser
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', dest='filein', help='input file')
  parser.add_argument('-o', dest='fileout', help='output file')
  parser.add_argument('-k', dest='filekey', help='key file')
  parser.add_argument('-m', dest='mode', help='d or e')

  # parse our arguments
  args = parser.parse_args()
  filein=args.filein
  fileout=args.fileout
  filekey = args.filekey
  mode = args.mode

  if mode != 'd' and mode != 'e':
    raise "Error! Mode can only be 'e' or 'd'."
  subcipher(filein, fileout, filekey, mode)

  # all done


