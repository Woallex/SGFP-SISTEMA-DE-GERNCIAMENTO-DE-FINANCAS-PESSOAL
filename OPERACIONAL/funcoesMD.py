import menu
def despesa(user_id, conn):
    categorias_definidas(conn) 
    while True:
        print("-----  MENU DE DESPESAS ----")
        print("1. Adicionar despesa") 
        print("2. Atualizar despesa")
        print("3. Remover despesa")
        print("4. Ver despesa")
        print("5. Voltar ao menu de finanças")

        opcao = int(input("Opção desejada: "))

        if opcao == 1:
            adicionar_despesa(user_id, conn)

        elif opcao == 2:
            atualizar_despesa(user_id, conn)

        elif opcao == 3:
            remover_despesa(user_id, conn)

        elif opcao == 4:
            ver_despesa(user_id, conn)

        elif opcao == 5:
            break

        else:
            print("Opção inválida. Tente novamente.")

def adicionar_despesa(user_id, conn):
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome FROM categorias')
    categorias = cursor.fetchall()

    if categorias:
        print("Categorias pré-definidas:")
        for categoria_id, categoria_nome in categorias:
            print(f"{categoria_id}. {categoria_nome}")

        categoria_escolhida = input("Escolha uma categoria pelo número (ou digite uma nova categoria): ")
        try:
            categoria_id = int(categoria_escolhida)
            if categoria_id in [cat[0] for cat in categorias]:
                categoria = categorias[categoria_id - 1][1]
                
            else:
                nova_categoria = input("Digite a nova categoria: ")
                cursor.execute('INSERT INTO categorias (nome) VALUES (?)', (nova_categoria,))
                categoria = nova_categoria
                
        except ValueError:
            cursor.execute('INSERT INTO categorias (nome) VALUES (?)', (categoria_escolhida,))
            categoria = categoria_escolhida

        valor = float(input("Digite o valor da despesa:"))
        cursor.execute('INSERT INTO despesa (user_id, categoria, valor) VALUES (?, ?, ?)', (user_id, categoria, valor))
        conn.commit()
        print("Gasto adicionado com sucesso!")
    else:
        print("Nenhuma categoria pré-definida disponível. Você precisa criar categorias antes de adicionar uma despesa.")

def atualizar_despesa(user_id, conn):
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome FROM categorias')
    categorias = cursor.fetchall()

    if categorias:
        print("Categorias pré-definidas:")
        for categoria_id, categoria_nome in categorias:
            print(f"{categoria_id}. {categoria_nome}")

        escolha_categoria = input("Escolha uma categoria pelo número (ou digite uma nova categoria): ")
        try:
            categoria_id = int(escolha_categoria)
            if categoria_id in [cat[0] for cat in categorias]:
                categoria = categorias[categoria_id - 1][1]
                
            else:
                nova_categoria = input("Digite a nova categoria: ")
                cursor.execute('INSERT INTO categorias (nome) VALUES (?)', (nova_categoria,))
                categoria = nova_categoria
                
        except ValueError:
            cursor.execute('INSERT INTO categorias (nome) VALUES (?)', (escolha_categoria,))
            categoria = escolha_categoria

    else:
        print("Nenhuma categoria pré-definida disponível. Você precisa criar categorias antes de atualizar uma despesa.")

def remover_despesa(user_id, conn):
    cursor = conn.cursor()

    cursor.execute('SELECT id, categoria, valor FROM despesa WHERE user_id = ?', (user_id,))
    despesas = cursor.fetchall()

    if despesas:
        print("\n----- VOCÊ ESTÁ DELETANDO DADOS DA DESPESA ----")
        for index, (despesa_id, categoria, valor) in enumerate(despesas, start=1):
            print(f"{index}. ID: {despesa_id}, Categoria: {categoria}, Valor: R$ {valor:.2f}")

        id_remover = int(input("\nDigite o ID da despesa que deseja remover: "))

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

    cursor.execute('SELECT categoria, valor FROM despesa WHERE user_id = ?', (user_id,))
    despesa = cursor.fetchall()

    if despesa:
        print("\n----- DESPESA ----")
        for categoria, valor in despesa:
            print(f"Categoria: {categoria}, Valor: R$ {valor:.2f}")
    else:
        print("Nenhuma despesa registrada.")

def categorias_definidas(conn):
    categorias = ['Alimentação', 'Transporte', 'Lazer', 'Moradia', 'Saúde', 'Educação', 'Outros']
    cursor = conn.cursor()
    for categoria in categorias:
        cursor.execute('INSERT INTO categorias (nome) VALUES (?)', (categoria,))
    conn.commit()