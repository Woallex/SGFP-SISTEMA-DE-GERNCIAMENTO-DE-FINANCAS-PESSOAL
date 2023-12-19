from DATABASE import database
import user
import menu
import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_inicial():
    print("  $ Olá, seja bem-vindo ao seu Sistema de Gerenciamento de Finanças Pessoal $")
    print("-----  MENU INICIAL ----")
    print("1. Login")
    print("2. Cadastro")
    print("3. Sair")

def realizar_login(conn):
    cpf = input("Digite seu CPF: ")
    senha = user.getpass("Digite sua senha: ")
    user_info = user.fazer_login(conn, cpf, senha)
    if user_info:
        user_id, nome = user_info
        print("Login realizado com sucesso!")
        menu.mostrar_menu_principal(user_id, conn, nome)
        time.sleep(1)
        limpar_tela()
    else:
        print("Credenciais inválidas. Tente novamente.")
        time.sleep(1)
        limpar_tela()

def realizar_cadastro(conn):
    nome = input("Digite seu nome: ").title()
    while len(nome) < 3:
        print("Nome deve ter pelo menos 3 caracteres. Tente novamente!")
        time.sleep(1)
        nome = input("Digite seu nome: ").title()

    cpf_valido = False
    while not cpf_valido:
        cpf = input("Digite seu CPF: ")
        if not user.validar_cpf(cpf):
            print("CPF inválido. Tente novamente.")
            time.sleep(1)

        else:
            cpf_valido = True

    senha = user.obter_senha_valida()
    user.fazer_cadastro(conn, nome, cpf, senha)
    limpar_tela()

def main():
    try:
        database.criar_banco_de_dados()

        while True:
            mostrar_menu_inicial()
            escolha = input("Escolha a opção: ")

            conn = database.conectar_banco_de_dados()

            if escolha == '1':
                realizar_login(conn)
            elif escolha == '2':
                realizar_cadastro(conn)
            elif escolha == '3':
                break
            else:
                print("Opção inválida. Tente novamente.")
                time.sleep(1)
                limpar_tela()

            database.desconectar_banco_de_dados(conn)

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
