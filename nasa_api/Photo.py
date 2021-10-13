# import libs
import tkinter as tk
from io import BytesIO
from PIL import Image, ImageTk

# variable from APOD_data
from APOD_data import cosmos


class Picture(tk.Frame):
    """
        A class to get picture from NASA API.
        Astronomy picture of day
    """

    def __init__(self, h, w):
        super().__init__()
        self.img = Image.open(BytesIO(cosmos.picture.content))
        self.img = self.img.resize((h, w))
        self.tk_image = ImageTk.PhotoImage(self.img)
        tk.Label(image=self.tk_image).pack()


class FullPhoto(Picture):
    def __init__(self, h, w):
        super().__init__(h, w)
