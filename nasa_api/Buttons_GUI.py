# import libs
import tkinter as tk
import tkinter.ttk as ttk


class AppButton(tk.Frame):
    """
    A class with we can create buttons and by click manipulate at App.

    Attributes
    ----------
    text : str
        text inside in button
    grid_row : int
        position Y of button in main frame
    grid_col : int
        position X of button in main frame

    Methods
    ----------
    .
    """

    def __init__(self, text, grid_row, grid_col):
        super().__init__()
        self.btn = ttk.Button(text=text).grid(row=grid_row, column=grid_col, padx=5, pady=5,
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
    grid_row : int
        position Y of button in main frame
    grid_col : int
        position X of button in main frame

    Methods
    ----------
    .
    """

    def __init__(self, text, grid_row, grid_col, parent):
        super(ExitButton, self).__init__()
        self.btn = ttk.Button(text=text, command=parent.destroy).grid(row=grid_row, column=grid_col, padx=5, pady=5,
                                                                      ipadx=5, ipady=5)


class DateButton(tk.Frame):
    def __init__(self, text, grab, grid_r, grid_c):
        super(DateButton, self).__init__()
        self.btn = tk.Button(text=text, command=grab)
        self.btn.grid(row=grid_r, column=grid_c)
