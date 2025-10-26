from modeling.metrics import metrics
import numpy as np
# testando metricas 
def test_metrics():
    y = 800
    y = np.array(y, ndmin=2)
    y_pred = 850
    y_pred = np.array(y_pred, ndmin=2)
    response = metrics(y, y_pred)
    assert isinstance(response, dict)
    