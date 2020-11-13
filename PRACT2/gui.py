import tkinter as tk
from tkinter import ttk
from pathlib import Path
from tkinter.filedialog import askopenfilename
import sys
from Crypto.Cipher import DES

def selectFile(event):
	global file
	global lblImg
	file = askopenfilename()
	lblImg["text"] = file
	file = open(file,"rb")
	#file_iv = open("iv.des","rb")

def encryptImage(event):
	global file
	global cbMode
	global txtKey
	key = str.encode(txtKey.get())
	mode = str(cbMode.get())
	if mode == 'ECB':
		cipher = DES.new(key,DES.MODE_ECB)
	elif mode == 'CBC':
		cipher = DES.new(key,DES.MODE_CBC)
	elif mode == 'CFB':
		cipher = DES.new(key,DES.MODE_CFB)
	else:
		cipher = DES.new(key,DES.MODE_OFB)
	file_out = open(file.name[:-4]+"_"+mode+".bmp","wb")
	file_iv = open("iv.des","wb")
	header = file.read(54)
	file_out.write(header) #IMAGE HEADER
	content = file.read()
	file_out.write(cipher.encrypt(content))
	file_iv.write(cipher.iv)
	file_out.close()
	file_iv.close()

#CREAMOS LA VENTANA Y ASIGNAMOS UN TAMAÑO
window = tk.Tk()
window.title("DES IMAGE ENCRYPTION")
frame = tk.Frame(master=window,width=700,height=620,bg="black")

#CREAMOS UN LABEL PARA VISUALIZAR LA IMAGEN
lblImg = tk.Label(foreground="medium purple",background="black",height=30,width=82,font=("Courier",10),anchor="w")
lblImg.place(x=20,y=20)

#CREAMOS EL BOTÓN PAR EL ARCHIVO
btnFile = tk.Button(text="LOAD FILE",width=10,height=1,fg="aqua",bg="black")
btnFile.bind("<Button-1>",selectFile)
btnFile.place(x=20,y=520)

#CREAMOS OTRO LABEL DE INSTRUCCIONES
lblKey = tk.Label(text="KEY:",foreground="medium purple",background="black",height=1,font=("Courier",10),anchor="w")
lblKey.place(x=110,y=520)

#CREAMOS UN ENTRY PARA LA CLAVE
txtKey = tk.Entry(width=10,fg="yellow",bg="black")
txtKey.place(x=150,y=520)

#CREAMOS UN LABEL PARA EL MODO
lblMode = tk.Label(text="MODE:",foreground="medium purple",background="black",height=1,font=("Courier",10),anchor="w")
lblMode.place(x=240,y=520)

#CREAMOS UN COMBOBOX PARA LISTAR LOS MODOS DE CIFRADO
cbMode = ttk.Combobox(values=["ECB","CBC","CFB","OFB"])
cbMode.current(0)
cbMode.place(x=300,y=520)

#CREAMOS EL BOTÓN DE ENCRYPT Y DECRYPT
encbtn = tk.Button(text="ENCRYPT",width=10,height=1,fg="hot pink",bg="black")
encbtn.bind("<Button-1>",encryptImage)
encbtn.place(x=20,y=570)
decbtn = tk.Button(text="DECRYPT",width=10,height=1,fg="hot pink",bg="black")
decbtn.place(x=110,y=570)

frame.pack()
file = None
try:
	window.mainloop()
except KeyboardInterrupt:
	sys.exit()