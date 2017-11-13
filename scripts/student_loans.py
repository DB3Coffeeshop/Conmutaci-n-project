from Tkinter import *
import MySQLdb


class Loans:

    def __init__(self, student_name):
        self.student_name = student_name
        self.master = Tk()
        self.article_frame = Frame(self.master, bd=5, relief="groove", width=400, height=400)
        self.loans_frame = Frame(self.master, bd=5, relief="groove", width=200, height=200)
        self.configure()
        self.make_list_articles()
        self.make_loans_frame()
        self.master.mainloop()

    def configure(self):
        self.master.title("Loans")
        title = Label(self.master, text="%s" % (self.student_name), bg='#dbe0df', font=("Cursive", 19))
        title.pack()
        #self.article_frame.place(relx=0.75, rely=0.18)
        self.article_frame.pack(side=RIGHT, padx=30, pady=10)
        self.loans_frame.pack(side=LEFT, padx=30)
        self.master.geometry("900x500")
        self.master.resizable(0,0)
        self.loans_frame.configure(background='#dbe0df')
        self.master.configure(background='#dbe0df')
        self.article_frame.configure(background='#dbe0df')


    def connect(self):
        data_base = MySQLdb.connect("LocalHost", "root", "natalia1", "GESTION")
        return data_base


    def make_list_articles(self):
        title = Label(self.article_frame, text="Articles", bg='#dbe0df')
        self.list = Listbox(self.article_frame, selectborderwidth=5)
        btn_aceptar = Button(self.article_frame, text="Add", highlightbackground='#dbe0df')
        btn_aceptar.pack(side=BOTTOM)
        title.pack()

        db = self.connect()
        cursor = db.cursor()
        sql = "SELECT name_product FROM Product"
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
        self.list_new_loans.insert(0, "saad")
        self.list_loans.insert(0,"adsads")



if __name__ == "__main__":
    l = Loans("Andres")