from datetime import datetime

def adicionar_renda(user_id, conn):
    cursor = conn.cursor()
    print('\n------ Por favor, informe o valor a ser adicionado!---------\n')

    valorR = input("Digite o valor da renda (ou pressione Enter para voltar ao Menu Principal): ")

    try:
        valor = float(valorR)
    except ValueError:
        print("Operação cancelada. Voltando ao Menu Principal...")
        return

    data = datetime.now().strftime("%Y-%m-%d")
    hora = datetime.now().strftime("%H:%M:%S")
    descricao = input("Descrição: ").capitalize()

    cursor.execute('INSERT INTO renda (user_id, valor, data, descricao, hora) VALUES (?, ?, ?, ?, ?)', (user_id, valor, data, descricao, hora))
    conn.commit()

    print("Renda adicionada com sucesso!")
