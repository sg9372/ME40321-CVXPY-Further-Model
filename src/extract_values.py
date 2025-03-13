import pandas as pd
import numpy as np

def extract_values(file, companies, start_Date, end_Date):
    # Read data
    df = pd.read_excel(file, sheet_name='ftse100_closing_prices') 
    
    # Convert from UK to US date format (DD/MM/YYYY to MM/DD/YYYY)
    US_start_Date = pd.to_datetime(start_Date, dayfirst=True).strftime('%m/%d/%Y')
    US_end_Date = pd.to_datetime(end_Date, dayfirst=True).strftime('%m/%d/%Y')

    # Filter based on the Date range
    filtered_df = df[(df['Date'] >= US_start_Date) & (df['Date'] <= US_end_Date)]
    
    # Calculate get data for the actual companies we want
    company_values = filtered_df[companies].to_numpy()
    return np.round(company_values, 2), filtered_df['Date']