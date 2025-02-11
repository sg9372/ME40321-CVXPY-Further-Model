from extract_data import extract_data 

def main(file, start, end, n):
    """
    Can alter holdings in each stock either by total allowable move in weighting or based on a maximum 
    ammount each holding can be altered by.
    1. Altering holdings based on total allowable change end with:
        1 maxChange
    2. Altering holdings based on allowable change for each holding end with:
        2 individualChange
    """
    # Get average values in sampling region
    [values, emissions] = extract_data(file, start, end)
    
    # Calculate optimal weights
    if 

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
        end = int(sys.argv[3])
        n = int(sys.argv[4])
        if 1<=n<=2:
            main(file, start, end, n)
        else:
            print("Please enter an integer from 1 to 2 inclusive.")    
    except:
        print("Wrong data type.")
        print("Please enter an integer from 1 to 2 inclusive.")
        sys.exit(1)