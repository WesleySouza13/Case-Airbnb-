
import sqlite3
import pandas as pd 
import os 

def read_query(query_path):
    with open(query_path) as query:
        return query.read()

query_path = os.path.join('abt.sql')

#utilizando a funcao read_query 
query = read_query(query_path=query_path)

# criando funçao para criaçao do banco de dados 
def create_abt_db(connect_or, connect_new, query, table_name):
    df = pd.read_sql_query(con=connect_or, sql=query)
    table = df.to_sql(table_name, con=connect_new, if_exists='replace', index=False)
    return table

# aplicando funcao create_abt_db
db_new = os.path.join('..', '..', 'data', 'abt_airbnb.db')
db_or =  os.path.join('..', '..', 'data', 'HostLifeCycle.db')

os.path.exists(db_or)
con_or = sqlite3.connect(db_or)
con_new = sqlite3.connect(db_new) # conexao original 
create_abt_db(connect_or=con_or, connect_new=con_new, query=query, table_name='abt_airbnb.db')

