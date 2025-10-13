import pandas as pd 
import os 
import sqlite3

# setando caminho pro banco de dados 
db_path = os.path.join('data', 'airbnb.db')

# conexao com o db sqlite 
con = sqlite3.connect(db_path)

# caminho para os dados 
data_path = os.path.join('data')
data_dir  = os.listdir(data_path) # setando diretorio para os dados 

# interando sobre os csv's do diretorio| filtro para pegar apenas o final .csv
for data in data_dir:
    if data.endswith('.csv'):
        try:
            print(f'lendo arquivo {data}...')
            table_name = data.replace('.csv', '').lower()
            
            #separando arqivos para leitura do dataframe
            data_file = os.path.join(data_path, data)
            # lendo arquivos csv como dataframes
            df = pd.read_csv(data_file)
            print(f'criando tabela {table_name}')
            # exportando como arquivo sql 
            df.to_sql(table_name, con=con, index=False, if_exists='replace')
        except Exception as e:
            print(f'erro ao ler arquivo {data}. Erro {e}')
            
print(f'banco de dados criado com sucesso em {db_path}')
print(f'fechando conexao.')
con.close()
