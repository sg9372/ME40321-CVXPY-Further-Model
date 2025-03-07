import pandas as pd
import numpy as np

def extract_values(file, companies, end_Date, rows):
    # Read data
    df = pd.read_excel(file, sheet_name='ftse100_closing_prices') 
    
    # Convert from UK to US date format (DD/MM/YYYY to MM/DD/YYYY)
    US_end_Date = pd.to_datetime(end_Date, dayfirst=True).strftime('%m/%d/%Y')

    # Filter based on the Date range
<<<<<<< HEAD
    filtered_df = df[df['Date'] <= US_end_Date]

    # Sort by date and select the last 'rows' number of rows
    filtered_df = filtered_df.tail(rows)
    
    # Get a separate df of future 'rows' number of rows
    future_df = df[df['Date'] > US_end_Date].head(rows)
    
    # Replace NaN with the average value of that stock across the whole data set
    for company in companies:
        mean_value = df[company].mean()
        filtered_df.loc[:, company] = filtered_df[company].fillna(mean_value)
        future_df.loc[:, company] = future_df[company].fillna(mean_value)

    # Extract values as a 2D array
    past_values = filtered_df[companies].to_numpy()
    future_values = future_df[companies].to_numpy()

    # Return
    return np.round(past_values, 2), np.round(future_values, 2),filtered_df['Date'].to_numpy()
=======
    filtered_df = df[(df['Date'] >= US_start_Date) & (df['Date'] <= US_end_Date)]
  
    # Calculate averages and round to 2dp
    average = filtered_df[companies].mean().to_numpy()
    return np.round(average, 2), filtered_df['Date']
>>>>>>> b697049128bba8e3694ebff41e7326c57f1be117
