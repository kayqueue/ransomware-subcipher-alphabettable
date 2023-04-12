Grade: 96/100

# Goal:
-------
Create a ransomware that performs the following:
[1] Generates a random alphabet table for symmetric encryption using substitution cipher.
[2] Encrypts all .txt files to .enc files in the current directory using the key that the
attacker generated in [1]. The files in the other folders or the files in the same
folder but having different file extensions must not be impacted by the ransomware.
[3] Comments out all the content of the existing .py files in the target folder (without deleting the content) and replicates itself to the .py files for the further propagation.
[4] The key in step [1] is encrypted to key.bin using public key encryption. (RSA 2048)
[5] Display a message asking for ransom “Your text files are encrypted. To decrypt them, you need to pay me $10,000 and send key.bin in your folder to {xxxx}.”

// A report is written to explain the necessary information and expected outcomes of the programs.
