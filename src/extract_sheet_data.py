import pandas as pd
import numpy as np

def extract_sheet_data(file, sheet_name):
    # Extract companies, weights and emissions data from sheet
    df = pd.read_excel(file, sheet_name=sheet_name)
    companies = df['Constituent RIC'].tolist()
    companies = [x for x in companies if str(x) != 'nan']

    weights = df['Weight percent'].to_numpy()
    weights = weights[~np.isnan(weights)]
    
    emissions = df['Emissions'].to_numpy()
    emissions = emissions[~np.isnan(emissions)]
    
    return companies, weights, emissions
