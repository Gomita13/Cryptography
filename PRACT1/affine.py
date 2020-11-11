# -*- coding: utf-8 -*-
class Affine:

	def __init__(self):
		pass

	def gcd(self,a,b):
		if b == 0:
			return a
		return self.gcd(b,a%b)

	def egcd(self,a,b):
		x,y, u,v = 0,1, 1,0
		while a != 0: 
			q, r = b//a, b%a 
			m, n = x-u*q, y-v*q 
			b,a, x,y, u,v = a,r, u,v, m,n 
			gcd = b 
		return gcd, x, y 

	def ainv(self,a,n):
		gcd, x,y = self.egcd(a,n)
		return x%n

	def encryptText(self,text,a,b,n):
		etext = ""
		text = text.replace(' ','')
		for m in text:
			if m == '\n' or m == '\r':
				etext = etext + m
				continue
			c = ((a*ord(m))+b)%n
			etext = etext + chr(c)
		return etext

	def decryptText(self,etext,a,b,n):
		dtext = ""
		ai = self.ainv(a,n)
		bm = n-b
		for c in etext:
			if c == '\n' or c == '\r':
				dtext = dtext + c
				continue
			m = (ai*(ord(c)+bm))%n
			dtext = dtext + chr(m)
		return dtext

