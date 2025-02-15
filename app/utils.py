import pandas as pd
import numpy as np

def load_data(file_path):
    """Load and preprocess the dataset."""
    data = pd.read_csv(file_path)
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    data.set_index('Timestamp', inplace=True)
    return data

def calculate_z_scores(df, columns):
    """Calculate Z-scores for specified columns."""
    z_scores = df[columns].apply(lambda x: (x - x.mean()) / x.std())
    return z_scores