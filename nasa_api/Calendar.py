import tkinter as tk
import tkcalendar as tkc
from datetime import datetime
from B_GUI import DateButton


class Calendar(tk.Frame):
    def __init__(self):
        super(Calendar, self).__init__()
        self.cal = tkc.Calendar(selectmode='day', date_pattern='dd-mm-yyyy')
        self.cal.pack()
        self.my_label = tk.Label(text='')
        self.my_label.pack(pady=5)
        self.btn = DateButton('Grab', self.grab_date)

    def grab_date(self):
        self.my_label.config(text=self.cal.get_date())
