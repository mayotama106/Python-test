#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import Tkinter

#
# GUI設定
#
root = Tkinter.Tk()
root.title(u"TkinterのCanvasを使ってみる")
root.geometry("800x450")

#キャンバスエリア
canvas = Tkinter.Canvas(root, width = 800, height = 450)#Canvasの作成
canvas.create_rectangle(0, 0, 800, 450, fill = 'green')#塗りつぶし

#キャンバスバインド
canvas.place(x=0, y=0)#Canvasの配置


#
# GUIの末端
#
root.mainloop()