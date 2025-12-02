import pandas as pd


def load_data (file_path: str):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

#Make column titles consistent with capitalization and spacing in order to make data set more professional and easier to work with
def uniform_column_names(df):
    """Standardize column names to lowercase and replace spaces with underscores."""
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace(r'_+', '_', regex=True).str.rstrip('_')  
    return df

#Rename qty to quantity for clarity
def rename_columns(df):
    """Rename columns for clarity."""
    df = df.rename(columns={'qty': 'quantity'})
    return df

#drop missing prices and quantities by dropping them in order to avoid skewed analysis
def drop_missing_values(df):
    """drop missing values in 'price' and 'quantity' columns by dropping rows with missing values."""
    df = df.dropna(subset=['price', 'quantity'])
    return df

# Strip leading/trailing whitespace from product names and categories
def strip_whitespace(df):
    """Strip extra whitespace from all text columns."""
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip()
    return df

# Remove currency symbols from price to allow for numerical operations
def remove_currency_symbols(df):
    """Remove currency symbols from 'price' column."""
    df['price'] = df['price'].replace('[\$,]', '', regex=True)
    return df
#strip whitespace in columns to ensure consistency
def strip_column_whitespace(df):
    """Strip spaces and special characters from column headers """
    df.columns = df.columns.str.strip()
    return df

# Convert data types to float for price and int for quantity to ensure correct calculations
def convert_data_types(df):
    """Convert data types of 'price' and 'quantity' columns."""
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    return df

# Drop missing prices and quantities by dropping them in order to avoid skewed analysis
def drop_missing_values(df):
    """Drop missing values in 'price' and 'quantity' columns by dropping rows with missing values."""
    df = df.dropna(subset=['price', 'quantity'])
    return df

# Remove rows with negative prices or quantities to prevent errors
def remove_invalid_rows(df):
    """Remove rows with negative 'price' or 'quantity'."""
    df = df[(df['price'] >= 0) & (df['quantity'] >= 0)]
    return df


if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)

    #Clean the data step by step
    df_clean = strip_column_whitespace(df_raw)
    df_clean = uniform_column_names(df_raw)
    df_clean = rename_columns(df_clean)
    df_clean = strip_whitespace(df_clean)
    df_clean = remove_currency_symbols(df_clean)
    df_clean = convert_data_types(df_clean)
    df_clean = drop_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)

df_clean.to_csv(cleaned_path, index=False)  
print(df_clean.head())