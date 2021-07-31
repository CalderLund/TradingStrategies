import numpy as np

L = "long"
S = "short"

def moving_average_signal(signal_type, column1, column2):
    def signal(df, name):
        if signal_type == L:
            df[name] = np.where((df[column1] > df[column2]) & (df[column1].shift(-1) <= df[column2].shift(-1)), 1, 0)
        elif signal_type == S:
            df[name] = np.where((df[column1] < df[column2]) & (df[column1].shift(-1) >= df[column2].shift(-1)), 1, 0)
        else:
            raise RuntimeError("unknown signal tyoe for Moving Average, must be 'long' or 'short'")
    return signal

# SMA Signals
def get_sma_signals():
    # SMA Signals (close vs. SMA)
    close_sma_signals = {}
    for length in [5, 10, 15, 20, 50]:
        close_sma_signals[(length, L)] = moving_average_signal(L, "close", "SMA_%d" % length)
        close_sma_signals[(length, S)] = moving_average_signal(S, "close", "SMA_%d" % length)

    # SMA Signals (SMA vs. SMA)
    sma_sma_signals = {}
    for l1 in [5, 10, 15, 20, 50]:
        for l2 in [5, 10, 15, 20, 50]:
            sma_sma_signals[(l1, l2, L)] = moving_average_signal(L, "SMA_%d" % l1, "SMA_%d" % l2)
            sma_sma_signals[(l1, l2, S)] = moving_average_signal(S, "SMA_%d" % l1, "SMA_%d" % l2)
    
    return close_sma_signals, sma_sma_signals

# EMA Signals
def get_ema_signals():
    # EMA Signals (close vs. EMA)
    close_ema_signals = {}
    for length in [5, 10, 15, 20, 50]:
        close_ema_signals[(length, L)] = moving_average_signal(L, "close", "EMA_%d" % length)
        close_ema_signals[(length, S)] = moving_average_signal(S, "close", "EMA_%d" % length)

    # EMA Signals (EMA vs. EMA)
    ema_ema_signals = {}
    for l1 in [5, 10, 15, 20, 50]:
        for l2 in [5, 10, 15, 20, 50]:
            ema_ema_signals[(l1, l2, L)] = moving_average_signal(L, "EMA_%d" % l1, "EMA_%d" % l2)
            ema_ema_signals[(l1, l2, S)] = moving_average_signal(S, "EMA_%d" % l1, "EMA_%d" % l2)

    return close_ema_signals, ema_ema_signals
