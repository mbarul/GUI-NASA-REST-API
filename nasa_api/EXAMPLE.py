# Use Tkinter for python 2, tkinter for python 3
import tkinter as tk


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.label = tk.Label(self, text='hi').pack()
        self.btn = AppButton(self)


class AppButton(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.btn = tk.Button(parent, text='Hi').pack()


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
