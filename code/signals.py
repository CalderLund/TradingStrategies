import numpy as np
from strategies import OL, CL, OS, CS

L = "long"
S = "short"

### MOVING AVERAGE SIGNALS ###
def moving_average_signal(signal_type, column1, column2):
    def signal(df, name):
        if signal_type == L:
            df[name] = np.where((df[column1] > df[column2]) & (df[column1].shift(1) <= df[column2].shift(1)), 1, 0)
        elif signal_type == S:
            df[name] = np.where((df[column1] < df[column2]) & (df[column1].shift(1) >= df[column2].shift(1)), 1, 0)
        else:
            raise RuntimeError("unknown signal type for Moving Average, must be 'long' or 'short'")
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

### RELATIVE STRENGTH INDEX SIGNALS ###
def rsi_signal(signal_type, column):
    def signal(df, name):
        if signal_type == OL:
            df[name] = np.where((df[column] > 30) \
                & (df[column].shift(1) <= 30) \
                & (df[column].shift(2) <= 30) \
                & (df[column].shift(3) <= 30) \
                & (df[column].shift(4) <= 30) \
                & (df[column].shift(5) <= 30),
            1, 0)
        elif signal_type == OS:
            df[name] = np.where((df[column] < 70) \
                & (df[column].shift(1) >= 70) \
                & (df[column].shift(2) >= 70) \
                & (df[column].shift(3) >= 70) \
                & (df[column].shift(4) >= 70) \
                & (df[column].shift(5) >= 70),
            1, 0)
        elif signal_type == CL:
            df[name] = np.where((df[column] < 30) & (df[column].shift(1) >= 30), 1, 0)
        elif signal_type == CS:
            df[name] = np.where((df[column] > 70) & (df[column].shift(1) <= 70), 1, 0)
        else:
            raise RuntimeError("unknown signal type for RSI, must be 'open long', 'close long', 'open short' or 'close short'")
    return signal

# RSI signals
def get_rsi_signals():
    rsi_signals = {}

    for length in (4, 6, 14):
        rsi_signals[(length, OL)] = rsi_signal(OL, "RSI_%d" % length)
        rsi_signals[(length, OS)] = rsi_signal(OS, "RSI_%d" % length)
        rsi_signals[(length, CL)] = rsi_signal(CL, "RSI_%d" % length)
        rsi_signals[(length, CS)] = rsi_signal(CS, "RSI_%d" % length)
        
    return rsi_signals

### BOLLINGER BANDS SIGNALS ###
def bb_signal(signal_type, column1, column2):
    def signal(df, name):
        if signal_type == L:
            df[name] = np.where((df[column1] > df[column2]) \
                & (df[column1].shift(1) <= df[column2].shift(1)) \
                & (df[column1].shift(2) <= df[column2].shift(2)) \
                & (df[column1].shift(3) <= df[column2].shift(3)) \
                & (df[column1].shift(4) <= df[column2].shift(4)) \
                & (df[column1].shift(5) <= df[column2].shift(5)),
            1, 0)
        elif signal_type == S:
            df[name] = np.where((df[column1] < df[column2]) \
                & (df[column1].shift(1) >= df[column2].shift(1)) \
                & (df[column1].shift(2) >= df[column2].shift(2)) \
                & (df[column1].shift(3) >= df[column2].shift(3)) \
                & (df[column1].shift(4) >= df[column2].shift(4)) \
                & (df[column1].shift(5) >= df[column2].shift(5)),
            1, 0)
        else:
            raise RuntimeError("unknown signal type for BB, must be 'long' or 'short'")
    return signal

# BB signals
def get_bb_signals():
    bb_signals = {}

    for length, std in ((12, 1), (20, 1), (12, 2), (20, 2)):
        bb_signals[(length, std, L, "L")] = bb_signal(L, "close", "BBL_%d_%d.0" % (length, std))
        bb_signals[(length, std, S, "L")] = bb_signal(S, "close", "BBL_%d_%d.0" % (length, std))
        bb_signals[(length, std, L, "M")] = bb_signal(L, "close", "BBM_%d_%d.0" % (length, std))
        bb_signals[(length, std, S, "M")] = bb_signal(S, "close", "BBM_%d_%d.0" % (length, std))
        bb_signals[(length, std, L, "U")] = bb_signal(L, "close", "BBU_%d_%d.0" % (length, std))
        bb_signals[(length, std, S, "U")] = bb_signal(S, "close", "BBU_%d_%d.0" % (length, std))
        
    return bb_signals

### MACD SIGNALS ###
def macd_signal(signal_type, macd, macds):
    def signal(df, name):
        if signal_type == OL:
            df[name] = np.where((df[macd] > df[macds]) \
                & (df[macd].shift(1) <= df[macds].shift(1)) \
                & (df[macd].shift(2) <= df[macds].shift(2)) \
                & (df[macd].shift(3) <= df[macds].shift(3)),
            1, 0)
        elif signal_type == OS:
            df[name] = np.where((df[macd] < df[macds]) \
                & (df[macd].shift(1) >= df[macds].shift(1)) \
                & (df[macd].shift(2) >= df[macds].shift(2)) \
                & (df[macd].shift(3) >= df[macds].shift(3)),
            1, 0)
        elif signal_type == CL:
            df[name] = np.where((df[macd] < df[macds]) & (df[macd].shift(1) >= df[macds].shift(1)), 1, 0)
        elif signal_type == CS:
            df[name] = np.where((df[macd] > df[macds]) & (df[macd].shift(1) <= df[macds].shift(1)), 1, 0)
        else:
            raise RuntimeError("unknown signal type for MACD, must be 'open long', 'close long', 'open short' or 'close short'")
    return signal

# MACD signals
def get_macd_signals():
    macd_signals = {}

    for length1, length2 in ((8, 21), (12, 26)):
        macd_signals[(length1, length2, OL)] = macd_signal(OL, "MACD_%d_%d_9" % (length1, length2), "MACDs_%d_%d_9" % (length1, length2))
        macd_signals[(length1, length2, CL)] = macd_signal(CL, "MACD_%d_%d_9" % (length1, length2), "MACDs_%d_%d_9" % (length1, length2))
        macd_signals[(length1, length2, OS)] = macd_signal(OS, "MACD_%d_%d_9" % (length1, length2), "MACDs_%d_%d_9" % (length1, length2))
        macd_signals[(length1, length2, CS)] = macd_signal(CS, "MACD_%d_%d_9" % (length1, length2), "MACDs_%d_%d_9" % (length1, length2))
        
    return macd_signals
