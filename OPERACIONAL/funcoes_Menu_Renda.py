def adicionar_renda(user_id, conn):

    valor = float(input("Digite o valor da renda: "))    

    cursor = conn.cursor()

    cursor.execute('INSERT INTO renda (user_id, valor) VALUES (?, ?)', (user_id, valor))

    conn.commit()
    
    print("Renda adicionada com sucesso!")