#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
# This is an Example Of Tkinter Canvas Graphics
# This Script Is Created For http://bitforestinfo.blogspot.in
# This Script is Written By
#
#
##################################################
######## Please Don't Remove Author Name #########
############### Thanks ###########################
##################################################
#
#
__author__='''

######################################################
                By S.S.B Group                          
######################################################

    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    http://bitforestinfo.blogspot.in/

    Note: We Feel Proud To Be Indian
######################################################
'''
# ----------- Importing Module --------------------------
import random,string

class number:
	def __init__(self, length=12,digit=True,uppercase=True,lowercase=True,symbol=True,punctuation=True,whitespace=0):
		self.length=length
		self.digit=digit
		self.uppercase=uppercase
		self.lowercase=lowercase
		self.symbol=symbol
		self.punctuation=punctuation
		self.whitespace=whitespace

	def generate(self):
		data=[]
		storeobj=[]
		if self.digit:
			storeobj.append(string.digits)
		if self.symbol:
			storeobj.append("#@&-_")
		if self.uppercase:
			storeobj.append(string.ascii_uppercase)
		if self.lowercase:
			storeobj.append(string.ascii_lowercase)
		if self.punctuation:
			storeobj.append(string.punctuation)
		if self.whitespace:
			storeobj.append(string.whitespace)
		for i in range(12):
			ch=random.choice(storeobj)
			data.append(str(random.choice(ch)))
		random.shuffle(data)
		password=''
		for i in data:
			password=password+i
		return password
		

if __name__ == '__main__':
	k=number()
	print (k.generate())