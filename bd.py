from datetime import date
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

    def fetchall_comand(self):
        return BD.cursor.fetchall()
        
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
            exit INTEGER,
            criado_em TEXT,
            atualizado_em TEXT,
            slot INTEGER UNIQUE
        )""")
    alt.persist()
    alt.desconectar_BD()

def SlotDB():
    alt = BD()
    alt.conn_bd()
    alt.execute_comand("""CREATE TABLE IF NOT EXISTS slot_table(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_veiculo INTEGER,
            espaco_para INTEGER,
            vazio_ou_nao INTEGER
        )""")
    alt.persist()
    alt.desconectar_BD()

def Slot_Space():
    alt = BD()
    alt.conn_bd()
    alt.execute_comand("SELECT * FROM slot_table")
    data = alt.fetchall_comand()
    alt.desconectar_BD()
    print(data)
    return data

def Slot_Disponivel():
    alt = BD()
    alt.conn_bd()
    alt.execute_comand("SELECT * FROM slot_table WHERE vazio_ou_nao = '1'")
    data = alt.fetchall_comand()
    alt.desconectar_BD()
    print(data)
    if len(data) > 0:
        return data[0][0]
    else:
        return False

InitDB()
VeiculoDB()
SlotDB()
Slot_Space()
Slot_Disponivel()