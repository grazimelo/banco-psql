'''
Lê os dados da planilha XLSX e salva no banco de dados.

https://gist.github.com/rg3915/1d9e49e14d610dbd4cfc03422012e000

https://gist.github.com/rg3915/5fb3a2e7338115bc92e82b7a9a2b372b
'''
import psycopg2
import pandas as pd
from decouple import config

path = 'projeto_psql'
df_categorias = pd.read_excel(f'{path}/categorias.xlsx')
df_produtos = pd.read_excel(f'{path}/produtos.xlsx')
df_produtos_com_categoria = pd.read_excel(f'{path}/produtos-com-categoria.xlsx')


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


connection = connection()
cursor = connection.cursor()


# Tabela categoria
for i, row in df_categorias.iterrows():
    name = row["categoria"]
    cur.execute(f"INSERT INTO categoria (categoria) VALUES ('{name}') ON CONFLICT DO NOTHING")  # noqa


connection.commit()


cur.execute("SELECT * FROM categoria;")
print(cur.fetchall())


# Tabela produto
for i, row in df_produtos.iterrows():
    produto = row["produto"]
    preco = row["preco"]
    cur.execute(f"INSERT INTO produto (produto, preco) VALUES ('{produto}','{preco}') ON CONFLICT DO NOTHING")  # noqa


connection.commit()


cur.execute("SELECT * FROM produto;")
print(cur.fetchall())
