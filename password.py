import random, string
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Password:
    def generate(self, length = 16):
        '''
        Generator is a random password generator based on user input
        '''
        base = bytes(''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length)), encoding='utf-8')        
        return base
