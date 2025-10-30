
from modeling.discriminant import discriminant
from sklearn.linear_model import LinearRegression

def test_discriminant():
    model_ = LinearRegression()
    metrics_ = {'R²': 0.9092242082906117, 'MSE': 772.4433223897794, 'MAE': 14.813408689834889}
    response = discriminant(model=model_, y_metric=metrics_)
    
