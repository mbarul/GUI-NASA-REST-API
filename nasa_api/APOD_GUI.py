from tkinter import *
import tkinter as tk
from tkinter import ttk

from APOD_data import cosmos

print(cosmos.title)


root = Tk()

my_label = Label(root, text=f'{cosmos.title}')
my_label.pack()

root.mainloop()
