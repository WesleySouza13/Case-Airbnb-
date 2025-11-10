# %%
import sys
import os 
# forçando python a reconhecer o pacote 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# %%
from fastapi import FastAPI, UploadFile, File
import joblib
from pydantic import BaseModel
from app.process_data import process_data
import pandas as pd
import io
# %% 
app = FastAPI(title='AirBnb - Price predict')
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, 'XGBoost.pkl')
model = joblib.load(model_path)

@app.get('/')
def home():
    return {'saida':'Api no ar'}
@app.get('/health')
def health():
    return {'status':'ok'}
async def upload_file(file:UploadFile):
    if file is not None:
        try:
            print(f'arquivo {file.filename} carregado com sucesso!')
            return await file.read()

        except Exception as e:
            print(f'Houve um erro. Saida {e}')
            return None
        
@app.post('/batch_predict')
async def batch_predict(file: UploadFile=File(...)):
    print(f'lendo dados')
    data = await upload_file(file=file)

    print(f'transformando dados...')
    df =  pd.read_csv(io.BytesIO(data))
    preprocess_data = process_data(df)
    
    print(f'fazendo previsoes')
    # passando dados preprocessados para o modelo 
    predict =  model.predict(preprocess_data)
    out_df = df.copy()
    out_df['price_pred'] = predict
    
    return out_df.to_dict(orient='records')

# %%
