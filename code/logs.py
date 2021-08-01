import pandas as pd
import os

OL = "Entry_signal_long_%s"
CL = "Exit_signal_long_%s"
OS = "Entry_signal_short_%s"
CS = "Exit_signal_short_%s"

def get_position(df, snum):
    # Make empty log
    df["LONG"] = 0
    df["SHORT"] = 0

    df["account_value"] = 100000
    df["cash_flow"] = 0
    df["shares_long"] = 0
    df["shares_short"] = 0

    for i in df.index:
        if OL % snum in df.columns and df[OL % snum][i] == 1:
            df.loc[i:, 'LONG'] += 1
            df.at[i, 'cash_flow'] -= 1000
            df.loc[i:, 'account_value'] -= 1000
            df.loc[i:, 'shares_long'] += 1000 / df["close"][i]
        elif CL % snum in df.columns and df[CL % snum][i] == 1:
            df.loc[i:, 'account_value'] += df["close"][i] * df['shares_long'][i]
            df.at[i, 'cash_flow'] += df["close"][i] * df['shares_long'][i]
            df.loc[i:, 'shares_long'] = 0
            df.loc[i:, 'LONG'] = 0
        elif OS % snum in df.columns and df[OS % snum][i] == 1:
            df.loc[i:, 'SHORT'] -= 1
            df.at[i, 'cash_flow'] += 1000
            df.loc[i:, 'account_value'] += 1000
            df.loc[i:, 'shares_short'] -= 1000 / df["close"][i]
        elif CS % snum in df.columns and df[CS % snum][i] == 1:
            df.loc[i:, 'account_value'] -= df["close"][i] * df['shares_short'][i]
            df.at[i, 'cash_flow'] -= df["close"][i] * df['shares_short'][i]
            df.loc[i:, 'shares_short'] = 0
            df.loc[i:, 'SHORT'] = 0
    
    

if __name__ == "__main__":
    data_dir = "data_files/"
    logs_dir = "log_files/"
    for ticker in filter(lambda x: x[0] != "." and x != "README.md", os.listdir(data_dir)):
        for indicator in filter(lambda x: x[0] != ".", os.listdir(os.path.join(data_dir, ticker))):
            for strategy in filter(lambda x: x[0] != ".", os.listdir(os.path.join(data_dir, ticker, indicator))):
                if not strategy.startswith("s"):
                    continue

                file = os.path.join(data_dir, ticker, indicator, strategy)
                
                snum = strategy.strip("s.csv")
                df = pd.read_csv(file)

                get_position(df, snum)

                df.to_csv(os.path.join(logs_dir, ticker, indicator, strategy))
