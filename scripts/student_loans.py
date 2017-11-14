from Tkinter import *
import MySQLdb
from student import Student

class Loans:

    def __init__(self, student):
        self.student = student
        self.master = Tk()
        self.article_frame = Frame(self.master, bd=5, relief="groove", width=400, height=400)
        self.loans_frame = Frame(self.master, bd=5, relief="groove", width=200, height=200)
        self.configure()
        self.make_list_articles()
        self.make_loans_frame()
        self.master.mainloop()

    def configure(self):
        self.master.title("Loans")
        title = Label(self.master, text="%s %s" % (self.student.name, self.student.last_name), bg='#dbe0df', font=("Cursive", 19))
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
        return data_base


    def make_list_articles(self):
        self.list = Listbox(self.article_frame, selectborderwidth=5)

        title = Label(self.article_frame, text="Articles", bg='#dbe0df')
        btn_aceptar = Button(self.article_frame, text="Add", highlightbackground='#dbe0df')
        lbl_quantity = Label(self.article_frame, text="quantity", font=("Cursive", 10), bg='#dbe0df')
        txt_quantity = Entry(self.article_frame, bd=5, text="Quantity here")

        btn_aceptar.pack(side=BOTTOM)
        txt_quantity.pack(side=BOTTOM, pady=10)
        lbl_quantity.pack(side=BOTTOM, pady=10)
        title.pack()

        db = self.connect()
        cursor = db.cursor()
        sql = "SELECT name FROM Material"
        cursor.execute(sql)
        data = cursor.fetchall()

        for article in data:
            self.list.insert(END, article)

        self.list.pack()
        db.close()


    def make_loans_frame(self):
        self.list_loans = Listbox(self.loans_frame, selectborderwidth=5)
        self.list_new_loans = Listbox(self.loans_frame, selectborderwidth=5)
        self.list_loans.pack(side=LEFT, padx=30)
        self.list_new_loans.pack(side=RIGHT, padx=30, pady=30)

        btn_accept = Button(self.master, text="Accept", highlightbackground='#dbe0df', width=10)
        btn_cancel = Button(self.master, text="Cancel", highlightbackground='#dbe0df', width=10)
        btn_exit = Button(self.master, text="exit", highlightbackground='#dbe0df', width=10)

        lbl_current_loans = Label(self.master, text="Student Loans", bg='#dbe0df')
        lbl_loans = Label(self.master, text="Current loans", bg='#dbe0df')

        lbl_current_loans.place(relx=0.12, rely=0.2)
        lbl_loans.place(relx=0.41, rely=0.2)
        btn_accept.place(relx=0.07, rely=0.9)
        btn_cancel.place(relx=0.27, rely=0.9)
        btn_exit.place(relx=0.47, rely=0.9)


if __name__ == "__main__":
    andres = Student("Andres", "Pulgarin", 12313, 123231, 321321, "sistemas")
    l = Loans(andres)