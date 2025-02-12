from extract_data import extract_data

def main(file, start, mid, end):
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
    
    # Calculate optimal weights
    

    #if n==1:
        
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 5:                                  
        print("Wrong ammount of input arguments, example usage:")
        print("'python src/main.py sample_data.xlsx 2 5 1'")
        sys.exit(1)
    
    try:
        file = str(sys.argv[1])
        start = int(sys.argv[2])
        mid = int(sys.argv[3])
        end = int(sys.argv[4])
        method = int(sys.argv[5])
        if method == 'total' or method == 'individual':
            main(file, start, mid, end, method)
        else:
            print("Please enter a valid method e.g. 'total'.")    
    except:
        print("Wrong data type.")
        print("Please enter an integer from 1 to 2 inclusive.")
        sys.exit(1)