# %%
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

def metrics(y, y_pred) -> dict:
    r2 = r2_score(y_true=y, y_pred=y_pred)
    mse = mean_squared_error(y_true=y, y_pred=y_pred)
    mae = mean_absolute_error(y_true=y, y_pred=y_pred)
    
    metrics_ = {
        'R²':r2,
        'MSE':mse, 
        'MAE':mae
    }
    return metrics_
# %%
