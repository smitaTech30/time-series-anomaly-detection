import pandas as pd

def load_time_series(path):
    df = pd.read_csv(
        path,
        sep=";",              # IMPORTANT: correct delimiter
        low_memory=False
    )

    # Clean column names
    df.columns = df.columns.str.strip()

    # Combine Date and Time into datetime
    df["datetime"] = pd.to_datetime(
        df["Date"] + " " + df["Time"],
        format="%d/%m/%Y %H:%M:%S"
    )

    # Sort by time
    df = df.sort_values("datetime").reset_index(drop=True)

    return df


if __name__ == "__main__":
    df = load_time_series("data/raw/power_consumption.csv")
    print(df.head())
    print(df.columns)

