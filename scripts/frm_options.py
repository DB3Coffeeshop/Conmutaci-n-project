from Tkinter import *
from loans import Bank
from PIL import Image, ImageTk
import tkMessageBox


class Main:
     
    def __init__(self):
         self.master = Tk()
         self.configure()
         self.make_frame()
         self.master.mainloop()


    def configure(self):
        self.master.title("Options")
        self.master.geometry = ("900x200")
        self.master.resizable(0,0)
        self.master.configure(background='#dbe0df')


    def make_frame(self):
        image_students = self.set_image("Estudiantes.png")
        image_inventory = self.set_image("Inventario.png")
        image_exit = self.set_image("Salida.png")

        title_students = Label(self.master, text="Stundents", bg='#dbe0df', fg='black')
        title_inventory = Label(self.master, text="Inventory", bg='#dbe0df', fg='black')
        title_exit = Label(self.master, text="Exit", bg='#dbe0df', fg='black')

        button_stundents = Button(self.master, image=image_students, highlightbackground='#deefed' , command=self.open_students_frame)
        button_inventory = Button(self.master, image=image_inventory, highlightbackground='#deefed')
        button_exit = Button(self.master, image=image_exit, highlightbackground='#deefed', command=self.go_back)

        button_stundents.image = image_students
        button_exit.image = image_exit
        button_inventory.image = image_inventory

        title_exit.pack(side=LEFT)
        title_inventory.place(relx=0.60, rely=0.92)
        title_students.place(relx=0.60, rely=0)

        button_exit.pack(side=LEFT)
        button_inventory.pack(side=BOTTOM, padx=100, pady=30)
        button_stundents.pack(padx=100, pady=30)
        

    def set_image(self, dir):
        image = ImageTk.PhotoImage(Image.open(str(dir)))
        return image


    def open_students_frame(self):
        self.master.destroy()
        students_frame = Bank()


    def go_back(self):
        answer = tkMessageBox.askquestion("Exit", "Are you sure?")

        if answer == "yes":
            self.master.destroy()
        else:
            pass
        

if __name__ == "__main__":
    print "adsasd"
    main = Main()