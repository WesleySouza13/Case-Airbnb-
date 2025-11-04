from fastapi import FastAPI, UploadFile
import joblib
from pydantic import BaseModel
from app.process_data import process_data
import pandas as pd
import os 

app = FastAPI(title='AirBnb - Price predict')
model_path = os.path.join('..', 'app', 'XGBoost.pkl')
model = joblib.load(model_path)
@app.get('/')
def home():
    return {'saida':'Api no ar'}

# criando gateway api prediçao em batch
