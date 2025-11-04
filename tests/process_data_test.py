import os
import pandas as pd
from app.process_data import process_data

def test_process_data():
    base_dir = os.path.dirname(__file__) 
    path = os.path.join(base_dir, '..', 'data', 'dados_predict.csv')
    path = os.path.abspath(path)  
    data = pd.read_csv(path)
    response = process_data(data)
    assert isinstance(response, pd.DataFrame)
    assert 'id' not in response.columns
    assert 'index' not in response.columns
    assert response.isna().sum().sum() == 0

# %%
