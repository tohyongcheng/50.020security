# import primes
import random

# p = 1208925819614629174706189
#
def square_multiply(m,k,n):
  res = 1
  for i in bin(k)[2:]:
    res = res * res %n
    if i == '1':
      res = res * m % n
  return res

def dhke_setup(nb):
    p = 1208925819614629174706189
    alpha = 2

    return p,alpha

def gen_priv_key(p):
    p = 551052924306346291129189
    return p

def get_pub_key(alpha, a, p):
    res = square_multiply(alpha,a,p)
    return res

def get_shared_key(keypub,keypriv,p):
    res = square_multiply(keypub, keypriv, p)
    return res

if __name__=="__main__":

    p,alpha= dhke_setup(80)
    print 'Generate P and alpha:'
    print 'P:',p
    print 'alpha:',alpha
    print
    # print square_multiply(11123423423141,p,p)
    a=gen_priv_key(p)
    b=gen_priv_key(p)
    print 'My private key is: ',a
    print 'Test other private key is: ',b
    print
    A=get_pub_key(alpha,a,p)
    B=get_pub_key(alpha,b,p)
    print 'My public key is: ',A
    print 'Test other public key is: ',B
    print
    sharedKeyA=get_shared_key(B,a,p)
    sharedKeyB=get_shared_key(A,b,p)
    print 'My shared key is: ',sharedKeyA
    print 'Test other shared key is: ',sharedKeyB
    print 'Length of key is %d bits.'%sharedKeyA.bit_length()

