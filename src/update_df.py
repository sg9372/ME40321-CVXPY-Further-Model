import pandas as pd
from datetime import datetime

def update_df(df, new_weights):
    # Append to df
    df.loc[len(df)] = new_weights
    return df