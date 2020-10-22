'''
Create tables with Python and subprocess.

https://gist.github.com/rg3915/4ffb0bfdccf1a205ee1761185730411d
'''
import subprocess

# DML - data manipulation language

# Cria tabela categoria
create_table_sql = """
    CREATE TABLE IF NOT EXISTS categoria 
    (id SERIAL PRIMARY KEY, categoria VARCHAR(50));"""

create_table_psql = f'psql -U postgres -c "{create_table_sql}" my_db'
subprocess.call(create_table_psql, shell=True)

# Cria tabela produto
create_table_sql = """
    CREATE TABLE IF NOT EXISTS produto 
    (id SERIAL PRIMARY KEY, produto VARCHAR(50), preco decimal);"""

create_table_psql = f'psql -U postgres -c "{create_table_sql}" my_db'
subprocess.call(create_table_psql, shell=True)

# Cria tabela produto com categoria
create_table_sql = """
    CREATE TABLE IF NOT EXISTS produto_categoria 
    (id SERIAL PRIMARY KEY, 
    produto VARCHAR(50), 
    preco decimal, 
    categoria_id INT REFERENCES categoria(id));"""

create_table_psql = f'psql -U postgres -c "{create_table_sql}" my_db'
subprocess.call(create_table_psql, shell=True)


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
