# import libs
import tkinter as tk

# taking classes from another files
from APOD_data import cosmos, title
from Buttons_GUI import AppButton, ExitButton
from Text_pole import Field
from Photo import Picture


class MainApplication(tk.Frame):
    """Main class where we put another classes"""

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.parent = parent
        self.field = Field(cosmos.title, 3, 1, 4, 15)
        self.field2 = Field(cosmos.explanation, 4, 1, 4)
        self.full_btn = AppButton("Full Photo", 1, 1)
        self.save_btn = AppButton("Save Photo", 1, 2)
        self.submit_btn = AppButton("Submit", 1, 3)
        self.exit_btn = ExitButton("Exit", 1, 4, parent)
        self.pict = Picture()


if __name__ == "__main__":
    root = tk.Tk()
    root.title(title)

    MainApplication(root)
    root.mainloop()
