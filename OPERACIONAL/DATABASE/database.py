import sqlite3

def criar_banco_de_dados():
    conn = sqlite3.connect('financas.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            cpf TEXT,
            senha TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS renda (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            valor REAL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS despesa (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            categoria TEXT,
            valor REAL
        )
    ''')


    conn.commit()
    conn.close()

def conectar_banco_de_dados():
    return sqlite3.connect('financas.db')

def desconectar_banco_de_dados(conn):
    conn.close()
