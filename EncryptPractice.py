# from cryptography.fernet import Fernet
# import cryptography
# file = open('pfile.txt', 'rb')
# key = file.read()
# file.close()

# message = "my darkest secret"
# encode = message.encode()

# f = Fernet(key)
# encrypted = f.encrypt(encode)

# file = open('pfile.txt', 'rb')
# key2 = file.read()
# file.close()

# # Decrypt origial message
# f2 = Fernet(key)
# decrypted = f2.decrypt(encrypted)
# print(decrypted)

# # Decode the message
# original_message = decrypted.decode()
# print(original_message)
# file = open('pfile.txt', 'w')
# file.write("hello world")
# with open('pfile.txt', 'w') as file:
#     file.write(b"hello world")
key = 'dodge'
dicton = {}
dicton[key].append("ram")
print(dicton)