import tkinter as tk
from pathlib import Path
from tkinter.filedialog import askopenfilename
import sys
from Crypto.Cipher import DES


def selectFile(event):
	global file
	global filesatus
	file = askopenfilename()
	#AQUI VA MI LABEL
	file = open(file,"rb")

def encryptImage(event):
	global file
	global keygen
	key = str.encode(keygen.get())
	cipher = DES.new(key,DES.MODE_ECB)
	file_out = open(file.name[:-4]+"_ECB.bmp","wb")
	header = file.read(54)
	file_out.write(header) #IMAGE HEADER
	content = file.read()
	file_out.write(cipher.encrypt(content))
	file_out.close()

#CREAMOS LA VENTANA Y ASIGNAMOS UN TAMAÑO
window = tk.Tk()
window.title("DES IMAGE ENCRYPTION")
frame = tk.Frame(master=window,width=500,height=330,bg="black")

#CREAMOS EL BOTÓN PAR EL ARCHIVO
loadfile = tk.Button(text="LOAD FILE",width=10,height=1,fg="aqua",bg="black")
loadfile.bind("<Button-1>",selectFile)
loadfile.place(x=20,y=190)

#CREAMOS UN LABEL STATUS PARA EL ARCHIVO
filesatus = tk.Label(text="NO FILE SELECTED...",foreground="lime",background="black",width=40,height=1,font=("Courier",10),anchor="w")
filesatus.place(x=130,y=190)

#CREAMOS OTRO LABEL DE INSTRUCCIONES
instC = tk.Label(text="SELECT OPERATION:",foreground="medium purple",background="black",height=2,font=("Courier",10),anchor="w")
instC.place(x=10,y=220)

#CREAMOS EL BOTÓN DE ENCRYPT Y DECRYPT
encbtn = tk.Button(text="ENCRYPT",width=10,height=1,fg="hot pink",bg="black")
encbtn.bind("<Button-1>",encryptText)
encbtn.place(x=20,y=265)
decbtn = tk.Button(text="DECRYPT",width=10,height=1,fg="hot pink",bg="black")
decbtn.bind("<Button-1>",decryptText)
decbtn.place(x=110,y=265)

frame.pack()
file = None
try:
	window.mainloop()
except KeyboardInterrupt:
	sys.exit()