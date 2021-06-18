# -*- coding: utf8 -*-
import tkinter as tk
from tkinter import filedialog

from PIL import Image, ImageTk, ImageOps  # 画像データ用

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()

        self.master.title("画像の表示")       # ウィンドウタイトル
        self.master.geometry("400x300")     # ウィンドウサイズ(幅x高さ)
        
        # メニューの作成
        self.create_menu()

        # Canvasの作成
        self.back_color = "#008B8B" # 背景色
        self.canvas = tk.Canvas(self.master, bg = self.back_color)
        # Canvasを配置
        self.canvas.pack(expand = True, fill = tk.BOTH)

    def create_menu(self):
        # メニューバーの作成
        menubar = tk.Menu(self)

        # ファイル
        menu_file = tk.Menu(menubar, tearoff = False)
        menu_file.add_command(label = "画像ファイルを開く", command = self.menu_file_open_click, accelerator="Ctrl+O")
        menu_file.add_separator() # 仕切り線
        menu_file.add_command(label = "終了", command = self.master.destroy)
        # ショートカットキーの関連付け
        menu_file.bind_all("<Control-o>", self.menu_file_open_click)

        # メニューバーに各メニューを追加
        menubar.add_cascade(label="ファイル", menu = menu_file)

        # 親ウィンドウのメニューに、作成したメニューバーを設定
        self.master.config(menu = menubar)

    def menu_file_open_click(self, event=None):
        filename = filedialog.askopenfilename(
            title = "ファイルを開く",
            filetypes = [("Image file", ".bmp .png .jpg .tif"), ("Bitmap", ".bmp"), ("PNG", ".png"), ("JPEG", ".jpg"), ("Tiff", ".tif") ], # ファイルフィルタ
            initialdir = "./" # 自分自身のディレクトリ
            )
        # 画像の表示
        self.disp_image(filename)

    def disp_image(self, filename):
        '''画像をCanvasに表示する'''
        if not filename:
            return
        # PIL.Imageで開く
        pil_image = Image.open(filename)

        # キャンバスのサイズを取得
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        # 画像のアスペクト比（縦横比）を崩さずに指定したサイズ（キャンバスのサイズ）全体に画像をリサイズする
        pil_image = ImageOps.pad(pil_image, (canvas_width, canvas_height), color = self.back_color)

        #PIL.ImageからPhotoImageへ変換する
        self.photo_image = ImageTk.PhotoImage(image=pil_image)

        # 画像の描画
        self.canvas.create_image(
                canvas_width / 2,       # 画像表示位置(Canvasの中心)
                canvas_height / 2,                   
                image=self.photo_image  # 表示画像データ
                )

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()
