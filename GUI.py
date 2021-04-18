import tkinter

top = tkinter.Tk()

def OnButtonPress():
	tkinter.messagebox.showinfo("you killed a turtle")

B = tkinter.Button(top, text="add plastic", command = OnButtonPress)
B.pack()

top.mainloop()