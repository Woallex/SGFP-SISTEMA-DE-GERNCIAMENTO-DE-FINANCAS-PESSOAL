import sqlite3
import main
import os
import time
import user 

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def configuracoes_usuario(user_id, conn):
    
    while True:
        cursor = conn.cursor()
        cursor.execute("SELECT nome, cpf FROM usuarios WHERE id = ?", (user_id,))
        resultado = cursor.fetchone()
        nome_atual = resultado[0]
        cpf_atual = resultado[1]

        print("----- CONFIGURAÇÕES DO USUÁRIO ----")
        print(f'Olá, {nome_atual}! O que deseja fazer?')
        print("1. Alterar Nome.")
        print("2. Alterar CPF.")
        print("3. Alterar Senha.")
        print('4. Deletar usuário.')
        print("5. Voltar ao Menu Principal.")

        escolha = input("Escolha a opção: ")

        if escolha == '1':
            senha = user.getpass("Digite a sua senha atual: ")
            if verificar_senha(conn, user_id, senha):
                novo_nome = input(f"Nome atual: {nome_atual}\nDigite o novo nome: ")
                if novo_nome == "":
                    print("Você esta inserindo um campo em branco. Por favor tente novamente.")
                    time.sleep(2)
                    configuracoes_usuario(user_id, conn)
                atualizar_nome_usuario(conn, user_id, novo_nome)
                print("Nome atualizado com sucesso!")
                time.sleep(2)
                limpar_tela()
            else:
                print("Senha incorreta. Tente novamente.")
                time.sleep(2)
                limpar_tela()

        elif escolha == '2':
            senha = user.getpass("Digite a sua senha atual: ")
            if verificar_senha(conn, user_id, senha):
                novo_cpf = input(f"CPF atual: {cpf_atual}\nDigite o novo CPF: ")
                if novo_cpf == "":
                    print("O CPF não pode ser um campo em branco. Tente novamente.")
                    time.sleep(2)
                    configuracoes_usuario(user_id, conn)
                atualizar_cpf_usuario(conn, user_id, novo_cpf)
                print("CPF atualizado com sucesso!")
                time.sleep(2)
                limpar_tela()
            else:
                print("Senha incorreta. Tente novamente.")
                time.sleep(2)
                limpar_tela()

        elif escolha == '3':
            senha = user.getpass("Digite a sua senha atual: ")
            if verificar_senha(conn, user_id, senha):
                nova_senha = input("Digite a nova senha: ")
                if nova_senha == "":
                    print("Você esta inserindo um campo em branco. Por favor tente novamente.")
                    time.sleep(2)
                    configuracoes_usuario(user_id, conn)
                confirmar_senha = user.getpass("Confirme a nova senha: ")
                if nova_senha == confirmar_senha:
                    atualizar_senha_usuario(conn, user_id, nova_senha)
                    print("Senha atualizada com sucesso!")
                    time.sleep(2)
                    limpar_tela()
                else:
                    print("As senhas não coincidem. Tente novamente.")
                    time.sleep(2)
            else:
                print("Senha incorreta. Tente novamente.")
                time.sleep(2)

        elif escolha == '4':
            senha = user.getpass("Digite a sua senha atual para confirmar a exclusão: ")
            if senha =="":
                print("Você esta inserindo um espaço em branco. Por favor tente novamente.")
                time.sleep(2)
                configuracoes_usuario(user_id, conn)
            conf_senha = user.getpass("Confirme sua senha: ")
            time.sleep(2)
            if conf_senha == senha:
                if verificar_senha(conn, user_id, senha):
                    deletar_usuario(conn, user_id)
                    print("Usuário deletado com sucesso!")
                    time.sleep(2)
                    limpar_tela()
                    main.main()
                    return
            else:
                print("Senha incorreta. A exclusão não foi realizada.")
                time.sleep(2)
                limpar_tela()
        
        elif escolha == '5':
            break

        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)
            limpar_tela()


def atualizar_nome_usuario(conn, user_id, novo_nome):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET nome = ? WHERE id = ?", (novo_nome, user_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao atualizar o nome do usuário: {e}")
        time.sleep(2)

def atualizar_cpf_usuario(conn, user_id, novo_cpf):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET cpf = ? WHERE id = ?", (novo_cpf, user_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao atualizar o CPF do usuário: {e}")
        time.sleep(2)

def atualizar_senha_usuario(conn, user_id, nova_senha):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET senha = ? WHERE id = ?", (nova_senha, user_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao atualizar a senha do usuário: {e}")
        time.sleep(2)

def deletar_usuario(conn, user_id):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (user_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao deletar o usuário: {e}")
        time.sleep(2)
        
def verificar_senha(conn, user_id, senha):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT senha FROM usuarios WHERE id = ?", (user_id,))
        resultado = cursor.fetchone()
        if resultado:
            senha_armazenada = resultado[0]
            return senha == senha_armazenada
        else:
            return False
    except sqlite3.Error as e:
        print(f"Erro ao verificar a senha: {e}")
        time.sleep(2)
        return False
