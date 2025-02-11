from extract_data import extract_data 

def main(file, n):
    """
    Description
    """
    data = extract_data(file)
    
    #if n==1:
        


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:                                  
        print("Wrong ammount of input arguments, example usage:")   # Reject if >1 input argument.
        print("'python src/main.py sample_data 1'")
        sys.exit(1)
    
    try:
        file = str(sys.argv[1])
        n = int(sys.argv[2])
        if 1<=n<=2:
            main(n)
        else:
            print("Please enter an integer from 1 to 2 inclusive.")    
    except:
        print("Wrong data type.")
        print("Please enter an integer from 1 to 2 inclusive.")
        sys.exit(1)