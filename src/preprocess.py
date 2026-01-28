import pandas as pd
from load_data import load_time_series

print(">>> preprocess.py started")

def preprocess_time_series(df, column="Global_active_power"):
    """
    Clean and prepare time-series for modeling.

    Parameters:
        df (pd.DataFrame): Raw dataframe
        column (str): Column to select

    Returns:
        pd.Series: Clean time-series
    """
    # Replace missing values marked as '?'
    df = df.replace("?", pd.NA)

    # Convert all columns to numeric
    df = df.apply(pd.to_numeric, errors="coerce")

    # Forward-fill missing values
    df = df.ffill()

    # Select one signal
    series = df[column]

    return series


if __name__ == "__main__":
    df = load_time_series("data/raw/power_consumption.csv")
    ts = preprocess_time_series(df)

    print(ts.head())
    print(ts.isna().sum())
print(">>> preprocess.py finished")

