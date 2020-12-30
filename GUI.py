from tkinter import *


root = Tk()

class Gui_Application():
    def __init__(self):
        self.root = root
        self.root.geometry("300x250")
        self.root.title("Gerenciamento de Estacionamento")

        self.LbDataBase = Label(self.root)
        self.LbDataBase.place(relx=0.033, rely=0.052, height=13, width=140)
        self.LbDataBase.configure(text="Nome do Banco de Dados:")
        
        self.EntryDataBase = Entry(self.root)
        self.EntryDataBase.place(relx=0.033, rely=0.152, height=20, relwidth=0.933)

        self.LbDataBase_Senha = Label(self.root)
        self.LbDataBase_Senha.place(relx=0.033, rely=0.3, height=14, width=140)
        self.LbDataBase_Senha.configure(text="Senha do Banco de Dados:")

        self.EntryDataBase_Senha = Entry(self.root)
        self.EntryDataBase_Senha.place(relx=0.033, rely=0.4, height=20, relwidth=0.933)

        self.LbNomeAdmin = Label(self.root)
        self.LbNomeAdmin.place(relx=0.0, rely=0.552, height=13, width=140)
        self.LbNomeAdmin.configure(text="Nome do Administrador:")

        self.EntryNomeAdmin = Entry(self.root)
        self.EntryNomeAdmin.place(relx=0.033, rely=0.652, height=20, relwidth=0.947)

        self.LbSenhaAdmin = Label(self.root)
        self.LbSenhaAdmin.place(relx=0.02, rely=0.8, height=14, width=140)
        self.LbSenhaAdmin.configure(text="Senha do Administrador:")

        self.EntrySenhaAdmin = Entry(self.root)
        self.EntrySenhaAdmin.place(relx=0.033, rely=0.9, height=20, relwidth=0.947)

        self.root.mainloop()


Gui_Application()