from tkinter import *
import tkinter.ttk as ttk


root = Tk()

verify_menu = None
verify_menu_add = None



class Home_Application():
    def __init__(self):
        self.root = root
        self.root.geometry("800x400")
        self.root.title("Home")

        self.TSeparator = ttk.Separator(self.root)
        self.TSeparator.place(x=0, y=60, width=800)

        self.BtInicio = ttk.Button(self.root)
        self.BtInicio.place(x=10, y=10, width=156, height=45)
        self.BtInicio.configure(text='Início', command=self.inicio)

        self.BtAdd = ttk.Button(self.root)
        self.BtAdd.place(x=170, y=10, width=156, height=45)
        self.BtAdd.configure(text='Adicionar Veiculo', command=self.add_veiculo)

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


    def inicio(self):
        green = '#5FED42'
        global verify_menu
        global verify_menu_add
        verify_menu = True
        print('Home criada')
        if verify_menu_add == True:
            self.FrAdd_Veiculo.destroy()
            print('Add deletada')
        else:
            pass
        self.FrInicio = Frame(self.root)
        self.FrInicio.place(relx=0.013, rely=0.175)
        self.FrInicio.configure(relief='groove', borderwidth="2",  height=325, width=776)

        self.Slot1 = Frame(self.FrInicio)
        self.Slot1.place(relx=0.026, rely=0.062)
        self.Slot1.configure(relief='groove', borderwidth="2", width=125, height=75, bg=green)

        self.Slot2 = Frame(self.FrInicio)
        self.Slot2.place(relx=0.219, rely=0.062)
        self.Slot2.configure(relief='groove', borderwidth="2", width=125, height=75, bg=green)

        self.Slot3 = Frame(self.FrInicio)
        self.Slot3.place(relx=0.412, rely=0.062)
        self.Slot3.configure(relief='groove', borderwidth="2", width=125, height=75, bg=green)

        self.Slot4 = Frame(self.FrInicio)
        self.Slot4.place(relx=0.606, rely=0.062)
        self.Slot4.configure(relief='groove', borderwidth="2", width=125, height=75, bg=green)

        self.Slot5 = Frame(self.FrInicio)
        self.Slot5.place(relx=0.799, rely=0.062)
        self.Slot5.configure(relief='groove', borderwidth="2", width=125, height=75, bg=green)

        self.Slot6 = Frame(self.FrInicio)
        self.Slot6.place(relx=0.219, rely=0.369)
        self.Slot6.configure(relief='groove', borderwidth="2", width=125, height=75, bg=green)

        self.Slot7 = Frame(self.FrInicio)
        self.Slot7.place(relx=0.412, rely=0.369)
        self.Slot7.configure(relief='groove', borderwidth="2", width=125, height=75, bg=green)

        self.Slot8 = Frame(self.FrInicio)
        self.Slot8.place(relx=0.606, rely=0.369)
        self.Slot8.configure(relief='groove', borderwidth="2", width=125, height=75, bg=green)

        self.Slot9 = Frame(self.FrInicio)
        self.Slot9.place(relx=0.799, rely=0.369)
        self.Slot9.configure(relief='groove', borderwidth="2", width=125, height=75, bg=green)

        self.Slot10 = Frame(self.FrInicio)
        self.Slot10.place(relx=0.026, rely=0.369)
        self.Slot10.configure(relief='groove', borderwidth="2", width=125, height=75, bg=green)

        self.Slot11 = Frame(self.FrInicio)
        self.Slot11.place(relx=0.026, rely=0.677)
        self.Slot11.configure(relief='groove', borderwidth="2", width=125, height=75, bg=green)

        self.Slot12 = Frame(self.FrInicio)
        self.Slot12.place(relx=0.219, rely=0.677)
        self.Slot12.configure(relief='groove', borderwidth="2", width=125, height=75, bg=green)

        self.Slot13 = Frame(self.FrInicio)
        self.Slot13.place(relx=0.412, rely=0.677)
        self.Slot13.configure(relief='groove', borderwidth="2", width=125, height=75, bg=green)

        self.Slot14 = Frame(self.FrInicio)
        self.Slot14.place(relx=0.606, rely=0.677)
        self.Slot14.configure(relief='groove', borderwidth="2", width=125, height=75, bg=green)

        self.Slot15 = Frame(self.FrInicio)
        self.Slot15.place(relx=0.799, rely=0.677)
        self.Slot15.configure(relief='groove', borderwidth="2", width=125, height=75, bg=green)

    def add_veiculo(self):
        global verify_menu
        global verify_menu_add
        print('Add criada')
        if verify_menu == True:
            self.FrInicio.destroy()
            verify_menu_add = True
            print('Home deletada')
        else:
            pass
        self.FrAdd_Veiculo = Frame(self.root)
        self.FrAdd_Veiculo.place(relx=0.013, rely=0.175)
        self.FrAdd_Veiculo.configure(relief='groove', borderwidth="2",  height=325, width=776)

        self.FrAdd_Nome = LabelFrame(self.FrAdd_Veiculo)
        self.FrAdd_Nome.place(relx=0.219, rely=0.092)
        self.FrAdd_Nome.configure(relief='groove', borderwidth="2",  height=75, width=450, text='Nome')
        self.EntryAdd_Nome = ttk.Entry(self.FrAdd_Nome)
        self.EntryAdd_Nome.place(relx=0.044, rely=0.4, relheight=0.333, relwidth=0.836)

        self.FrAdd_ID = LabelFrame(self.FrAdd_Veiculo)
        self.FrAdd_ID.place(relx=0.219, rely=0.369)
        self.FrAdd_ID.configure(relief='groove', borderwidth="2",  height=75, width=450, text='ID do Veiculo')
        self.EntryAdd_ID = ttk.Entry(self.FrAdd_ID)
        self.EntryAdd_ID.place(relx=0.044, rely=0.4, relheight=0.333, relwidth=0.836)

        self.FrAdd_Telefone = LabelFrame(self.FrAdd_Veiculo)
        self.FrAdd_Telefone.place(relx=0.219, rely=0.646)
        self.FrAdd_Telefone.configure(relief='groove', borderwidth="2",  height=75, width=450, text='Telefone')
        self.EntryAdd_Telefone = ttk.Entry(self.FrAdd_Telefone)
        self.EntryAdd_Telefone.place(relx=0.044, rely=0.4, relheight=0.333, relwidth=0.836)

        self.BtSalvarVeiculo = ttk.Button(self.FrAdd_Veiculo)
        self.BtSalvarVeiculo.place(relx=0.619, rely=0.892, width=140, height=30)
        self.BtSalvarVeiculo.configure(text='Salvar Veiculo')
        
Home_Application()
