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

    def __init__(self):
        super(Picture, self).__init__()
        self.img = Image.open(BytesIO(cosmos.picture.content))
        self.img = self.img.resize((500, 350))
        self.tkimage = ImageTk.PhotoImage(self.img)
        tk.Label(image=self.tkimage).grid(row=5, column=2, columnspan=4, rowspan=20, padx=5, pady=5)
