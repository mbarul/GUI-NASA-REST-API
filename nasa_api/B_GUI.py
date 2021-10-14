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

    def __init__(self, text, x, y):
        super().__init__()
        self.btn = ttk.Button(text=text).place(relx=1, x=x, y=y, anchor='ne')

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
        self.btn = ttk.Button(text=text, command=parent.destroy).place(relx=1, x=-128, y=85, anchor='ne')


class DateButton(tk.Frame):
    def __init__(self, text, grab):
        super(DateButton, self).__init__()
        self.btn = tk.Button(text=text, command=grab)
        self.btn.place(x=152, y=275)


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
        self.btn = ttk.Button(text=text, command=self.open).place(relx=1, x=-240, y=50, anchor='ne')
        # configure style
        self.style = ttk.Style(self)
        self.style.configure('TButton', bg='yellow', font=('Helvetica', 10))

    @staticmethod
    def open():
        FullPhotoWindow()


