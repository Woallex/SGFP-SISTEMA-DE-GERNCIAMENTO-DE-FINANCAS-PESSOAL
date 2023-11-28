from validate_docbr import CPF
import msvcrt

def getpass(prompt="Password: "):
    print(prompt, end="", flush=True)
    password = ""
    while True:
        key = msvcrt.getch()
        if key == b'\r' or key == b'\n':
            print()
            break
        elif key == b'\x08':
            if password:
                password = password[:-1]
                print("\b \b", end="", flush=True)
        else:
            password += key.decode("utf-8")
            print("*", end="", flush=True)
    return password

def validar_cpf(cpf):
    cpf_validator = CPF()
    return cpf_validator.validate(cpf)

def validar_senha(senha):
    return len(senha) >= 6


def obter_cpf_valido():
    while True:
        cpf = input("Digite seu CPF: ")
        if validar_cpf(cpf):
            return cpf
        else:
            print("CPF inválido. Tente novamente.")

def obter_senha_valida():
    senha_valida = False
    while not senha_valida:
        senha = getpass("Digite sua senha: ")
        senha_confirmacao = getpass("Confirme sua senha: ")

        if senha != senha_confirmacao:
            print("Senhas não coincidem. Tente novamente.")
        elif not validar_senha(senha):
            print("Senha deve ter pelo menos 6 caracteres. Tente novamente.")
        else:
            senha_valida = True

    return senha


def fazer_login(conn, cpf, senha):
    cursor = conn.cursor()

    if not validar_cpf(cpf):
        return None

    cursor.execute('SELECT id, nome FROM usuarios WHERE cpf = ? AND senha = ?', (cpf, senha))
    user_info = cursor.fetchone()

    if user_info:
        return user_info
    else:
        print("Credenciais inválidas. Tente novamente.")
        return None

def fazer_cadastro(conn, nome, cpf, senha):
    cursor = conn.cursor()
    
    cursor.execute('SELECT id FROM usuarios WHERE cpf = ?', (cpf,))
    if cursor.fetchone():
        print("CPF já cadastrado. Tente novamente.")
        return

    cursor.execute('INSERT INTO usuarios (nome, cpf, senha) VALUES (?, ?, ?)', (nome, cpf, senha))
    conn.commit()

def mostrar_saldo(conn, user_id):
    cursor = conn.cursor()

    cursor.execute('SELECT SUM(valor) FROM renda WHERE user_id = ?', (user_id,))
    total_renda = cursor.fetchone()[0] or 0.0

    cursor.execute('SELECT SUM(valor) FROM despesa WHERE user_id = ?', (user_id,))
    total_gastos = cursor.fetchone()[0] or 0.0

    saldo = total_renda - total_gastos

    return saldo

def mostrar_saldoPoupanca(conn, user_id):
    cursor = conn.cursor()

    cursor.execute('SELECT SUM(valorP) FROM poupanca WHERE user_id = ?', (user_id,))
    total_valorP = cursor.fetchone()[0] or 0.0

    saldoPoupanca = total_valorP

    return saldoPoupanca

def exibir_extrato_gastos(user_id, conn):
    cursor = conn.cursor()

    cursor.execute('SELECT categoria, valor, data, hora FROM despesa WHERE user_id = ?', (user_id,))

    gastos = cursor.fetchall()

    if gastos:
        print("\nExtrato de Gastos:")
        for gasto in gastos:
            categoria, valor, data, hora = gasto
            print(f"{categoria}: R$ {valor:.2f} em {data} às {hora}")
    else:
        print("Nenhum gasto registrado.")
