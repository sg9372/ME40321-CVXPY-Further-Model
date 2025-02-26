import numpy as np

from extract_sheet_names import get_sheet_names
from src.extract_sheet_data import extract_sheet_data
#from extract_values import extract_values
#from optimizer import optimizer
#from store_weights import store_weights

def main(file, start, mid, end, method):
    # Obtain sheet names and date ranges
    sheet_names, dates = get_sheet_names(file)

    # Iterate through each date range
    for i in range(len(dates)-1):
        start_date = dates[i]
        end_date = dates[i+1]
        sheet_name = sheet_names[i]
        
        # Extract sheet data
        companies, weights, emissions = extract_sheet_data(file, sheet_name)

        # Extract values
    
        # Calculate optimal weights
        #new_weights = optimizer(values, emissions, weights)
        
        # Store new weights in excel file
        #store_weights(file, start_date, end_date ,sheet_name, new_weights)
    


'''
    if method=='average':
        # Get average values in sampling region
        [values, emissions] = extract_averages(file, start, mid)
        old_weights = np.random.rand(len(values))
        old_weights /= old_weights.sum()  # Normalize to sum to 1
        new_weights = average_optimizer(values, emissions, old_weights)
    elif method=='trend':
        # Get data trends for predicting future va;ues and emissions, and optimize based on these.
        [historical_values, historical_emissions] = extract_trends(file, start, mid)
        old_weights = np.random.rand(len(historical_values[0]))
        old_weights /= old_weights.sum()  # Normalize to sum to 1
        new_weights = trend_optimizer(historical_values, historical_emissions, old_weights, end)
      
    # Calculate results from optimal results
    [future_values, future_emissions] = extract_averages(file, mid, end)

    # Display results and comparison
    # Emissions
    old_emissions = np.sum(future_emissions * old_weights)
    new_emissions = np.sum(future_emissions * new_weights)
    print("Old emissions:", np.round(old_emissions,2))
    print("New emissions:", np.round(new_emissions,2))

    # Output Returns
    old_returns = np.sum(future_values * old_weights)
    new_returns = np.sum(future_values * new_weights)
    print("Old returns:", np.round(old_returns,2))
    print("New returns:", np.round(new_returns,2))'''

        
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 6:                                  
        print("Wrong ammount of input arguments, example usage:")
        print("'python src/main.py sample_data.xlsx 2 5 1'")
        sys.exit(1)
    try:
        file = str(sys.argv[1])
        start = int(sys.argv[2])
        mid = int(sys.argv[3])
        end = int(sys.argv[4])
        method = str(sys.argv[5])
        if method == 'average' or method=='trend':
            main(file, start, mid, end, method)
        else:
            print("Please enter a valid method e.g. 'average'.")    
    except:
        print("Wrong data type.")
        print("Please enter an integer from 1 to 2 inclusive.")
        sys.exit(1)