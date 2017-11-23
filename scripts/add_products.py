from Tkinter import *
from ttk import *
import MySQLdb
from frm_options import *
import tkMessageBox
import getpass
from PIL import Image, ImageTk

class App(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.conectar()
        self.make_frame()


    def make_frame(self):
        #LABELS
        id_label = Label(self.master,text="Id_Producto :", bg='#17202a', fg="white",font=(None, 15))
        #2
        last_label= Label(self.master,text="Categoria 1 : ", bg='#17202a', fg="white",font=(None, 15))
        #3
        mail_label = Label(self.master,text="Categoria 2 : ", bg='#17202a', fg="white",font=(None, 15))
        #4
        nombre_label = Label(root,text="Nombre : ", bg='#17202a', fg="white",font=(None, 15))
        #5
        stock_label = Label(root,text="Stock : ", bg='#17202a', fg="white",font=(None, 15))


        #OTHERS
        Id_producto_str = StringVar()
        id_entry = Entry(root,textvariable=Id_producto_str)
        #2
        Categoria_1 = StringVar()
        last_entry = Entry(root,textvariable=Categoria_1)
        #3
        Categoria_2 = StringVar()
        mail_entry = Entry(root,textvariable=Categoria_2)
        #4
        Nombre_str = StringVar()
        nombre_entry = Entry(root,textvariable=Nombre_str)
        #5
        Stock_str = StringVar()
        stock_entry = Entry(root,textvariable=Stock_str)
    
        

        #BUTTOMS
        button_agregar = Button(self.master, text="Agregar", highlightbackground='#17202a')
        button_back = Button(self.master, text="Atras", highlightbackground='#17202a', command=self.back)
        button_exit = Button(self.master, text="Exit", highlightbackground='#17202a', command=self.exit)
        
        #IMAGE  Descomente estoooooooo
        image_students = self.set_image("../images/Estudiantes.png")

        button_stundents = Button(self.master, image=image_students, highlightbackground='#deefed')
        
        button_stundents.image = image_students

        #Pociciones
        id_label.place(relx=0.08,rely=0.10)
        id_entry.place(relx=0.08,rely=0.15)
        last_label.place(relx=0.08,rely=0.25)
        last_entry.place(relx=0.08,rely=0.30)
        mail_label.place(relx=0.08,rely=0.40)
        mail_entry.place(relx=0.08,rely=0.45)
        nombre_label.place(relx=0.08,rely=0.55)
        nombre_entry.place(relx=0.08,rely=0.60)
        stock_label.place(relx=0.08,rely=0.70)
        stock_entry.place(relx=0.08,rely=0.75)

        button_agregar.place(relx=0.45, rely=0.45)
        button_back.place(relx=0.55, rely=0.45)
        button_exit.place(relx=0.52, rely=0.52)

        #DESCOMENTE ESTOOOOOO TAMBIEN
        button_stundents.pack(padx=100, pady=30)

    def db_execute(self,texts):
        self.cur.execute(texts)
        return self.cur.fetchall()
            
    def conectar(self):
        self.db = MySQLdb.connect("LocalHost", "root", "natalia1", "Eafit_Loans") #Ignoren la contra, no supe como cambiarla
        self.cur = self.db.cursor()

    def exit(self):
        answer = tkMessageBox.askquestion("Exit", "Are you sure?")
        if answer == 'yes':
            self.master.destroy()

    def back(self):
        self.master.destroy()
        main = Main()

    def set_image(self, dir):
        image = ImageTk.PhotoImage(Image.open(str(dir)))
        return image


root = Tk()
root.title("Main")
root.resizable(0,0)
root.configure(background='#17202a')
app = App(root)
root.geometry("810x410")
root.mainloop()
