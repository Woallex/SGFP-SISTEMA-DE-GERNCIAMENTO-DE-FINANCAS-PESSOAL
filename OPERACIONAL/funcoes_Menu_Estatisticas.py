import pandas as pd

def estatistica(user_id, conn):

    cursor = conn.cursor()

    cursor.execute('SELECT categoria, valor FROM despesa WHERE user_id = ?', (user_id,))
    dados = cursor.fetchall()

    if dados:

        dados = pd.DataFrame(dados, columns=['Categoria', 'Valor']) #Um DataFrame é uma estrutura de dados tabular semelhante a uma planilha.

        largura = 50

        max_gasto = dados['Valor'].max()

        for _, linha in dados.iterrows(): #dados.iterrows() é um método que percorre as linhas do DataFrame dados e retorna um iterador que produz pares (índice, linha).

            categoria = linha['Categoria']
            gasto = linha['Valor']

            n_barras = int(gasto / max_gasto * largura)

            print(f'{categoria.ljust(15)} | {"#" * n_barras} ({gasto:.2f})')
            # ljust(15) alinha a categoria à esquerda com uma largura de 15 caracteres. 
    else:
        print("Nenhum gasto registrado.")
