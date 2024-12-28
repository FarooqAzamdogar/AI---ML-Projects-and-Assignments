def load_data(file_path):
    """Load dataset from a specified file path."""
    import pandas as pd
    return pd.read_csv(file_path)

def preprocess_data(df):
    """Preprocess the dataset."""
    # Example preprocessing steps
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

def save_processed_data(df, file_path):
    """Save the processed dataset to a specified file path."""
    df.to_csv(file_path, index=False)