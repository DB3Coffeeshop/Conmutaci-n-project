from Tkinter import *
import MySQLdb
from student import Student
import tkMessageBox
from article import Article
from datetime import date


class Loans:

    def __init__(self, student):
        self.list_articles = []
        self.student = student
        self.master = Tk()
        self.article_frame = Frame(self.master, bd=5, relief="groove", width=400, height=400)
        self.loans_frame = Frame(self.master, bd=5, relief="groove", width=200, height=200)
        self.configure()
        self.make_list_articles()
        self.make_loans_frame()
        self.student_loans_list()
        self.master.mainloop()


    def configure(self):
        self.master.title("Loans")
        self.head = StringVar()
        title = Label(self.master, textvariable=self.head, bg='#dbe0df', font=("Cursive", 19))
        self.head.set("%s %s" % (self.student.name, self.student.last_name))
        title.pack()
        self.article_frame.pack(side=RIGHT, padx=30)
        self.loans_frame.pack(side=LEFT, padx=30)
        self.master.geometry("900x500")
        self.master.resizable(0,0)
        self.loans_frame.configure(background='#dbe0df')
        self.master.configure(background='#dbe0df')
        self.article_frame.configure(background='#dbe0df')


    def connect(self):
        data_base = MySQLdb.connect("LocalHost", "root", "natalia1", "Eafit_Loans")
        data_base.autocommit(True)
        return data_base


    def fill_list(self, list_articles):
        for article in list_articles:
            self.list.insert(END, article)


    def make_list_articles(self):
        self.list = Listbox(self.article_frame, selectborderwidth=5)

        title = Label(self.article_frame, text="Articles", bg='#dbe0df')
        self.btn_add = Button(self.article_frame, text="Add", highlightbackground='#dbe0df', command=self.add_button)
        lbl_quantity = Label(self.article_frame, text="quantity", font=("Cursive", 10), bg='#dbe0df')
        self.txt_quantity = Entry(self.article_frame, bd=5, text="Quantity here")

        self.btn_add.pack(side=BOTTOM)
        self.txt_quantity.pack(side=BOTTOM, pady=10)
        lbl_quantity.pack(side=BOTTOM, pady=10)
        title.pack()

        db = self.connect()
        cursor = db.cursor()
        sql = "SELECT name FROM Materials WHERE stock>0"
        cursor.execute(sql)
        data = cursor.fetchall()

        self.fill_list(data)

        self.list.pack()

        db.close()


    def make_loans_frame(self):
        self.list_loans = Listbox(self.loans_frame, selectborderwidth=5)
        self.list_new_loans = Listbox(self.loans_frame, selectborderwidth=5)
        self.list_loans.pack(side=LEFT, padx=30)
        self.list_new_loans.pack(side=RIGHT, padx=30, pady=30)

        self.btn_accept = Button(self.master, text="Accept", highlightbackground='#dbe0df', width=10, command=self.accept_button)
        self.btn_cancel = Button(self.master, text="Cancel", highlightbackground='#dbe0df', width=10, command=self.cancel_button)
        btn_exit = Button(self.master, text="exit", highlightbackground='#dbe0df', width=10, command=self.go_back)

        lbl_current_loans = Label(self.master, text="Student Loans", bg='#dbe0df')
        lbl_loans = Label(self.master, text="Current loans", bg='#dbe0df')

        lbl_current_loans.place(relx=0.12, rely=0.2)
        lbl_loans.place(relx=0.41, rely=0.2)
        self.btn_accept.place(relx=0.07, rely=0.9)
        self.btn_cancel.place(relx=0.27, rely=0.9)
        btn_exit.place(relx=0.47, rely=0.9)


    def get_item(self, list_box):
        return (list_box.get(ACTIVE), list_box.index(ACTIVE))


    def add_button(self):
        if self.txt_quantity.get() != "" and int(self.txt_quantity.get()) > 0:
            db = self.connect()
            cursor = db.cursor()
            sql = "SELECT * FROM Materials WHERE name='%s'" % (self.get_item(self.list)[0])
            cursor.execute(sql)
            data_sql = cursor.fetchall()[0]

            if int(data_sql[4]) > int(self.txt_quantity.get()):
                data = self.get_item(self.list)[0]
                self.list_new_loans.insert(END, data)
                self.list.delete(self.get_item(self.list)[1])
                article = Article(int(data_sql[0]), data_sql[1], data_sql[2], data_sql[3], int(data_sql[4]))
                self.list_articles.append((article, self.txt_quantity.get()))
                self.txt_quantity.delete(0, END)

            else:
                tkMessageBox.showerror("No stock", "Error, article stock: %d" % (int(data_sql[4])))
        else:
            tkMessageBox.showerror("Error", "Please enter a positive integer")


    def fill_list_loans(self):
        self.list_new_loans.delete(0, END)

        for article in self.list_articles:
            self.list_loans.insert(END, article[0].name_article)


    def accept_button(self):
        db = self.connect()

        if len(self.list_articles) > 0:
            cursor = db.cursor()

            for article in self.list_articles:
                sql_student = "SELECT student_code FROM Students WHERE student_code=%d" % (int(self.student.stundent_code))
                cursor.execute(sql_student)
                student_code = cursor.fetchall()[0][0]
                sql_article = "SELECT id_Materials FROM Materials WHERE id_Materials=%d" % (int(article[0].id_article))
                cursor.execute(sql_article)
                id_material = cursor.fetchall()[0][0]

                try:
                    sql = "INSERT INTO Loan(student_code, material, cant, date, status) VALUES(%d, %d, %d, '%s', %d)" % (student_code, id_material, int(article[1]), date.today(), 1)
                    cursor.execute(sql)

                    sql_stock = "UPDATE Materials SET stock = stock - %d WHERE id_Materials=%d" % (int(article[1]), id_material)
                    cursor.execute(sql_stock)

                except:
                    tkMessageBox.showerror("Error", "Unexpected error")

        self.fill_list_loans()
        self.success()
        db.close()


    def success(self):
        self.head.set("Success")
        self.btn_add['state'] = 'disabled'
        self.btn_accept['state'] = 'disabled'
        self.btn_cancel['state'] = 'disabled'
    
    
    def student_loans_list(self):
        data_base = self.connect()
        cursor = data_base.cursor()
        sql = "SELECT Materials.name FROM Loan INNER JOIN Materials ON Loan.material = Materials.id_Materials WHERE student_code=%d" % (int(self.student.stundent_code))
        cursor.execute(sql)
        data = cursor.fetchall()

        for current in range(len(data)):
            self.list_loans.insert(END, data[current][0])

        data_base.close()


    def go_back(self):
        from loans import Register
        if len(self.list_articles) > 0:
            answer = tkMessageBox.askquestion("Exit", "Are you sure")

            if answer == 'yes':
                self.master.destroy()
                student_frame = Register()

        else:
            self.master.destroy()
            student_frame = Register()


    def cancel_button(self):
        self.list_new_loans.delete(0, END)
        self.list_articles = []



if __name__ == "__main__":
    andres = Student("Andres", "Pulgarin", 12313, 123231, "pulga", "sistemas")
    l = Loans(andres)