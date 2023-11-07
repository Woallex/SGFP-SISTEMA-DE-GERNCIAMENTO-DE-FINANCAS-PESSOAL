from DATABASE import database
import user
import menu
import pandas as pd


def main():
    database.criar_banco_de_dados()

    while True:
        print("  ☆ Olá, seja bem-vindo ao seu Sistema de Gerenciamento de Finanças Pessoal ☆")
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

#AJUSTES A SEREM RALIZADOS

#1. AO ADICIONAR UMA DISPESA O SISTEMA DEVE MOSTRAR O CAMPO "MENU DE DISPESA"

#2. APÓS MOSTRAR A ESTATISTICA DEVE APARECER A OPÇÃO "VOLTAR PARA O MEU PRINCIPLA"

#3. APÓS ADICIONAR NOVA DISPESA DEVE APARECER UM CAMPO "ADD NOVA DESPESA S/N?". SE "SIM", MOSTRAR CATEGORIA E VALOR
#                   SE "NÃO", DIRECIONAR PARA O MEU DE DESPESAS

#4.SEMPRE ENTRE UM ACESSO E OUTRO DEVE TER A OPÇÃO DE VOLTAR. 