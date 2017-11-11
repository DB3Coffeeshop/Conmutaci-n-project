from tkinter import *
from PIL import Image, ImageTk
import tkMessageBox
import getpass

class Bank:

    def __init__(self):
        self.master = Tk()
        self.stundent_frame = Frame(self.master, bd=2, relief="groove", width=700, height=320)
        self.configure()
        self.txt_student_name = Entry(self.stundent_frame)
        self.txt_student_code = Entry(self.stundent_frame)
        self.txt_student_card = Entry(self.stundent_frame)
        self.txt_student_lastname = Entry(self.stundent_frame)
        self.txt_stundent_career = Entry(self.stundent_frame)
        self.txt_student_phone = Entry(self.stundent_frame)
        self.make_formulary()
        self.master.mainloop()


    def configure(self):
        self.master.title("Inventory")
        self.master.geometry("900x550")
        self.master.resizable(0,0)
        self.master.configure(background='#dbe0df')
        self.stundent_frame.configure(background='#dbe0df')


    def make_formulary(self):
        self.stundent_frame.place(relx=0.05, rely=0.2)
        self.txt_student_card.place(relx=0.25, rely=0.1, width=120)
        self.txt_student_code.place(relx=0.75, rely=0.1, width=120)
        self.txt_student_name.place(relx=0.25, rely=0.3, width=120)
        self.txt_student_lastname.place(relx=0.75, rely=0.3, width=120)
        self.txt_stundent_career.place(relx=0.25, rely=0.5, width=120)
        self.txt_student_phone.place(relx=0.75 , rely=0.5, width=120)

        label_frame = Label(self.master, text="Loans", font=("Helvetica", 19), bg='#dbe0df', fg='black')
        label_frame.pack(pady=30)
        label_card_code = Label(self.stundent_frame, text="Card code", bg='#dbe0df', fg='black')
        label_stundent_code = Label(self.stundent_frame, text="Stundent code", bg='#dbe0df', fg='black')
        label_stundent_name = Label(self.stundent_frame, text="Name", bg='#dbe0df', fg='black')
        label_stundent_lastname = Label(self.stundent_frame, text="Last name", bg='#dbe0df', fg='black')
        label_student_career = Label(self.stundent_frame, text="Career", bg='#dbe0df', fg='black')
        label_stundent_phone = Label(self.stundent_frame, text="Phone", bg='#dbe0df', fg='black')

        btn_accept = Button(self.stundent_frame, text="Accept", highlightbackground='#dbe0df', width=10)
        btn_cancel = Button(self.stundent_frame, text="Cancel", highlightbackground='#dbe0df', width=10)
        btn_add = Button(self.stundent_frame, text="Add", highlightbackground='#dbe0df', width=10)


        label_card_code.place(relx=0.05, rely=0.1)
        label_stundent_code.place(relx=0.55, rely=0.1)
        label_stundent_name.place(relx=0.05, rely=0.3)
        label_stundent_lastname.place(relx=0.55, rely=0.3)
        label_student_career.place(relx=0.05, rely=0.5)
        label_stundent_phone.place(relx=0.55, rely=0.5)

        btn_accept.place(relx=0.053, rely=0.72)
        btn_cancel.place(relx=0.43, rely=0.72)
        btn_add.place(relx=0.77, rely=0.72)


if __name__ == "__main__":
    b = Bank()