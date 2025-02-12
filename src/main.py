import numpy as np

from extract_data import extract_data
from total_weight_change_limit import total_weight_change_optimize

def main(file, start, mid, end, method):
    """
    Can alter holdings in each stock either by total allowable move in weighting or based on a maximum 
    ammount each holding can be altered by.
    1. Altering holdings based on total allowable change end with:
        1 maxChange
    2. Altering holdings based on allowable change for each holding end with:
        2 individualChange
    """
    
    # Get average values in sampling region
    [values, emissions] = extract_data(file, start, mid)

    # Original (fixed) weights before optimization
    old_weights = np.random.rand(len(values))
    old_weights /= old_weights.sum()  # Normalize to sum to 1
    
    # Calculate optimal weights
    if method=='average':
        new_weights = total_weight_change_optimize(values, emissions, old_weights)
    elif method=='linear':
    
    # Calculate results from optimal results
    [future_values, future_emissions] = extract_data(file, mid, end)

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
        if method == 'average':
            main(file, start, mid, end, method)
        else:
            print("Please enter a valid method e.g. 'average'.")    
    except:
        print("Wrong data type.")
        print("Please enter an integer from 1 to 2 inclusive.")
        sys.exit(1)