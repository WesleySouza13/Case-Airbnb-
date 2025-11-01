# %% 
from sklearn.metrics import r2_score
import optuna
from sklearn.ensemble import RandomForestRegressor
import os
import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
import json
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
def objective(trial):
    params = {
        'n_estimators': trial.suggest_int('n_estimators', 100, 300),
    'max_depth' :trial.suggest_int('max_depth', 50, 300),
    'min_samples_split': trial.suggest_int('min_samples_split', 2, 10),
    'min_samples_leaf': trial.suggest_int('min_samples_leaf', 1, 10),
    'random_state':42
    }
    model = RandomForestRegressor(**params)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    r2 = r2_score(y_test, y_pred)
    
    return r2
study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=200, show_progress_bar=True)
# %%
hyperparameters = study.best_params
joblib.dump(hyperparameters, 'RandomForestHyperparameters.json')


# %%
