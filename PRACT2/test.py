from Crypto.Cipher import DES
key = b'holacomo'
cipher = DES.new(key, DES.MODE_OFB)
image = open("C://Users//gamma//Desktop//sombra.bmp","rb")
new_image = open("C://Users//gamma//Desktop//sombra_OFB.bmp","wb")
new_file = open("iv.txt","wb")
new_image.write(image.read(54))
bytes_to_encrypt = image.read()
new_file.write(cipher.iv)
new_image.write(cipher.encrypt(bytes_to_encrypt))