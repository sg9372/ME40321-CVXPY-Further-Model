import pandas as pd

# Get weights in correct format.
def format_weights(all_companies, companies, optimized_weights, dates_range):
    formatted_weights = [0] * len(all_companies)
    for i in range(len(companies)):
        ind = all_companies.index(companies[i])
        formatted_weights[ind] = optimized_weights[i]
    
    # Create a DataFrame with dates as the LHS column and optimized weights as the weights in every single row
    formatted_weights_df = pd.DataFrame([formatted_weights]*len(dates_range), columns=all_companies)
    formatted_weights_df.insert(0, 'Date', dates_range)
    
    return formatted_weights_df