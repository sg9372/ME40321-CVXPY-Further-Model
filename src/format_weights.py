import pandas as pd

# Get weights in correct format.
def format_weights(all_companies, companies, optimized_weights, end_date):
    new_weights = [0] * len(all_companies)
    for i in range(len(companies)):
        ind = all_companies.index(companies[i])
        new_weights[ind] = optimized_weights[i]
    formatted_weights = [end_date] + new_weights
    return formatted_weights