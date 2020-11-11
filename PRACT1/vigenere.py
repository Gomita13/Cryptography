class Vigenere:
	
	def __init__(self):
		pass

	def encryptText(self,text,key):
		etext = ""
		i = 0
		for m in text:
			if i == len(key):
				i = 0
			c = (ord(m)+ord(key[i]))%256
			etext = etext + chr(c)
			i=i+1
		return etext


	def decryptText(self,etext,key):
		dtext = ""
		i = 0
		for character in etext:
			if i == len(key):
				i = 0
			mk = 256 - ord(key[i])
			c = (ord(character)+mk)%256
			dtext = dtext + chr(c)
			i=i+1
		return dtext
		

