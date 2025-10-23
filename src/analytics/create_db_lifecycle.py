import sqlite3
import os
import pandas as pd
#caminho para a query
path = os.path.join('src', 'analytics', 'HostLifeCycle.sql')
#criando funçao para leitura da query 
def read_query(query_path):
    with open(query_path) as query:
        return query.read()

# aplicando funçao 
query = read_query(path)

# criando funçao para modelar o banco de dados LifeCycle.db a partir da query
db_or = os.path.join('data', 'airbnb.db') # banco de origem
db_dest = os.path.join('data', 'HostLifeCycle.db') # banco de destino

con_or = sqlite3.connect(db_or) # conexao de origem
con_dest = sqlite3.connect(db_dest) # conexao de destino 

def create_db_life(query, con_origem, con_destino):
    #con = sqlite3.connect(db_path)
    df = pd.read_sql_query(sql=query, con=con_origem)
    #exportando para tabela 
    df.to_sql(name='HostLifeCycle', con=con_destino, index=False, if_exists='replace')

# aplicando funçao 
create_db_life(query=query, con_origem=con_or, con_destino=con_dest)


    