import tkinter as tk
import tkcalendar as tkc
from datetime import datetime
from Buttons_GUI import DateButton


class Calendar(tk.Frame):
    def __init__(self, grid_r, grid_c):
        super(Calendar, self).__init__()
        self.cal = tkc.Calendar(selectmode='day', date_pattern='dd-mm-yyyy')
        self.cal.grid(row=grid_r, column=grid_c)
        self.btn = DateButton('Grab', self.grab_date, 5, 1)
        self.my_label = tk.Label(text='')
        self.my_label.grid(row=6, column=1)

    def grab_date(self):
        self.my_label.config(text=self.cal.get_date())


# calendar = Calendar()
# root.mainloop()

