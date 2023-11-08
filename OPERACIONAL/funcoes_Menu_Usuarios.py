import sqlite3
import main

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
            senha = input("Digite a sua senha atual: ")
            if verificar_senha(conn, user_id, senha):
                novo_nome = input(f"Nome atual: {nome_atual}\nDigite o novo nome: ")
                atualizar_nome_usuario(conn, user_id, novo_nome)
                print("Nome atualizado com sucesso!")
            else:
                print("Senha incorreta. Tente novamente.")

        elif escolha == '2':
            senha = input("Digite a sua senha atual: ")
            if verificar_senha(conn, user_id, senha):
                novo_cpf = input(f"CPF atual: {cpf_atual}\nDigite o novo CPF: ")
                atualizar_cpf_usuario(conn, user_id, novo_cpf)
                print("CPF atualizado com sucesso!")
            else:
                print("Senha incorreta. Tente novamente.")

        elif escolha == '3':
            senha = input("Digite a sua senha atual: ")
            if verificar_senha(conn, user_id, senha):
                nova_senha = input("Digite a nova senha: ")
                confirmar_senha = input("Confirme a nova senha: ")
                if nova_senha == confirmar_senha:
                    atualizar_senha_usuario(conn, user_id, nova_senha)
                    print("Senha atualizada com sucesso!")
                else:
                    print("As senhas não coincidem. Tente novamente.")
            else:
                print("Senha incorreta. Tente novamente.")

        elif escolha == '4':
            senha = input("Digite a sua senha atual para confirmar a exclusão: ")
            conf_senha = input("Confirme sua senha: ")
            if conf_senha == senha:
                if verificar_senha(conn, user_id, senha):
                    deletar_usuario(conn, user_id)
                    print("Usuário deletado com sucesso!")
                    main.main()
                    return
            else:
                print("Senha incorreta. A exclusão não foi realizada.")
        
        elif escolha == '5':
            break

        else:
            print("Opção inválida. Tente novamente.")


def atualizar_nome_usuario(conn, user_id, novo_nome):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET nome = ? WHERE id = ?", (novo_nome, user_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao atualizar o nome do usuário: {e}")

def atualizar_cpf_usuario(conn, user_id, novo_cpf):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET cpf = ? WHERE id = ?", (novo_cpf, user_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao atualizar o CPF do usuário: {e}")

def atualizar_senha_usuario(conn, user_id, nova_senha):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET senha = ? WHERE id = ?", (nova_senha, user_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao atualizar a senha do usuário: {e}")

def deletar_usuario(conn, user_id):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (user_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao deletar o usuário: {e}")
        
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
        return False
