# import libs
import tkinter as tk
import tkinter.ttk as ttk

#
from New_Window import FullPhotoWindow


class AppButton(tk.Frame):
    """
    A class with we can create buttons and by click manipulate at App.

    Attributes
    ----------
    text : str
        text inside in button

    Methods
    ----------
    .
    """

    def __init__(self, text):
        super().__init__()
        self.btn = ttk.Button(text=text).pack(
            ipadx=5, ipady=5)

        # configure style
        self.style = ttk.Style(self)
        self.style.configure('TButton', bg='yellow', font=('Helvetica', 10))


class ExitButton(tk.Frame):
    """
    A class to exit our program

    Attributes
    ----------
    text : str
        text inside in button

    Methods
    ----------
    .
    """

    def __init__(self, text, parent):
        super().__init__()
        self.btn = ttk.Button(text=text, command=parent.destroy).pack(
            ipadx=5, ipady=5)


class DateButton(tk.Frame):
    def __init__(self, text, grab):
        super(DateButton, self).__init__()
        self.btn = tk.Button(text=text, command=grab)
        self.btn.pack(pady=(0, 40))


class OpenButton(tk.Frame):
    """
    A class with we can create buttons and by click manipulate at App.

    Attributes
    ----------
    text : str
        text inside in button


    Methods
    ----------
    .
    """

    def __init__(self, text):
        super().__init__()
        self.btn = ttk.Button(text=text, command=self.open).pack(
            ipadx=5, ipady=5)
        # configure style
        self.style = ttk.Style(self)
        self.style.configure('TButton', bg='yellow', font=('Helvetica', 10))

    def open(self):
        FullPhotoWindow()
