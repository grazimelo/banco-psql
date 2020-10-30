'''
Create tables with Python and subprocess.

https://gist.github.com/rg3915/4ffb0bfdccf1a205ee1761185730411d
'''
import psycopg2
from decouple import config


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


# Cria tabela cliente
create_table_sql = """
    CREATE TABLE IF NOT EXISTS cliente 
    (id SERIAL PRIMARY KEY, nome VARCHAR(50) UNIQUE);"""

cursor.execute(create_table_sql)

# Cria tabela categoria
create_table_sql = """
    CREATE TABLE IF NOT EXISTS categoria
    (id SERIAL PRIMARY KEY, categoria VARCHAR(50) UNIQUE);"""

cursor.execute(create_table_sql)


# Cria tabela produto com categoria
create_table_sql = """
    CREATE TABLE IF NOT EXISTS produto
    (id SERIAL PRIMARY KEY,
    produto VARCHAR(50) UNIQUE,
    preco decimal,
    categoria_id INT REFERENCES categoria(id));"""

cursor.execute(create_table_sql)

# Cria tabela venda
create_table_sql = """
    CREATE TABLE IF NOT EXISTS venda
    (id SERIAL PRIMARY KEY,
    data DATE,
    slug VARCHAR(36),
    cliente_id INT REFERENCES cliente(id));"""

cursor.execute(create_table_sql)

# Cria tabela itens da venda
create_table_sql = """
    CREATE TABLE IF NOT EXISTS itens_venda
    (id SERIAL PRIMARY KEY,
    quantidade INT,
    preco_venda DECIMAL,
    venda_id INT REFERENCES venda(id),
    produto_id INT REFERENCES produto(id));"""

cursor.execute(create_table_sql)

connection.commit()

# To show columns name type
print()
print('To show columns name type:')
print('$ sudo su - postgres')
print('$ psql my_db')
print("my_db=# SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'categoria';")  # noqa
print(' column_name ')
print('-------------')
print(' id')
print(' categoria')
print('(2 rows)')
