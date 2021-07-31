OL = "open long"
CL = "close long"
OS = "open short"
CS = "close short"

def run_strategy(df, strategy, snum, sname):
    dfc = df.copy()
    if strategy[OL] is not None:
        strategy[OL](dfc, "Entry_signal_long_%d" % snum)
    if strategy[CL] is not None:
        strategy[CL](dfc, "Exit_signal_long_%d" % snum)
    if strategy[OS] is not None:
        strategy[OS](dfc, "Entry_signal_short_%d" % snum)
    if strategy[CS] is not None:
        strategy[CS](dfc, "Exit_signal_short_%d" % snum)
    dfc.to_csv("strategies/%s" % sname)
