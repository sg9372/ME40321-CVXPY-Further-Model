import numpy as np

from averages_extract import extract_averages
from averages_optimizer import average_optimizer
from trends_extract import extract_trends
from trends_optimizer import trend_optimizer
from extract_sheets import extract_sheet_data

def main(file, start, mid, end, method):
    # Calculate optimal weights
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
    print("New returns:", np.round(new_returns,2))

        
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