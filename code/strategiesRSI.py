from signals import L, S, OL, CL, OS, CS, get_rsi_signals
from strategies import run_strategy
from reader import read_csv
import argparse
import textwrap

rsi_signals = get_rsi_signals()

# RSI
RSI_1 = {
    OL: rsi_signals[4, OL],
    CL: rsi_signals[4, OS],
    OS: rsi_signals[4, OS],
    CS: rsi_signals[4, OL]
}

RSI_2 = {
    OL: rsi_signals[6, OL],
    CL: rsi_signals[6, OS],
    OS: rsi_signals[6, OS],
    CS: rsi_signals[6, OL]
}

RSI_3 = {
    OL: rsi_signals[14, OL],
    CL: rsi_signals[14, OS],
    OS: rsi_signals[14, OS],
    CS: rsi_signals[14, OL]
}

RSI_4 = {
    OL: rsi_signals[4, OL],
    CL: rsi_signals[4, CL],
    OS: rsi_signals[4, OS],
    CS: rsi_signals[4, CS]
}

RSI_5 = {
    OL: rsi_signals[6, OL],
    CL: rsi_signals[6, CL],
    OS: rsi_signals[6, OS],
    CS: rsi_signals[6, CS]
}

RSI_6 = {
    OL: rsi_signals[14, OL],
    CL: rsi_signals[14, CL],
    OS: rsi_signals[14, OS],
    CS: rsi_signals[14, CS]
}


if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Strategies RSI",
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent("""\
    NDX ->\tpython code/strategiesRSI.py
    XAU ->\tpython code/strategiesRSI.py"""))

    # Load files
    ndx_RSI = read_csv("processed/ndx-RSI.csv", "ndx")
    xau_RSI = read_csv("processed/xau-RSI.csv", "xau")

    run_strategy(ndx_RSI, RSI_1, 1, "ndx/rsi/s1.csv")
    run_strategy(ndx_RSI, RSI_1, 2, "ndx/rsi/s2.csv")
    run_strategy(ndx_RSI, RSI_1, 3, "ndx/rsi/s3.csv")
    run_strategy(ndx_RSI, RSI_1, 4, "ndx/rsi/s4.csv")
    run_strategy(ndx_RSI, RSI_1, 5, "ndx/rsi/s5.csv")
    run_strategy(ndx_RSI, RSI_1, 6, "ndx/rsi/s6.csv")

    run_strategy(xau_RSI, RSI_1, 1, "xau/rsi/s1.csv")
    run_strategy(xau_RSI, RSI_2, 2, "xau/rsi/s2.csv")
    run_strategy(xau_RSI, RSI_3, 3, "xau/rsi/s3.csv")
    run_strategy(xau_RSI, RSI_4, 4, "xau/rsi/s4.csv")
    run_strategy(xau_RSI, RSI_5, 5, "xau/rsi/s5.csv")
    run_strategy(xau_RSI, RSI_6, 6, "xau/rsi/s6.csv")
