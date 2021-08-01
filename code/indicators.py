from reader import read_csv
import argparse
import textwrap
import matplotlib.pyplot as plt

def roi(df):
    df["ROI"] = df.close / df.close.shift(1) - 1

def sma(df, lengths=[5,10,15,20,50]):
    for length in lengths:
        df.ta.sma(length=length, append=True)

def ema(df, lengths=[5,10,15,20,50]):
    for length in lengths:
        df.ta.ema(length=length, append=True)

def rsi(df, lengths=[4, 6, 14]):
    for length in lengths:
        df.ta.rsi(length=length, append=True)

def bbands(df, lengths_std=[(12, 1), (20, 1), (12, 2), (20, 2)]):
    for length, std in lengths_std:
        df.ta.bbands(length=length, append=True, std=std)

def macd(df, fastslow=[(8, 21), (12, 26)]):
    for fast, slow in fastslow:
        df.ta.macd(fast=fast, slow=slow, append=True)

if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Indicators", 
                                    formatter_class=argparse.RawDescriptionHelpFormatter,
                                    epilog=textwrap.dedent("""\
    NDX ->\tpython code/indicators.py data/NDX-daily.csv "%Y-%m-%d" ndx
    XAU ->\tpython code/indicators.py data/XAU-1h.csv "%Y-%m-%d %H:%M" xau"""))
    parser.add_argument("file")
    parser.add_argument("format")
    parser.add_argument("ticker")

    # Run program
    args = parser.parse_args()
    df = read_csv(args.file, ticker=args.ticker, format=args.format)

    df = df.iloc[::-1]

    # Apply indicators
    sma(df)
    ema(df)
    rsi(df)
    bbands(df)
    macd(df)
    roi(df)

    # See plots for various indicators
    #df[["close", "SMA_5", "SMA_10", "SMA_15", "SMA_20", "SMA_50"]].plot()
    #df[["close", "EMA_5", "EMA_10", "EMA_15", "EMA_20", "EMA_50"]].plot()
    #df[["RSI_14", "RSI70", "RSI30"]].plot()
    #df[["close", "BBL_20_2.0", "BBM_20_2.0", "BBU_20_2.0"]].plot()
    #df[["MACD_8_21_9", "MACDh_8_21_9", "MACDs_8_21_9"]].plot()
    #plt.show(block=True)

    # Save indicator
    df.to_csv("processed/%s.csv" % args.ticker)
    df[["close", "ROI", "SMA_5", "SMA_10", "SMA_15", "SMA_20", "SMA_50"]].to_csv("processed/%s-SMA.csv" % args.ticker)
    df[["close", "ROI", "EMA_5", "EMA_10", "EMA_15", "EMA_20", "EMA_50"]].to_csv("processed/%s-EMA.csv" % args.ticker)
    df[["close", "ROI", "RSI_4", "RSI_6", "RSI_14"]].to_csv("processed/%s-RSI.csv" % args.ticker)
    df[["close", "ROI", "BBL_12_1.0", "BBU_12_1.0", "BBM_12_1.0",
                        "BBL_20_1.0", "BBU_20_1.0", "BBM_20_1.0",
                        "BBL_12_2.0", "BBU_12_2.0", "BBM_12_2.0",
                        "BBL_20_2.0", "BBU_20_2.0", "BBM_20_2.0"]].to_csv("processed/%s-BB.csv" % args.ticker)
    df[["close", "ROI", "MACD_8_21_9", "MACDh_8_21_9", "MACDs_8_21_9",
                        "MACD_12_26_9", "MACDh_12_26_9", "MACDs_12_26_9"]].to_csv("processed/%s-MACD.csv" % args.ticker)
