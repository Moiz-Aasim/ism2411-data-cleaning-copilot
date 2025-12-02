import pandas as pd


def load_data (file_path: str):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

#Make column titles consistent with capitalization and spacing in order to make data set more professional and easier to work with
def uniform_column_names(df):
    """Standardize column names to lowercase and replace spaces with underscores."""
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    return df

#drop missing prices and quantities by dropping them in order to avoid skewed analysis
def drop_missing_values(df):
    """drop missing values in 'price' and 'quantity' columns by dropping rows with missing values."""
    df = df.dropna(subset=['price', 'quantity'])
    return df

