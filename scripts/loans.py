from Tkinter import *
import MySQLdb
from PIL import Image, ImageTk
from student_loans import Loans
from student import Student
import tkMessageBox

class Register:

    def __init__(self):
        self.master = Tk()
        self.student_frame = Frame(self.master, bd=2, relief="groove", width=700, height=320)
        self.configure()
        self.txt_student_name = Entry(self.student_frame, state="disabled")
        self.txt_student_code = Entry(self.student_frame, state="disabled")
        self.txt_student_card = Entry(self.student_frame)
        self.txt_student_lastname = Entry(self.student_frame, state="disabled")
        self.txt_student_career = Entry(self.student_frame, state="disabled")
        self.txt_student_mail = Entry(self.student_frame, state="disabled")
        self.make_formulary()
        self.master.mainloop()


    def configure(self):
        self.master.title("Students")
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
        self.txt_student_mail.place(relx=0.75 , rely=0.5, width=120)

        label_frame = Label(self.master, text="Students", font=("Helvetica", 19), bg='#dbe0df', fg='black')
        label_frame.pack(pady=30)
        label_card_code = Label(self.student_frame, text="Card code", bg='#dbe0df', fg='black')
        label_student_code = Label(self.student_frame, text="Stundent code", bg='#dbe0df', fg='black')
        label_student_name = Label(self.student_frame, text="Name", bg='#dbe0df', fg='black')
        label_student_lastname = Label(self.student_frame, text="Last name", bg='#dbe0df', fg='black')
        label_student_career = Label(self.student_frame, text="Career", bg='#dbe0df', fg='black')
        label_student_mail = Label(self.student_frame, text="Mail", bg='#dbe0df', fg='black')

        btn_accept = Button(self.student_frame, text="Accept", highlightbackground='#dbe0df', width=10, command=self.button_accept)
        btn_cancel = Button(self.student_frame, text="Clear", highlightbackground='#dbe0df', width=10, command=self.button_clear)
        btn_add = Button(self.student_frame, text="Add", highlightbackground='#dbe0df', width=10, command=self.button_add)
        btn_loans = Button(self.master, text="Loans", highlightbackground='#dbe0df', width=10, command=self.loans)
        btn_exit = Button(self.master, text="Exit", highlightbackground='#dbe0df', width=10, command=self.go_back)


        label_card_code.place(relx=0.05, rely=0.1)
        label_student_code.place(relx=0.55, rely=0.1)
        label_student_name.place(relx=0.05, rely=0.3)
        label_student_lastname.place(relx=0.55, rely=0.3)
        label_student_career.place(relx=0.05, rely=0.5)
        label_student_mail.place(relx=0.55, rely=0.5)

        btn_add.place(relx=0.053, rely=0.72)
        btn_accept.place(relx=0.42, rely=0.72)
        btn_cancel.place(relx=0.77, rely=0.72)
        btn_loans.place(relx=0.85, rely=0.27)
        btn_exit.place(relx=0.85, rely=0.4)


    def button_clear(self):
        self.clean()
        self.txt_student_card['state'] = 'normal'
        self.txt_student_code['state'] = 'disabled'
        self.txt_student_name['state'] = 'disabled'
        self.txt_student_lastname['state'] = 'disabled'
        self.txt_student_career['state'] = 'disabled'
        self.txt_student_mail['state'] = 'disabled'

     
    def button_add(self):
        if self.txt_student_card.get() != "":
            self.txt_student_card['state'] = 'disabled'
            self.txt_student_code['state'] = 'normal'
            self.txt_student_name['state'] = 'normal'
            self.txt_student_lastname['state'] = 'normal'
            self.txt_student_career['state'] = 'normal'
            self.txt_student_mail['state'] = 'normal'
        
        else:
            tkMessageBox.showwarning("Error", "Please scan the card first")


    def button_accept(self):
        card_code = self.txt_student_card.get()
        student_code = self.txt_student_code.get()
        name = self.txt_student_name.get()
        last_name = self.txt_student_lastname.get()
        mail = self.txt_student_mail.get()
        career = self.txt_student_career.get()

        if card_code != "" and student_code != "" and name != "" and last_name != "" and mail != "" and career != "":
            self.add_student(name, last_name, mail, career, card_code, student_code)

        else:
            tkMessageBox.showwarning("Error", "Please fill al the places")


    def go_back(self):
        self.master.destroy()
        from frm_options import Main
        main = Main()
        
    
    def loans(self):
        if self.txt_student_card.get() != "":
            card = self.txt_student_card.get()

            db = self.connect_database()
            cursor = db.cursor()
            sql = "SELECT * FROM Students WHERE card_code=%s" % (str(card))
            cursor.execute(sql)

            try:
                data = cursor.fetchall()[0]
            except:
                data = []


            if len(data) > 0:
                student = Student(data[2], data[3], data[4], data[1], data[0], data[5])
                self.master.destroy()
                db.close()
                loans = Loans(student)
            else:
                tkMessageBox.showinfo("Not found", "Student with card %s doesn't exists" % (card))

        else:
            tkMessageBox.showerror("Error", "Please scan the card")


    def clean(self):
        self.txt_student_card.delete(0, END)
        self.txt_student_career.delete(0, END)
        self.txt_student_code.delete(0, END)
        self.txt_student_lastname.delete(0, END)
        self.txt_student_name.delete(0, END)
        self.txt_student_mail.delete(0, END)


    def connect_database(self):
        data_base = MySQLdb.connect("LocalHost", "root", "natalia1", "Eafit_Loans")
        data_base.autocommit(True)
        cursor = data_base.cursor()
        return data_base

    
    def add_student(self, name_student, last_name_student, mail_student, career_student, card_code_student, code_student):
        db = self.connect_database()
        cursor = db.cursor()
        sql = "INSERT INTO Students(student_code,card_code, name, last_name, mail, career) VALUES(%d, '%s', '%s', '%s', '%s', '%s')" % (int(code_student), str(card_code_student), str(name_student), str(last_name_student), str(mail_student), str(career_student))

        try:
            cursor.execute(sql)
            tkMessageBox.showinfo("Success", "Student %s has been added" % (name_student))
            self.clean()

        except MySQLdb.IntegrityError:
            tkMessageBox.showerror("Duplicate code", "Student with code %s already exists" % (card_code_student))
            db.rollback()

        except:
            tkMessageBox.showerror("Error", "Unexpected value error")
            db.rollback()

        db.close()

if __name__ == "__main__":
    b = Register()