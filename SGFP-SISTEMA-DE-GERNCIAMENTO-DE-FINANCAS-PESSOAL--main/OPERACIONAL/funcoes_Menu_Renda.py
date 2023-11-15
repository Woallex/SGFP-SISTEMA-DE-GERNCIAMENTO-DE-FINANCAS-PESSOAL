from datetime import datetime

def adicionar_renda(user_id, conn):
    cursor = conn.cursor()
    print('\n------ Por favor, informe o valor a ser adicionado!---------\n')

    valor_input = input("\nDigite o valor da renda (ou pressione Enter para voltar ao menu): ")

    if valor_input == '':
        print("Operação cancelada. Voltando ao menu principal...")
        return

    valor = float(valor_input)
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute('INSERT INTO renda (user_id, valor, data) VALUES (?, ?, ?)', (user_id, valor, data))
    conn.commit()

    print("Renda adicionada com sucesso!")
