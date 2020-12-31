from tkinter import *
import tkinter.ttk as ttk


root = Tk()

verify_menu = None


class Home_Application():
    def __init__(self):
        self.root = root
        self.root.geometry("800x400")
        self.root.title("Home")

        self.TSeparator = ttk.Separator(self.root)
        self.TSeparator.place(x=0, y=60, width=800)

        self.BtInicio = ttk.Button(self.root)
        self.BtInicio.place(x=10, y=10, width=156, height=45)
        self.BtInicio.configure(text='Início', command=self.menus)

        self.BtAdd = ttk.Button(self.root)
        self.BtAdd.place(x=170, y=10, width=156, height=45)
        self.BtAdd.configure(text='Adicionar Veiculo', command=self.menus2)

        self.BtGerenciar = ttk.Button(self.root)
        self.BtGerenciar.place(x=330, y=10, width=156, height=45)
        self.BtGerenciar.configure(text='Gerenciar Veiculos')

        self.BtHistorico = ttk.Button(self.root)
        self.BtHistorico.place(x=490, y=10, width=156, height=45)
        self.BtHistorico.configure(text='Historico')

        self.BtConfig = ttk.Button(self.root)
        self.BtConfig.place(x=690, y=20, width=96, height=35)
        self.BtConfig.configure(text='Configurações')

        self.root.mainloop()


    def menus(self):
        global verify_menu
        verify_menu = True
        self.test1 = Frame(self.root)
        self.test1.pack(padx=10, pady=70)
        self.test1.configure(relief='groove', borderwidth="2",  height=325, width=776)

    def menus2(self):
        global verify_menu
        if verify_menu == True:
            self.test1.destroy()
        else:
            pass
        self.test = Label(self.root)
        self.test.place(x=300, y=180)
        self.test.configure(text='Test 2')
        
Home_Application()
