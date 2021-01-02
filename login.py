from tkinter import *
import tkinter.ttk as ttk
import bd
from homescreen import Home_Application

root = Tk()

Logado = False


class Login_Application():
    def __init__(self):
        self.root = root
        self.root.geometry("250x220")
        self.root.title("Login")

        self.Lb_Usuario = Label(self.root)
        self.Lb_Usuario.place(relx=0.04, rely=0.136, height=20, width=111)
        self.Lb_Usuario.configure(text="Nome do Admin")

        self.Entry_Usuario = ttk.Entry(self.root)
        self.Entry_Usuario.place(relx=0.04, rely=0.227, relheight=0.114, relwidth=0.92)

        self.Lb_Senha = Label(self.root)
        self.Lb_Senha.place(relx=0.04, rely=0.364, height=20, width=111)
        self.Lb_Senha.configure(text="Senha do Admin")
        
        self.Entry_Senha = ttk.Entry(self.root)
        self.Entry_Senha.place(relx=0.04, rely=0.455, relheight=0.114, relwidth=0.92)

        self.Bt_Login = ttk.Button(self.root)
        self.Bt_Login.place(relx=0.24, rely=0.682, relwidth=0.504, relheight=0.159)
        self.Bt_Login.configure(text='Login', command=self.Login_V)

        self.root.mainloop()

    def Login_V(self):
        global Logado
        self.VerifyUsuario = self.Entry_Usuario.get()
        self.VerifySenha = self.Entry_Senha.get()
        alt = bd.BD()
        alt.conn_bd()
        alt.execute_comand("""
        SELECT * FROM admin_table
        WHERE (username = ? and password = ?)
        """, (self.VerifyUsuario, self.VerifySenha))
        print('Selecionado')
        self.VerifyLogin = alt.cursor.fetchone()
        try:
            if (self.VerifyUsuario in self.VerifyLogin and self.VerifySenha in self.VerifyLogin):
                print('Acesso Permitido')
                Logado = True
            else:
                pass
        except:
            print('Acesso Negado')

        if Logado == True:
            self.root.destroy()
            Home_Application()

        
