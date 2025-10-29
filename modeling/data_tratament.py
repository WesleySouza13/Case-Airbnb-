# %% 
import pandas as pd 
import sqlite3 
import os 
import matplotlib.pyplot as plt 
import seaborn as sns 

db_path = os.path.join('..', 'data', 'abt_airbnb.db')
con = sqlite3.connect(db_path)
query = "SELECT * FROM abt_airbnb"

df = pd.read_sql_query(query, con=con)
display(df.head())

# %%
plt.title(f'mapa de dados nulos')
sns.heatmap(df.isna())
# %%
for i in df.columns:
    if df[i].isna().sum() > 500:
        print(f'colunas que possuem o somatorio de valores nulos > 500: {i} = {df[i].isna().sum()}')
    
# %%
some_cols = ['tempoHost', 'weekly_price', 'monthly_price', 'security_deposit', 'cleaning_fee', 'review_per_year', 'review_scores_rating',
            'reviews_per_month']
df[some_cols].describe().T.sort_values(by='std')

# %%
# inputando valores em algumas colunas pela sua media pois o desvio padrao nao é significativo 
mean_cols = ['reviews_per_month', 'review_scores_rating']
for mean in mean_cols:
    df[mean] = df[mean].fillna(df[mean].mean())
    print(f'std: {df[mean].std()} e valores nulos em {mean}: {df[mean].isna().sum()}')

# %%
# substituindo pela mediana
median_cols = ['review_per_year', 'cleaning_fee', 'security_deposit']

for median in median_cols:
    df[median] = df[median].fillna(df[median].median())
    print(f'std: {df[median].std()} e valores nulos em {median}: {df[median].isna().sum()}')


# %%
# excluindo colunas do nosso estudo 
exclude_cols = ['monthly_price', 'weekly_price']
df = df.drop(exclude_cols, axis=1)
# %%
df.shape
# %%
df = df.dropna(axis=1) # dropando as demais linhas nulas pois nao possuem significancia no dataset 

# %%
df.shape

# exportando dataset tratado 
new_path = os.path.join('..','data', 'feature_store.db')
new_con = sqlite3.connect(new_path)

df.to_sql('feature_store', new_con, index=True, if_exists='replace') 


# %%
