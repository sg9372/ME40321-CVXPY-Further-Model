import pandas as pd
import numpy as np
import pandas as pd
import numpy as np
import xgboost as xgb
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import MinMaxScaler

def xgboost_daily_analysis(values: np.ndarray, window_size,plot=False, justTrain=False):
    # Convert the numpy array to a pandas DataFrame
    data = pd.DataFrame(values, columns=['Close'])

    # Create features and target variable using a rolling window of 60 days
    X = []
    y = []

    for i in range(len(data) - window_size):
        X.append(data['Close'][i:i + window_size].values)
        y.append(data['Close'][i + window_size])

    X = np.array(X)
    y = np.array(y)

    # Scale the features using MinMaxScaler
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
  
    if justTrain==True:
        # Split the scaled data into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.01,random_state=42)
    else:
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)


    # Create and fit the XGBoost model
    model = xgb.XGBRegressor()
    model.fit(X_train, y_train)

    # Predict stock prices
    y_pred = model.predict(X_test)

    # Calculate RMSE, MAE, and R-squared
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)
    r_squared = r2_score(y_test, y_pred)

    #print('Root Mean Squared Error (RMSE):', rmse)
    #print('Mean Absolute Error (MAE):', mae)
    #print('R-squared:', r_squared)
        
    return model, y_pred

def justTest(model, window_data, days):
    future_predictions = []
    window_size=len(window_data)
    window = window_data.copy()
    print("Window_Data:", window_data)
    for _ in range(days):    
        input = window
        print("Input:", input)
        next_pred = model.predict(window)
        future_predictions.append(next_pred[0])
        print("Window:", window)
        print("Window[1:]:", window[1:])
        print("next_pred[0]:", next_pred[0])
        window = np.append(window[1:], [[next_pred[0]]], axis = 0)
        

    return np.array([future_predictions]).T

def plot_data(y_test, y_pred, y_train=None):
    print("y_test shape:", y_test.shape)
    print("y_pred shape:", y_pred.shape)
    if y_train is not None:
        print("y_train shape:", y_train.shape)
    TrueData = np.concatenate((y_train, y_test), axis=0)
    predictedData = np.concatenate((y_train, y_pred), axis=0)
    #TrueData = y_test
    #predictedData = y_pred
    
    dataLen = len(predictedData)
    dates = np.linspace(1, dataLen, dataLen)
    
    plt.figure(figsize=(12, 6))
    plt.plot(dates, TrueData, label='Actual')
    plt.plot(dates, predictedData, label='Predicted')
    plt.ylim(0, 1000)
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.title('XGBoost Predictions')
    plt.legend()
    plt.show()