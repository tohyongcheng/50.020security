from gf2ntemplate import *

print "\nAddition Table\n--------------------------\n"
for i in range(16):
  answer=""
  for j in range(16):
    g1=GF2N(i,4,Polynomial2([1,0,0,1,1]))
    g2=GF2N(j,4,Polynomial2([1,0,0,1,1]))
    g3=g1.add(g2)
    answer+=(str(g3.getInt())+" ")
  print answer


print "\nMultiplication Table\n--------------------------\n"

for i in range(16):
  answer=""
  for j in range(16):
    g1=GF2N(i,4,Polynomial2([1,0,0,1,1]))
    g2=GF2N(j,4,Polynomial2([1,0,0,1,1]))
    g3=g1.mul(g2)
    answer+=(str(g3.getInt())+" ")
  print answer