###########################################################################################
##Import Modules
import datetime as dt

import sys, getopt

#print("This is the name of the script: ", sys.argv[0])
#print("Number of arguments: ", len(sys.argv))
#print("The arguments are: " , str(sys.argv))


import plotly.plotly as py
import plotly.graph_objs as go

symbol = str(sys.argv[1])
# Import Log Modules
#import numpy as np
#import pylab

#import matplotlib.pyplot as plt
#from matplotlib import style
#from matplotlib.mpl_finance import candlestick_ohlc
#pip install https://github.com/matplotlib/mpl_finance/archive/master.zip
#from mpl_finance import candlestick_ohlc
#import matplotlib.dates as mdates

import pandas as pd
import pandas_datareader.data as web

#######
##style.use('ggplot')

start = dt.datetime(2011,1,1)
end = dt.datetime(2018,1,31)

###########################################################################################
## Save Yahoo data to CSV ###########
df = web.DataReader(symbol, 'yahoo')#, start, end)

trace = go.Ohlc(x=df.index,
                open=df.Open,
                high=df.High,
                low=df.Low,
                close=df.Close)
data = [trace]
py.iplot(data, filename='simple_ohlc')
