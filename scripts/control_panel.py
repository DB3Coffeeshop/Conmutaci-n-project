from Tkinter import *
from ttk import *
from frm_options import *
import tkMessageBox
import getpass

class App(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.make_frame()
        self.student_code_text = Entry(self.master)
        self.pass_text = Entry(self.master, show="*")
        self.student_code_text.place(relx=0.5,rely=0.1)
        self.pass_text.place(relx=0.3, rely=0.4)
        
    def make_frame(self):
        #LABELS
        title = Label(self.master, text="Digital control", bg='#17202a', fg="white",font=(None, 15))
        self.category_first_label = Label(self.master, text="Primera Categoria:", bg='#17202a', fg="white",font=(None, 10))
        self.category_second_label = Label(self.master, text="Segunda Categoria:", bg='#17202a', fg="white",font=(None, 10))
        self.student_code_label=Label(self.master, text="Codigo Estudiante:", bg='#17202a', fg="white",font=(None, 10))

        #ComboBox
        self.category_first_Cbox = Combobox(self.master, state="readonly")
        self.category_second_Cbox = Combobox(self.master, state="readonly")
        self.category_first_Cbox['values'] = ['Pulga', 'Marika', 'Soplon']
        self.category_second_Cbox['values'] = ['Marika', 'Es', 'Pulga']

        #BUTTOMS
        button_search = Button(self.master, text="Search", highlightbackground='#17202a', command=self.search)
        button_back = Button(self.master, text="Atras", highlightbackground='#17202a', command=self.back)
        button_exit = Button(self.master, text="Exit", highlightbackground='#17202a', command=self.exit)

        
        #Pociciones
        title.place(relx=0.01,rely=0.01)
        self.category_first_label.place(relx=0.01,rely=0.065)
        self.category_second_label.place(relx=0.25,rely=0.065)
        self.student_code_label.place(relx=0.5,rely=0.065)

        self.category_first_Cbox.place(relx=0.01,rely=0.1)
        self.category_second_Cbox.place(relx=0.25,rely=0.1)

        button_search.place(relx=0.75, rely=0.065)
        button_back.place(relx=0.75, rely=0.12)
        button_exit.place(relx=0.6, rely=0.7)


    def exit(self):
        answer = tkMessageBox.askquestion("Exit", "Are you sure?")

        if answer == 'yes':
            self.master.destroy()

    def search(self):
        self.category_first_Cbox['values'] = ['ASDAW', 'dwada', 'dwadwa']

    def back(self):
        self.master.destroy()
        main = Main()

    def ololo(self):
        if self.user_text.get() == "andres" and self.pass_text.get() == "12345":
            tkMessageBox.showinfo("Correct", "Welcome {0}".format(getpass.getuser()))
            self.master.destroy()
            main = Main()
        else:
            if self.user_text.get() == "andres" and self.pass_text.get() != "12345":
                tkMessageBox.showerror("Error", "Invalid password")
            
            elif self.user_text.get() != "andres" and self.pass_text.get() == "12345":
                tkMessageBox.showerror("Error", "Invalid user")

            else:
                tkMessageBox.showinfo("Error", "Invalid user and password")

        



if __name__ == "__main__":
    root = Tk()
    root.title("Main")
    root.resizable(0,0)
    root.configure(background='#17202a')
    app = App(root)
    root.geometry("800x600")
    root.mainloop()