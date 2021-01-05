from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import bd

# Criar janela
root = Tk()

# Variavel que define se o login foi feito com sucesso
Logado = False


class Login_Application():
    # Construtor
    def __init__(self):
        # Configurações da janela
        self.root = root
        self.root.geometry("250x220")
        self.root.title("Login")

        # Entrys & Labels
        self.Lb_Usuario = Label(self.root)
        self.Lb_Usuario.place(relx=0.04, rely=0.136, height=20, width=111)
        self.Lb_Usuario.configure(text="Nome do Admin")

        self.Entry_Usuario = ttk.Entry(self.root)
        self.Entry_Usuario.place(relx=0.04, rely=0.227, relheight=0.114, relwidth=0.92)

        self.Lb_Senha = Label(self.root)
        self.Lb_Senha.place(relx=0.04, rely=0.364, height=20, width=111)
        self.Lb_Senha.configure(text="Senha do Admin")
        
        self.Entry_Senha = ttk.Entry(self.root, show='*')
        self.Entry_Senha.place(relx=0.04, rely=0.455, relheight=0.114, relwidth=0.92)

        # Botão para logar no sistema
        self.Bt_Login = ttk.Button(self.root)
        self.Bt_Login.place(relx=0.24, rely=0.682, relwidth=0.504, relheight=0.159)
        self.Bt_Login.configure(text='Login', command=self.Login_V)

        self.root.mainloop()

    # Algoritmo de verificação do login
    def Login_V(self):
        # Determina a variavel como global
        global Logado
        # Pegar dados das entrys
        self.VerifyUsuario = self.Entry_Usuario.get()
        self.VerifySenha = self.Entry_Senha.get()

        # Conectar-se ao banco
        alt = bd.BD()
        alt.conn_bd()
        # Executar comando
        alt.execute_comand("""
        SELECT * FROM admin_table
        WHERE (username = ? and password = ?)
        """, (self.VerifyUsuario, self.VerifySenha))
        print('Selecionado')

        self.VerifyLogin = alt.cursor.fetchone()
        # Processo de autorização de login
        try:
            # Verificar se os dados passados na entry batem com os dados do banco
            if (self.VerifyUsuario in self.VerifyLogin and self.VerifySenha in self.VerifyLogin):
                print('Acesso Permitido')
                # Permite o acesso
                Logado = True
            else:
                pass
        except:
            # Acesso recusado
            print('Acesso Negado')
            Logado = False
            messagebox.showerror(title='Erro', message='Usuário ou senha está incorreto.')
            

        # Após logar com exito
        if Logado == True:
            # Destroi a janela login, e chama a tela home
            self.root.destroy()
            from homescreen import Home_Application
            Home_Application()
