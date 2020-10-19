import subprocess

# Cria db
subprocess.call("createdb -U postgres my_db", shell=True)

# Cria tabela
create_table_sql = "CREATE TABLE produtos (id SERIAL PRIMARY KEY, produto VARCHAR(100));"
create_table_psql = f'psql -U postgres -c "{create_table_sql}" estoque'
subprocess.call(create_table_psql, shell=True)