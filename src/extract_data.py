import pandas as pd

def get_average_values(df, start_day, end_day):
    # Filter based on the day range
    filtered_df = df[(df['Day'] >= start_day) & (df['Day'] <= end_day)]

    value_columns = [col for col in df.columns if col.startswith('Value')]
    return filtered_df[value_columns].mean().to_numpy()

def get_average_emissions(df, start_day, end_day):
    # Filter based on the day range
    filtered_df = df[(df['Day'] >= start_day) & (df['Day'] <= end_day)]

    emission_columns = [col for col in df.columns if col.startswith('Emission')]
    return filtered_df[emission_columns].mean().to_numpy()

def extract_data(file, start, end):
    # Read data
    df = pd.read_excel(file, index_col = 1)    
    
    values = get_average_values(df, start, end)
    emissions = get_average_emissions(df, start, end)
    return [values, emissions]