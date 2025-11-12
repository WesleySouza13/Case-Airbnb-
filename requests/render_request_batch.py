#%%
import os
import requests
data_path = os.path.join('..', 'data', 'dados_predict.csv')
url = 'https://case-airbnb-1.onrender.com/batch_predict'

def inference(url, data_path):
    with open(data_path) as f:
        files = {'file': ('dados_predict.csv', f, 'text/csv')}
        try:
            response = requests.post(url=url, files=files)
            if response.status_code==200:
                print(f'requisiçao bem sucedida: {response.status_code}')
                return response.json()
        except Exception as e:
            print(f'Erro. Saida: {e}')
y_pred = inference(url, data_path)
y_pred
# %%
