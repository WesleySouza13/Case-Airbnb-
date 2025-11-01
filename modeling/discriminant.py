# %% 
def discriminant(model, y_metric):
    r2 = y_metric.get('R²', 0)
    mse =  y_metric.get('MSE', float('inf'))
    mae = y_metric.get('MAE', float('inf'))
    
    # separaçao de modelos com base a criterios propios 
    if r2 > 0.6 and mse < 10000 and mae < 50:
        out = {
            'modelo': model.__class__.__name__,
            'R²': r2,
            'MSE': mse,
            'MAE': mae
        }
        return out
    else: 
        return None

# %%
