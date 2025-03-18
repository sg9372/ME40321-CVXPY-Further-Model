import pandas as pd
import numpy as np
import xgboost as xgb
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import MinMaxScaler

def xgboost_daily_analysis(values: np.ndarray, window_size, plot=False, justTrain=False):
    # Create features and target variable using a rolling window of 60 days
    X = []
    y = []

    # Feature engineering
    for i in range(len(values) - window_size):
        X.append(values[i:i + window_size])
        y.append(values[i + window_size])
    
    # Turn back into arrays
    X = np.array(X)
    y = np.array(y)

    # Reshape X for scaling, scale and then reshape back.
    X_scaled = X.reshape(X.shape[0], X.shape[1])

    # Split the scaled data into train and test sets
    test_size = 0.01 if justTrain else 0.2
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=test_size, random_state=42)
    
    # Create and fit the XGBoost model
    model = xgb.XGBRegressor()
    model.fit(X_train, y_train)
   
    # Predict stock prices
    y_pred = model.predict(X_test)

    return model, y_pred

def justTest(model, window_data, days):
    future_predictions = []
    window_size = len(window_data)
    window = window_data.T.copy()

    # Initialize the scaler and fit it on the window data
    window_scaled = window.reshape(1, -1)
    input = window_scaled

    for _ in range(days):
        next_pred = model.predict(input)
        future_predictions.append(next_pred[0])
        window = np.append(window[0][:], next_pred, axis=0).reshape(1, -1)
        window_scaled = window.reshape(1, -1)
        input = window_scaled[0][-window_size:].reshape(1, -1)

    return np.array([future_predictions]).T

def plot_data(y_test, y_pred, y_train=None):
    TrueData = np.concatenate((y_train, y_test), axis=0)
    predictedData = np.concatenate((y_train, y_pred), axis=0)
    
    dataLen = len(predictedData)
    dates = np.linspace(1, dataLen, dataLen)
    
    # Calculate RMSE, MAE, and R-squared
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)
    r_squared = r2_score(y_test, y_pred)

    print('Root Mean Squared Error (RMSE):', rmse)
    print('Mean Absolute Error (MAE):', mae)
    print('R-squared:', r_squared)

    plt.figure(figsize=(12, 6))
    plt.plot(dates, TrueData, label='Actual')
    plt.plot(dates, predictedData, label='Predicted')
    plt.ylim(0, 1000)
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.title('XGBoost Predictions')
    plt.legend()
    plt.show()

