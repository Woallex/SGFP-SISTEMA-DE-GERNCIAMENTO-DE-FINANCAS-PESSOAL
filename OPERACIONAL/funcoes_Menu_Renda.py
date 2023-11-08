def adicionar_renda(user_id, conn):
    print('\n------ Por favor informe o valor a ser adicionado!---------\n')
    valor = float(input("\nDigite o valor da renda: "))    

    cursor = conn.cursor()

    cursor.execute('INSERT INTO renda (user_id, valor) VALUES (?, ?)', (user_id, valor))

    conn.commit()
    
    print("Renda adicionada com sucesso!")