from Tkinter import *
from ttk import *

class App:

    def __init__(self):
        self.master = Tk()
        self.combo = Combobox(self.master, state="readonly")
        self.combo['values'] = ['santi', 'es', 'gay']
        self.combo.pack()
        self.master.mainloop()


a = App()