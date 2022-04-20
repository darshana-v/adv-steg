from cryptography.fernet import Fernet

with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
    
fernet = Fernet(key)

# opening the encrypted file
with open('text.csv', 'rb') as enc_file:
    encrypted = enc_file.read()
  
# decrypting the file
decrypted = fernet.decrypt(encrypted)
  
# opening the file in write mode and
# writing the decrypted data
with open('text.csv', 'wb') as dec_file:
    dec_file.write(decrypted)
