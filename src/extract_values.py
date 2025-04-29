import pandas as pd
import numpy as np

def extract_values(file, companies, start_Date, curr_Date, end_Date):
    # Read data
    df = pd.read_excel(file, sheet_name='ftse100_closing_prices') 
    
    # Convert from UK to US date format (DD/MM/YYYY to MM/DD/YYYY)
    US_start_Date = pd.to_datetime(start_Date, dayfirst=True).strftime('%m/%d/%Y')
    US_curr_Date = pd.to_datetime(curr_Date, dayfirst=True).strftime('%m/%d/%Y')
    US_end_Date = pd.to_datetime(end_Date, dayfirst=True).strftime('%m/%d/%Y')

    # Filter based on the Date range
    filtered_df = df[(df['Date'] >= US_start_Date) & (df['Date'] <= US_curr_Date)].copy()
    filtered_df.interpolate(method='linear', inplace=True, limit_direction='both', axis=0)
    dates_df = df[(df['Date'] > US_curr_Date) & (df['Date'] <= US_end_Date)]
    
    if US_end_Date in df['Date'].values:
        future_values = df[df['Date'] == US_end_Date][companies].to_numpy()
    else:
        last_date_before_end = df[df['Date'] < US_end_Date]['Date'].max()
        future_values = df[df['Date'] == last_date_before_end][companies].to_numpy()
    
    # Calculate get data for the actual companies we want
    company_values = filtered_df[companies].to_numpy()

    # Get the current values and mean values
    curr_values = company_values[-1, :]
    #mean_values = np.mean(company_values, axis=0)
    current_values = company_values[-1,:]

    return np.round(curr_values, 2), dates_df['Date'].to_numpy(), future_values

def extract_all_values(file, curr_Date):
    # Read data
    df = pd.read_excel(file, sheet_name='ftse100_closing_prices') 
    
    # Convert from UK to US date format (DD/MM/YYYY to MM/DD/YYYY)
    US_curr_Date = pd.to_datetime(curr_Date, dayfirst=True).strftime('%m/%d/%Y')

    # Filter based on the Date range
    filtered_df = df[(df['Date'] >= '01/01/2020') & (df['Date'] <= US_curr_Date)].copy()
    filtered_df = filtered_df.drop('Date', axis=1)
    filtered_df.interpolate(method='linear', inplace=True, limit_direction='both', limit_area='inside', axis=0)

    
    # Calculate get data for the actual companies we want
    company_values = filtered_df.to_numpy()

    return np.round(company_values, 2)