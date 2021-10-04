import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

from APOD_data import cosmos, title

# root = tk.Tk()
# root.title(title)
# root.geometry('500x500')


import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.field = Field(cosmos.title)
        self.field2 = Field(cosmos.explanation)


class Field(tk.Frame):
    def __init__(self, text):
        super().__init__()
        self.my_label = tk.Label(text=text, relief='groove', wraplength=300).pack()


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

# class TextField(Field):
#   def __init__(self, text):
#      super().__init__()


# class AppButton(tk.Tk):
#  def __init__(self, master, text, grid_r, grid_c):
#      super().__init__()
#      self.btn = tk.Button(master, text=text).grid(row=grid_r, column=grid_c)


# TextField(root, cosmos.explanation, 5, 1)

# my_label = Field(root, cosmos.title, 4, 1)
# my_label2 = tk.Label(root, text=cosmos.explanation, relief='groove', wraplength=300).grid(row=5, column=1)
# submit_btn = AppButton(root, "Submit", 1, 3)
# full_btn = AppButton(root, "Full Photo", 2, 3)
# save_btn = AppButton(root, "Save Photo", 3, 3)
# exit_btn = AppButton(root, "Exit", 4, 3)

root.mainloop()
