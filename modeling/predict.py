# %% 
from sklearn.ensemble import RandomForestRegressor
from metrics import metrics
import os
import pandas as pd 
from sklearn.model_selection import train_test_split
import sqlite3
import joblib
# %% 
db_path = os.path.join('..', 'data', 'feature_store.db')
con = sqlite3.connect(db_path)
query = "select * from feature_store"
df = pd.read_sql_query(query, con=con)
display(df)
drop = ['index', 'id']
df = df.drop(drop, axis=1)
display(df)

# %%
X = df.drop('price', axis=1)
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=42)
params_path = os.path.join('..', 'optuna', 'RandomForestHyperparameters.json')
params = joblib.load(params_path)
model = RandomForestRegressor(**params).fit(X_train, y_train)
# %%
pred = model.predict(X_test)
metrics(y_test, pred)
# %%
model_path = os.path.join('..', 'RandomForest.pkl')
joblib.dump(model, model_path)
# %%
