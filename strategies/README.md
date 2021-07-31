# Strategies

## SMA
* s1: open long when SMA_20 crosses above price, close long when SMA_20 crosses below price
* s2: open long when SMA_15 crosses above price, close long when SMA_10 crosses below price
* s3: open long when SMA_5 crosses below price, close long when SMA_10 crosses below price
* s4: open long when SMA_50 crosses above price, close long when SMA_20 crosses below price, open short when SMA_15 crosses below price, close short when SMA_5 crosses above price
* s5: open short when SMA_20 crosses below price, close short when SMA_20 crosses above price
* s6: open long when SMA_20 crosses above SMA_50, close long when SMA_20 crosses below SMA_50
* s7: open long when SMA_10 crosses above SMA_20, close long when SMA_10 crosses below SMA_20
* s8: open long when SMA_10 crosses above SMA_20, close long when SMA_5 crosses below SMA_15
* s9: open long when SMA_15 crosses above SMA_50, close long when SMA_10 crosses below SMA_20, open short when SMA_10 crosses below SMA_20, close short when SMA_10 crosses above SMA_15
* s10: open short when SMA_15 crosses below SMA_50, close short when SMA_15 crosses above SMA_50

## EMA
* s1: open long when EMA_20 crosses above price, close long when EMA_20 crosses below price
* s2: open long when EMA_15 crosses above price, close long when EMA_10 crosses below price
* s3: open long when EMA_5 crosses below price, close long when EMA_10 crosses below price
* s4: open long when EMA_50 crosses above price, close long when EMA_20 crosses below price, open short when EMA_15 crosses below price, close short when EMA_5 crosses above price
* s5: open short when EMA_20 crosses below price, close short when EMA_20 crosses above price
* s6: open long when EMA_20 crosses above EMA_50, close long when EMA_20 crosses below EMA_50
* s7: open long when EMA_10 crosses above EMA_20, close long when EMA_10 crosses below EMA_20
* s8: open long when EMA_10 crosses above EMA_20, close long when EMA_5 crosses below EMA_15
* s9: open long when EMA_15 crosses above EMA_50, close long when EMA_10 crosses below EMA_20, open short when EMA_10 crosses below EMA_20, close short when EMA_10 crosses above EMA_15
* s10: open short when EMA_15 crosses below EMA_50, close short when EMA_15 crosses above EMA_50

## RSI
* s1: open long & close short when RSI_4 crosses above 30 after being below 30 for 5 periods, close long & open short when RSI_4 crosses below 70 after being above 70 for 5 periods
* s2: open long & close short when RSI_6 crosses above 30 after being below 30 for 5 periods, close long & open short when RSI_6 crosses below 70 after being above 70 for 5 periods
* s3: open long & close short when RSI_14 crosses above 30 after being below 30 for 5 periods, close long & open short when RSI_14 crosses below 70 after being above 70 for 5 periods
* s4: open long when RSI_4 crosses above 30 after being below 30 for 5 periods, close long when RSI_4 crosses below 70 after being above 70 for 5 periods, open short when RSI_4 crosses below 30, close short when RSI_4 crosses above 70
* s5: open long when RSI_6 crosses above 30 after being below 30 for 5 periods, close long when RSI_6 crosses below 70 after being above 70 for 5 periods, open short when RSI_6 crosses below 30, close short when RSI_6 crosses above 70
* s6: open long when RSI_14 crosses above 30 after being below 30 for 5 periods, close long when RSI_14 crosses below 70 after being above 70 for 5 periods, open short when RSI_14 crosses below 30, close short when RSI_14 crosses above 70

## BB
* s1: open long & close short when price crosses above BBL_20_2.0 after being below for 5 periods, close long & open short when price crosses below BBL_20_2.0 after being above for 5 periods
* s2: open long & close short when price crosses above BBL_12_2.0 after being below for 5 periods, close long & open short when price crosses below BBL_12_2.0 after being above for 5 periods
* s3: open long & close short when price crosses above BBL_20_1.0 after being below for 5 periods, close long & open short when price crosses below BBL_20_1.0 after being above for 5 periods
* s4: open long & close short when price crosses above BBL_12_1.0 after being below for 5 periods, close long & open short when price crosses below BBL_12_1.0 after being above for 5 periods
