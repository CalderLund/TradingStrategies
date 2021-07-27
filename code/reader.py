import pandas as pd
import pandas_ta as pdt

def read_csv(filename, format, ticker):
    df = pd.read_csv(filename)
    df["Date"] = pd.to_datetime(df["Date"], format=format)
    df.ta.ticker(ticker)
    df.set_index(df["date"], inplace=True)
    return df
