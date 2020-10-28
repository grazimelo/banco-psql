'''
Lê os dados da planilha XLSX e salva no banco de dados.

https://gist.github.com/rg3915/1d9e49e14d610dbd4cfc03422012e000

https://gist.github.com/rg3915/5fb3a2e7338115bc92e82b7a9a2b372b
'''
import psycopg2
import pandas as pd
from decouple import config
from pprint import pprint

# DML - data manipulation language


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
    for i, row in df_categorias.iterrows():
        name = row["categoria"]
        cursor.execute(f"INSERT INTO categoria (categoria) VALUES ('{name}') ON CONFLICT DO NOTHING")  # noqa
    connection.commit()


def insert_produto():
    for i, row in df_produtos.iterrows():
        produto = row["produto"]
        preco = row["preco"]~

def insert_produtos_com_categoria():
    for produto in df_produtos_com_categoria.itertuples():
        campo = dict_categoria.get(str(produto.categoria))
        cursor.execute(f"SELECT * FROM categoria WHERE categoria='{campo}';")
        categoria = cursor.fetchall()
        categoria_id = categoria[~o_sql)
    connection.commit()


if __name__ == '__main__':
    path = 'projeto_psql'
    df_categorias = pd.read_excel(f'{path}/categorias.xlsx')
    df_produtos = pd.read_excel(f'{path}/produtos.xlsx')
    df_produtos_com_categoria = pd.read_excel(f'{path}/produtos-com-categoria.xlsx')

    connection = connection()
    cursor = connection.cursor()

    # Monta uma lista de categorias.
    items = df_categorias.T.apply(dict).tolist()

    # Monta um dicionário de categorias.
    dict_categoria = get_data(items)

    insert_categoria()

    cursor.execute("SELECT * FROM categoria;")
    pprint(cursor.fetchall())

    insert_produto()

    cursor.execute("SELECT * FROM produto;")
    pprint(cursor.fetchall())

    insert_produtos_com_categoria()

    cursor.execute("SELECT * FROM produto_categoria;")
    pprint(cursor.fetchall())

    cursor.execute("""
        SELECT * FROM produto_categoria as p INNER JOIN categoria ON 
        (p.categoria_id = categoria.id) ORDER BY p.id;
        """)
    result = cursor.fetchall()

    res = pd.DataFrame(result, columns=['id', 'produto', 'preco', 'categoria_id', 'id', 'categoria'])  # noqa
    print(res)
