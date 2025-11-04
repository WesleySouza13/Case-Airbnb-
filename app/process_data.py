# %% 
import pandas as pd 

def process_data(data:pd.DataFrame):
    if 'id' in data.columns and 'index' in data.columns:
        drop_cols = ['id', 'index']
        df = data.drop(drop_cols, axis=1)
    for nan in df.columns:
        if df[nan].isna().sum() > 1:
            print(f'ha valores nulos: {nan}')
            
            # definindo coeficiente de variaçao dos dados (cv)
            cv = df[nan].std()/df[nan].mean()
            if cv < 0.15:
                df = df[nan].fillna(df[nan].mean(), inplace=True)
            elif cv > 0.15:
                df = df[nan].fillna(df[nan].median(), inplace=True)
            print(f'dados tratados com sucesso! {df[nan].std()}')
        else:
            print(f'nao há valores nulos em: {nan}')
        
    return df
# %%
