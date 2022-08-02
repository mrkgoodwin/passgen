''' Build a password generator that inputs the amount of max and min charaters
and prints random numbers in between the amountand uses at least one capitol letter,
lowercase letter, at least 3 numbers, and special charaters.
'''

import os
import sys
import random, string
import base64
from tokenize import Token
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from .password import Password

password1 = b'YouShallNotPass!$'
salt = os.urandom(16)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=390000,
)
key = base64.urlsafe_b64encode(kdf.derive(password1))
key_return = Fernet(key)

def generator():
    '''
    Generator is a random password generator based on user input
    '''
    # characters used for password input based on user input.
    maxcharacter = int(input("Enter amout of Max Charaters: "))
    mincharacter = int(input("Enter amount of Min Charaters: "))
    passwordstrlen = random.randrange(mincharacter, maxcharacter)
    base = bytes(''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=passwordstrlen)), encoding='utf-8')
    token_byte = key_return.encrypt(base)
    return token_byte

    
def enctyption():
    site_input = (input('Enter site name: ',))
    outside_password = generator()
    site_input_byte = bytes(site_input, 'utf-8')
    #Symetric encryption for password

    #encrypts password into file
    bytepass = outside_password
    token = key_return.encrypt(bytepass)

    with open('pwd.csv', 'a', encoding='utf-8') as pfcsv:
        pfcsv.write(f'{site_input_byte}, {token}\n')

    #decrypts password from file
    dectoken = key_return.decrypt(token)

    with open("pfile.txt", "w", encoding='utf-8') as pfile1:
        key_return.encrypt(b'pfile1')
        pfile1.write(f'token{token}, {key_return}')
    return 

def main():
    if len(sys.argv) <= 1:
        print('Please tell me what to do')
        return
    

    command = sys.argv[1]

    if command == "generate":
        print(Password.generate())
    elif command == "save":
        print('call save')
    elif command == "get":
        print('call get')

    return



    # print(key_return)
    gen_run = input("Would you like to create or retrieve? ")
    create_ = "create"

    if gen_run in create_:
        enctyption()
    
    else :
        site_input = (input('Enter site name: ',))
        with open('pwd.csv','r', encoding='utf-8') as read_csv:
            line = read_csv
            for line in read_csv:
            
                if line.startswith(f'b\'{site_input}\''):
                    fresh_cut = line.split('b\'')
                    cut_decrypt = bytes(fresh_cut[2], 'utf-8')
        with open('pfile.txt', 'r', encoding='utf-8') as read_pfile:
            pline = read_pfile
            for pline in read_pfile:
                if pline.startswith(f'tokenb\'{key_return}\''):
                
                    print_output = key_return.decrypt(cut_decrypt)
                    print(print_output)

                    print(cut_decrypt)
                    print(fresh_cut)

if __name__ == "__main__":
    main()