from Tkinter import *
from frm_options import *
import tkMessageBox
import getpass

class App(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.make_frame()
        self.user_text = Entry(self.master)
        self.pass_text = Entry(self.master, show="*")
        self.user_text.place(relx=0.4, rely=0.2)
        self.pass_text.place(relx=0.4, rely=0.4)


    def make_frame(self):
        title = Label(self.master, text="Digital control", bg='#dbe0df', fg="white")
        title = Label(self.master, text="Digital control", bg='#dbe0df', fg="white")
        user_label = Label(self.master, text="User", bg='#dbe0df', fg='white')
        pass_label = Label(self.master, text="Password", bg='#dbe0df', fg='white')
        button_accept = Button(self.master, text="Accept", highlightbackground='#dbe0df', command=self.check_user)
        button_exit = Button(self.master, text="Exit", highlightbackground='#dbe0df', command=self.exit)
        user_label.place(relx=0.2, rely=0.2)
        pass_label.place(relx=0.2, rely=0.4)
        button_accept.place(relx=0.3, rely=0.7)
        button_exit.place(relx=0.6, rely=0.7)
        title.pack()


    def exit(self):
        answer = tkMessageBox.askquestion("Exit", "Are you sure?")

        if answer == 'yes':
            self.master.destroy()


    def check_user(self):
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
    root.configure(background='#dbe0df')
    app = App(root)
    root.geometry("400x300")
    root.mainloop()