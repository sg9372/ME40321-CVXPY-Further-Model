import numpy as np
import pandas as pd
from datetime import datetime
import traceback
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

from src.extract_sheet_names import get_sheet_names
from src.get_sector_indicies import get_sector_indicies
from src.extract_sheet_data import extract_sheet_data
from src.format_sector_weights import determine_sector_weights
from src.extract_values import extract_values
from src.format_weights import format_weights
from src.write_df import write_df
from src.averages_optimizer import average_optimizer

def main():    
    # File name
    file = "Monthly FTSE Data - New.xlsx"

    # Sectors list
    all_sectors = [
    "Finance and Insurance",
    "Manufacturing",
    "Mining, Quarrying, and Oil and Gas Extraction",
    "Wholesale Trade",
    "Information",
    "Utilities",
    "Real Estate and Rental and Leasing",
    "Transportation and Warehousing",
    "Professional, Scientific, and Technical Services",
    "Construction",
    "Accommodation and Food Services",
    "Arts, Entertainment, and Recreation",
    "Administrative and Support and Waste Management and Remediation Services",
    "Retail Trade",
    "Health Care and Social Assistance"
]
    
    # Obtain sheet names and date ranges
    sheet_names, dates = get_sheet_names(file)

    # Create a DataFrame with the top row of company tickers
    all_companies_df = pd.read_excel(file, sheet_name='ftse100_closing_prices')
    all_companies = all_companies_df.columns.tolist()[1:]

    # Define needed dataframes for weights and sector weights    
    optimized_weights_df = pd.DataFrame(columns=['Date'] + all_companies)
    old_weights_df = pd.DataFrame(columns=['Date'] + all_companies)

    old_sectors_df = pd.DataFrame(columns=['Date'] + all_sectors)
    optimized_sectors_df = pd.DataFrame(columns=['Date'] + all_sectors)

    start=40

    # Iterate through each date range
    for i in range(start,len(dates)-1):
        start_date = dates[i-1]             #datetime.strptime(dates[i-1], '%d/%m/%Y') + pd.DateOffset(days=1)   #start_date = start_date.strftime('%d/%m/%Y')
        curr_date = dates[i]
        end_date = dates[i+1]
        sheet_name = sheet_names[i]
        print(start_date)

        # Extract sheet data
        companies, weights, emissions, company_sectors = extract_sheet_data(file, sheet_name)

        # Extract values
        current_values, dates_range, end_date_values = extract_values(file, companies, start_date, curr_date, end_date)
        print("Current values:", current_values)
        print("End date values", end_date_values)


        # Clean data
        if np.isnan(current_values).any():
            emissions = np.nan_to_num(emissions)
            weights = np.nan_to_num(weights)
        
        # Get sector indicies
        sector_indicies = get_sector_indicies(all_sectors, company_sectors)

        # Calculate optimal weights
        if i==start:    
            optimized_weights = average_optimizer(current_values, emissions, weights, sector_indicies)
        else:
            optimized_weights = average_optimizer(current_values, emissions, weights, sector_indicies, end_of_last_sector_portfolio_value)
        
        end_of_last_sector_portfolio_value = np.sum(end_date_values * optimized_weights)
        print("End of last sector portfolio value", end_of_last_sector_portfolio_value)
        print("End of last sector FTSE value", np.sum(end_date_values * weights))
        
        # Put new weights in "all company list" format
        formatted_optimized_weights_df = format_weights(all_companies, companies, optimized_weights, dates_range)
        formatted_old_weights_df = format_weights(all_companies, companies, weights, dates_range)
        # Put new sectors into correct format
        formatted_optimized_sectors_df = determine_sector_weights(all_sectors, company_sectors, optimized_weights, dates_range)
        formatted_old_sectors_df = determine_sector_weights(all_sectors, company_sectors, weights, dates_range)

        # Append new weights to new_weights_df
        optimized_weights_df = pd.concat([optimized_weights_df, formatted_optimized_weights_df], ignore_index=True)
        old_weights_df = pd.concat([old_weights_df, formatted_old_weights_df], ignore_index=True)
        #Append to sectors dfs.
        optimized_sectors_df = pd.concat([optimized_sectors_df, formatted_optimized_sectors_df], ignore_index=True)
        old_sectors_df = pd.concat([old_sectors_df, formatted_old_sectors_df], ignore_index=True) 

    # Write df to new sheet
    write_df(optimized_weights_df, old_weights_df, optimized_sectors_df, old_sectors_df)
    
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