
'''
Lê os dados da planilha XLSX e salva no banco de dados.

https://gist.github.com/rg3915/1d9e49e14d610dbd4cfc03422012e000

https://gist.github.com/rg3915/5fb3a2e7338115bc92e82b7a9a2b372b
'''
import psycopg2
import pandas as pd
from decouple import config
from pprint import pprint


def connection():
    # Conectando no banco
    try:
        connection = psycopg2.connect(
            user="my_user",
            password=config("PASSWORD"),
            host="127.0.0.1",
            port="5432",
            database="my_db"
        )

        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print(connection.get_dsn_parameters(), "\n")

        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")
        return connection

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)


def insert_cliente():
    for i, row in df_cliente.iterrows():
        name = row["nome"]
        cursor.execute(f"INSERT INTO cliente (nome) VALUES ('{name}') ON CONFLICT DO NOTHING")  # noqa
    connection.commit()    


def get_data(items, field='categoria'):
    '''
    Lê os dados para extrair id e um outro campo como identificador único
    e monta um dicionário.
    # https://gist.github.com/rg3915/0f63ee9bde818c4a56abb110c94b855b
    '''
    my_dict = {}
    for item in items:
        my_dict[str(item['id'])] = item[field]
    return my_dict


def insert_categoria():
    for i, row in df_categoria.iterrows():
        name = row["categoria"]
        cursor.execute(f"INSERT INTO categoria (categoria) VALUES ('{name}') ON CONFLICT DO NOTHING")  # noqa
    connection.commit()


def insert_produto():
    for i, row in df_produto.iterrows():
        produto = row["produto"]
        preco = round(row['preco'] * 5.6, 2)
        print(row['categoria_id'])
        campo = dict_categoria.get(str(row['categoria_id']))
        print(campo)
        cursor.execute(f"SELECT * FROM categoria WHERE categoria='{campo}';")
        categoria = cursor.fetchall()
        print(categoria)
        print(categoria[0][0])
        categoria_id = categoria[0][0]
        cursor.execute(f"INSERT INTO produto (produto, preco, categoria_id) VALUES ('{produto}', '{preco}', '{categoria_id}') ON CONFLICT DO NOTHING")  # noqa
    connection.commit()


def insert_venda():
    for i, row in df_venda.iterrows():
        print(row)
        data = row['data']
        campo = dict_cliente.get(str(row['cliente_id']))
        print(campo)
        cursor.execute(f"SELECT * FROM cliente WHERE nome='{campo}';")
        cliente = cursor.fetchall()
        print(cliente)
        print(cliente[0][0])
        cliente_id = cliente[0][0]
        slug = row['slug']
        cursor.execute(f"INSERT INTO venda (data, cliente_id, slug) VALUES ('{data}', '{cliente_id}', '{slug}') ON CONFLICT DO NOTHING")  # noqa
    connection.commit()


def insert_itens_venda():
    for i, row in df_itens_venda.iterrows():
        quantidade = int(row['quantidade'])
        preco_venda = row['preco_venda']
        venda_id = str(row['venda_id']).replace('.0', '')
        print(venda_id)
        venda = dict_venda.get(venda_id)
        cursor.execute(f"SELECT * FROM venda WHERE slug='{venda}';")
        venda = cursor.fetchall()
        venda_id = venda[0][0]
        produto_id = str(row['produto_id']).replace('.0', '')
        print(produto_id)
        produto = dict_produto.get(produto_id)
        cursor.execute(f"SELECT * FROM produto WHERE produto='{produto}';")
        produto = cursor.fetchall()
        print(produto)
        produto_id = produto[0][0]
        cursor.execute(f"INSERT INTO itens_venda (quantidade, preco_venda, venda_id, produto_id) VALUES ('{quantidade}', '{preco_venda}', '{venda_id}', '{produto_id}') ON CONFLICT DO NOTHING")  # noqa
    connection.commit()

if __name__ == '__main__':
    path = 'projeto_psql'
    df_itens_venda = pd.read_excel(f'{path}/itens_venda.xlsx')
    df_venda = pd.read_excel(f'{path}/venda.xlsx')
    df_cliente = pd.read_excel(f'{path}/cliente.xlsx')
    df_categoria = pd.read_excel(f'{path}/categoria.xlsx')
    df_produto = pd.read_excel(f'{path}/produto.xlsx')

    connection = connection()
    cursor = connection.cursor()


    insert_cliente()
 
    # Monta uma lista de categorias.
    items = df_categoria.T.apply(dict).tolist()

    # Monta um dicionário de categorias.
    dict_categoria = get_data(items)

    insert_categoria()

    # Monta uma lista de clientes.
    items_cliente = df_cliente.T.apply(dict).tolist()
    items_cliente[:1]

    # Monta um dicionário de clientes.
    dict_cliente = get_data(items=items_cliente, field='nome')
    dict_cliente

   # Monta uma lista de vendas.
    items_venda = df_venda.T.apply(dict).tolist()
    items_venda[:2]

    # Monta uma lista de produtos.
    items_produto = df_produto.T.apply(dict).tolist()
    items_produto[:2]

    # Monta um dicionário de produtos.
    dict_produto = get_data(items=items_produto, field='produto')
    dict_produto

    insert_produto()

    insert_itens_venda()