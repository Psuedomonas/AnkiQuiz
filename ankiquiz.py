'''
Author: Nicholas A Zehm
Filename: ankiquiz.py
7-11-20

TODO: Switch to frames?
Haven't done multi-file or header/cpp style coding for a while. I intend to do that but not arbitrarily
'''

from tkinter import * #GUI
import random #random numbers

class Window(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master=None)
		self.master = master
		self.init_window()
	
	def init_window(self):
		self.master.title("Word to the Perd")
		self.pack(fill=BOTH, expand=1)
		
		#menu
		menu = Menu(self.master)
		self.master.config(menu=menu)
		mainMenu = Menu(menu)
		
		#Menu options
		mainMenu.add_command(label="Quess the word", command=)
		mainMenu.add_command(label="Define the word", command=)
		mainMenu.add_command(label="Match dem up", command=)
		mainMenu.add_command(label="Exit", command=lambda : self.client_exit)
		
		menu.add_cascade(label=Main menu", menu=mainMenu)
		
		text = Text(root)
		
	def client_exit(self):
		exit()

root = Tk()
root.geometry("800x600)
app = Window(root)
root.mainloop()
