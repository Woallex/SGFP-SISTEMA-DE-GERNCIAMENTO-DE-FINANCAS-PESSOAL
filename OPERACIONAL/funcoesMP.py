import menu

def poupanca(user_id, conn):
    
    print("-----  MENU POUPANÇAS ----")
    print("1. Adcionar poupança")
    print("2. Atualizar poupança")
    print("3. Remover poupança")
    print("4. Ver poupanças")
    print("5. Voltar ao menu de finanças")

    opcao = int(input("Opção desejada: "))

    if opcao == 1:

        adicionar_poupanca(user_id, conn)

    elif opcao == 2:

        atualiza_poupanca()

    elif opcao == 3:

        remove_poupanca()

    elif opcao == 4:

        lista_poupanca()

    elif opcao == 5:

        return menu

    else:
        print("Opção inválida. Tente novamente.")


def adicionar_poupanca(user_id, conn):
    saldo = int(input("Digite o Saldo da poupança: "))
    objetivo = input("Digite a descrição/objetivo da poupança: ")
    contaAssociada = ("Conta bancaria que esta armazenada a pupança: ")

    valorp = float(input("Digite o valor a ser depositado na sua poupança: "))
        
    cursor = conn.cursor()
        
    cursor.execute('INSERT INTO poupanca (user_id, valorP) VALUES (?, ?)', (user_id, valorp))

    conn.commit()
        
    print("Valor adicionado com sucesso!")
    

def atualiza_poupanca():
    saldo = int(input("Digite o Saldo da poupança: "))
    objetivo = input("Digite a descrição/objetivo da poupança: ")
    contaAssociada = ("Conta bancaria que esta armazenada a pupança: ")

def remove_poupanca():
    print("Em breve")
    
def lista_poupanca():
    print("Em breve")
        
