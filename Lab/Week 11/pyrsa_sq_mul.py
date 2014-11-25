from Crypto.PublicKey import RSA
from base64 import b64encode,b64decode
import random

def square_multiply(m,k,n):
  res = 1
  for i in bin(k)[2:]:
    res = res * res %n
    if i == '1':
      res = res * m % n
  return res

# function to convert long int to byte string
def pack_bigint(i):
    b=bytearray()
    while i:
        b.append(i&0xFF)
        i>>=8
    return b

# function to convert byte string to long int
def unpack_bigint(b):
    b=bytearray(b)
    return sum((1<<(bi*8))* bb for (bi,bb) in enumerate(b))

if __name__=="__main__":
    key = open('mykey.pem.pub','r')
    rsakey = RSA.importKey(key)

    pub_n = rsakey.n
    pub_e = rsakey.e


