from cryptography.fernet import Fernet

# key generation
key = Fernet.generate_key()

# print(key)
# string the key in a file
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)
   
# using the generated key
fernet = Fernet(key)

# opening the original file to encrypt
with open('text.csv', 'rb') as file:
    original = file.read()

# encrypting the file
encrypted = fernet.encrypt(original)

# opening the file in write mode and writing the encrypted data
with open('text.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
