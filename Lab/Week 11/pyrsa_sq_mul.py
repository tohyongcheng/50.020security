from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from base64 import b64encode,b64decode
import random

def square_multiply(m,k,n):
    res = 1
    for i in bin(k)[2:]:
    	res = res * res % n
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

	  # PART I
    msg_file = open('message.txt', 'r')
    plaintext = msg_file.read()


    key = open('mykey.pem.pub', 'r')
    rsakey = RSA.importKey(key)
    pub_n = rsakey.n
    pub_e = rsakey.e

    public_encrypted_message = square_multiply(unpack_bigint(plaintext), pub_e, pub_n)

    print public_encrypted_message

    key = open('mykey.pem.priv', 'r')
    rsakey = RSA.importKey(key)
    pri_n = rsakey.n
    pri_d = rsakey.d

    private_encrypted_message = square_multiply(unpack_bigint(plaintext), pri_d, pri_n)

    print
    print private_encrypted_message

    sha_object = SHA256.new(plaintext)
    hashed_signature = sha_object.hexdigest()

    print
    print "hashed signature"
    print hashed_signature
    print
    print "using private key to encrypt"

    enc_hash = square_multiply(unpack_bigint(hashed_signature), pri_d, pri_n)
    print enc_hash

    decrypted_signature = square_multiply(enc_hash, pub_e, pub_n)

    print
    print "using public key to decrypt"
    print pack_bigint(decrypted_signature)
    print

    # PART II

    to_test = 1000
    enc_100 = square_multiply(to_test, pub_e, pub_n)
    print "Encrypting:    ",  to_test
    print "Result:"
    print enc_100
    print

    ys = square_multiply(10, pub_e, pub_n)

    new_m = (enc_100 * ys) % pub_n
    print "Modified to:"
    print new_m


    dec_200 = square_multiply(new_m, pri_d, pri_n)
    print "Decrypted: ", dec_200




