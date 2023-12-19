import time
import menu
import user
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def poupanca(user_id, conn):
    try:
        print("\n")
        print("------------------------ MENU POUPANÇAS ------------------------")
        saldoPoupanca = user.mostrar_saldoPoupanca(conn, user_id)
        print(f"Valor total em Poupança: R${saldoPoupanca:.2f}")
        print("1. Adcionar poupança")
        print("2. Atualizar poupança")
        print("3. Remover poupança")
        print("4. Ver poupanças")
        print("5. Voltar ao menu de finanças")

        opcao = int(input("Opção desejada: "))

        if opcao == 1:

            adicionar_poupanca(user_id, conn)

        elif opcao == 2:

            atualiza_poupanca(user_id, conn)

        elif opcao == 3:

            remove_poupanca(user_id, conn)

        elif opcao == 4:

            lista_poupanca(user_id, conn)

        elif opcao == 5:

            return menu()

        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)
            limpar_tela()

    except:
        print("Desculpe, ocorreu um erro inesperado")
        time.sleep(1)
        limpar_tela()

def adicionar_poupanca(user_id, conn):
    try:
        print("\n")
        print("-------------------- ADCIONAR POUPANÇA --------------------")

        valorP = float(input("Digite o Saldo da poupança: R$"))
        if valorP <= 0:
                raise ValueError("O valor da poupança deve ser maior que zero e não pode ser em branco.")
                
    
        objetivo = input("Digite a descrição/objetivo da poupança: ").capitalize()
        if objetivo == "":
            objetivo = ""

        contaAssociada = input("Conta bancaria que esta armazenada a poupança: ").capitalize()
        while contaAssociada == "":
            print("Este é um campo obrigatório, por favor preencha o campo.")
            time.sleep(2)
            contaAssociada = input("Conta bancaria que esta armazenada a poupança: ").capitalize()

        data = input("Digite a data de abertura da poupança: ") 
        if data == "":
            data = ""

        print("\n") 
        print(f"Você esta inserindo as seguintes informações:\nSaldo: R${valorP:.2f}\nObjetivo: {objetivo}\nConta que armazena a poupança: {contaAssociada}\nData de abertura da poupança:{data}")

        tecla_S =  input("Pressione a tecla S para confirmar: ").upper()
        if tecla_S in ["Sim", "S", "s", "sim", "SIM"]:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO poupanca (user_id, valorP, objetivo, contaAssociada, data) VALUES (?, ?, ?, ?, ?)', (user_id, valorP, objetivo,contaAssociada, data))
            conn.commit()
            print("Poupança adicionada com sucesso!")
            print("Voltando ao Menu Poupança.")
            time.sleep(2)
            limpar_tela()
            poupanca(user_id, conn)
        else:
            print("Voltando ao Menu Poupança.")
            time.sleep(2)
            limpar_tela()
            poupanca(user_id, conn)

    except ValueError as ve:
        print(f"Erro: {ve}")

def atualiza_poupanca(user_id, conn):
    try:
        print("\n")
        lista_poupanca(user_id, conn, return_to_menu = False)

        id = int(input("Digite o ID da poupança a ser atualizada: "))


        cursor = conn.cursor()
        cursor.execute("SELECT id FROM poupanca WHERE id = ?", (id,))
        resultado = cursor.fetchone()
        if resultado:

            valorP = float(input("Digite o Saldo da poupança: R$"))
            if valorP <= 0: 
                raise ValueError("O valor da poupança deve ser maior que zero e não pode ser em branco.")
            
            objetivo = input("Digite a descrição/objetivo da poupança: ").capitalize()
            if objetivo == "":
                objetivo = ""

            contaAssociada = input("Conta bancaria que esta armazenada a poupança: ").capitalize()
            while contaAssociada == "":
                print("Este é um campo obrigatório, por favor preencha o campo.")
                contaAssociada = input("Conta bancaria que esta armazenada a poupança: ").capitalize()

            data = input("Digite a data de abertura da poupança: ")
            if data == "":
                data = ""

            print(f"Você esta atualizando as seguintes informações:\nSaldo: R$ {valorP:.2f}\nObjetivo: {objetivo}\nConta que armazena a poupança: {contaAssociada}\nData de abertura da poupança:{data}")
            
            tecla_S =  input("Pressione a tecla S para confirmar a atualização: ").upper()
            if tecla_S in ["Sim", "S", "s", "sim"]:
                cursor = conn.cursor()
                cursor.execute("UPDATE poupanca SET valorP= ?, objetivo = ?, contaAssociada= ?, data = ? WHERE id = ?", (valorP, objetivo, contaAssociada, data, id,))
                conn.commit()
                print("Poupança atualizada com sucesso com sucesso!")
                time.sleep(2)
                limpar_tela()
                poupanca(user_id, conn)
            else:
                print("Voltando ao Menu Poupança.")
                time.sleep(2)
                limpar_tela()
                poupanca(user_id, conn)
        else:
            print("Nenhuma poupança relacionada ao ID que você informou.")
            time.len.sleep(2)
            limpar_tela()
            poupanca(user_id, conn)
    except:
        print("Ocorreu um erro durante a atualização da poupança, por favor tente novamente")
        time.len.sleep(2)
        limpar_tela()

def remove_poupanca(user_id, conn):
    try: 
        print("\n")
        lista_poupanca(user_id, conn, return_to_menu = False)
        print("\n")
        id = int(input("Digite o ID da poupança a ser removida: "))
        # Verifica se o ID existe no banco de dados
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM poupanca WHERE id = ?", (id,))
        resultado = cursor.fetchone()
        if resultado:
            # Se O ID existe, então permita a remoção
            cursor = conn.cursor()
            cursor.execute("DELETE FROM poupanca WHERE id = ?", (id,))
            conn.commit()
            print("Poupança removida com sucesso!")
            print("Voltando ao Menu Poupança...")
            time.sleep(2)
            limpar_tela()
            poupanca(user_id, conn)
        else:
            print("ID da Poupança não encontrado. A despesa não pode ser Removida.")
            print("Voltando ao Menu Poupança...")
            time.sleep(2)
            limpar_tela()
            poupanca(user_id, conn)
    except:
        print("Ocorreu um erro durante a atualização da poupança, por favor tente novamente")
        time.sleep(2)
        limpar_tela()

def lista_poupanca(user_id, conn, return_to_menu = True):
    try:
        print("\n")
        print("------------------- AQUI ESTÃO SUAS POUPANÇAS: -------------------")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM poupanca WHERE user_id = ?', (user_id,))
        for e in cursor.fetchall():
            print("ID da poupança: ",e[0])
            print("Valor que você esta armazenando na poupança:R$", e[2])
            print("Seu objetivo com a poupança é: ", e[3])
            print("Conta que armazena a poupança: ", e[4])
            print("A data de abertura dessa poupança foi: ", e[5])
            print("---------------------------------------------------------")

        if return_to_menu:
            poupanca(user_id, conn)
    except:
        print("Ocorreu um erro durante a atualização da poupança, por favor tente novamente")
        time.sleep(2)
        limpar_tela()

