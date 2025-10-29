# %%
import pandas as pd 
import os 
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from xgboost import XGBRegressor
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns 

df_path = os.path.join('..', 'data', 'dataframe_tratado.csv')
df = pd.read_csv(df_path)
display(df)
# dropando coluna Unnamed: 0
df = df.drop('Unnamed: 0', axis=1)
display(df)
# %%
df.isnull().sum()
# %%
df.describe().T.sort_values(by='std')

# %%
