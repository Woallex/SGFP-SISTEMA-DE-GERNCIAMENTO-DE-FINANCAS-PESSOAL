def adicionar_poupanca(user_id, conn):
        
    valorPoupanca = float(input("Digite o valor a ser depositado na sua poupança: "))
        
    cursor = conn.cursor()
        
    cursor.execute('INSERT INTO poupanca (user_id, valorP) VALUES (?, ?)', (user_id, valorP))

    conn.commit()
        
    print("Valor adicionado com sucesso!")

    