# -*- coding: utf-8 -*-
import tkinter as tk
from pathlib import Path
from tkinter.filedialog import askopenfilename
import sys
from vigenere import Vigenere
from affine import Affine

def load_file_affine():
	global file 
	file = askopenfilename()
	fstatB["text"] = "SELECTED: "+str(file)
	file = open(file,"rb")

def load_file_vigenere():
	global file 
	file = askopenfilename()
	fstatA["text"] = "SELECTED: "+str(file)
	file = open(file,"rb")	

def encryptVigenere():
	global file,keyvig
	content = file.read().decode('utf-8')
	key = keyvig.get()
	new_content = vigObj.encryptText(content,key)
	new_file = open(file.name[:-4]+".vig","wb")
	new_file.write(bytes(new_content,'utf-8'))
	fstatA["text"] = "SAVED!"
	file.close()
	new_file.close()

def decryptVigenere():
	global file,keyvig
	content = file.read().decode('utf-8')
	print(content)
	key = keyvig.get()
	original = vigObj.decryptText(content,key)
	new_file = open(file.name[:-4]+".txt","w")
	new_file.write(original)
	fstatA["text"] = "SAVED!"
	file.close()
	new_file.close()

def verifyKeys():
	global affA, affB, ksstat
	a = int(affA.get())	
	b = int(affB.get())
	c = 0
	if a>b:
		c = affObj.gcd(a,b)
	else:
		c = affObj.gcd(b,a)
	if c == 1:
		ksstat["text"] = "Valid key!"
	else:
		ksstat["text"] = "Invalid key! gcd="+str(c)

def calculateInv():
	global vakey,vkstat
	a,n = vakey.get().split(',')
	c = affObj.ainv(int(a),int(n))
	vkstat["text"] = f"({a}^-1) mod {n} = "+str(c)

def encryptAffine():
	global affkey, affn,file,fstatB
	content = file.read().decode('utf-8')
	content = content.replace(' ','')
	print(content)
	a,b = affkey.get().split(',')
	n = affn.get()
	if n=='' or n==' ':
		n = 256
	else:
		n = int(n)
		if n<98: #Se usan puras mayusculas
			content = content.upper()
	if affObj.egcd(int(a),int(n))[0]!=1:
		fstatB["text"] = "ERROR, Invalid Affine keys!"	
		file.close()
	else:
		new_content = affObj.encryptText(content,int(a),int(b),n)
		new_file = open(file.name[:-4]+".aff","wb")
		new_file.write(bytes(new_content,'utf-8'))
		fstatB["text"] = "SAVED!"
		file.close()
		new_file.close()

def decryptAffine():
	global affkey, affn,file,fstatB
	econtent = file.read().decode('utf-8')
	a,b = affkey.get().split(',')
	n = affn.get()
	if n=='' or n==' ':
		n = 256
	else:
		n = int(n)
	original = affObj.decryptText(econtent,int(a),int(b),n)
	new_file = open(file.name[:-4]+".txt","w")
	new_file.write(original)
	fstatB["text"] = "SAVED!"
	file.close()
	new_file.close()

#AQUÍ MI MAIN
file = None
vigObj = Vigenere()
affObj = Affine()
#CREAMOS LA VENTANA Y ASIGNAMOS UN TAMAÑO
window = tk.Tk()
window.title("PRACTICA 1")
frame = tk.Frame(master=window,width=510,height=420,bg="black")
#CREAMOS EL SALUDO
greeting = tk.Label(text="WELCOME!",foreground="crimson",background="black",width=35,height=4,font=("Courier",16))
greeting.place(x=10,y=0)

#CREAMOS UN LABEL DE INSTRUCCIONES
instA = tk.Label(text="VIGENERE:\n\nKEY:",foreground="orange",background="black",height=4,font=("Courier",10),anchor="w")
instA.place(x=10,y=60)

#CREAMOS EL BOTÓN KEYGEN Y LOADKEY
keyvig = tk.Entry(width=20,fg="yellow",bg="black")
keyvig.place(x=80,y=100)

vebtn = tk.Button(text="ENCRYPT",width=10,fg="hot pink",bg="black",command=encryptVigenere)
vebtn.place(x=230,y=97)

vdbtn = tk.Button(text="DECRYPT",width=10,fg="hot pink",bg="black",command=decryptVigenere)
vdbtn.place(x=320,y=97)

lvfile = tk.Button(text="LOAD FILE",width=10,fg="hot pink",bg="black",command=load_file_vigenere)
lvfile.place(x=410,y=97)

#CREAMOS OTRO LABEL DE INSTRUCCIONES
fstatA = tk.Label(text="SELECTED FILE:\tNone",foreground="lime",background="black",height=2,font=("Courier",10),anchor="w")
fstatA.place(x=30,y=120)

instB = tk.Label(text="VERIFY AFFINE KEYS:",foreground="orange",background="black",height=1,font=("Courier",10),anchor="w")
instB.place(x=10,y=160)

affA = tk.Entry(width=15,fg="yellow",bg="black")
affA.place(x=30,y=190)

affB = tk.Entry(width=15,fg="yellow",bg="black")
affB.place(x=140,y=190)

chkbtn = tk.Button(text="VERIFY",width=10,fg="hot pink",bg="black",command=verifyKeys)
chkbtn.place(x=250,y=187)

ksstat = tk.Label(text="KEYS STATUS",foreground="orange",background="black",height=1,font=("Courier",10),anchor="w")
ksstat.place(x=340,y=187)

instC = tk.Label(text="CALCULATE (a^-1) mod n: [a,n]",foreground="orange",background="black",height=1,font=("Courier",10),anchor="w")
instC.place(x=10,y=220)

vakey = tk.Entry(width=15,fg="yellow",bg="black")
vakey.place(x=30,y=255)

vkbtn = tk.Button(text="CALCULATE",width=10,fg="hot pink",bg="black",command=calculateInv)
vkbtn.place(x=140,y=252)

vkstat = tk.Label(text="(a^-1) mod n = ",foreground="orange",background="black",height=1,font=("Courier",10),anchor="w")
vkstat.place(x=230,y=252)

instD = tk.Label(text="AFFINE:\n\nKEY:\n\nn[256]:",foreground="orange",background="black",height=6,font=("Courier",10),anchor="w")
instD.place(x=10,y=290)

affkey = tk.Entry(width=20,fg="yellow",bg="black")
affkey.place(x=70,y=320)

affn = tk.Entry(width=5,fg="yellow",bg="black")
affn.place(x=70,y=360)

aebtn = tk.Button(text="ENCRYPT",width=10,fg="hot pink",bg="black",command=encryptAffine)
aebtn.place(x=210,y=317)

adbtn = tk.Button(text="DECRYPT",width=10,fg="hot pink",bg="black",command=decryptAffine)
adbtn.place(x=300,y=317)
 
lafile = tk.Button(text="LOAD FILE",width=10,fg="hot pink",bg="black",command=load_file_affine)
lafile.place(x=390,y=317)

fstatB = tk.Label(text="SELECTED FILE: None",foreground="lime",background="black",height=1,font=("Courier",10),anchor="w")
fstatB.place(x=120,y=360)

frame.pack()
try:
	window.mainloop()
except KeyboardInterrupt:
	sys.exit()
except UnicodeDecodeError:
	pass