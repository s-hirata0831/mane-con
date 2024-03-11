import tkinter as tk
import customtkinter
import os
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

FONT_TYPE = "meiryo"

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # メンバー変数の設定
        self.fonts = (FONT_TYPE, 15, "bold")
        self.smallFonts= (FONT_TYPE, 10)
        self.corner= (50)
        #タイトルバーの非表示
        self.wm_overrideredirect(True)

        # フォームのセットアップをする
        self.setup_form()
    
    def setup_form(self):
        # CustomTkinter のフォームデザイン設定
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("green")

        # フォームサイズ設定
        self.geometry("1024x600")
        self.title("Magical Present Box")

        #行方向のマスのレイアウトを設定
        self.grid_rowconfigure(0)
        #列方向のマスのレイアウトを設定
        self.grid_columnconfigure(0)

        #全体の背景色設定
        self.config(bg="#e3e3e3")

        #タイトル画面へ移行
        self.title_frame()

#タイトル画面(画面01)========================================================================
    def title_frame(self):
        #クローズボタン
        self.closeB = customtkinter.CTkButton(master=self, text="Close", command=self.destroy,font=self.smallFonts,width=10, height=5, corner_radius=self.corner, text_color="yellow")
        self.closeB.place(x = 10, y = 10)
        
        #タイトル画像
        self.title_image()

        #交換開始ボタン
        self.exchangeB = customtkinter.CTkButton(master=self, text="交換する！", command=self.go_to_openBox,font=self.fonts,width=220, height=50, corner_radius=self.corner, text_color="white")
        self.exchangeB.place(relx = 0.5, y = 500, anchor="center")

        #サンタ画像
        self.santa_image()

        #プレゼントイメージ画像
        self.present_image()

    def title_image(self):
        #画像の読み込み
        self.image_path = os.path.join(os.path.dirname(__file__), R"./cu.png")
        self.image = Image.open(self.image_path)
        self.image = ImageTk.PhotoImage(self.image)
        #キャンバスの作成
        self.canvas = customtkinter.CTkCanvas(master=self, width=self.image.width()-5, height=self.image.height()-5, bd=0)
        self.canvas.place(x=50, y=50, anchor="nw")
        #キャンバスに画像を描画
        self.canvas.create_image( 50,50, image = self.image, anchor="nw")

    def santa_image(self):
        #画像の読み込み
        self.santa_path = os.path.join(os.path.dirname(__file__), R"./cu.png")
        self.santa = Image.open(self.santa_path)
        self.santa = ImageTk.PhotoImage(self.santa)
        #キャンバスの作成
        self.santa_canvas = customtkinter.CTkCanvas(master=self, width=self.santa.width()-1, height=self.santa.height()-1, bd =0)
        self.santa_canvas.place(x=50, y=250, anchor="nw")
        #キャンバスに画像を描画
        self.santa_canvas.create_image(0,0,image=self.santa, anchor="nw")

    def present_image(self):
        #画像の読み込み
        self.present_path = os.path.join(os.path.dirname(__file__), R"./cu.png")
        self.present = Image.open(self.present_path)
        self.present = ImageTk.PhotoImage(self.present)
        #キャンバスの作成
        self.present_canvas = customtkinter.CTkCanvas(master=self, width=self.present.width()-1, height=self.present.height()-1, bd =0)
        self.present_canvas.place(x=780, y=468, anchor="nw")
        #キャンバスに画像を描画
        self.present_canvas.create_image(0,20,image=self.present, anchor="nw")

#プレゼント入れる(02)========================================================================
    def go_to_openBox(self):
        self.canvas.destroy()
        self.santa_canvas.destroy()
        self.present_canvas.destroy()
        self.closeB.destroy()
        self.exchangeB.destroy()
        self.openBox_frame()

    def openBox_frame(self):
        #交換開始ボタン
        self.inPresent = customtkinter.CTkButton(master=self, text="交換する！",command=self.destroy, font=self.fonts,width=220, height=50, corner_radius=self.corner, text_color="white")
        self.inPresent.place(relx = 0.5, y = 500, anchor="center")

if __name__ == "__main__":
    # アプリケーション実行
    app = App()
    app.mainloop()