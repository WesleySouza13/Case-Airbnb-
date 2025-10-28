from modeling.metrics import metrics
import numpy as np
# testando metricas 
def test_metrics():
    y = [800, 990, 700]
    y_pred = [750, 900, 750]
    response = metrics(y, y_pred)
    assert isinstance(response, dict)
    