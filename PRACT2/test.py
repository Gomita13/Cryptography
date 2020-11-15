from Crypto.Cipher import DES
key = b'holacomo'
op = int(input('Ingresa operacion (encrypt 0, decrypt 1)\n>'))
if op == 0:
	cipher = DES.new(key, DES.MODE_OFB)
	image = open("C://Users//gamma//Desktop//PruebaCOVID//thunder.bmp","rb")
	new_image = open("C://Users//gamma//Desktop//PruebaCOVID//thunder_OFB.bmp","wb")
	new_file = open("C://Users//gamma//Desktop//PruebaCOVID//iv.txt","wb")
	new_image.write(image.read(54))
	bytes_to_encrypt = image.read()
	new_file.write(cipher.iv)
	new_image.write(cipher.encrypt(bytes_to_encrypt))
else:
	new_file = open("C://Users//gamma//Desktop//PruebaCOVID//iv.txt","rb")
	iv = new_file.read()
	cipher = DES.new(key, DES.MODE_OFB,iv)
	image = open("C://Users//gamma//Desktop//PruebaCOVID//thunder_OFB.bmp","rb")
	new_image = open("C://Users//gamma//Desktop//PruebaCOVID//thunder.bmp","wb")
	new_image.write(image.read(54))
	bytes_to_decrypt = image.read()	
	new_image.write(cipher.decrypt(bytes_to_decrypt))