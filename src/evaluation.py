import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error

def compute_rmse(y_true, y_pred):
    """
    Compute the Root Mean Squared Error (RMSE) between actual and predicted ratings.
    """
    return np.sqrt(mean_squared_error(y_true, y_pred))

def compute_mae(y_true, y_pred):
    """
    Compute the Mean Absolute Error (MAE) between actual and predicted ratings.
    """
    return mean_absolute_error(y_true, y_pred)
