from cryptography.fernet import Fernet
from stegano import lsb

with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
    
fernet = Fernet(key)

# # opening the encrypted file
# with open('text.csv', 'rb') as enc_file:
#     encrypted = enc_file.read()

# print(lsb.reveal('./encoded_image.jpeg'))
# encrypted = bytes(lsb.reveal('./encoded_example.png'), 'utf-8')
encrypted = lsb.reveal('./encoded_example.png')
print(type(encrypted))
print(encrypted)

# decrypting the file
decrypted = fernet.decrypt(encrypted.encode('utf-8'))
print(decrypted)
# opening the file in write mode and
# writing the decrypted data
with open('text.csv', 'wb') as dec_file:
    dec_file.write(decrypted)
