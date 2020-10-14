Projeto para treinamento em banco de dados PostgreSQL. 

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

## Criando banco de dados

```
sudo su - postgres
createdb my_db
createuser -P my_usuario
psql my_db
GRANT ALL PRIVILEGES ON DATABASE my_db TO my_usuario;
```


Após a intalação das dependências digite: 

```
jupyter-notebook
```