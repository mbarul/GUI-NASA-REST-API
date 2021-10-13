import tkinter as tk
import tkcalendar as tkc
# import libs
import tkinter as tk
from io import BytesIO
from PIL import Image, ImageTk

# variable from APOD_data
from APOD_data import cosmos


root = tk.Tk()
top = tk.Toplevel()
img = Image.open(BytesIO(cosmos.picture.content))
img = img.resize((500, 350))
tkimage = ImageTk.PhotoImage(img)
lbl = tk.Label(top, image=tkimage).pack()
#
# def grab_date
#   my_label.config(text=cal.get_date())
#  queryDate = f'&date={cal.get_date()}&'
#  print(queryDate)


# cal = tkc.Calendar(selectmode='day', date_pattern='dd-mm-yyyy')
# cal.pack()
# btn = tk.Button(root, text='hi', command=grab_date)
# btn.pack()
# my_label = tk.Label(text='')
# my_label.pack()
# x = cal.get_date()
root.mainloop()
