from signals import L, S, get_sma_signals
from strategies import OL, CL, OS, CS, run_strategy
from reader import read_csv
import argparse
import textwrap

close_sma_signals, sma_sma_signals = get_sma_signals()

# Price vs. SMA
SMA_1 = {
    OL: close_sma_signals[20, L],
    CL: close_sma_signals[20, S],
    OS: None,
    CS: None
}

SMA_2 = {
    OL: close_sma_signals[15, L],
    CL: close_sma_signals[10, S],
    OS: None,
    CS: None
}

SMA_3 = {
    OL: close_sma_signals[5, S],
    CL: close_sma_signals[10, S],
    OS: None,
    CS: None
}

SMA_4 = {
    OL: close_sma_signals[50, L],
    CL: close_sma_signals[20, S],
    OS: close_sma_signals[15, S],
    CS: close_sma_signals[5, L]
}

SMA_5 = {
    OL: None,
    CL: None,
    OS: close_sma_signals[20, S],
    CS: close_sma_signals[20, L]
}

# SMA vs. SMA
SMA_6 = {
    OL: sma_sma_signals[20, 50, L],
    CL: sma_sma_signals[20, 50, S],
    OS: None,
    CS: None
}

SMA_7 = {
    OL: sma_sma_signals[10, 20, L],
    CL: sma_sma_signals[10, 20, S],
    OS: None,
    CS: None
}

SMA_8 = {
    OL: sma_sma_signals[10, 20, L],
    CL: sma_sma_signals[5, 15, S],
    OS: None,
    CS: None
}

SMA_9 = {
    OL: sma_sma_signals[15, 50, L],
    CL: sma_sma_signals[10, 20, S],
    OS: sma_sma_signals[10, 20, S],
    CS: sma_sma_signals[10, 15, L]
}

SMA_10 = {
    OL: None,
    CL: None,
    OS: sma_sma_signals[15, 50, S],
    CS: sma_sma_signals[15, 50, L]
}

if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Strategies SMA",
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent("""\
    NDX ->\tpython code/strategiesSMA.py
    XAU ->\tpython code/strategiesSMA.py"""))

    # Load files
    ndx_SMA = read_csv("processed/ndx-SMA.csv", "ndx")
    xau_SMA = read_csv("processed/xau-SMA.csv", "xau")

    run_strategy(ndx_SMA, SMA_1, 1, "ndx/sma/s1.csv")
    run_strategy(ndx_SMA, SMA_2, 2, "ndx/sma/s2.csv")
    run_strategy(ndx_SMA, SMA_3, 3, "ndx/sma/s3.csv")
    run_strategy(ndx_SMA, SMA_4, 4, "ndx/sma/s4.csv")
    run_strategy(ndx_SMA, SMA_5, 5, "ndx/sma/s5.csv")
    run_strategy(ndx_SMA, SMA_6, 6, "ndx/sma/s6.csv")
    run_strategy(ndx_SMA, SMA_7, 7, "ndx/sma/s7.csv")
    run_strategy(ndx_SMA, SMA_8, 8, "ndx/sma/s8.csv")
    run_strategy(ndx_SMA, SMA_9, 9, "ndx/sma/s9.csv")
    run_strategy(ndx_SMA, SMA_10, 10, "ndx/sma/s10.csv")

    run_strategy(xau_SMA, SMA_1, 1, "xau/sma/s1.csv")
    run_strategy(xau_SMA, SMA_2, 2, "xau/sma/s2.csv")
    run_strategy(xau_SMA, SMA_3, 3, "xau/sma/s3.csv")
    run_strategy(xau_SMA, SMA_4, 4, "xau/sma/s4.csv")
    run_strategy(xau_SMA, SMA_5, 5, "xau/sma/s5.csv")
    run_strategy(xau_SMA, SMA_6, 6, "xau/sma/s6.csv")
    run_strategy(xau_SMA, SMA_7, 7, "xau/sma/s7.csv")
    run_strategy(xau_SMA, SMA_8, 8, "xau/sma/s8.csv")
    run_strategy(xau_SMA, SMA_9, 9, "xau/sma/s9.csv")
    run_strategy(xau_SMA, SMA_10, 10, "xau/sma/s10.csv")