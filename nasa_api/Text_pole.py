# import libs
import tkinter as tk
import tkinter.ttk as ttk


class Field(ttk.Frame):
    """
        A class where with REST API we can describe our picture

        Attributes
        ----------
        text : str
            text inside in label
        grid_row : int
            position Y of label in main frame
        grid_col : int
            position X of label in main frame
        span : int
            how large can me label (X)
        size : int
            size of font in label

        Methods
        ----------
        .
        """

    def __init__(self, text, size=10):
        super().__init__()
        self.my_label = tk.Label(text=text, font=('Helvetica', size), relief='groove', wraplength=1000).pack(pady=10)
