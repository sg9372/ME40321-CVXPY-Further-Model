import numpy as np
import time

from sklearn.model_selection import train_test_split
from src.extract_values import extract_values, extract_all_values
from src.extract_sheet_data import extract_sheet_data
from src.extract_sheet_names import get_sheet_names
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pandas as pd
from sklearn.linear_model import LinearRegression


def test_real_data():
    abs_max_error = 0
    # Test if the model can be trained with real data
    window_sizes = [0,2,5,10,20,40,80,160,320,640] # [2,5,10,20,40,80,160,320,640]
    window_sizes.reverse()
    all_data = extract_all_values('Monthly FTSE Data - New.xlsx', '01/12/2023')
    pred_interval = 20    
    step_size = 25

    incomplete_companies = []
    
    start_company = 0
    start_date = 640
    prediction_sector = 60
    
    for i in range(start_company, 61): # len(all_data[0,:])
    #for i in range(30):
        print("Company", i)
        data = all_data[:, i]
        if len(data) == 946 and  not np.isnan(data).any():
            # Predict future stock value based on the average of the last 60 days
            predErrors = []
            results = {'method': [], 'Error': []}
            method = 'average'

            for j in range(start_date, len(data) - pred_interval - 60, step_size):
                # Calculate the average of the last 60 days
                avg_60_days = np.mean(data[j:j + 60])
                # Predict the value 13 days ahead
                predicted_value = avg_60_days
                # Actual value 13 days ahead
                actual_value = data[j + 60 + 13]
                # Calculate the error
                error = (predicted_value - actual_value)/actual_value
                predErrors.append(error)

            results['method'] += [method] * len(predErrors)
            results['Error'] += predErrors
            predErrors = []

            # Perform linear regression on the last 60 days
            method = 'linear regression'

            for j in range(start_date, len(data) - pred_interval, step_size):
                # Prepare the data for linear regression
                X = np.arange(60).reshape(-1, 1)  # Days 0 to 59
                y = data[j - prediction_sector:j]  # Stock values for the last 60 days

                # Fit the linear regression model
                model = LinearRegression()
                model.fit(X, y)

                # Predict the value 13 days ahead
                predicted_value = model.predict(np.array([[prediction_sector + pred_interval]]))[0]
                # Actual value 13 days ahead
                actual_value = data[j + pred_interval]
                # Calculate the error
                error = (predicted_value - actual_value)/actual_value
                predErrors.append(error)

            results['method'] += [method] * len(predErrors)
            results['Error'] += predErrors

            method = 'last value'

            predErrors = []

            for j in range(start_date, len(data) - pred_interval, step_size):
                predErrors.append((data[j]-data[j + pred_interval])/data[j + pred_interval])

            results['method'] += [method] * len(predErrors)
            results['Error'] += predErrors      
            
            
            
            if i == start_company:
                final_df = pd.DataFrame(results)
            else:
                results = pd.DataFrame(results['Error'])
                final_df = pd.concat([final_df, results], axis=1)
        else:
            incomplete_companies.append(i)
            print("Appended company", i)
        
        if i % 5 == 0:
            print(incomplete_companies)
            final_df.to_excel('prediction_test_results.xlsx', index=False)
            # Add incomplete companies to a new sheet in the Excel file
            with pd.ExcelWriter('prediction_test_results.xlsx', mode='a', engine='openpyxl') as writer:
                pd.DataFrame({'Incomplete Companies': incomplete_companies}).to_excel(writer, sheet_name='Incomplete Companies', index=False)
            

test_real_data()