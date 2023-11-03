from DATABASE import database

import os

import user

import funcoesMD

import pandas as pd

def mostrar_menu_principal(user_id, conn):

    while True:        

        saldo = user.mostrar_saldo(conn, user_id)

        print("-----  MENU DE PRINCIPAL ----")

        print(f"\nSaldo atual R$: {saldo}")

        print("1. Adicionar Saldo")

        print("2. Despesa")

        print("3. Extrato")

        print("4. Estatisticas")

        print("5. Poupança")

        print("6. Outros")

        print("7. Configurações do Usuário")

        print("8. Sair")

        escolha = input("Escolha a opção: ")

        conn = database.conectar_banco_de_dados()

        if escolha == '1': 

            adicionar_renda(user_id, conn)

        elif escolha == '2':

            despesa(user_id, conn)

        elif escolha == '3':

            exibir_extrato_gastos(conn, user_id)

        elif escolha == '4':
            estatistica(user_id, conn)

        elif escolha == '8':

            database.desconectar_banco_de_dados(conn)

            break 
        else:

            print("Opção inválida. Tente novamente.")
        

def adicionar_renda(user_id, conn):

    valor = float(input("Digite o valor da renda: "))    

    cursor = conn.cursor()

    cursor.execute('INSERT INTO renda (user_id, valor) VALUES (?, ?)', (user_id, valor))

    conn.commit()
    
    print("Renda adicionada com sucesso!")

##################################### DESPESAS ################################################

def despesa(user_id, conn):

    print("-----  MENU DE DESPESAS ----")
    print("1. Adcionar despesa") 
    print("2. Atualizar despesa")
    print("3. Remover depesa")
    print("4. Ver despesa")
    print("5. Voltar ao menu de finanças")

    opcao = int(input("Opção desejada: "))

    if opcao == 1:
        funcoesMD.adicionar_despesa(user_id, conn)
    elif opcao == 2:
        atualizar_despesa()
    elif opcao == 3:
        remover_despesa()
    elif opcao == 4:
        funcoesMD.ver_despesa(user_id, conn)
    elif opcao == 5:
        menu_sistema()
    else:
        print("Opção inválida. Tente novamente.")



#def nova_despesa():
#    categoria = input("Categoria: ")
 #   valor = input("Valor R$: ")
  #  descricao = input("Descricao da Despesa: ")
   # data = input("Digite a data: ")

def lista_despesas():
    print("em breve...")

    
def estatistica(user_id, conn):

    cursor = conn.cursor()

    cursor.execute('SELECT categoria, valor FROM gastos WHERE user_id = ?', (user_id,))
    dados = cursor.fetchall()

    if dados:

        dados = pd.DataFrame(dados, columns=['Categoria', 'Valor']) #Um DataFrame é uma estrutura de dados tabular semelhante a uma planilha.

        largura = 50

        max_gasto = dados['Valor'].max()

        for _, linha in dados.iterrows(): #dados.iterrows() é um método que percorre as linhas do DataFrame dados e retorna um iterador que produz pares (índice, linha).

            categoria = linha['Categoria']
            gasto = linha['Valor']

            n_barras = int(gasto / max_gasto * largura)

            print(f'{categoria.ljust(15)} | {"#" * n_barras} ({gasto:.2f})')
            # ljust(15) alinha a categoria à esquerda com uma largura de 15 caracteres. 
    else:
        print("Nenhum gasto registrado.")


def exibir_extrato_gastos(user_id, conn):

    cursor = conn.cursor()

    cursor.execute('SELECT descricao, valor FROM gastos WHERE user_id = ?', (user_id,))

    gastos = cursor.fetchall()
    
    if gastos:

        print("\nExtrato de Gastos:")

        for gasto in gastos:

            descricao, valor = gasto

            print(f"{descricao}: R$ {valor:.2f}")
    else:

        print("Nenhum gasto registrado.")

############################################### POUPANÇA ############################

def poupanca():
    print("-----  MENU POUPANÇAS ----")
    print("1. Adcionar poupança")
    print("2. Atualizar poupança")
    print("3. Remover poupança")
    print("4. Ver poupanças")
    print("5. Voltar ao menu de finanças")

    opcao = int(input("Opção desejada: "))

    if opcao == 1:
        nova_poupanca()
    elif opcao == 2:
        atualiza_poupanca()
    elif opcao == 3:
        remove_poupanca()
    elif opcao == 4:
        lista_poupanca()
    elif opcao == 5:
        menu_sistema()
    else:
        print("Opção inválida. Tente novamente.")

def nova_poupanca():
    saldo = int(input("Digite o Saldo da poupança: "))
    objetivo = input("Digite a descrição/objetivo da poupança: ")
    contaAssociada = ("Conta bancaria que esta armazenada a pupança: ")

def atualiza_poupanca():
    saldo = int(input("Digite o Saldo da poupança: "))
    objetivo = input("Digite a descrição/objetivo da poupança: ")
    contaAssociada = ("Conta bancaria que esta armazenada a pupança: ")

def remove_poupanca():
    print("Em breve")
    
def lista_poupanca():
    print("Em breve")
        

#def limpar_tela():

#    if os.name == 'nt':

#        os.system('cls')


