# %% 
import joblib
import os
import pandas as pd
import numpy as np
model_path = os.path.join('..', 'app', 'XGBoost.pkl')
model = joblib.load(model_path)
# %%
data_path = os.path.join('..', 'data', 'dados_predict.csv')
df = pd.read_csv(data_path)
display(df)
# %%
df.isnull().sum()
# %%

df.describe().T.sort_values(by='std', ascending=False)
# %%
df.shape
# %%
drop_cols = ['index', 'id']
df_pred = df.drop(drop_cols, axis=1)
y_pred = model.predict(df_pred)
y_pred

# %%
