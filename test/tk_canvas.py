#-*- coding: utf-8 -*-
import sys
import Tkinter

#
# GUI設定
#
root = Tkinter.Tk()
root.title(u"TkinterのCanvasを使ってみる")
root.geometry("800x450")

#キャンバスエリア
canvas = Tkinter.Canvas(root, width = 800, height = 450)

#キャンバスバインド
canvas.place(x=0, y=0)


#
# GUIの末端
#
root.mainloop()