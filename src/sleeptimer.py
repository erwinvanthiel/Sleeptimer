#!/usr/bin/env python3
import subprocess
import tkinter
from timer import sec_timer

class Gui:

	def __init__(self):

		self.root = tkinter.Tk()
		self.root.geometry("500x300") #You want the size of the app to be 500x500
		self.root.resizable(0, 0) #Don't allow resizing in the x or y direction
		self.root.title('Sleeptimer')
		self.topframe = tkinter.Frame(self.root)
		self.bottomframe = tkinter.Frame(self.root)
		self.inputtext = tkinter.Text(self.bottomframe, width=20, height=1) 
		self.timer = tkinter.Label(self.topframe, text='00:00', fg='black')
		self.button = tkinter.Button(self.bottomframe, text="start", command=self.start)


	def setup_window(self):
		self.topframe.pack()
		self.bottomframe.pack()
		self.inputtext.pack()
		self.button.pack()
		self.timer.pack()
		self.root.mainloop()

	def start(self):
		try:
			timervalue = int(self.inputtext.get('1.0'))
			shutdown(str(timervalue))
			sec_timer(self.update_label, timervalue)
		except ValueError:
			print("not a number")
			self.inputtext.delete(1.0, tkinter.END)

	def update_label(self, content):
		print (content)
		self.timer.config(text=str(content))
		self.root.update()


def shutdown(timer):

	command = ['shutdown','-h',timer]
	#o = subprocess.check_output(command, shell=True)

gui = Gui()
gui.setup_window()
