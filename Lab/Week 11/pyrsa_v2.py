from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode,b64encode
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA256
import argparse
import sys
import binascii
import pyrsa_sq_mul as hack

#python pyrsa_v2.py -pub mykey.pem.pub -priv mykey.pem.priv -message message.txt


def square_multiply(m,k,n):
    res = 1
    for i in bin(k)[2:]:
    	res = res * res % n
    	if i == '1':
    		res = res * m % n
    return res


def generate_RSA(bits=1024):
	print "HEL"
	key = RSA.generate(bits)
	private_key=key.d
	public_key=key.e
	return private_key, public_key

def encrypt_RSA(public_key_file,message):
	key=open(public_key_file,'r')
	rsakey=RSA.importKey(key)
	cipher = PKCS1_OAEP.new(rsakey)
	encrypted = cipher.encrypt(message)
	return encrypted
	pass

def decrypt_RSA(private_key_file,ciphertext):
	key=open(private_key_file,'r')
	rsakey=RSA.importKey(key)
	cipher = PKCS1_OAEP.new(rsakey)
	decrypted = cipher.decrypt(ciphertext)
	return decrypted

def sign_RSA(private_key_loc,data):
	key=open(private_key_loc,'r')
	rsakey=RSA.importKey(key)
	hash = SHA256.new()
	hash.update(data)
	signer = PKCS1_PSS.new(rsakey)
	signature = signer.sign(hash)
	return signature
	pass

def verify_sign(public_key_loc,sign,message):
	key=open(public_key_loc,'r')
	rsakey=RSA.importKey(key)
	hash = SHA256.new()
	hash.update(message)
	verifier=PKCS1_PSS.new(rsakey)
	if verifier.verify(hash,sign):
		print "VERIFIED"
	else:
		print "NOT VERIFIED"
	pass

def attack(pub,cipher):
	key=open(pub,'r')
	rsakey=RSA.importKey(key)
	s=2
	modified = square_multiply(s,rsakey.e,rsakey.n)
	cipher = int(binascii.hexlify(cipher),16)
	return (cipher*modified)%rsakey.n



if __name__=="__main__":
	parser=argparse.ArgumentParser(description='RSA')
	parser.add_argument('-pub', dest='pub',help='public key')
	parser.add_argument('-priv', dest='priv',help='private key')
	parser.add_argument('-message', dest='message', help='message')

	args=parser.parse_args()
	pub=args.pub
	priv=args.priv
	message=open(args.message).read()

	ciphertext = encrypt_RSA(pub,message)
	plaintext = decrypt_RSA(priv,ciphertext)
	signature = sign_RSA(priv,message)
	verify = verify_sign(pub,signature,message)
	signature = bin(100)
	key=open(pub,'r')
	rsakey=RSA.importKey(key)
	message = bin(square_multiply(100,rsakey.e,rsakey.n))
	verify_sign(pub,signature,message)



	message=bin(100)
	cipher = encrypt_RSA(pub,message)
	modified = attack(pub,cipher)
	modified = binascii.unhexlify(hex(modified)[2:-1])
	decrypt = decrypt_RSA(priv,modified)
	print "ENCRYPTING:",message
	print "CIPHER:",cipher
	print "MODIFIED:",modified
	print "DECRYPTED:",ord(decrypt)
	print ""

	pass
