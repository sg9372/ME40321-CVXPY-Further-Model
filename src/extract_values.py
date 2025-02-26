import pandas as pd
import numpy as np

def extract_values(file, companies, start_Date, end_Date):
    # Read data
    df = pd.read_excel(file, sheet_name='ftse100_closing_prices') 
    
    # Filter based on the Date range
    filtered_df = df[(df['Date'] >= start_Date) & (df['Date'] <= end_Date)]
  
    # Calculate averages and round to 2dp
    average = filtered_df[companies].mean().to_numpy()
    return np.round(average, 2)