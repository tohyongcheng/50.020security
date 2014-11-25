from gf2ntemplate import *

answer=""
for i in range(256):
  g10=GF2N(i,8,ip)
  g11=g10.mulInv()
  g12=g11.affineMap()
  answer += (hex(g12.getInt())[2:].zfill(2).upper()+" ")
  if i==0:
    print "00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15"
    print "-----------------------------------------------"
  if (i+1)%16==0:
    print answer
    answer=""
