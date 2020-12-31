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

InitDB()
