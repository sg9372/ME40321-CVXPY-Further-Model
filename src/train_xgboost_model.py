import xgboost as xgb
import numpy as np
from sklearn.model_selection import train_test_split

def train_xgboost_model(current_values: np.ndarray, future_values: np.ndarray):
    # Calculate the average future values for each stock
    future_averages = np.mean(future_values, axis=0)
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(current_values.T, future_averages, test_size=0.2, random_state=42)
    
    # Print the indices of the companies selected for testing
    #test_indices = np.where(np.isin(current_values.T, X_test))[0]
    #print(f"Companies selected for testing: {test_indices}")

    # Train the XGBoost model
    model = xgb.XGBRegressor(objective='reg:squarederror')
    model.fit(X_train, y_train)
    
    # Predict the average future values for the test set
    predictions = model.predict(X_test)
    print('Predictions:', predictions,"\nY Test", y_test)
    return model, predictions