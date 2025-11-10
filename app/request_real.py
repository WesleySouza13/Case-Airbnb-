# %% 
import requests
import pandas as pd
import os

url = 'http://127.0.0.1:8000/real_time_predict'
data_dict = {
    "is_location_exact": 1,
    "property_type": 3,
    "room_type": 2,
    "bed_type": 1,
    "has_availability": 1,
    "binTempo": 2,
    "FAIXA_RATING": 4,
    "tempoHost": 36,
    "accommodates": 4,
    "bathrooms": 2,
    "bedrooms": 2,
    "beds": 3,
    "accommodates_per_bedroom": 2,
    "beds_per_bedroom": 1,
    "bathrooms_per_bedroom": 1,
    "accommodates_per_bed": 1,
    "beds_per_accommodate": 1,
    "security_deposit": 200.0,
    "cleaning_fee": 80.0,
    "guests_included": 2,
    "extra_people": 50,
    "minimum_nights": 2,
    "maximum_nights": 30,
    "number_of_reviews": 45,
    "review_scores_rating": 4.6,
    "reviews_per_month": 1.2,
    "availability_30": 12,
    "availability_60": 24,
    "availability_90": 40,
    "availability_365": 180,
    "mean_availability": 64.0,
    "review_per_year": 14.4
}
def inference(url, data):
    try:
        response = requests.post(url=url, json=data)
        if response.status_code == 200:
            print('requisiçao bem sucedida')
        return response.json()
    except Exception as e:
        return {'Erro':{e}}
    
pred = inference(url=url, data=data_dict)
# %%
df = pd.DataFrame([data_dict])
df['price_pred'] = pred
# %%
data_path = os.path.join('..', 'data', 'df_predict_real_time.csv')
df.to_csv(data_path)

# %%
