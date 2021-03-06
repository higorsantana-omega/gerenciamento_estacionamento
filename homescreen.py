import sqlite3
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import bd
from datetime import date, datetime


root = Tk()

# Variaveis para verificar se está em algum menu
verify_menu = None
verify_where = 0

CheckVariavel = IntVar()


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
        alt = bd.Slot_Space()

        # Cor dos slots
        green = '#5FED42'
        # Verificação de menu
        global verify_menu, verify_where
        verify_menu = True
        verify_where = 1
        print('--- Inicio veiculo criada ---')
        if verify_menu == True:
            if verify_where == 4:
                self.FrAdd_Veiculo.destroy()
            if verify_where == 2:
                self.FrManager_Veiculo.destroy()
            if verify_where == 3:
                self.FrHistory_Veiculo.destroy()

        # Frames para os slots
        self.FrInicio = Frame(self.root)
        self.FrInicio.place(relx=0.013, rely=0.175)
        self.FrInicio.configure(relief='groove', borderwidth="2",  height=325, width=776)

        # Slots
        row = 80
        j = 0
        for data in alt:
            self.slot = Frame(self.FrInicio)
            if data[2] == 1:
                self.slot.configure(bg='red', relief='groove', borderwidth="2", width=125, height=75)
            else:
                self.slot.configure(bg='green', relief='groove', borderwidth="2", width=125, height=75)

            if j == 625:
                j = 0
                row += 110
            
            self.slot.place(x=j, y=row)
            j += 125

    # Tela adicionar veiculo
    def add_veiculo(self):
        # Verificação de menu
        global verify_menu, verify_where
        verify_menu = True
        print('--- Adicionar veiculo criada ---')
        if verify_menu == True:
            if verify_where == 1:
                self.FrInicio.destroy()
            if verify_where == 2:
                self.FrManager_Veiculo.destroy()
            if verify_where == 3:
                self.FrHistory_Veiculo.destroy()
            
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
        # Verificação de menu
        global verify_menu, verify_where
        verify_menu = True
        verify_where = 2
        print('--- Manager veiculo criada ---')
        if verify_menu == True:
            if verify_where == 4:
                self.FrAdd_Veiculo.destroy()
            if verify_where == 1:
                self.FrInicio.destroy()
            if verify_where == 3:
                self.FrHistory_Veiculo.destroy()

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
        self.BtExcluirTree.configure(text='Excluir Veiculo', command=self.excluir_veiculo)

        self.atualizar_tree()

    # Tela historico dos veiculos
    def historico_veiculo(self):
        # Verificação de menu
        global verify_menu, verify_where
        verify_menu = True
        verify_where = 3
        print('--- Historico veiculo criada ---')
        if verify_menu == True:
            if verify_where == 4:
                self.FrAdd_Veiculo.destroy()
            if verify_where == 2:
                self.FrManager_Veiculo.destroy()
            if verify_where == 1:
                self.FrInicio.destroy()

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

        # Definir que o veiculo está no estacionamento
        global CheckVariavel
        CheckVariavel.set(1)
        exit_veiculo = CheckVariavel.get()

        spacid = bd.Slot_Disponivel()
        if spacid:
            # Inserir informações no Banco de Dados
            alt = bd.BD()
            alt.conn_bd()
            alt.execute_comand("INSERT INTO veiculo_table (nome, telefone, placa, data_entrada, exit, criado_em) values (?, ?, ?, ?, ?, ?)", (self.nome, self.placa, self.telefone, self.data_entrada, exit_veiculo, self.data_entrada))
            alt.persist()
            alt.execute_comand("UPDATE slot_table SET id_veiculo=?, vazio_ou_nao='1' WHERE id = ?", (self.placa, str(spacid)))
            alt.persist()
            alt.desconectar_BD()
            print('deu')
            # Deletar as entrys após dar commit no banco de dados
            self.EntryAdd_Nome.delete(0, 'end')
            self.EntryAdd_ID.delete(0, 'end')
            self.EntryAdd_Telefone.delete(0, 'end')
            self.EntryAdd_Nome.delete(0, 'end')
            self.EntryAdd_ID.delete(0, 'end')
            self.EntryAdd_Telefone.delete(0, 'end')
            return True
        else:
            # Deletar as entrys após dar commit no banco de dados
            self.EntryAdd_Nome.delete(0, 'end')
            self.EntryAdd_ID.delete(0, 'end')
            self.EntryAdd_Telefone.delete(0, 'end')
            return print('Sem espaço')

    # Função para gerenciar os veiculos
    def editar_manager(self):
        # Selecionar da treeview e banco
        self.sel = self.Manager_tree.item(self.Manager_tree.selection())['values'][0]

        # Variaveis relacionadas ao veiculo selecionado no treeview
        nome_sel = self.Manager_tree.item(self.Manager_tree.selection())['values'][1]
        placa_sel = self.Manager_tree.item(self.Manager_tree.selection())['values'][3]
        telefone_sel = self.Manager_tree.item(self.Manager_tree.selection())['values'][2]
        entrada_sel = self.Manager_tree.item(self.Manager_tree.selection())['values'][4]
        saida_sel = self.Manager_tree.item(self.Manager_tree.selection())['values'][5]
        criado_sel = self.Manager_tree.item(self.Manager_tree.selection())['values'][7]
        atualizado_sel = self.Manager_tree.item(self.Manager_tree.selection())['values'][8]

        # Criar janela TopLevel
        self.editar_window = Toplevel(self.root)
        self.editar_window.geometry('600x200')

        # Editar nome
        LbNome = LabelFrame(self.editar_window, text='Nome')
        LbNome.place(x=10, y=0, width=330, height=45)
        self.EntryNome = ttk.Entry(LbNome)
        self.EntryNome.place(x=10, y=0, width=306, height=20)
        self.EntryNome.insert(0, nome_sel)

        # Editar placa
        LbPlaca = LabelFrame(self.editar_window, text='Placa')
        LbPlaca.place(x=360, y=0, width=160, height=45)
        self.EntryPlaca = ttk.Entry(LbPlaca)
        self.EntryPlaca.place(x=10, y=0, width=136, height=20)
        self.EntryPlaca.insert(0, placa_sel)

        # Editar telefone
        LbTelefone = LabelFrame(self.editar_window, text='Telefone')
        LbTelefone.place(x=10, y=50, width=330, height=45)
        self.EntryTelefone = ttk.Entry(LbTelefone)
        self.EntryTelefone.place(x=10, y=0, width=306, height=20)
        self.EntryTelefone.insert(0, telefone_sel)

        # Verificar se o "exit" do banco está como 0 ou 1
        Checkstatus = int(self.Manager_tree.item(self.Manager_tree.selection())['values'][6])
        global CheckVariavel
        if Checkstatus == 0:
            CheckVariavel.set(0)
        else:
            CheckVariavel.set(1)
        
        # Editar check
        LbCheck = LabelFrame(self.editar_window, text='Está no estacionamento?')
        LbCheck.place(x=360, y=50, width=160, height=45)
        self.CheckSim = Radiobutton(LbCheck, text='Sim', variable=CheckVariavel, value=1)
        self.CheckSim.place(x=10, y=0, width=59, height=20)
        self.CheckNao = Radiobutton(LbCheck, text='Não', variable=CheckVariavel, value=0)
        self.CheckNao.place(x=80, y=0, width=59, height=20)

        # Data de entrada
        LbEntrada = LabelFrame(self.editar_window, text='Data de entrada')
        LbEntrada.place(x=10, y=120, width=150, height=45)
        self.EntryEntrada = Label(LbEntrada, text=entrada_sel)
        self.EntryEntrada.place(x=10, y=0, width=115, height=20)

        # Data de saída
        LbSaida = LabelFrame(self.editar_window, text='Data de saída')
        LbSaida.place(x=170, y=120, width=150, height=45)
        self.EntrySaida = Label(LbSaida, text=saida_sel)
        self.EntrySaida.place(x=10, y=0, width=115, height=20)

        # Criado em
        LbCriado = LabelFrame(self.editar_window, text='Criado em')
        LbCriado.place(x=330, y=120, width=130, height=45)
        self.EntryCriado = Label(LbCriado, text=criado_sel)
        self.EntryCriado.place(x=10, y=0, width=100, height=20)

        # Atualizado em
        LbEntrada = LabelFrame(self.editar_window, text='Atualizado em')
        LbEntrada.place(x=470, y=120, width=120, height=45)
        self.EntryEntrada = Label(LbEntrada, text=atualizado_sel)
        self.EntryEntrada.place(x=10, y=0, width=95, height=20)

        # Botão Salvar/Cancelar
        BtSalvar = Button(self.editar_window, text='Salvar', background='#53dd00', command=self.salvar_configs)
        BtSalvar.place(x=10, y=170, width=95, height=25)
        self.BtCancelar = Button(self.editar_window, text='Cancelar', background='#fb4a4a')
        self.BtCancelar.place(x=110, y=170, width=95, height=25)

        # Manter janela aberta
        self.editar_window.mainloop()

    # Função para salvar
    def salvar_configs(self):
        # Data em que foi atualizado
        atualizado = datetime.now()
        atualizado_em = atualizado.strftime("%d/%m/%Y %H:%M")
        
        # gets
        nome_get = self.EntryNome.get()
        telefone_get = self.EntryTelefone.get()
        placa_get = self.EntryPlaca.get()
        exit_get = CheckVariavel.get()

        # Conectar-se ao banco de dados e inserir novos dados
        alt = bd.BD()
        try:
            alt.conn_bd()
            alt.execute_comand("""
            UPDATE veiculo_table
            SET nome = ?, telefone = ?, placa = ?, exit = ?, atualizado_em = ?
            WHERE id = ?
            """, (nome_get, telefone_get, placa_get,
                exit_get, atualizado_em, self.sel))
            alt.persist()
            alt.desconectar_BD()
            messagebox.showinfo(title='Dados alterado', message='Os dados foram alterados com sucesso.')
            self.editar_window.destroy()
        except:
            messagebox.showerror(title='Erro', message='Ocorreu um erro ao se conectar com o banco de dados')

        self.atualizar_tree()

    # Excluir veiculo do banco de dados
    def excluir_veiculo(self):
        # Excluir veiculo selecionado
        sel = self.Manager_tree.item(self.Manager_tree.selection())['values'][0]

        # Tentar conectar-se ao banco de dados
        try:
            # Conectar-se ao banco
            alt = bd.BD()
            alt.conn_bd()
            alt.execute_comand("DELETE FROM veiculo_table WHERE id = ? ", (sel,))
            alt.persist()
            alt.desconectar_BD()
            messagebox.showinfo(title='Deletado', message='Veiculo deletado com sucesso.')
        except:
            messagebox.showerror(title='Erro', message='Ocorreu um erro tentar deletar o veiculo')

        # Atualizar Tree
        self.atualizar_tree()

    # Atualizar a tree quando necessario
    def atualizar_tree(self):
        # Apagar o que está antes da atualização
        for i in self.Manager_tree.get_children():
            self.Manager_tree.delete(i)
        
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
