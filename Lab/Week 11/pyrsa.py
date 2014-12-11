from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode,b64encode
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA256
import argparse
import sys
import binascii
from pyrsa_sq_mul import square_multiply


#python pyrsa.py -pub mykey.pem.pub -priv mykey.pem.priv -message message.txt

def generate_RSA(bits=1024):
    rsakeys = RSA.generate(bits)
    private_key = rsakeys.exportKey()
    public_key = rsakeys.public_key().exportKey()

    return private_key, public_key

def encrypt_RSA(public_key_file,message):
    f = open(public_key_file, 'r')
    key = RSA.importKey(f.read())

    enc_obj = PKCS1_OAEP.new(key)
    c = enc_obj.encrypt(message)
    return c

def decrypt_RSA(private_key_file,cipher):
    f = open(private_key_file, 'r')
    key = RSA.importKey(f.read())

    enc_obj = PKCS1_OAEP.new(key)
    m = enc_obj.decrypt(cipher)

    return m

def sign_RSA(private_key_loc,data):
    f = open(private_key_loc, 'r')
    key = RSA.importKey(f.read())

    sha_object = SHA256.new(data)

    signer = PKCS1_PSS.new(key)
    signature = signer.sign(sha_object)
    return signature

def verify_sign(private_key_loc,sign,data):
    f = open(private_key_loc, 'r')
    key = RSA.importKey(f.read())

    sha_object = SHA256.new(data)

    verifier = PKCS1_PSS.new(key)
    if verifier.verify(sha_object, sign):
        print "The signature is authentic"
    else:
        print "The signature is not authentic"

def attack(public_key_file,cipher):
    key=open(public_key_file,'r')
    rsakey=RSA.importKey(key)
    s=2
    modified = square_multiply(s,rsakey.e,rsakey.n)
    cipher = int(binascii.hexlify(cipher),16)
    modified = (cipher*modified)%rsakey.n
    return binascii.unhexlify(hex(modified)[2:-1])


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
    print plaintext
    signature = sign_RSA(priv, message)
    verify = verify_sign(pub,signature,message)

    signature = bin(100)
    key=open(pub,'r')
    rsakey=RSA.importKey(key)
    message = bin(square_multiply(100,rsakey.e,rsakey.n))
    verify_sign(pub,signature,message)


    message=bin(100)
    cipher = encrypt_RSA(pub,message)
    modified = attack(pub,cipher)
    decrypt = decrypt_RSA(priv,modified)
    print "ENCRYPTING:",message
    print "CIPHER:",cipher
    print "MODIFIED:",modified
    print "DECRYPTED:",ord(decrypt)
    print ""