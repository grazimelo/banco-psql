Projeto para treinamento em banco de dados PostgreSQL.

# Desafio 1 - importar dados de planilha Excel

Dada uma planilha em Excel, inserir os dados da planilha num banco de dados PostgreSQL.

**Dica:** você pode usar Python junto com [psycopg2](https://www.psycopg.org/docs/install.html) para se conectar no PostgreSQL.

Passos:

1. Criar uma virtualenv
2. Instalar psycopg2
3. Ler os dados da planilha Excel
4. Tratar os dados, se necessário
5. Inserir os dados no banco PostgreSQL
6. Coloque seu projeto no Gitlab, ou Github pessoal e me manda o link do repositório


# Desafio 2 - importar dados de planilhas relacionadas

Dada uma planilha com dados de Produtos e outra de Categorias, inserir os dados num banco de dados PostgreSQL, relacionando cada produto com sua categoria.

Os passos são idênticos aos anteriores.

Coloque tudo no mesmo repositório.

https://gist.github.com/rg3915/1d9e49e14d610dbd4cfc03422012e000


## Como rodar o projeto

```
git clone https://github.com/grazimelo/banco-psql.git
cd banco-psql
python -m venv .venv
```

Para ativar a virtualenv  digite:

```
source .venv/bin/activate
```

Para instalar as dependências:

```
pip install -r requirements.txt
```

## Criando banco de dados manualmente

### Opção 1

```
sudo su - postgres
createdb my_db
createuser -P my_user
psql my_db
GRANT ALL PRIVILEGES ON DATABASE my_db TO my_user;
```

### Opção 2

```
sudo su - postgres
psql
CREATE ROLE my_user ENCRYPTED PASSWORD 'suasenha' login;
CREATE DATABASE my_db OWNER my_user;
```


Crie um arquivo `.env` com sua senha:

```
PASSWORD=<sua_senha>
```

## Criando banco de dados com Python

Caso você queira deletar o usuário e o banco antes, digite

```
psql -U postgres -c "DROP USER my_user;"
psql -U postgres -c "DROP DATABASE my_db;"
```

Criando banco e tabelas

```
python create_database.py
python create_tables.py
```

## Inserindo os dados

```
python import_data.py
```


## Jupyter notebook

```
jupyter-notebook
```

## Links

http://pythonclub.com.br/tutorial-postgresql.html

https://github.com/juliano777/pgsql_fs2w/blob/master/postgresql_sql_basico.pdf

https://github.com/rg3915/fast-database
