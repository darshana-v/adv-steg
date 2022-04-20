from stegano import lsb

# with open('text.csv', 'rb') as enc_file:
#     encrypted = enc_file.read()


secret = lsb.hide("./1.jpeg", "encrypted")

secret.save("./encoded_image.jpeg")