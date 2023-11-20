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
        print(f"Saldo atual em conta R$: {saldo}")
        print("1. Adicionar despesa") 
        print("2. Remover despesa")
        print("3. Ver despesa")
        print("4. Voltar ao Menu Principal")

        opcao = input("Opção desejada (ou pressione Enter para mostrar o menu novamente): ")

        if opcao == '1':
            adicionar_despesa(user_id, conn)
        elif opcao == '2':
            remover_despesa(user_id, conn)
        elif opcao == '3':
            ver_despesa(user_id, conn)
        elif opcao == '4':
            break
        elif opcao == '':
            continue
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

        if categoria_escolhida == '':
            print("Operação cancelada. Voltando ao menu despesa...")
            return

        try:
            categoria_id = int(categoria_escolhida)
            if categoria_id in [cat[0] for cat in categorias]:
                categoria = categorias[categoria_id - 1][1]
                
            else:
                nova_categoria = input("\nDigite a nova categoria: ")
                cursor.execute('INSERT INTO categorias (nome) VALUES (?)', (nova_categoria,))
                categoria = nova_categoria
                
        except ValueError:
            cursor.execute('INSERT INTO categorias (nome) VALUES (?)', (categoria_escolhida,))
            categoria = categoria_escolhida

        valor = input("\nDigite o valor da despesa (ou pressione Enter para voltar ao menu): ")

        if valor == '' or str:
            print("Operação cancelada. Voltando ao Menu Despesa...")
            return
        
        valor = float(valor)
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        descricao = input("Descrição: ")

        cursor.execute('INSERT INTO despesa (user_id, categoria, valor, data, descricao) VALUES (?, ?, ?, ?, ?)', (user_id, categoria, valor, data, descricao))
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
    despesas = cursor.fetchall()

    if despesas:
        print("\n----- VOCÊ ESTÁ DELETANDO DADOS DA DESPESA ----")
        for index, (despesa_id, categoria, valor) in enumerate(despesas, start=1):
            print(f"{index}. ID: {despesa_id}, Categoria: {categoria}, Valor: R$ {valor:.2f}")

        id_remover = input("\nDigite o ID da despesa que deseja remover (ou pressione Enter para voltar ao menu): ")

        if id_remover == '' or str:
            print("Operação cancelada. Voltando ao Menu Despesa...")
            return  

        id_remover = int(id_remover)

        if id_remover in [d[0] for d in despesas]:
            cursor.execute('DELETE FROM despesa WHERE id = ? AND user_id = ?', (id_remover, user_id))
            conn.commit()

            print(f"Despesa com ID {id_remover} removida com sucesso!")
        else:
            print("ID inválido. Tente novamente.")
    else:
        print("Nenhuma despesa registrada.")

def ver_despesa(user_id, conn):
    cursor = conn.cursor()

    cursor.execute('SELECT categoria, valor, descricao, data FROM despesa WHERE user_id = ?', (user_id,))
    despesa = cursor.fetchall()
    if despesa:
        print("\n----- DESPESA ----")
        for categoria, valor, descricao, data in despesa:
            print(f"Categoria: {categoria} \nValor: R$ {valor:.2f} \nDescrição: {descricao} \nData: {data} \n")
    else:
        print("Nenhuma despesa registrada.")