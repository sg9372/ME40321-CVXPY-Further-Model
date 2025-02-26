import pandas as pd
import numpy as np

def extract_values(file, companies, start_Date, end_Date):
    # Read data
    df = pd.read_excel(file, sheet_name='ftse100_closing_prices') 
    
    # Filter based on the Date range
    filtered_df = df[(df['Date'] >= start_Date) & (df['Date'] <= end_Date)]
    
    # Go through companies in order and add to value_columns if they are in the dataframe (which they hopefully always will be)
    value_columns = []
    for company in companies:
        if company in df.columns:
            value_columns.append(company)
    
    value_columns = [company for company in companies if company in df.columns]
    
    print(companies)
    average = filtered_df[value_columns].mean().to_numpy()
    print("Averages:", average)
    return np.round(average, 2)