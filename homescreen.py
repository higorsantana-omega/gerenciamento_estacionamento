import sqlite3
from funções import get_veiculo
from tkinter import *
import tkinter.ttk as ttk
import bd
from datetime import date, datetime


root = Tk()

verify_menu = None
verify_menu_add = None
verify_menu_manager = None
verify_menu_history = None


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
        self.BtGerenciar.configure(text='Gerenciar Veiculos', command=self.manager_veiculo)

        self.BtHistorico = ttk.Button(self.root)
        self.BtHistorico.place(x=490, y=10, width=156, height=45)
        self.BtHistorico.configure(text='Historico', command=self.historico_veiculo)

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
        self.BtSalvarVeiculo.configure(text='Salvar Veiculo', command=self.get_veiculo)

    def manager_veiculo(self):
        global verify_menu
        global verify_menu_add
        global verify_menu_manager
        print('Manager criada')
        if verify_menu == True or verify_menu_add == True:
            self.FrInicio.destroy()
            self.FrAdd_Veiculo.destroy()
            verify_menu_manager = True
            print('Home & Add deletada')
        else:
            pass
        self.FrManager_Veiculo = Frame(self.root)
        self.FrManager_Veiculo.place(relx=0.013, rely=0.175)
        self.FrManager_Veiculo.configure(relief='groove', borderwidth="2",  height=325, width=776)

        self.TreeManager = ttk.Treeview(self.FrManager_Veiculo, columns=(1, 2, 3, 4, 5), show='headings')
        self.TreeManager.place(relx=0.026, rely=0.154, relheight=0.791, relwidth=0.956)
        self.TreeManager.heading(1, text="ID")
        self.TreeManager.heading(2, text='Nome')
        self.TreeManager.heading(3, text='Número Veiculo')
        self.TreeManager.heading(4, text='Telefone')
        self.TreeManager.heading(5, text='Hora de Entrada')
        self.TreeManager.column(1, width=1)
        self.TreeManager.column(2, width=7)
        self.TreeManager.column(3, width=4)
        self.TreeManager.column(4, width=5)
        self.TreeManager.column(5, width=1)

        self.BtEditTree = ttk.Button(self.FrManager_Veiculo)
        self.BtEditTree.place(x=20, y=10, width=126, height=35)
        self.BtEditTree.configure(text='Editar Veiculo')

        self.BtExcluirTree = ttk.Button(self.FrManager_Veiculo)
        self.BtExcluirTree.place(x=160, y=10, width=126, height=35)
        self.BtExcluirTree.configure(text='Excluir Veiculo')

    def historico_veiculo(self):
        global verify_menu
        global verify_menu_add
        global verify_menu_manager
        global verify_menu_history
        print('History criada')
        if verify_menu == True or verify_menu_add == True or verify_menu_manager == True:
            self.FrInicio.destroy()
            self.FrAdd_Veiculo.destroy()
            self.FrManager_Veiculo.destroy()
            verify_menu_history= True
            print('Home & Add & History deletada')
        else:
            pass

        self.FrHistory_Veiculo = Frame(self.root)
        self.FrHistory_Veiculo.place(relx=0.013, rely=0.175)
        self.FrHistory_Veiculo.configure(relief='groove', borderwidth="2",  height=325, width=776)

        self.TreeHistory = ttk.Treeview(self.FrHistory_Veiculo, columns=(1, 2, 3, 4, 5, 6), show='headings')
        self.TreeHistory.place(relx=0.026, rely=0.031, relheight=0.914, relwidth=0.956)
        self.TreeHistory.heading(1, text="ID")
        self.TreeHistory.heading(2, text='Nome')
        self.TreeHistory.heading(3, text='Número Veiculo')
        self.TreeHistory.heading(4, text='Telefone')
        self.TreeHistory.heading(5, text='Hora de Entrada')
        self.TreeHistory.heading(6, text='Hora de Saída')
        self.TreeHistory.column(1, width=1)
        self.TreeHistory.column(2, width=7)
        self.TreeHistory.column(3, width=4)
        self.TreeHistory.column(4, width=5)
        self.TreeHistory.column(5, width=1)
        self.TreeHistory.column(6, width=1)

    def get_veiculo(self):
        # Campos para inserir as informações do veiculo
        self.nome = self.EntryAdd_Nome.get()
        self.placa = self.EntryAdd_ID.get()
        self.telefone = self.EntryAdd_Telefone.get()

        # Data de registro no sistema
        data_atual = datetime.now()
        self.data_entrada = data_atual.strftime("%d/%m/%Y %H:%M")

        # Verificar se o veiculo ainda está no estacionamento
        self.exit = False

        # Inserir informações no Banco de Dados
        alt = bd.BD()
        alt.conn_bd()
        alt.execute_comand("INSERT INTO veiculo_table (nome, telefone, placa, data_entrada, exit, criado_em) values (?, ?, ?, ?, ?, ?)", (self.nome, self.placa, self.telefone, self.data_entrada, self.exit, self.data_entrada))
        alt.persist()
        alt.desconectar_BD()

        self.EntryAdd_Nome.delete(0, 'end')
        self.EntryAdd_ID.delete(0, 'end')
        self.EntryAdd_Telefone.delete(0, 'end')

        alt.conn_bd()
        self.tree_manager = alt.execute_comand("SELECT * FROM veiculo_table ORDER BY id DESC")
        self.tree_manager = list(self.tree_manager)
        print(self.tree_manager)
        self.TreeManager.insert('', 'end', values=self.tree_manager[0])
        self.TreeManager.insert('', 'end', values=self.tree_manager[1])
        self.TreeManager.insert('', 'end', values=self.tree_manager[3])
        self.TreeManager.insert('', 'end', values=self.tree_manager[2])
        self.TreeManager.insert('', 'end', values=self.tree_manager[4])
        alt.desconectar_BD()


    def get_manager(self):
        pass
