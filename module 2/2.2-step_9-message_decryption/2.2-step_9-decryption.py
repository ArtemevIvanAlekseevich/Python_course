from simplecrypt import decrypt
import os
def decryption():
    current_dir = os.path.abspath(os.path.dirname(__file__))

    with open(os.path.join(current_dir, 'encrypted.bin'), "rb") as inp:
        encrypted = inp.read()

    with open(os.path.join(current_dir, 'passwords.txt'), "rb") as inp:
        passwords = inp.read().split()

    for i in passwords:
        try:
            plaintext = decrypt(i, encrypted)
            print(plaintext)
        except: 
            print (i, "is not correct password")

if __name__ == "__main__":
    decryption()