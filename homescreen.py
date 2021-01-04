import sqlite3
from tkinter import *
import tkinter.ttk as ttk
import bd
from datetime import date, datetime


root = Tk()

# Variaveis para verificar se está em algum menu
verify_menu = None
verify_menu_add = None
verify_menu_manager = None
verify_menu_history = None


class Home_Application():
    # Construtor
    def __init__(self):
        # Configurações da janela
        self.root = root
        self.root.geometry("800x400")
        self.root.title("Home") 

        # Separador tkinter
        self.TSeparator = ttk.Separator(self.root)
        self.TSeparator.place(x=0, y=60, width=800)

        # Botão tela home
        self.BtInicio = ttk.Button(self.root)
        self.BtInicio.place(x=10, y=10, width=156, height=45)
        self.BtInicio.configure(text='Início', command=self.inicio)

        # Botão tela adicionar veiculo
        self.BtAdd = ttk.Button(self.root)
        self.BtAdd.place(x=170, y=10, width=156, height=45)
        self.BtAdd.configure(text='Adicionar Veiculo', command=self.add_veiculo)

        # Botão tela gerenciar veiculos
        self.BtGerenciar = ttk.Button(self.root)
        self.BtGerenciar.place(x=330, y=10, width=156, height=45)
        self.BtGerenciar.configure(text='Gerenciar Veiculos', command=self.manager_veiculo)

        # Botão tela historico
        self.BtHistorico = ttk.Button(self.root)
        self.BtHistorico.place(x=490, y=10, width=156, height=45)
        self.BtHistorico.configure(text='Historico', command=self.historico_veiculo)

        # Botão tela configurações
        self.BtConfig = ttk.Button(self.root)
        self.BtConfig.place(x=690, y=20, width=96, height=35)
        self.BtConfig.configure(text='Configurações')

        self.root.mainloop()

    # Tela home
    def inicio(self):
        # Cor dos slots
        green = '#5FED42'
        # Verificação de menu
        global verify_menu
        global verify_menu_add
        verify_menu = True
        print('Home criada')
        if verify_menu_add == True:
            self.FrAdd_Veiculo.destroy()
            print('Add deletada')
        else:
            pass

        # Frames para os slots
        self.FrInicio = Frame(self.root)
        self.FrInicio.place(relx=0.013, rely=0.175)
        self.FrInicio.configure(relief='groove', borderwidth="2",  height=325, width=776)

        # Slots
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

    # Tela adicionar veiculo
    def add_veiculo(self):
        # Verificação do menu
        global verify_menu
        global verify_menu_add
        print('Add criada')
        if verify_menu == True:
            self.FrInicio.destroy()
            verify_menu_add = True
            print('Home deletada')
        else:
            pass

        # Frames e Entrys
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
        
        # Botão para salvar no banco de dados as informações
        self.BtSalvarVeiculo = ttk.Button(self.FrAdd_Veiculo)
        self.BtSalvarVeiculo.place(relx=0.619, rely=0.892, width=140, height=30)
        self.BtSalvarVeiculo.configure(text='Salvar Veiculo', command=self.get_veiculo)

    # Tela gerenciar veiculos
    def manager_veiculo(self):
        # Verificação do menu
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

        # Frame
        self.FrManager_Veiculo = Frame(self.root)
        self.FrManager_Veiculo.place(relx=0.013, rely=0.175)
        self.FrManager_Veiculo.configure(relief='groove', borderwidth="2",  height=325, width=776)

        # Treeview
        self.Manager_tree = ttk.Treeview(self.FrManager_Veiculo, columns=(1, 2, 3, 4, 5), show='headings')
        self.Manager_tree.place(relx=0.026, rely=0.154, relheight=0.791, relwidth=0.956)
        self.Manager_tree.heading(1, text="ID")
        self.Manager_tree.heading(2, text='Nome')
        self.Manager_tree.heading(3, text='Telefone')
        self.Manager_tree.heading(4, text='Número Veiculo')
        self.Manager_tree.heading(5, text='Hora de Entrada')
        self.Manager_tree.column(1, width=1)
        self.Manager_tree.column(2, width=7)
        self.Manager_tree.column(3, width=4)
        self.Manager_tree.column(4, width=5)
        self.Manager_tree.column(5, width=1)

        # Botões editar e excluir
        self.BtEditTree = ttk.Button(self.FrManager_Veiculo)
        self.BtEditTree.place(x=20, y=10, width=126, height=35)
        self.BtEditTree.configure(text='Editar Veiculo', command=self.editar_manager)

        self.BtExcluirTree = ttk.Button(self.FrManager_Veiculo)
        self.BtExcluirTree.place(x=160, y=10, width=126, height=35)
        self.BtExcluirTree.configure(text='Excluir Veiculo')

        # Conectar-se ao banco de dados e selecionar tudo o que estiver na tabela
        alt = bd.BD()
        alt.conn_bd()
        alt.execute_comand("SELECT * FROM veiculo_table ORDER BY id")
        re = alt.fetchall_comand()

        # Inserir os dados da tabela no treeview
        for row in re:
            self.Manager_tree.insert('', 'end', values=row)

        # Desconectar do banco de dados
        alt.desconectar_BD()

    # Tela historico dos veiculos
    def historico_veiculo(self):
        # Verificação do menu
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

        # Frame
        self.FrHistory_Veiculo = Frame(self.root)
        self.FrHistory_Veiculo.place(relx=0.013, rely=0.175)
        self.FrHistory_Veiculo.configure(relief='groove', borderwidth="2",  height=325, width=776)

        # Treeview de historico
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

    # Função para inserir veiculos no banco de dados
    def get_veiculo(self):
        # Campos para inserir as informações do veiculo
        self.nome = self.EntryAdd_Nome.get()
        self.placa = self.EntryAdd_ID.get()
        self.telefone = self.EntryAdd_Telefone.get()

        # Data de registro no sistema
        data_atual = datetime.now()
        self.data_entrada = data_atual.strftime("%d/%m/%Y %H:%M")

        # Verificar se o veiculo ainda está no estacionamento
        self.exit = 0

        # Inserir informações no Banco de Dados
        alt = bd.BD()
        alt.conn_bd()
        alt.execute_comand("INSERT INTO veiculo_table (nome, telefone, placa, data_entrada, exit, criado_em) values (?, ?, ?, ?, ?, ?)", (self.nome, self.placa, self.telefone, self.data_entrada, self.exit, self.data_entrada))
        alt.persist()
        alt.desconectar_BD()

        # Deletar as entrys após dar commit no banco de dados
        self.EntryAdd_Nome.delete(0, 'end')
        self.EntryAdd_ID.delete(0, 'end')
        self.EntryAdd_Telefone.delete(0, 'end')

    # Função para gerenciar os veiculos
    def editar_manager(self):
        # Selecionar da treeview e banco
        sel = self.Manager_tree.item(self.Manager_tree.selection())['values'][0]
        print(sel)

        # Variaveis relacionadas ao veiculo selecionado no treeview
        nome_sel = self.Manager_tree.item(self.Manager_tree.selection())['values'][1]
        placa_sel = self.Manager_tree.item(self.Manager_tree.selection())['values'][3]
        telefone_sel = self.Manager_tree.item(self.Manager_tree.selection())['values'][2]
        entrada_sel = self.Manager_tree.item(self.Manager_tree.selection())['values'][4]
        saida_sel = self.Manager_tree.item(self.Manager_tree.selection())['values'][5]
        criado_sel = self.Manager_tree.item(self.Manager_tree.selection())['values'][7]
        atualizado_sel = self.Manager_tree.item(self.Manager_tree.selection())['values'][8]

        # Criar janela TopLevel
        editar_window = Toplevel(self.root)
        editar_window.geometry('600x200')

        # Editar nome
        LbNome = LabelFrame(editar_window, text='Nome')
        LbNome.place(x=10, y=0, width=330, height=45)
        EntryNome = ttk.Entry(LbNome)
        EntryNome.place(x=10, y=0, width=306, height=20)
        EntryNome.insert(0, nome_sel)

        # Editar placa
        LbPlaca = LabelFrame(editar_window, text='Placa')
        LbPlaca.place(x=360, y=0, width=160, height=45)
        EntryPlaca = ttk.Entry(LbPlaca)
        EntryPlaca.place(x=10, y=0, width=136, height=20)
        EntryPlaca.insert(0, placa_sel)

        # Editar telefone
        LbTelefone = LabelFrame(editar_window, text='Telefone')
        LbTelefone.place(x=10, y=50, width=330, height=45)
        EntryTelefone = ttk.Entry(LbTelefone)
        EntryTelefone.place(x=10, y=0, width=306, height=20)
        EntryTelefone.insert(0, telefone_sel)

        # Verificar se o "exit" do banco está como 0 ou 1
        Checkstatus = int(self.Manager_tree.item(self.Manager_tree.selection())['values'][6])
        CheckVariavel = IntVar()
        if Checkstatus == 0:
            CheckVariavel.set(2)
        else:
            CheckVariavel.set(1)
        
        # Editar check
        LbCheck = LabelFrame(editar_window, text='Está no estacionamento?')
        LbCheck.place(x=360, y=50, width=160, height=45)
        CheckSim = Radiobutton(LbCheck, text='Sim', variable=CheckVariavel, value=1)
        CheckSim.place(x=10, y=0, width=59, height=20)
        CheckNao = Radiobutton(LbCheck, text='Não', variable=CheckVariavel, value=2)
        CheckNao.place(x=80, y=0, width=59, height=20)

        # Data de entrada
        LbEntrada = LabelFrame(editar_window, text='Data de entrada')
        LbEntrada.place(x=10, y=120, width=150, height=45)
        EntryEntrada = Label(LbEntrada, text=entrada_sel)
        EntryEntrada.place(x=10, y=0, width=115, height=20)

        # Data de saída
        LbSaida = LabelFrame(editar_window, text='Data de saída')
        LbSaida.place(x=170, y=120, width=150, height=45)
        EntrySaida = Label(LbSaida, text=saida_sel)
        EntrySaida.place(x=10, y=0, width=115, height=20)

        # Criado em
        LbCriado = LabelFrame(editar_window, text='Criado em')
        LbCriado.place(x=330, y=120, width=130, height=45)
        EntryCriado = Label(LbCriado, text=criado_sel)
        EntryCriado.place(x=10, y=0, width=100, height=20)

        # Atualizado em
        LbEntrada = LabelFrame(editar_window, text='Atualizado em')
        LbEntrada.place(x=470, y=120, width=120, height=45)
        EntryEntrada = Label(LbEntrada, text=atualizado_sel)
        EntryEntrada.place(x=10, y=0, width=95, height=20)

        # Botão Salvar/Cancelar
        BtSalvar = Button(editar_window, text='Salvar', background='#53dd00')
        BtSalvar.place(x=10, y=170, width=95, height=25)
        BtCancelar = Button(editar_window, text='Cancelar', background='#fb4a4a')
        BtCancelar.place(x=110, y=170, width=95, height=25)

        # Manter janela aberta
        editar_window.mainloop()
