import menu
def despesa(user_id, conn):
    while True:
        print("-----  MENU DE DESPESAS ----")
        print("1. Adcionar despesa") 
        print("2. Atualizar despesa")
        print("3. Remover depesa")
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
    categoria = input("Qual a categoria do despesa: ")
        
    valor = float(input("Digite o valor do despesa: "))
        
    cursor = conn.cursor()
        
    cursor.execute('INSERT INTO despesa (user_id, categoria, valor) VALUES (?, ?, ?)', (user_id, categoria, valor))

    conn.commit()
        
    print("Gasto adicionado com sucesso!")


def atualizar_despesa(user_id, conn):
    cursor = conn.cursor()

    cursor.execute('SELECT categoria, valor FROM despesa WHERE user_id = ?', (user_id,))
    despesas = cursor.fetchall()

    if despesas:
        print("\n----- VOCÊ ESTÁ ALTERANDO DADOS DA DESPESA ----")
        for index, despesa in enumerate(despesas, start=1):
            categoria, valor = despesa #Desempacota a tupla 'despesa' em duas variáveis chamadas 'categoria' e 'valor'
            print(f"{index}. Categoria: {categoria}, Valor: R$ {valor:.2f}")

        escolha = int(input("\nDigite o número da despesa que deseja atualizar: "))

        if 1 <= escolha <= len(despesas):
            despesa_escolhida = despesas[escolha - 1] #indice inicail 0
            categoria, valor = despesa_escolhida

            nova_categoria = input(f"Nova categoria para '{categoria}' (ou pressione Enter para manter a mesma): ")
            novo_valor = input(f"Novo valor para '{valor:.2f}' (ou pressione Enter para manter o mesmo): ")

            
            if nova_categoria or novo_valor:
                sql = 'UPDATE despesa SET ' #Comando SQL para atualizar a despesa
                parametros = [] #Valores que seram usados na consulta SQL
            
                if nova_categoria:
                    sql += 'categoria = ?, '
                    parametros.append(nova_categoria)

                if novo_valor:
                    sql += 'valor = ?, '
                    parametros.append(float(novo_valor))

                sql = sql.rstrip(', ') #Remove a ultima virgula da string do SQL
                sql += ' WHERE categoria = ? AND valor = ? AND user_id = ?'
                parametros.extend([categoria, valor, user_id])#Adiciona os dados a lista de parametros

                cursor.execute(sql, parametros)
                conn.commit() #Salva e altera o banco

                print("Despesa atualizada com sucesso!")
            else:
                print("Nenhuma mudança realizada.")
        



def remover_despesa(user_id, conn):
    cursor = conn.cursor()

    cursor.execute('SELECT categoria, valor FROM despesa WHERE user_id = ?', (user_id,))
    despesas = cursor.fetchall()

    if despesas:
        print("\n----- VOCÊ ESTÁ DELETANDO DADOS DA DESPESA ----")
        for index, despesa in enumerate(despesas, start=1):
            categoria, valor = despesa
            print(f"{index}. Categoria: {categoria}, Valor: R$ {valor:.2f}")

        categoria_remover = input("\nDigite a categoria da despesa que deseja remover: ")

        if categoria_remover in [d[0] for d in despesas]:
            cursor.execute('DELETE FROM despesa WHERE categoria = ? AND user_id = ?', (categoria_remover, user_id))
            conn.commit()

            print(f"Despesa na categoria '{categoria_remover}' removida com sucesso!")
        else:
            print("Categoria inválida. Tente novamente.")
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