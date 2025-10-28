# %%
import pandas as pd
import sqlite3
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.preprocessing import MinMaxScaler
db_path = os.path.join('..', 'data', 'HostLifeCycle.db')
con = sqlite3.connect(db_path)
query = "SELECT * FROM HostLifeCycle"

df = pd.read_sql_query(query, con=con)
df
# irei agrupar os host entre quantidades de avaliações por mes e rating total das avaliações
plt.figure(figsize=(10,5))
plt.title('Distribuiçao de Score review por Numero de Reviews')
sns.scatterplot(data=df, x='review_scores_rating', y='reviews_per_month')
plt.grid()
# %%
#separando variaveis para cluster
cluster_col = ['review_scores_rating','reviews_per_month'] 
x = df[cluster_col]
print(x.isnull().sum())
# %%
print(x.describe())
# %%
#x = x.dropna() # dropando dados nulos
x = x.fillna(x.median()) #substituinda nulos pela mediana
# normalizando dados 
min_max = MinMaxScaler()
x = min_max.fit_transform(x)
# teste do cotovelo 
ebow = []
for i in range(2,10):
    kmeans_ = KMeans(n_clusters=i, max_iter=1000, random_state=42).fit(x)
    ebow.append(kmeans_.inertia_)
    sil_score = silhouette_score(x, kmeans_.labels_)
    davies_score = davies_bouldin_score(x, kmeans_.labels_)
    print(f'sillueta para cluster {i}: {sil_score} e davies bouldin: {davies_score}')
    
# plotando cotovelo dos clusters 
plt.figure(figsize=(10,5))
plt.title('Teste de cotovelo do cluster - Dados normalizados com Min Max')
plt.plot(ebow, marker='o')
plt.ylabel('erro')
plt.xlabel('numero de clusters')
plt.grid()
plt.show()
# %%
# aplicando segmentaçao com n_cluster = 2
kmeans = KMeans(n_clusters=2, max_iter=100, random_state=42).fit(x)
df['cluster'] = kmeans.labels_

#plotando clusters
plt.figure(figsize=(10,5))
plt.title('Cluster')
sns.scatterplot(data=df, x='review_scores_rating',y='reviews_per_month', hue='cluster')
plt.legend()
plt.grid()
plt.show()

# %%
