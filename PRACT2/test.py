from Crypto.Cipher import DES
key = b'holacomo'
cipher = DES.new(key, DES.MODE_OFB)
image = open("rutaAlArchivo.bmp","rb")
new_image = open("rutaAlArchivo_OFB.bmp","wb")
new_image.write(image.read(54))
bytes_to_encrypt = image.read()
new_image.write(cipher.encrypt(bytes_to_encrypt))