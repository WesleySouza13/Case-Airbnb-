# %%
import requests
import os
import pandas as pd 

url = 'http://127.0.0.1:8000/batch_predict'
data_path = os.path.join('..', 'data', 'dados_predict.csv')
# %%

def inference(model_url, data):
    with open(data) as f:
        files = {'file': ('dados_predict.csv', f, 'text/csv')}
        try:
            response = requests.post(url=model_url, files=files)
            if response.status_code == 200:
                print('requisiçao bem sucedida')
                return  response.json()
            else:
                print(f'nao achamoms dados. {response.status_code}: {response.text}')
        except Exception as e:
            print(f'erro de inferencia {e}')
predict = inference(model_url=url, data=data_path)
predict
# %%
data_out = pd.DataFrame(predict)
only_cols = ['id', 'price_pred']
data_out[only_cols]

# %%
out_path = os.path.join('..', 'data', 'df_predict_batch.csv')
data_out.to_csv(out_path)
# %%
