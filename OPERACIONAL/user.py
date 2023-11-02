import sqlite3

def fazer_login(conn, cpf, senha):
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM usuarios WHERE cpf = ? AND senha = ?', (cpf, senha))
    user_id = cursor.fetchone()
    return user_id

def fazer_cadastro(conn, nome, cpf, senha):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nome, cpf, senha) VALUES (?, ?, ?)', (nome, cpf, senha))
    conn.commit()


def mostrar_saldo(conn, user_id):
    cursor = conn.cursor()

    cursor.execute('SELECT SUM(valor) FROM renda WHERE user_id = ?', (user_id,))
    total_renda = cursor.fetchone()[0] or 0.0

    cursor.execute('SELECT SUM(valor) FROM despesa WHERE user_id = ?', (user_id,))
    total_gastos = cursor.fetchone()[0] or 0.0

    saldo = total_renda - total_gastos

    return saldo
