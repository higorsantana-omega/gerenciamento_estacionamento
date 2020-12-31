from tkinter import *
import tkinter.ttk as ttk


root = Tk()

class Config_Application():
    def __init__(self):
        self.root = root
        self.root.geometry("300x400")
        self.root.title("Gerenciamento de Estacionamento")

        self.LbDataBase = Label(self.root)
        self.LbDataBase.place(relx=0.033, rely=0.025, height=22, width=140)
        self.LbDataBase.configure(text="Nome do Banco de Dados:")
        
        self.EntryDataBase = Entry(self.root)
        self.EntryDataBase.place(relx=0.033, rely=0.075, height=20, relwidth=0.933)

        self.LbDataBase_Senha = Label(self.root)
        self.LbDataBase_Senha.place(relx=0.033, rely=0.15, height=22, width=140)
        self.LbDataBase_Senha.configure(text="Senha do Banco de Dados:")

        self.EntryDataBase_Senha = Entry(self.root)
        self.EntryDataBase_Senha.place(relx=0.033, rely=0.2, height=20, relwidth=0.933)

        self.LbNomeAdmin = Label(self.root)
        self.LbNomeAdmin.place(relx=0.033, rely=0.275, height=22, width=130)
        self.LbNomeAdmin.configure(text="Nome do Administrador:")

        self.EntryNomeAdmin = Entry(self.root)
        self.EntryNomeAdmin.place(relx=0.033, rely=0.325, height=20, relwidth=0.947)

        self.LbSenhaAdmin = Label(self.root)
        self.LbSenhaAdmin.place(relx=0.033, rely=0.4, height=23, width=140)
        self.LbSenhaAdmin.configure(text="Senha do Administrador:")

        self.EntrySenhaAdmin = Entry(self.root)
        self.EntrySenhaAdmin.place(relx=0.033, rely=0.45, height=20, relwidth=0.947)

        self.Bt_SalvarConfig = ttk.Button(self.root)
        self.Bt_SalvarConfig.place(relx=0.0, rely=0.55, height=25, width=300)
        self.Bt_SalvarConfig.configure(text="Salvar Configuração")

        self.LbSucess = Label(self.root)
        self.LbSucess.place(relx=0.0, rely=0.925, height=20, width=100)
        self.LbSucess.configure(font="-family {System} -size 10 -weight bold", text='Salvo')

        self.TSeparator = ttk.Separator(self.root)
        self.TSeparator.place(relx=0.0, rely=0.975, relwidth=1.0)

        self.root.mainloop()

Config_Application()
