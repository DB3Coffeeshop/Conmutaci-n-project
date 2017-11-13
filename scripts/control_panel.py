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
        self.student_code_text.place(relx=0.5,rely=0.1)
        
    def make_frame(self):
        #LABELS
        title = Label(self.master, text="Digital control", bg='#17202a', fg="white",font=(None, 15))
        self.category_first_label = Label(self.master, text="Primera Categoria:", bg='#17202a', fg="white",font=(None, 10))
        self.category_second_label = Label(self.master, text="Segunda Categoria:", bg='#17202a', fg="white",font=(None, 10))
        self.student_code_label=Label(self.master, text="Codigo Estudiante:", bg='#17202a', fg="white",font=(None, 10))

        #ComboBox
        self.category_first_Cbox = Combobox(self.master, state="readonly")
        self.category_second_Cbox = Combobox(self.master, state="readonly")
        self.category_first_Cbox['values'] = ['','Pulga', 'Marika', 'Soplon']
        self.category_second_Cbox['values'] = ['Marika', 'Es', 'Pulga']

        #BUTTOMS
        button_search = Button(self.master, text="Search", highlightbackground='#17202a', command=self.search)
        button_back = Button(self.master, text="Atras", highlightbackground='#17202a', command=self.back)
        button_exit = Button(self.master, text="Exit", highlightbackground='#17202a', command=self.exit)
        button_moreinf = Button(self.master, text="More inf", highlightbackground='#17202a', command=self.selected_tree)

        #TREEVIEW
        self.grid()
        tree = self.tree = Treeview(self,columns=('Code Student','Material','Date','Return'),show="headings",selectmode='browse')
        tree.heading("Code Student", text="Code Student")
#        tree.column('Code Studen',anchor='center',width=30)
        tree.heading("Material", text="Material")
        tree.heading("Date",text="Date")
        tree.heading("Return",text="Return")
        tree.grid(padx = 5,pady=5)
        #tree.grid(place=2)

        i = tree.insert('','end',values = ['0353','567','adwa','adwad'])
        tree.insert(i,'end',values = ['0353','567','adwa','adwad'])
        
        #Pociciones
        title.place(relx=0.01,rely=0.01)
        self.category_first_label.place(relx=0.01,rely=0.065)
        self.category_second_label.place(relx=0.25,rely=0.065)
        self.student_code_label.place(relx=0.5,rely=0.065)

        self.category_first_Cbox.place(relx=0.01,rely=0.1)
        self.category_second_Cbox.place(relx=0.25,rely=0.1)

        button_search.place(relx=0.75, rely=0.065)
        button_back.place(relx=0.75, rely=0.12)
        button_moreinf.place(relx=0.75, rely=0.175)
        button_exit.place(relx=0.75, rely=0.23)

        #tree.place(relx=0.1,rely=0.2)

    def selected_tree(self):
        curItem = self.tree.focus();
        print self.tree.item(curItem)['values'][0]
        self.quit()

    def remove_all(self):
        pass

    def exit(self):
        answer = tkMessageBox.askquestion("Exit", "Are you sure?")

        if answer == 'yes':
            self.master.destroy()

    def search(self):
        item=""
        student_code=self.student_code_text.get()
        self.category_first_Cbox['values'] = ['ASDAW', 'dwada', 'dwadwa']

        if item != "":
            if student_code != "":
                #Enviar codigo con ambos requisitos
            #else:
                #Perdir solo por item
                pass

        #else:
            if student_code != "": 
                #pedir por codigo          
            #else:
                tkMessageBox.showinfo("Error", "Select one")
                pass


    def back(self):
        self.master.destroy()
        main = Main()


if __name__ == "__main__":
    root = Tk()
    root.title("Main")
    root.resizable(0,0)
    root.configure(background='#17202a')
    app = App(root)
    root.geometry("800x600")
    root.mainloop()