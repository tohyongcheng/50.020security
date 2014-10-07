# Import libraries
import sys
import argparse
import random

def encrypt(filein,fileout, filekey, mode):
  # open file handles to both files
  fin  = open(filein)       # by default, read mode
  fout = open(fileout,'w')  # write mode
  keyout = open(filekey, 'w')
  c    = fin.read()         # read in file into c

  key_string = ""
  enc_string = ""

  for char in c:
    rand_int = random.randint(0,255)
    encrypted = rand_int ^ ord(char)

    key_string += (chr(rand_int))
    enc_string += (chr(encrypted))

  # and write to fileout
  fout.write(enc_string)
  keyout.write(key_string)

def decrypt(filein,fileout,filekey,mode):
  fin  = open(filein)       # by default, read mode
  fout = open(fileout,'w')  # write mode
  keyin = open(filekey)

  encrypted    = fin.read()         # read in file into c
  key = keyin.read()

  output = ""

  for i in xrange(len(encrypted)):
    decrypted = ord(encrypted[i]) ^ ord(key[i])
    output += chr(decrypted)

  fout.write(output)


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

  if mode == 'd':
    decrypt(filein, fileout, filekey, mode)
  elif mode == 'e':
    encrypt(filein, fileout, filekey, mode)
  else:
    raise "Error! Mode can only be 'e' or 'd'."
  # all done


