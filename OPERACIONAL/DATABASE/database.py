import sqlite3

def criar_banco_de_dados():
    conn = sqlite3.connect('financas.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT VARCHAR(45),
            cpf TEXT VARCHAR(11),
            senha TEXT VARCHAR(45)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS renda (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE,
            valor FLOAT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS despesa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE,
            categoria TEXT VARCHAR(45),
            valor FLOAT
        )
    ''')

    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS poupanca (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE,
        valorP FLOAT 
        )
    ''')


    conn.commit()
    conn.close()

def conectar_banco_de_dados():
    return sqlite3.connect('financas.db')

def desconectar_banco_de_dados(conn):
    conn.close()
