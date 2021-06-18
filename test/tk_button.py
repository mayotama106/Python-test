from tkinter import*
from PIL import ImageTk, Image
root = Tk()

def myClick():
  mylabel = Label(root, text="great!").pack()

myButton = Button(root, text="click me", width=50, height=10 , command=myClick).pack()
exitButton = Button(root, text="exit", command=root.quit).pack()

root.mainloop()