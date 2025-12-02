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

#Convert data types to float for price and int for quantity to ensure correct calculations
def convert_data_types(df):
    """Convert data types of 'price' and 'quantity' columns."""
    df['price'] = df['price'].astype(float)
    df['quantity'] = df['quantity'].astype(int)
    return df

#Remove currency symbols from price to allow for numerical operations
def remove_currency_symbols(df):
    """Remove currency symbols from 'price' column."""
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
    return df
