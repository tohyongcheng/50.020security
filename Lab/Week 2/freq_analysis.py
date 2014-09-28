# Import libraries
import sys
import argparse
import collections

def freq_analysis(initfile, filein,fileout):
  # open file handles to both files

  finit = open(initfile)
  fin  = open(filein)       # by default, read mode
  fout = open(fileout,'w')  # write mode

  init_string = finit.read()
  init_d = collections.defaultdict(int)

  for char in init_string:
    if char.isalpha():
      init_d[char.upper()] += 1

  correct_d = ""
  for w in sorted(init_d, key=init_d.get, reverse=True):
    # print w, init_d[w]
    correct_d += w

  correct_d = list(correct_d)

  # do manual swapping
  correct_d = swap(correct_d, 'H', 'O')
  correct_d = swap(correct_d, 'I', 'N')
  correct_d = swap(correct_d, 'S', 'O')
  correct_d = swap(correct_d, 'I', 'O')
  correct_d = swap(correct_d, 'P', 'U')
  correct_d = swap(correct_d, 'P', 'G')
  correct_d = swap(correct_d, 'F', 'D')
  correct_d = swap(correct_d, 'F', 'C')
  correct_d = swap(correct_d, 'K', 'V')
  correct_d = swap(correct_d, 'C', 'D')
  correct_d = swap(correct_d, 'C', 'M')
  correct_d = swap(correct_d, 'X', 'J')
  correct_d = swap(correct_d, 'Y', 'K')


  print "---"

  d = collections.defaultdict(int)
  sub = collections.defaultdict(str)

  c    = fin.read()         # read in file into c

  for char in c:
    if char.isalpha():
      d[char] += 1

  i = 0
  for w in sorted(d, key=d.get, reverse=True):
    print w, d[w]
    sub[w] = correct_d[i]
    i += 1

  print sub

  string = ""
  for char in c:
    if char.isalpha():
      string += sub[char]
    else:
      string += char
  print string


  fout.write(string)

# our main function

def swap(s, a, b):
  a_i = s.index(a)
  b_i = s.index(b)
  s[a_i], s[b_i] = b, a
  return s

if __name__=="__main__":
  # set up the argument parser
  parser = argparse.ArgumentParser()
  parser.add_argument('-init', dest='init', help='init file')
  parser.add_argument('-i', dest='filein', help='input file')
  parser.add_argument('-o', dest='fileout', help='output file')

  # parse our arguments
  args = parser.parse_args()
  init=args.init
  filein=args.filein
  fileout=args.fileout

  freq_analysis(init, filein, fileout)

  # all done


