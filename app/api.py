from fastapi import FastAPI, UploadFile
import joblib
from pydantic import BaseModel
from app.process_data import process_data

app = FastAPI(title='AirBnb - Price predict')

@app.get('/')
def home():
    return {'saida':'Api no ar'}