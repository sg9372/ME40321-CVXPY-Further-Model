import numpy as np
import pandas as pd
from datetime import datetime
import traceback

from _Archive.src.supervised_learning_optimizer import supervised_learning_optimizer
from extract_sheet_names import get_sheet_names
from extract_sheet_data import extract_sheet_data
from extract_values import extract_values
from format_weights import format_weights
from update_df import update_df
from write_df import write_df

def main():    
    # File name
    file = "Monthly FTSE Data - New.xlsx"
    
    # Obtain sheet names and date ranges
    sheet_names, dates = get_sheet_names(file)

    # Create a DataFrame with the top row of company tickers
    all_companies_df = pd.read_excel(file, sheet_name='ftse100_closing_prices')
    all_companies = all_companies_df.columns.tolist()[1:]
    optimized_weights_df = pd.DataFrame(columns=['Date'] + all_companies)
    old_weights_df = pd.DataFrame(columns=['Date'] + all_companies)
    
    # Iterate through each date range
    for i in range(len(dates)-1):
        start_date = datetime.strptime(dates[i], '%d/%m/%Y') + pd.DateOffset(days=1)
        start_date = start_date.strftime('%d/%m/%Y')
        end_date = dates[i+1]
        sheet_name = sheet_names[i]
        print(start_date)

        # Extract sheet data
        companies, weights, emissions = extract_sheet_data(file, sheet_name)

        # Extract values
        values, dates_range = extract_values(file, companies, start_date, end_date)
        
        # Clean data
        if np.isnan(values).any():
            emissions = np.nan_to_num(emissions)
            values = np.nan_to_num(values)
            weights = np.nan_to_num(weights)
        
        # Calculate optimal weights
<<<<<<< HEAD
        optimized_weights = supervised_learning_optimizer(values, emissions, weights)
        
        # Put new weights in "all company list" format
        formatted_optimized_weights_df = format_weights(all_companies, companies, optimized_weights, dates_range)
        formatted_old_weights_df = format_weights(all_companies, companies, weights, dates_range)

        # Append new weights to new_weights_df
        optimized_weights_df = update_df(optimized_weights_df, formatted_optimized_weights_df)
=======
        optimized_weights = average_optimizer(values, emissions, weights)
        
        # Put new weights in "all company list" format and create a DataFrame
        formatted_weights_df = format_weights(all_companies, companies, optimized_weights, dates_range)
        formatted_old_weights_df = format_weights(all_companies, companies, weights, dates_range)

        # Append new dataframes to existing dataframes
        optimized_weights_df = update_df(optimized_weights_df, formatted_weights_df)
>>>>>>> b697049128bba8e3694ebff41e7326c57f1be117
        old_weights_df = update_df(old_weights_df, formatted_old_weights_df)

    # Write df to new sheet
    write_df(optimized_weights_df, old_weights_df)
    
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 1:                                  
        print("Wrong ammount of input arguments, example usage:")
        print("'python src/main.py'")
        sys.exit(1)
    
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        print(traceback.format_exc())
        sys.exit(1)