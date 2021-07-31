from signals import L, S, OL, CL, OS, CS, get_macd_signals
from strategies import run_strategy
from reader import read_csv
import argparse
import textwrap

macd_signals = get_macd_signals()

# Price vs. MACD
MACD_1 = {
    OL: macd_signals[8, 21, OL],
    CL: macd_signals[8, 21, OS],
    OS: macd_signals[8, 21, OS],
    CS: macd_signals[8, 21, OL],
}

MACD_2 = {
    OL: macd_signals[12, 26, OL],
    CL: macd_signals[12, 26, OS],
    OS: macd_signals[12, 26, OS],
    CS: macd_signals[12, 26, OL],
}

MACD_3 = {
    OL: macd_signals[8, 21, OL],
    CL: macd_signals[8, 21, CL],
    OS: macd_signals[8, 21, OS],
    CS: macd_signals[8, 21, CS],
}

MACD_4 = {
    OL: macd_signals[12, 26, OL],
    CL: macd_signals[12, 26, CL],
    OS: macd_signals[12, 26, OS],
    CS: macd_signals[12, 26, CS],
}

if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Strategies MACD",
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent("""\
    NDX ->\tpython code/strategiesMACD.py
    XAU ->\tpython code/strategiesMACD.py"""))

    # Load files
    ndx_MACD = read_csv("processed/ndx-MACD.csv", "ndx")
    xau_MACD = read_csv("processed/xau-MACD.csv", "xau")

    run_strategy(ndx_MACD, MACD_1, 1, "ndx/macd/s1.csv")
    run_strategy(ndx_MACD, MACD_2, 2, "ndx/macd/s2.csv")
    run_strategy(ndx_MACD, MACD_3, 3, "ndx/macd/s3.csv")
    run_strategy(ndx_MACD, MACD_4, 4, "ndx/macd/s4.csv")

    run_strategy(xau_MACD, MACD_1, 1, "xau/macd/s1.csv")
    run_strategy(xau_MACD, MACD_2, 2, "xau/macd/s2.csv")
    run_strategy(xau_MACD, MACD_3, 3, "xau/macd/s3.csv")
    run_strategy(xau_MACD, MACD_4, 4, "xau/macd/s4.csv")
