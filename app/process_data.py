# %% 
import pandas as pd 
import numpy as np 
import os
data_path = os.path.join('..', 'data', 'dados_predict.csv')
df = pd.read_csv(data_path)
def process_data(data:pd.DataFrame):
    if 'id' and 'index' in data:
        drop_cols = ['id', 'index']
        df = data.drop(drop_cols, axis=1)
    for nan in df.columns:
        if df[nan].isna().sum() > 1:
            print(f'ha valores nulos: {nan}')
            
            # definindo coeficiente de variaçao dos dados (cv)
            cv = df[nan].std()/df[nan].mean()
            if cv < 0.15:
                df = df[nan].mean()
            elif cv > 0.15:
                df = df[nan].median()
            print(f'dados tratados com sucesso! {df[nan].std()}')
        else:
            print(f'nao há valores nulos em: {nan}')
        
        return df
new_df = process_data(df)
display(new_df)
# %%
