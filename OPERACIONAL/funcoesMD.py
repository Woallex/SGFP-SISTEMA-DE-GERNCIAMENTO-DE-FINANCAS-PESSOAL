def adicionar_despesa(user_id, conn):
    categoria = input("Qual a categoria do despesa: ")
        
    valor = float(input("Digite o valor do despesa: "))
        
    cursor = conn.cursor()
        
    cursor.execute('INSERT INTO despesa (user_id, categoria, valor) VALUES (?, ?, ?)', (user_id, categoria, valor))

    conn.commit()
        
    print("Gasto adicionado com sucesso!")

#def atualizar_despesa():
    ###################

#def remover_despesa():
    ###################

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