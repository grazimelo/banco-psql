#!/usr/bin/env python
# coding: utf-8

# In[1]:


import psycopg2
import pandas as pd
from decouple import config
# # https://gist.github.com/rg3915/5fb3a2e7338115bc92e82b7a9a2b372b


# In[2]:


df_produtos = pd.read_excel('produtos-com-categoria.xlsx')
df_categorias = pd.read_excel('categorias.xlsx')


# In[3]:


df_produtos


# In[4]:


try:
    connection = psycopg2.connect(user = "my_usuario",
                                  password = config("PASSWORD"),
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "my_db")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)


# In[5]:


cur = connection.cursor()


# In[6]:


df_categorias


# In[7]:


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


# In[8]:


items = df_categorias.T.apply(dict).tolist()
items


# In[ ]:





# In[9]:


dicionario = {}


# In[10]:


dicionario['nome'] = 'Regis'


# In[11]:


dicionario['sobrenome'] = 'Santos'


# In[12]:


dicionario


# In[ ]:





# In[ ]:





# In[13]:


d = {}
for item in items:
    print(item)
    d[str(item['id'])] = item['categoria']


# In[14]:


d


# In[15]:


d['700']


# In[16]:


d['915']


# In[17]:


dict_categoria = get_data(df_categorias.T.apply(dict).tolist())
dict_categoria


# In[18]:


for produto in df_produtos.head().iterrows():
    print(produto[1][2])


# In[19]:


for produto in df_produtos.head().itertuples():
    print(produto.produto, produto.preco, produto.categoria)


# In[20]:


dict_categoria.get(str('314'))


# In[24]:


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


# In[ ]:


cur.execute("DELETE FROM produtos_categoria;")
connection.commit()


# In[23]:


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


# In[25]:


connection.commit()


# In[26]:


cur.execute("SELECT * FROM produtos_categoria;")
cur.fetchall()


# In[27]:


cur.execute("SELECT * FROM produtos_categoria as p INNER JOIN categoria ON (p.categoria_tipo = categoria.id) ORDER BY p.id;")
result = cur.fetchall()
result


# In[28]:


pd.DataFrame(result, columns = ['id', 'nome_produto', 'valor_produto', 'categoria_tipo', 'id', 'nome'])


# In[ ]:




