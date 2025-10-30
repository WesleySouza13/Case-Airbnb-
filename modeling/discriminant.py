# %% 
def discriminant(model, y_metric):
    r2 = y_metric.get('R²', 0)
    mse =  y_metric.get('MSE', float())
    mae = y_metric.get('MAE')
    
    # separaçao de modelos com base a criterios propios 
    if r2 > 0.89 and mse < 100 and mae < 50:
        print('== Modelos promissores ==')
        print(f'{model.__class__.__name__} -> {y_metric}')
    else:
        print( '== Modelos que nao cumprem os criterios mas nao descarto == ')
        print(model.__class__.__name__)

# %%
