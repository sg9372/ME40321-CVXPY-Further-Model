import pandas as pd
import numpy as np

def get_average_values(df, start_day, end_day):
    # Filter based on the day range
    filtered_df = df[(df['Day'] >= start_day) & (df['Day'] <= end_day)]
    
    # Gather data, find mean, and round to 2dp
    value_columns = [col for col in df.columns if col.startswith('Value')]
    average = filtered_df[value_columns].mean().to_numpy()
    return np.round(average, 2)

def get_average_emissions(df, start_day, end_day):
    # Filter based on the day range
    filtered_df = df[(df['Day'] >= start_day) & (df['Day'] <= end_day)]

    # Gather data, find mean, and round to 2dp
    emission_columns = [col for col in df.columns if col.startswith('Emission')]
    average = filtered_df[emission_columns].mean().to_numpy()
    return np.round(average, 2)

def extract_data(file, start, end):
    # Read data
    df = pd.read_excel(file)    
    
    values = get_average_values(df, start, end)
    emissions = get_average_emissions(df, start, end)
    return [values, emissions]