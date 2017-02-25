#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
# This Script Is Created For http://bitforestinfo.blogspot.in
# This Script is Written By
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
try:
	import Tkinter
except:
	import tkinter as Tkinter

import time

class Message(Tkinter.Toplevel):
	def __init__(self,width=700,height=200,text="Copy To Clipboard",bg="white",font=('arial 20 bold italic')):
		Tkinter.Toplevel.__init__(self)
		self.font=font
		self.text=text
		self.bg=bg
		self.width=width
		self.height=height
		self.focus_force()
		self.overrideredirect(True)
		self.coordinate_position()
		self.creating_label()
		self.timer_is_starting()

	def creating_label(self):
		Tkinter.Label(self,text=self.text,bg=self.bg,font=self.font).pack(expand='yes',fill='both')
		return

	def coordinate_position(self):
		self.geometry("%dx%d+%d+%d" % (self.width,self.height,\
			self.winfo_screenwidth()/2-(self.width/2),\
			self.winfo_screenheight()/2-(self.height/2),\
			))
		return

	def timer_is_starting(self):
		x=1.0
		for i in range(110):
			time.sleep(0.02)
			self.update_idletasks()
			self.update()
			self.attributes('-alpha',x)
			x=x-0.01
		return

def main():
	#root=Tkinter.Tk()
	Message()
	#Tkinter.Button(root,text="Test",command=Message).pack()
	
	return

# Main Trigger
if __name__ == '__main__':
	main()
