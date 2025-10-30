# %%
import pandas as pd 
import os 
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from metrics import metrics
from discriminant import discriminant
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns 
import sqlite3
from statsmodels.stats.outliers_influence import variance_inflation_factor
import shap
# %%
db_path = os.path.join('..', 'data', 'feature_store.db')
con = sqlite3.connect(db_path)
query = "SELECT * FROM feature_store"
df = pd.read_sql(query, con)
display(df)
# %%
drop = ['index', 'id']
df = df.drop(drop, axis=1)
display(df)
# %%
X = df.drop('price', axis=1)
y = df['price']

# %%
X.shape, y.shape
# %%

X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=42, test_size=.2)

print(f'media de y_train: {y_train.mean()} | media de y_test {y_test.mean()}')
# %%

# separando modelos para treinamento 
models = {
    'Regressao linear': LinearRegression(),
    'Arvore de decisao':DecisionTreeRegressor(random_state=42),
    'Random forest':RandomForestRegressor(random_state=42),
    'AdaBooost': AdaBoostRegressor(random_state=42), 
    'XGboost': XGBRegressor()
}

# treinando modelos 
best_models = []
for i, model in models.items():
    model.fit(X_train, y_train)
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    
    metrics_train = metrics(y_train, y_pred_train)
    metrics_test = metrics(y_test, y_pred_test)
    print(f'[TREINO] Modelo: {i} -> {metrics_train}')
    print(f'[TESTE]  Modelo: {i} -> {metrics_test}')

    # aplicaçao da funçao descriminante das metricas 
    disc = discriminant(model=model, y_metric=metrics_test)
    if disc:
        best_models.append(disc)
best_models_df = pd.DataFrame(best_models)
display(best_models_df)
# %%

# ANALISE DE VIF
data_vif = pd.DataFrame()
data_vif['features'] = X.columns
data_vif['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
display(data_vif.sort_values(by='VIF'))
# %%
plt.figure(figsize=(10,8))
plt.title('Analise de multicolinearidade das features')
sns.barplot(data=data_vif, x='features', y='VIF', palette='viridis')
plt.xlabel('features')
plt.ylabel('valores de VIF - Coeficiente de multicolinearidade')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
# %%
model = RandomForestRegressor(random_state=42).fit(X_train, y_train)
explainer = shap.TreeExplainer(model, X_train)
# %%
shap_ = explainer.shap_values(X_test)
shap.summary_plot(shap_, X_test)
# %%
