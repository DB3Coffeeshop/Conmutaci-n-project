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
        self.txt_student_card = Entry(self.student_frame)
        self.txt_student_lastname = Entry(self.student_frame, state="disabled")
        self.txt_student_career = Entry(self.student_frame, state="disabled")
        self.txt_student_phone = Entry(self.student_frame, state="disabled")
        self.make_formulary()
        self.master.mainloop()


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

        btn_accept = Button(self.student_frame, text="Accept", highlightbackground='#dbe0df', width=10, command=self.button_accept)
        btn_cancel = Button(self.student_frame, text="Clear", highlightbackground='#dbe0df', width=10, command=self.button_clear)
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


    def button_clear(self):
        self.txt_student_card['state'] = 'normal'
        self.txt_student_code['state'] = 'disabled'
        self.txt_student_name['state'] = 'disabled'
        self.txt_student_lastname['state'] = 'disabled'
        self.txt_student_career['state'] = 'disabled'
        self.txt_student_phone['state'] = 'disabled'
        self.clean()

     
    def button_add(self):
        if self.txt_student_card.get() != "":
            self.txt_student_card['state'] = 'disabled'
            self.txt_student_code['state'] = 'normal'
            self.txt_student_name['state'] = 'normal'
            self.txt_student_lastname['state'] = 'normal'
            self.txt_student_career['state'] = 'normal'
            self.txt_student_phone['state'] = 'normal'
        
        else:
            tkMessageBox.showwarning("Error", "Please scan the card first")


    def button_accept(self):
        card_code = self.txt_student_card.get()
        student_code = self.txt_student_code.get()
        name = self.txt_student_name.get()
        last_name = self.txt_student_lastname.get()
        phone = self.txt_student_phone.get()
        career = self.txt_student_career.get()

        if card_code != "" and student_code != "" and name != "" and last_name != "" and phone != "" and career != "":
            self.add_student(name, last_name, phone, career, card_code, student_code)

        else:
            tkMessageBox.showwarning("Error", "Please fill al the places")


    def clean(self):
        self.txt_student_card.delete(0, END)
        self.txt_student_career.delete(0, END)
        self.txt_student_code.delete(0, END)
        self.txt_student_lastname.delete(0, END)
        self.txt_student_name.delete(0, END)
        self.txt_student_phone.delete(0, END)


    def connect_database(self):
        data_base = MySQLdb.connect("LocalHost", "root", "natalia1", "GESTION")
        data_base.autocommit(True)
        cursor = data_base.cursor()
        return (data_base, cursor)

    
    def add_student(self, name_student, last_name_student, phone_student, career_student, card_code_student, code_student):
        cursor = self.connect_database()[1]
        db = self.connect_database()[0]
        sql = "INSERT INTO Student(card_code, student_code, name, last_name, phone, career) VALUES(%d, %d, '%s', '%s', %d, '%s')" % (int(card_code_student), int(code_student), str(name_student), str(last_name_student), int(phone_student), str(career_student))

        try:
            cursor.execute(sql)
            tkMessageBox.showinfo("Success", "Student %s has been added" % (name_student))
            self.clean()

        except MySQLdb.IntegrityError:
            tkMessageBox.showerror("Duplicate code", "Student already exists")
            db.rollback()

        except:
            tkMessageBox.showerror("Error", "Unexpected value error")
            db.rollback()

        db.close()




if __name__ == "__main__":
    b = Bank()