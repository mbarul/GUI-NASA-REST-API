import tkinter as tk
import tkcalendar as tkc
from datetime import datetime
from B_GUI import DateButton


class Calendar(tk.Frame):
    """
    A class GUI of Calendar.
    Imported date button from B_GUI

    Attributes
    ----------
    self :
        represents the instance of the class

    Methods
    ----------
    grab_date : returning of date which we choosing by clicking at Calendar
    """

    def __init__(self):
        super(Calendar, self).__init__()
        # calendar
        self.cal = tkc.Calendar(selectmode='day', date_pattern='dd-mm-yyyy')
        self.cal.place(x=50, y=50)
        # place for date what we chose
        self.my_label = tk.Label(text='')
        self.my_label.place(x=140, y=250)
        # button to access date
        self.btn = DateButton('Grab', self.grab_date)
        self.a = self.grab_date()
        print(self.a)

    def grab_date(self):
        """
        Method for taking date from calendar
        :return: str
            variable - string
        """
        self.my_label.config(text=self.cal.get_date())
        b = self.my_label.cget("text")
        return b
