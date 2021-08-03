import pandas as pd
import os

if __name__ == "__main__": 
    with open("account_values.txt", "w") as f:
        logs_dir = "log_files/"
        for ticker in filter(lambda x: x[0] != "." and x != "README.md", os.listdir(logs_dir)):
            for indicator in filter(lambda x: x[0] != ".", os.listdir(os.path.join(logs_dir, ticker))):
                for strategy in filter(lambda x: x[0] != ".", os.listdir(os.path.join(logs_dir, ticker, indicator))):
                    if not strategy.startswith("s"):
                        continue

                    file = os.path.join(logs_dir, ticker, indicator, strategy)
                    df = pd.read_csv(file)

                    i = df.index[-1]
                    f.write("%s: value %s, profit %s\n" % (file, str(df.at[i, "account_value"]), str(df.at[i, "account_value"] - 100000)))
