from DATABASE import database
import user
import menu
import pandas as pd



def main():
    database.criar_banco_de_dados()

    while True:
        print("  ☆ Olá, seja bem-vindo1 ao seu Sistema de Gerenciamento de Finanças Pessoal ☆")
        print("-----  MENU INICIAL ----")
        print("1. Login")
        print("2. Cadastro")
        print("3. Sair")

        opcao = input("Escolha a opção: ")

        conn = database.conectar_banco_de_dados()

        if opcao == '1':
            cpf = input("Digite seu CPF: ")
            senha = input("Digite sua senha: ")
            user_info = user.fazer_login(conn, cpf, senha)
            if user_info:
                user_id, nome = user_info
                print("Login realizado com sucesso!")
                menu.mostrar_menu_principal(user_id, conn, nome)

            else:
                print("Credenciais inválidas. Tente novamente.")
        elif opcao == '2':
            nome = input("Digite seu nome: ")
            cpf = input("Digite seu CPF: ")
            senha = input("Digite sua senha: ")
            user.fazer_cadastro(conn, nome, cpf, senha)
            print("Cadastro realizado com sucesso.")

        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

        database.desconectar_banco_de_dados(conn)

if __name__ == "__main__":
    main()
    