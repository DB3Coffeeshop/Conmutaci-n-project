from tkinter import *
import MySQLdb
from PIL import Image, ImageTk
import tkMessageBox
import getpass

class Bank:

    def __init__(self):
        self.master = Tk()
        self.student_frame = Frame(self.master, bd=2, relief="groove", width=700, height=320)
        self.configure()
        self.txt_student_name = Entry(self.student_frame, state="disabled")
        self.txt_student_code = Entry(self.student_frame, state="disabled")
        self.txt_student_card = Entry(self.student_frame, state="disabled")
        self.txt_student_lastname = Entry(self.student_frame, state="disabled")
        self.txt_student_career = Entry(self.student_frame, state="disabled")
        self.txt_student_phone = Entry(self.student_frame, state="disabled")
        self.make_formulary()
        self.master.mainloop()


    def connect_database(self):
        db = MySQLdb.connect("LocalHost", "root", "natalia1", "COMPENSAR")

    def configure(self):
        self.master.title("Inventory")
        self.master.geometry("900x550")
        self.master.resizable(0,0)
        self.master.configure(background='#dbe0df')
        self.student_frame.configure(background='#dbe0df')


    def make_formulary(self):
        self.student_frame.place(relx=0.05, rely=0.2)
        self.txt_student_card.place(relx=0.25, rely=0.1, width=120)
        self.txt_student_code.place(relx=0.75, rely=0.1, width=120)
        self.txt_student_name.place(relx=0.25, rely=0.3, width=120)
        self.txt_student_lastname.place(relx=0.75, rely=0.3, width=120)
        self.txt_student_career.place(relx=0.25, rely=0.5, width=120)
        self.txt_student_phone.place(relx=0.75 , rely=0.5, width=120)

        label_frame = Label(self.master, text="Loans", font=("Helvetica", 19), bg='#dbe0df', fg='black')
        label_frame.pack(pady=30)
        label_card_code = Label(self.student_frame, text="Card code", bg='#dbe0df', fg='black')
        label_student_code = Label(self.student_frame, text="Stundent code", bg='#dbe0df', fg='black')
        label_student_name = Label(self.student_frame, text="Name", bg='#dbe0df', fg='black')
        label_student_lastname = Label(self.student_frame, text="Last name", bg='#dbe0df', fg='black')
        label_student_career = Label(self.student_frame, text="Career", bg='#dbe0df', fg='black')
        label_student_phone = Label(self.student_frame, text="Phone", bg='#dbe0df', fg='black')

        btn_accept = Button(self.student_frame, text="Accept", highlightbackground='#dbe0df', width=10)
        btn_cancel = Button(self.student_frame, text="Cancel", highlightbackground='#dbe0df', width=10, command=self.button_cancel)
        btn_add = Button(self.student_frame, text="Add", highlightbackground='#dbe0df', width=10, command=self.button_add)


        label_card_code.place(relx=0.05, rely=0.1)
        label_student_code.place(relx=0.55, rely=0.1)
        label_student_name.place(relx=0.05, rely=0.3)
        label_student_lastname.place(relx=0.55, rely=0.3)
        label_student_career.place(relx=0.05, rely=0.5)
        label_student_phone.place(relx=0.55, rely=0.5)

        btn_add.place(relx=0.053, rely=0.72)
        btn_accept.place(relx=0.42, rely=0.72)
        btn_cancel.place(relx=0.77, rely=0.72)


    def button_cancel(self):
        self.txt_student_card['state'] = 'disabled'
        self.txt_student_code['state'] = 'disabled'
        self.txt_student_name['state'] = 'disabled'
        self.txt_student_lastname['state'] = 'disabled'
        self.txt_student_career['state'] = 'disabled'
        self.txt_student_phone['state'] = 'disabled'

     

    def button_add(self):
        self.txt_student_card['state'] = 'normal'
        self.txt_student_code['state'] = 'disabled'
        self.txt_student_name['state'] = 'disabled'
        self.txt_student_lastname['state'] = 'disabled'
        self.txt_student_career['state'] = 'disabled'
        self.txt_student_phone['state'] = 'disabled'





if __name__ == "__main__":
    b = Bank()