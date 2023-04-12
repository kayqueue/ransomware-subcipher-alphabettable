import string
import os
import sys
import glob

# to make sure key.txt is present before running the file_recovery program
try:
	fin = open("key.txt", "rb")
	encoded_symkey = fin.read()
	symkey = encoded_symkey.decode('utf-8')
except FileNotFoundError as error:
	sys.exit(error)

################################

# LOCATES FILES TO BE DECRYPTED
# stores a list of files to be encrypted
files = []

for file in glob.glob("*.enc"): # enc files only
	files.append(file) # add to files list

################################

# DECRYPT THE ENC FILES
# all letters
alphabet = string.ascii_letters

# MAP SUBSTITUTION VALUES
# create a dictionary
og_dict = {}

# iterate through the alphabet list
for i, c in enumerate(alphabet):
	og_dict[c] = symkey[i]

# swap key-value pairs
swap_dict = dict([(value, key) for key, value in og_dict.items()])


# go through all the files, read and decrypt
for file in files:
	with open(file, "r") as f:
		contents = f.read()
	# decrypt the contents
	for i, c in enumerate(contents):
		contents = list(contents)
		if contents[i] in swap_dict: # if key value exists in dictionary
			contents[i] = swap_dict[c]
	# write decrypted data to txt file
	fout = open(str(f.name.split('.')[0]) + ".txt", "w")
	fout.write(''.join(contents))
	fout.close()

################################

# delete the enc files
def delete_enc_files():
	for file in files:
		os.remove(file) # delete enc files

delete_enc_files()

################################