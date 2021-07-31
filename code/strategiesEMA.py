from signals import L, S, OL, CL, OS, CS, get_ema_signals
from strategies import run_strategy
from reader import read_csv
import argparse
import textwrap

close_ema_signals, ema_ema_signals = get_ema_signals()

# Price vs. EMA
EMA_1 = {
    OL: close_ema_signals[20, L],
    CL: close_ema_signals[20, S],
    OS: None,
    CS: None
}

EMA_2 = {
    OL: close_ema_signals[15, L],
    CL: close_ema_signals[10, S],
    OS: None,
    CS: None
}

EMA_3 = {
    OL: close_ema_signals[5, S],
    CL: close_ema_signals[10, S],
    OS: None,
    CS: None
}

EMA_4 = {
    OL: close_ema_signals[50, L],
    CL: close_ema_signals[20, S],
    OS: close_ema_signals[15, S],
    CS: close_ema_signals[5, L]
}

EMA_5 = {
    OL: None,
    CL: None,
    OS: close_ema_signals[20, S],
    CS: close_ema_signals[20, L]
}

# EMA vs. EMA
EMA_6 = {
    OL: ema_ema_signals[20, 50, L],
    CL: ema_ema_signals[20, 50, S],
    OS: None,
    CS: None
}

EMA_7 = {
    OL: ema_ema_signals[10, 20, L],
    CL: ema_ema_signals[10, 20, S],
    OS: None,
    CS: None
}

EMA_8 = {
    OL: ema_ema_signals[10, 20, L],
    CL: ema_ema_signals[5, 15, S],
    OS: None,
    CS: None
}

EMA_9 = {
    OL: ema_ema_signals[15, 50, L],
    CL: ema_ema_signals[10, 20, S],
    OS: ema_ema_signals[10, 20, S],
    CS: ema_ema_signals[10, 15, L]
}

EMA_10 = {
    OL: None,
    CL: None,
    OS: ema_ema_signals[15, 50, S],
    CS: ema_ema_signals[15, 50, L]
}

if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Strategies EMA",
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent("""\
    NDX ->\tpython code/strategiesEMA.py
    XAU ->\tpython code/strategiesEMA.py"""))

    # Load files
    ndx_EMA = read_csv("processed/ndx-EMA.csv", "ndx")
    xau_EMA = read_csv("processed/xau-EMA.csv", "xau")

    run_strategy(ndx_EMA, EMA_1, 1, "ndx/ema/s1.csv")
    run_strategy(ndx_EMA, EMA_2, 2, "ndx/ema/s2.csv")
    run_strategy(ndx_EMA, EMA_3, 3, "ndx/ema/s3.csv")
    run_strategy(ndx_EMA, EMA_4, 4, "ndx/ema/s4.csv")
    run_strategy(ndx_EMA, EMA_5, 5, "ndx/ema/s5.csv")
    run_strategy(ndx_EMA, EMA_6, 6, "ndx/ema/s6.csv")
    run_strategy(ndx_EMA, EMA_7, 7, "ndx/ema/s7.csv")
    run_strategy(ndx_EMA, EMA_8, 8, "ndx/ema/s8.csv")
    run_strategy(ndx_EMA, EMA_9, 9, "ndx/ema/s9.csv")
    run_strategy(ndx_EMA, EMA_10, 10, "ndx/ema/s10.csv")

    run_strategy(xau_EMA, EMA_1, 1, "xau/ema/s1.csv")
    run_strategy(xau_EMA, EMA_2, 2, "xau/ema/s2.csv")
    run_strategy(xau_EMA, EMA_3, 3, "xau/ema/s3.csv")
    run_strategy(xau_EMA, EMA_4, 4, "xau/ema/s4.csv")
    run_strategy(xau_EMA, EMA_5, 5, "xau/ema/s5.csv")
    run_strategy(xau_EMA, EMA_6, 6, "xau/ema/s6.csv")
    run_strategy(xau_EMA, EMA_7, 7, "xau/ema/s7.csv")
    run_strategy(xau_EMA, EMA_8, 8, "xau/ema/s8.csv")
    run_strategy(xau_EMA, EMA_9, 9, "xau/ema/s9.csv")
    run_strategy(xau_EMA, EMA_10, 10, "xau/ema/s10.csv")
