# TradingStrategies
Application and analysis of various trading strategies on daily and hourly data.

## Installation
* `git clone https://github.com/CalderLund/TradingStrategies.git` from your github account or download from GitHub's user interface.
* install `python >= 3.6`
* from TradingStrategies repo, `pip install -r requirements.txt`

## Running
* `python code/indicators.py data/NDX-daily.csv "%Y-%m-%d" ndx` creates processed data in `processed/`
* `python code/indicators.py data/XAU-1h.csv "%Y-%m-%d %H:%M" xau` creates processed data in `processed/`
* `python code/strategies<indicator>.py` for each indicator in `data_files/`
* `python code/logs.py` creates the log files for each in `log_files/`

## Useful libraries
* https://github.com/twopirllc/pandas-ta/tree/main/pandas_ta
* https://pandas.pydata.org/docs/
* https://matplotlib.org/
