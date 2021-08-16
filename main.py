import tkinter as tk
import random

class Application(tk.Frame):
    # label Widgetの文字列情報を格納する変数
    var = None

    # おみくじリスト
    omikujiList = [
        '中吉',
        '凶',
        '小吉',
        '大吉',
    ]

    # おみくじを返す関数
    def getOmikuji(self):
        # random参考 : https://note.nkmk.me/python-random-randrange-randint/
        return self.omikujiList[random.randint(0, len(self.omikujiList) - 1)]

    # ボタンを選択した場合に、実行する関数
    def changeLabelText(self):
        self.var.set(self.getOmikuji())

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200")

        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素とした場合に、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # label Widgetの文字列情報をstring型の変数とする。
        # StringVarについて : https://kuroro.blog/python/K53voPjJuKFfYrjmP8FP/
        self.var = tk.StringVar()
        # label Widgetの文字列情報の初期化を行う。
        self.var.set(self.getOmikuji())

        # frame Widget(Frame)を親要素として、label Widgetを作成する。
        # textvariable : label Widgetへ文字列を表示する。値を可変なself.varとする。
        # width : 幅の設定
        # height : 高さの設定
        # bg : 背景色の設定
        # 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label = tk.Label(frame, textvariable=self.var, width=30, height=15, bg="green")
        # frame Widget(Frame)を親要素とした場合に、label Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        label.pack()

        # frame Widget(Frame)を親要素として、button Widgetを作成する。
        # text : テキスト情報
        # command : ボタンを選択した場合に、実行する関数を設定する。self.changeLabelTextとする。
        # Buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        button = tk.Button(frame, text='おみくじを引く', command=self.changeLabelText)
        # frame Widget(Frame)を親要素として、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        button.pack()

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    # Windowを生成する。
    # Windowについて : https://kuroro.blog/python/116yLvTkzH2AUJj8FHLx/
    root = tk.Tk()
    app = Application(master=root)

    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
