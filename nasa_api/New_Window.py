# import libs
import tkinter as tk
from Photo import Picture,FullPhoto


class FullPhotoWindow(tk.Frame):
    def __init__(self):
        super().__init__()
        self.top = tk.Toplevel()
        self.top.attributes('-fullscreen', True)
        self.top.title('FULL PHOTO')
        self.lbl = tk.Label(self.top, image=FullPhoto(900,650).tk_image, justify='center')
        self.lbl.pack(pady=8, ipady=10, ipadx=10)

        self.exit_btn = tk.Button(self.top, text='Close window', command=self.top.destroy).pack()
