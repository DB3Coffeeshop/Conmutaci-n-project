from Tkinter import *
from ttk import *
import MySQLdb
from frm_options import *
import tkMessageBox
import getpass

class App(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.conectar()
        self.make_frame()
        self.fill_table()
        self.student_code_text = Entry(self.master)
        self.student_code_text.place(relx=0.5,rely=0.2)
        
    def make_frame(self):
        #LABELS
        title = Label(self.master, text="Digital control", bg='#17202a', fg="white",font=(None, 15))
        category_first_label = Label(self.master, text="Primera Categoria:", bg='#17202a', fg="white",font=(None, 10))
        category_second_label = Label(self.master, text="Segunda Categoria:", bg='#17202a', fg="white",font=(None, 10))
        student_code_label=Label(self.master, text="Codigo Estudiante:", bg='#17202a', fg="white",font=(None, 10))

        #ComboBox
        self.category_first_Cbox = Combobox(self.master, state="readonly")
        self.category_second_Cbox = Combobox(self.master, state="readonly")
        self.category_first_Cbox['values'] = []
        self.category_second_Cbox['values'] = []
        #self.combo["values"] = []
        #self.category_first_Cbox.bind("<<ComboboxSelected>>", self.cbox_category_change)
        self.refill_cbox("category_first",1)
        self.refill_cbox("category_second",2)

        #BUTTOMS
        button_search = Button(self.master, text="Search", highlightbackground='#17202a', command=self.search)
        button_back = Button(self.master, text="Atras", highlightbackground='#17202a', command=self.back)
        button_exit = Button(self.master, text="Exit", highlightbackground='#17202a', command=self.exit)
        button_moreinf = Button(self.master, text="More inf", highlightbackground='#17202a', command=self.selected_tree)

        #TREEVIEW
        self.grid()
        self.tree = self.tree = Treeview(self,columns=('Code Student','Material','Date','cant'),show="headings",selectmode='browse')
        self.tree.heading("Code Student", text="Code Student")
#        tree.column('Code Studen',anchor='center',width=30)
        self.tree.heading("Material", text="Material")
        self.tree.heading("Date",text="Date")
        self.tree.heading("cant",text="cant")
        self.tree.grid(padx = 5,pady=110)

        #Pociciones
        title.place(relx=0.01,rely=0.01)
        category_first_label.place(relx=0.01,rely=0.15)
        category_second_label.place(relx=0.25,rely=0.15)
        student_code_label.place(relx=0.5,rely=0.15)

        self.category_first_Cbox.place(relx=0.01,rely=0.2)
        self.category_second_Cbox.place(relx=0.25,rely=0.2)

        button_search.place(relx=0.75, rely=0.065)
        button_moreinf.place(relx=0.75, rely=0.15)
        button_back.place(relx=0.85, rely=0.065)
        button_exit.place(relx=0.85, rely=0.15)


    def fill_table(self):
        sql = "SELECT student_code, material, cant, date FROM Loan"
        list_data = self.db_execute(sql)

        for data in list_data:
            self.tree.insert('', 'end', values=[data[0], data[1], data[3], data[2]])
            
        

      
    def selected_tree(self):
        try:
            curItem = self.tree.focus();
            print self.tree.item(curItem)['values'][0]
            
        except Exception, e:
            tkMessageBox.showinfo("Error", "Select One inf")

    def refill_cbox(self,requisito,num_cbox):
        table_name="Materials"
        scrip="Select DISTINCT "+ requisito + " From "+ table_name
        table=self.db_execute(scrip)
        #print self.category_first_Cbox['values']
        #print table[0]
        if num_cbox ==1 :
            self.category_first_Cbox['values'] = ['']
            for i in range(len(table)):
                values = list(self.category_first_Cbox["values"])
                self.category_first_Cbox['values']= values + [table[i][0]]
        elif num_cbox==2:           
            for i in range(len(table)):
                values = list(self.category_second_Cbox["values"])
                self.category_second_Cbox['values']= values + [table[i][0]]
                

    def search(self):
        first_category = self.category_second_Cbox.get()
        second_category = self.category_first_Cbox.get()

        sql = "SELECT student_code, material, date, cant FROM Loan INNER JOIN Materials ON Loan.material = Material.id_Materials WHERE student_code=%d AND Materials.category_first='%s' AND Materials.category_second='%s'" % (int(self.student_code_text.get()), first_category, second_category)
        sql_2 = "SELECT student_code, material, date, cant, FROM Loan INNER JOIN Materials ON Loan.material = Material.id_Materials WHERE Material.category_first='%s' AND Material.category_second='%s'" % (first_category, second_category)
        sql_3 = "SELECT student_code, material, date, cant, FROM Loan INNER JOIN Materials ON Loan.material = Material.id_Materials WHERE Material.category_first='%s'" % (first_category)
        sql_4 = "SELECT student_code, material, date, cant, FROM Loan INNER JOIN Materials ON Loan.material = Material.id_Materials WHERE Material.category_second='%s'" % (second_category)
        sql_5 = "SELECT student_code, material, date, cant FROM Loan INNER JOIN Materials ON Loan.material = Material.id_Materials WHERE student_code=%d" % (int(self.student_code_text.get()))
        
        if first_category != '' and second_category != '' and self.student_code_text.get() != '':
            self.db_execute(sql)

        elif first_category != ''  and second_category != '':
            self.db_execute(sql_2)

        elif first_category != '':
            self.db_execute(sql_3)
        
        elif first_category != '':
            self.db_execute(sql_4)
        
        else:
            self.db_execute(sql_5)


    def db_execute(self,texts):
        self.cur.execute(texts)
        return self.cur.fetchall()
            
    def conectar(self):
        self.db = MySQLdb.connect("LocalHost", "root", "natalia1", "Eafit_Loans") #Ignoren la contra, no supe como cambiarla
        self.db.autocommit(True)
        self.cur = self.db.cursor()


    def cleartext(self,tex):
        texto=str(tex)
        texto.replace('(','')
        texto.replace(')','')
        texto.replace(',','')
        return texto
    def exit(self):
        answer = tkMessageBox.askquestion("Exit", "Are you sure?")
        if answer == 'yes':
            self.master.destroy()

    def back(self):
        self.master.destroy()
        main = Main()


if __name__ == "__main__":
    root = Tk()
    root.title("Main")
    root.resizable(0,0)
    root.configure(background='#17202a')
    app = App(root)
    root.geometry("810x410")
    root.mainloop()
