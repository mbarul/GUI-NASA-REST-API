import tkinter as tk
import tkcalendar as tkc

root = tk.Tk()


def grab_date():
    my_label.config(text=cal.get_date())
    queryDate = f'&date={cal.get_date()}&'
    print(queryDate)


cal = tkc.Calendar(selectmode='day', date_pattern='dd-mm-yyyy')
cal.pack()
btn = tk.Button(root, text='hi', command=grab_date)
btn.pack()
my_label = tk.Label(text='')
my_label.pack()
x = cal.get_date()
root.mainloop()
