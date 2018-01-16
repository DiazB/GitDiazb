###########################################################################################
##Import Modules
import datetime as dt

import sys, getopt

#print("This is the name of the script: ", sys.argv[0])
#print("Number of arguments: ", len(sys.argv))
#print("The arguments are: " , str(sys.argv))

symbol = str(sys.argv[1])
# Import Log Modules
#import numpy as np
#import pylab

import matplotlib.pyplot as plt
from matplotlib import style
#from matplotlib.mpl_finance import candlestick_ohlc
#pip install https://github.com/matplotlib/mpl_finance/archive/master.zip
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

import pandas as pd
import pandas_datareader.data as web

#######
style.use('ggplot')

start = dt.datetime(2011,1,1)
end = dt.datetime(2018,1,31)

###########################################################################################
## Save Yahoo data to CSV ###########
df = web.DataReader(symbol, 'yahoo', start, end)
#df = web.DataReader('BTC-USD', 'yahoo', start, end)
#df = web.DataReader('LTC-USD', 'yahoo', start, end)
#df = web.DataReader('XRP-USD', 'yahoo', start, end)

df.to_csv('Stock.csv')

## Read CSV data ###########
dd = pd.read_csv('Stock.csv', parse_dates=True, index_col=0)
dd['50ma'] = dd['Adj Close'].rolling(window=50).mean()
dd['200ma'] = dd['Adj Close'].rolling(window=200).mean()
dd['50va'] = dd['Volume'].rolling(window=50).mean()

# Print current day's data
print("Symbol: ", symbol)
print(dd.tail(1))


## Set up Chart ###########
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(dd.index, dd['Adj Close'])
ax1.plot(dd.index, dd['50ma'])
ax1.plot(dd.index, dd['200ma'])


ax2.bar(dd.index, dd['Volume'])
ax2.plot(dd.index, dd['50va'])

## Display Chart
ax1.set_yscale('log')
plt.show()