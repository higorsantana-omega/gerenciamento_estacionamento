import sqlite3

class BD():
    database = 'veiculos.db'
    conn = None
    cursor = None
    connected = None

    def conn_bd(self):
        BD.conn = sqlite3.connect(BD.database)
        BD.cursor = BD.conn.cursor()
        BD.connected = True

    # Desconectar
    def desconectar_BD(self):
        BD.conn.close()
        BD.connected = False
    
    # Executar comando no BD
    def execute_comand(self, sql, params=None):
        if BD.connected == True:
            if params == None:
                BD.cursor.execute(sql)
            else:
                BD.cursor.execute(sql, params)
            return (True,)
        else:
            return str(False)
        
    # Efetivar alterações
    def persist(self):
        if BD.connected == True:
            BD.conn.commit()
            return True
        else:
            return False

def InitDB():
    alt = BD()
    alt.conn_bd()
    alt.execute_comand("""CREATE TABLE IF NOT EXISTS admin_table(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )""")
    alt.persist()
    alt.desconectar_BD()

def VeiculoDB():
    alt = BD()
    alt.conn_bd()
    alt.execute_comand("""CREATE TABLE IF NOT EXISTS veiculo_table(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            telefone INTEGER,
            placa TEXT,
            data_entrada TEXT,
            data_saida TEXT,
            exit NUMERIC,
            criado_em TEXT,
            atualizado_em TEXT
        )""")
    alt.persist()
    alt.desconectar_BD()

def SlotDB():
    alt = BD()
    alt.conn_bd()
    alt.execute_comand("""CREATE TABLE IF NOT EXISTS slot_table(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_veiculo INTEGER,
            vazio_ou_nao NUMERIC,
            FOREIGN KEY(id_veiculo) REFERENCES veiculo_table(id)
        )""")
    alt.persist()
    alt.desconectar_BD()

InitDB()
VeiculoDB()
SlotDB()
