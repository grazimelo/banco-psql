#!/usr/bin/env python
# coding: utf-8


import psycopg2
import pandas as pd
from decouple import config
# # https://gist.github.com/rg3915/5fb3a2e7338115bc92e82b7a9a2b372b


df_produtos = pd.read_excel('produtos-com-categoria.xlsx')
df_categorias = pd.read_excel('categorias.xlsx')


df_produtos


try:
    connection = psycopg2.connect(user="my_usuario",
                                  password=config("PASSWORD"),
                                  host="127.0.0.1",
                                  port="5432",
                                  database="my_db")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)


cur = connection.cursor()


df_categorias


# https://gist.github.com/rg3915/0f63ee9bde818c4a56abb110c94b855b
def get_data(items, field='categoria'):
    '''
    Lê os dados para extrair id e um outro campo como identificador único
    e monta um dicionário.
    '''
    my_dict = {}
    for item in items:
        my_dict[str(item['id'])] = item[field]
    return my_dict


items = df_categorias.T.apply(dict).tolist()
items


dicionario = {}


dicionario['nome'] = 'Regis'


dicionario['sobrenome'] = 'Santos'


dicionario


d = {}
for item in items:
    print(item)
    d[str(item['id'])] = item['categoria']


d


d['700']


d['915']


dict_categoria = get_data(df_categorias.T.apply(dict).tolist())
dict_categoria


for produto in df_produtos.head().iterrows():
    print(produto[1][2])


for produto in df_produtos.head().itertuples():
    print(produto.produto, produto.preco, produto.categoria)


dict_categoria.get(str('314'))


for produto in df_produtos.itertuples():
    campo = dict_categoria.get(str(produto.categoria))
    print(produto.categoria, campo)
    print({'categoria': campo})
    cur.execute(f"SELECT * FROM categoria WHERE nome='{campo}';")
    categoria = cur.fetchall()
    print(categoria)
    print(categoria[0])
    print(categoria[0][0])
    print()


cur.execute("DELETE FROM produtos_categoria;")
connection.commit()


for produto in df_produtos.itertuples():
    campo = dict_categoria.get(str(produto.categoria))
    cur.execute(f"SELECT * FROM categoria WHERE nome='{campo}';")
    categoria = cur.fetchall()
    categoria_id = categoria[0][0]
    # print(categoria_id)
    nome_produto = produto.produto
    valor_produto = produto.preco
    categoria_tipo = int(categoria_id)
    cur.execute(f"INSERT INTO produtos_categoria (nome_produto, valor_produto, categoria_tipo) VALUES ('{nome_produto}',{valor_produto},{categoria_tipo})")


connection.commit()


cur.execute("SELECT * FROM produtos_categoria;")
cur.fetchall()


cur.execute("SELECT * FROM produtos_categoria as p INNER JOIN categoria ON (p.categoria_tipo = categoria.id) ORDER BY p.id;")
result = cur.fetchall()
result


pd.DataFrame(result, columns=['id', 'nome_produto',
                              'valor_produto', 'categoria_tipo', 'id', 'nome'])
