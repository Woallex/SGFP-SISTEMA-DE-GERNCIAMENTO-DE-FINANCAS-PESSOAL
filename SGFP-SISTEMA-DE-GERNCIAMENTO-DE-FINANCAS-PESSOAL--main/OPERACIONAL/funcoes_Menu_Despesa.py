import menu
import user
import funcoes_Menu_Renda
from datetime import datetime

def despesa(user_id, conn):
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM categorias')
    count = cursor.fetchone()[0]

    if count == 0:
        categorias_definidas(conn)

    while True:
        saldo = user.mostrar_saldo(conn, user_id)

        print("\n-----  MENU DE DESPESA  ----\n")
        print(f"Saldo atual em conta R$: {saldo}\n")
        print("1. Adicionar Despesa") 
        print("2. Remover Despesa")
        print("3. Ver Despesa")

        opcao = input("\nOpção desejada (ou pressione Enter para voltar ao Menu Principal): ")

        if opcao == '1':
            adicionar_despesa(user_id, conn)
        elif opcao == '2':
            remover_despesa(user_id, conn)
        elif opcao == '3':
            ver_despesa(user_id, conn)
        elif opcao == '':
            return
        else:
            print("Opção inválida. Tente novamente.")

def adicionar_despesa(user_id, conn):
    saldo = user.mostrar_saldo(conn, user_id)
    cursor = conn.cursor()
    
    cursor.execute('SELECT id, nome FROM categorias')
    categorias = cursor.fetchall()


    if categorias:
        print("\n----Categorias pré-definidas:-----\n")
        for categoria_id, categoria_nome in categorias:
            print(f"{categoria_id}. {categoria_nome}")

        categoria_escolhida = input("\nEscolha uma categoria pelo número (ou digite uma nova categoria): ")
        while categoria_escolhida == '':
                    categoria_escolhida = input("\nEscolha uma categoria pelo número (ou digite uma nova categoria): ")


        try:
            categoria_id = int(categoria_escolhida)
            if categoria_id in [cat[0] for cat in categorias]: # cria uma nova lista contendo apenas os IDs de categoria da lista original
                categoria = categorias[categoria_id - 1][1] 
                
            else:
                nova_categoria = input("\nDigite a nova categoria: ").capitalize()
                cursor.execute('INSERT INTO categorias (nome) VALUES (?)', (nova_categoria,))
                categoria = nova_categoria
                
        except ValueError:
            cursor.execute('INSERT INTO categorias (nome) VALUES (?)', (categoria_escolhida,))
            categoria = categoria_escolhida

        valorD = input("\nDigite o valor da despesa (ou pressione Enter para voltar ao Menu de Despesa): ")
        
        try:
            valor = float(valorD)
        except ValueError:
            print("Operação cancelada. Voltando ao Menu Principal...")
            return

        data = datetime.now().strftime("%Y-%m-%d")
        hora = datetime.now().strftime("%H:%M:%S")

        descricao = input("Descrição: ").capitalize()

        cursor.execute('INSERT INTO despesa (user_id, categoria, valor, descricao, data,  hora) VALUES (?, ?, ?, ?, ?, ?)', (user_id, categoria, valor, descricao, data, hora))
        conn.commit()

    
        if valor > saldo:
            novoSaldo = saldo - valor
            print(f"\nATENÇÃO: O valor da despesa ({valor:.2f}) é maior que o saldo disponível ({saldo:.2f}).")
            print(f"         SEU SALDO ATUAL É DE: {novoSaldo}")
            print("         PARA UM MELHOR CONTROLE DE SUAS FINANÇAS ACONSELHAMOS MANTER SEMPRE O SALDO POSITIVO.")

    else:
        print("Nenhuma categoria pré-definida disponível. Você precisa criar categorias antes de adicionar uma despesa.")

def categorias_definidas(conn):
    categorias = ['Alimentação', 'Transporte', 'Lazer', 'Moradia', 'Saúde', 'Educação', 'Outros']
    cursor = conn.cursor()
    for categoria in categorias:
        cursor.execute('INSERT INTO categorias (nome) VALUES (?)', (categoria,))
    conn.commit()


def remover_despesa(user_id, conn):
    cursor = conn.cursor()

    cursor.execute('SELECT id, categoria, valor FROM despesa WHERE user_id = ?', (user_id,))
    despesa = cursor.fetchall()

    if despesa:
        print("\n----- VOCÊ ESTÁ DELETANDO DADOS DA DESPESA ----")
        for index, (despesa_id, categoria, valor) in enumerate(despesa, start=1):
            print(f"{index}. ID: {despesa_id}, Categoria: {categoria}, Valor: R$ {valor:.2f}")

        id_remover = input("\nDigite o ID da despesa que deseja remover (ou pressione Enter para voltar ao Menu de Despesa): ")

        try:
            id_remover = int(id_remover)
        except ValueError:
            print("Operação cancelada. Voltando ao Menu de Despesa...")
            return

        if id_remover in [d[0] for d in despesa]:
            cursor.execute('DELETE FROM despesa WHERE id = ? AND user_id = ?', (id_remover, user_id))
            conn.commit()

            print(f"Despesa com ID {id_remover} removida com sucesso!")
        else:
            print("ID inválido. Tente novamente.")
    else:
        print("Nenhuma despesa registrada.")

def ver_despesa(user_id, conn):
    cursor = conn.cursor()

    cursor.execute('SELECT categoria, valor, descricao, data, hora FROM despesa WHERE user_id = ?', (user_id,))
    despesa = cursor.fetchall()
    
    if despesa:
        print("\n----- DESPESA ----")
        for categoria, valor, descricao, data, hora in despesa:
            print(f"Categoria: {categoria} \nValor: R$ {valor:.2f} \nDescrição: {descricao} \nData: {data} \nHora: {hora} \n")
    else:
        print("Nenhuma despesa registrada.")