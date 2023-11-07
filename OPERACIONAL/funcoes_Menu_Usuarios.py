import sqlite3
def configuracoes_usuario(user_id, conn):
    while True:
        print("----- CONFIGURAÇÕES DO USUÁRIO ----")
        print("1. Alterar Nome")
        print("2. Alterar CPF")
        print("3. Alterar Senha")
        print("4. Voltar ao Menu Principal")

        escolha = input("Escolha a opção: ")

        if escolha == '1':
            novo_nome = input("Digite o novo nome: ")
            # Atualize o nome do usuário no banco de dados
            atualizar_nome_usuario(conn, user_id, novo_nome)
            print("Nome atualizado com sucesso!")

        elif escolha == '2':
            novo_cpf = input("Digite o novo CPF: ")
            # Atualize o CPF do usuário no banco de dados
            atualizar_cpf_usuario(conn, user_id, novo_cpf)
            print("CPF atualizado com sucesso!")

        elif escolha == '3':
            nova_senha = input("Digite a nova senha: ")
            # Atualize a senha do usuário no banco de dados
            atualizar_senha_usuario(conn, user_id, nova_senha)
            print("Senha atualizada com sucesso!")

        elif escolha == '4':
            break

        else:
            print("Opção inválida. Tente novamente.")

# Funções de exemplo para atualização de dados do usuário
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