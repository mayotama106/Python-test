from tkinter import*
root = Tk()


#text
mylabel = Label(root, text="hello world")
#put into the screen
#1  mylabel.pack()<- dont fix element

mylabel.grid(row=0, column=0)

root.mainloop()