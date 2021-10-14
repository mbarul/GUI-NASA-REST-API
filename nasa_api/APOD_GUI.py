# import libs
import tkinter as tk

# taking classes from another files
from APOD_data import cosmos, title
from B_GUI import AppButton, ExitButton, OpenButton
from Text_pole import Field
from Photo import Picture, FullPhoto
from Calendar import Calendar


class MainApplication(tk.Frame):
    """Main class where we put another classes
   """

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.parent = parent
        self.field = Field(cosmos.title)
        self.field2 = Field(cosmos.explanation)
        self.full_btn = OpenButton("Full Photo")
        self.save_btn = AppButton("Save Photo", -128, 50)
        self.submit_btn = AppButton("Submit", -20, 50)
        self.exit_btn = ExitButton("Exit", parent)
        self.pict = Picture(500, 350)
        self.calendar = Calendar()


if __name__ == "__main__":
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.title(title)
    MainApplication(root)
    tk.mainloop()
