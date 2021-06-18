from tkinter import*
from PIL import ImageTk, Image
root = Tk()

myImage = ImageTk.PhotoImage(Image.open("camera.png"))

exitButton = Button(root, text="exit", command=root.quit).pack()

root.mainloop()