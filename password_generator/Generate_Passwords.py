#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
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
print (__author__)
# Importing Module 
try:
	import Tkinter,ttk
except Exception as e:
	print e
	import tkinter as Tkinter
	import tkinter.ttk as ttk

from toolkit import numbergenerator as ng
from toolkit import notification as nt

# Creating Main Class
class Window(Tkinter.Tk):
	def __init__(self, *args, **kwargs):
		Tkinter.Tk.__init__(self, *args, **kwargs)
		self['padx']=10
		self['pady']=10
		self.creating_password_panel()
		self.creating_input_panels()

	def creating_password_panel(self):
		self.Password=Tkinter.StringVar()
		self.PasswordLength=Tkinter.IntVar()
		self.PasswordLength.set(12)
		frame=Tkinter.LabelFrame(self,text='Password')
		frame.pack(side='left',expand='yes',fill='both')
		frame['padx']=5
		frame['pady']=5
		Tkinter.Entry(frame,textvariable=self.Password).pack(side='top',fill='x')
		Tkinter.Button(frame,text='Generate', command=self.generate_pass).pack(side='top',fill='x')
		Tkinter.Button(frame,text='Copy To Clipboard', command=self.copy_to_clipboard).pack(side='top',fill='x')
		frame1=Tkinter.LabelFrame(frame,text='Password Length')
		frame1.pack(side='top',expand='yes',fill='both',pady=5,padx=5,ipadx=5,ipady=5)
		Tkinter.Spinbox(frame1,from_=0,to_=100,textvariable=self.PasswordLength).pack()
		return

	def copy_to_clipboard(self):
		pas=self.Password.get()
		self.clipboard_clear()
		self.clipboard_append(pas)
		nt.Message()
		return

	def generate_pass(self):
		pasg=ng.number(\
			length=self.PasswordLength.get(),\
			digit=self.answer[0].get(),\
			uppercase=self.answer[1].get(),\
			lowercase=self.answer[2].get(),\
			symbol=self.answer[3].get(),\
			punctuation=self.answer[4].get(),\
			whitespace=self.answer[5].get()\
			)
		self.Password.set(pasg.generate())
		return

	def creating_input_panels(self):
		frame=Tkinter.LabelFrame(self,text='Panel')
		frame.pack(side='left')
		frame['padx']=10
		frame['pady']=10
		self.answer=[]
		l=18
		for i in ['Digits','Uppercase','Lowercase','Symbol','Punctuation','Whitespace']:
			i=' '*(l-len(i))+i
			var=Tkinter.IntVar()
			var.set(1)
			Tkinter.Checkbutton(frame,text=i,variable=var).pack(side='top',expand='yes',fill='both')
			self.answer.append(var)
		var.set(0)
		return
# main trigger
#if __name__ == '__main__':
	#
Window(className=" Password Generator").mainloop()
