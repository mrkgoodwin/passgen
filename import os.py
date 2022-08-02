import os
import random, string
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


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
    #Base list of options in a 2d sequence to stack for password
    # yesvalues = ["yes", "Yes", "yeah", "ok", "okay","y"]
    # spcharacter = (input("Are special Charaters required?: "))
    return token_byte

def main():
    out_pass = generator()
    print(out_pass)
if __name__ == "__main__":
    main()