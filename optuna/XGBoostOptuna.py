# %% 
from sklearn.metrics import r2_score
import optuna
from xgboost import XGBRegressor
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
# %% 
def objective(trial):
    params = {
        'max_depth': trial.suggest_int('max_depth', 3, 30),                     
        'learning_rate': trial.suggest_float('learning_rate', 0.005, 0.5, log=True), 
        'n_estimators': trial.suggest_int('n_estimators', 100, 2000),           
        'subsample': trial.suggest_float('subsample', 0.5, 1.0),                
        'colsample_bytree': trial.suggest_float('colsample_bytree', 0.5, 1.0),  
        'gamma': trial.suggest_float('gamma', 0, 5),                            
        'reg_alpha': trial.suggest_float('reg_alpha', 0, 10),                   
        'reg_lambda': trial.suggest_float('reg_lambda', 0, 10),                
        'min_child_weight': trial.suggest_int('min_child_weight', 1, 10),       
        'max_delta_step': trial.suggest_int('max_delta_step', 0, 10),           
        'random_state': 42,
        'n_jobs': -1,
        'objective': 'reg:squarederror' 
        }
    model = XGBRegressor(**params).fit(X_train, y_train)
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    return r2

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=200, show_progress_bar=True)
# %%
joblib.dump(study.best_params, 'XGBoostHyperparameters.json')
# %%
