import pandas as pd
import sqlite3
from datetime import datetime
import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def estatistica(user_id, conn):

    cursor = conn.cursor()
    print("\n-----  MENU DE ESTATÍSTICAS  ----")
    
    mes = input("Digite o mês (2 digitos): ")
    ano = input("Digite o ano (4 digitos): ")
    while not (mes.isdigit() and ano.isdigit() and 1 <= int(mes) <= 12):
        print("Entrada inválida para mês ou ano. Por favor, tente novamente.")
        mes = input("Digite o mês (2 digitos): ")
        ano = input("Digite o ano (4 digitos): ")

    cursor.execute('SELECT categoria, valor FROM despesa WHERE user_id = ? AND strftime("%Y-%m", data) = ?', (user_id, f"{ano}-{mes}"))
    dados = cursor.fetchall()


    if dados:

        print("-----  ESTATÍSTICAS  ----")
        print(f"\nMês e Ano selecionados: {mes}/{ano}")

        dados = pd.DataFrame(dados, columns=['Categoria', 'Valor'])

        largura = 50

        max_gasto = dados['Valor'].max()

        for _, linha in dados.iterrows():

            categoria = linha['Categoria']
            gasto = linha['Valor']

            n_barras = int(gasto / max_gasto * largura)

            print(f'{categoria.ljust(15)} | {"#" * n_barras} ({gasto:.2f})')
            time.sleep(2)
    else:
        print("Nenhum gasto registrado para o mês/ano especificado.")
        time.sleep(2)
limpar_tela()
