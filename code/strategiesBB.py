from signals import L, S, OL, CL, OS, CS, get_bb_signals
from strategies import run_strategy
from reader import read_csv
import argparse
import textwrap

bb_signals = get_bb_signals()

# Price vs. BB
BB_1 = {
    OL: bb_signals[20, 2, L, "L"],
    CL: bb_signals[20, 2, S, "U"],
    OS: bb_signals[20, 2, S, "U"],
    CS: bb_signals[20, 2, L, "L"]
}

BB_2 = {
    OL: bb_signals[12, 2, L, "L"],
    CL: bb_signals[12, 2, S, "U"],
    OS: bb_signals[12, 2, S, "U"],
    CS: bb_signals[12, 2, L, "L"]
}

BB_3 = {
    OL: bb_signals[20, 2, L, "L"],
    CL: bb_signals[20, 1, L, "U"],
    OS: bb_signals[20, 2, S, "U"],
    CS: bb_signals[20, 1, S, "L"]
}

BB_4 = {
    OL: bb_signals[12, 2, L, "L"],
    CL: bb_signals[12, 1, L, "U"],
    OS: bb_signals[12, 2, S, "U"],
    CS: bb_signals[12, 1, S, "L"]
}

BB_5 = {
    OL: bb_signals[20, 1, L, "L"],
    CL: bb_signals[20, 1, L, "U"],
    OS: bb_signals[20, 1, S, "U"],
    CS: bb_signals[20, 1, S, "L"]
}

BB_6 = {
    OL: bb_signals[12, 1, L, "L"],
    CL: bb_signals[12, 1, L, "M"],
    OS: bb_signals[12, 1, S, "U"],
    CS: bb_signals[12, 1, S, "M"]
}


if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Strategies BB",
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent("""\
    NDX ->\tpython code/strategiesBB.py
    XAU ->\tpython code/strategiesBB.py"""))

    # Load files
    ndx_BB = read_csv("processed/ndx-BB.csv", "ndx")
    xau_BB = read_csv("processed/xau-BB.csv", "xau")

    run_strategy(ndx_BB, BB_1, 1, "ndx/bb/s1.csv")
    run_strategy(ndx_BB, BB_1, 2, "ndx/bb/s2.csv")
    run_strategy(ndx_BB, BB_1, 3, "ndx/bb/s3.csv")
    run_strategy(ndx_BB, BB_1, 4, "ndx/bb/s4.csv")
    run_strategy(ndx_BB, BB_1, 5, "ndx/bb/s5.csv")
    run_strategy(ndx_BB, BB_1, 6, "ndx/bb/s6.csv")

    run_strategy(xau_BB, BB_1, 1, "xau/bb/s1.csv")
    run_strategy(xau_BB, BB_2, 2, "xau/bb/s2.csv")
    run_strategy(xau_BB, BB_3, 3, "xau/bb/s3.csv")
    run_strategy(xau_BB, BB_4, 4, "xau/bb/s4.csv")
    run_strategy(xau_BB, BB_5, 5, "xau/bb/s5.csv")
    run_strategy(xau_BB, BB_6, 6, "xau/bb/s6.csv")
