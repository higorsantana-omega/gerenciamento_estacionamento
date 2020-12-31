from tkinter import *
import tkinter.ttk as ttk


root = Tk()

root.geometry("300x400")
root.title("Gerenciamento de Estacionamento")

LbDataBase = Label(root)
LbDataBase.place(relx=0.033, rely=0.025, height=22, width=140)
LbDataBase.configure(text="Nome do Banco de Dados:")
        
EntryDataBase = Entry(root)
EntryDataBase.place(relx=0.033, rely=0.075, height=20, relwidth=0.933)

LbDataBase_Senha = Label(root)
LbDataBase_Senha.place(relx=0.033, rely=0.15, height=22, width=140)
LbDataBase_Senha.configure(text="Senha do Banco de Dados:")

EntryDataBase_Senha = Entry(root)
EntryDataBase_Senha.place(relx=0.033, rely=0.2, height=20, relwidth=0.933)

LbNomeAdmin = Label(root)
LbNomeAdmin.place(relx=0.033, rely=0.275, height=22, width=130)
LbNomeAdmin.configure(text="Nome do Administrador:")

EntryNomeAdmin = Entry(root)
EntryNomeAdmin.place(relx=0.033, rely=0.325, height=20, relwidth=0.947)

LbSenhaAdmin = Label(root)
LbSenhaAdmin.place(relx=0.033, rely=0.4, height=23, width=140)
LbSenhaAdmin.configure(text="Senha do Administrador:")

EntrySenhaAdmin = Entry(root)
EntrySenhaAdmin.place(relx=0.033, rely=0.45, height=20, relwidth=0.947)

Bt_SalvarConfig = ttk.Button(root)
Bt_SalvarConfig.place(relx=0.0, rely=0.55, height=25, width=300)
Bt_SalvarConfig.configure(text="Salvar Configuração")

LbSucess = Label(root)
LbSucess.place(relx=0.0, rely=0.925, height=20, width=100)
LbSucess.configure(font="-family {System} -size 10 -weight bold", text='Salvo')

TSeparator = ttk.Separator(root)
TSeparator.place(relx=0.0, rely=0.975, relwidth=1.0)

root.mainloop()
