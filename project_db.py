#!/usr/bin/env python
# coding: utf-8

# # Objetivo
#
# Dada uma planilha em Excel, inserir os dados da planilha num banco de dados PostgreSQL.
#
# Dica: você pode usar Python junto com psycopg2 para se conectar no PostgreSQL.
#
# Passos:
#
# * Criar uma virtualenv
#
# * Instalar psycopg2
#
# * Ler os dados da planilha Excel
#
# * Tratar os dados, se necessário
# * Inserir os dados no banco PostgreSQL
# * Coloque seu projeto no Gitlab, ou Github pessoal e me manda o link do repositório

# # Dependências

# ## Biblioteca


import psycopg2
import pandas as pd
from decouple import config


# ## Dados e Constantes


df = pd.read_excel('categorias.xlsx')
df_1 = pd.read_excel('produtos.xlsx')
df_2 = pd.read_excel('produtos-com-categoria.xlsx')


# tabela categoria
df.head()


# Tabela produtos
df_1.head()


# Produtos com categorias
df_2.head()


df_2.columns


# ## Inserindo os dados no banco Psql


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


# ## Tabela `categoria`


# Criando tabela para categoria
cur.execute(
    """CREATE TABLE IF NOT EXISTS categoria (id SERIAL PRIMARY KEY, nome VARCHAR(50));""")


for i, row in df.iterrows():
    name = row["categoria"]
    cur.execute(f"INSERT INTO categoria (nome) VALUES ('{name}')")


connection.commit()


cur.execute("SELECT * FROM categoria;")
cur.fetchall()


# ## Tabela `produtos`


# Criando tabela para produtos.
cur.execute("""CREATE TABLE IF NOT EXISTS produtos(id SERIAL PRIMARY KEY, nome_produto VARCHAR(50), valor_produtos decimal);""")


for i, row in df_1.iterrows():
    nome_produto = row["produto"]
    valor_produtos = row["preco"]
    cur.execute(f"INSERT INTO produtos (nome_produto, valor_produtos) VALUES ('{nome_produto}','{valor_produtos}')")


connection.commit()


cur.execute("SELECT * FROM produtos;")
cur.fetchall()


# ## Tabela `produtos_categoria`


# Produtos com categoria
cur.execute("""CREATE TABLE IF NOT EXISTS produtos_categoria (id SERIAL PRIMARY KEY, nome_produto VARCHAR(50), valor_produto decimal, categoria_tipo INT REFERENCES categoria(id));""")


connection.commit()


for i, row in df_2.iterrows():
    nome_produto = row["produto"]
    valor_produto = row["preco"]
    categoria_tipo = row["categoria"]
    # cur.execute(f"INSERT INTO produtos_categoria (nome_produto,
    # valor_produto, categoria_tipo) VALUES
    # ('{nome_produto}','{valor_produto}',{categoria_tipo})")


# connection.commit()


# cur.execute("SELECT * FROM produtos_categoria;")
# cur.fetchall()


#cur.execute("DELETE FROM produtos where id > 64;")
#cur.execute("DROP TABLE IF EXISTS produtos;")
#cur.execute("ALTER TABLE produtos DROP COLUMN valor_produto;")
#cur.execute("ALTER TABLE produtos ADD valor_produtos decimal;")
