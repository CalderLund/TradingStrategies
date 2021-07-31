import pandas as pd
import pandas_ta as pdt

def read_csv(filename, ticker, format=None):
    df = pd.read_csv(filename)
    if format is not None:
        df["Date"] = pd.to_datetime(df["Date"], format=format)
    df.ta.ticker(ticker)
    df.set_index(df["date"], inplace=True)
    return df
