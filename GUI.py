import tkinter
from tkinter import messagebox
from tkinter import *

top = tkinter.Tk()

progOne = tkinter.Progressbar(top, orient = HORIZONTAL, length = 100, mode ='determinate')

def OnButtonPress():
	tkinter.messagebox.showinfo("you killed a turtle")
	progOne.pack()
	progOne["value"] += 10


B = tkinter.Button(top, text="add plastic", command = OnButtonPress)
B.pack()

top.mainloop()