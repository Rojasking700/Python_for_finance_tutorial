
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style 
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

#dataframe
df = pd.read_csv('tsla.csv', parse_dates = True, index_col=0 )

# df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean() # gets the rolling avg of adjusted cose for a 100 days  

#ohlc = Open High Low Close
#resamples data to adj close every 10 days 
df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)
# print(df_ohlc.head())

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1) 
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1) #doesnt acutally share axis

#takes mdates and makes them look pretty 
ax1.xaxis_date()

# 1st Param : what axis
# 2nd param : whats the data
# 3rd param : width of candle sticks
# 4th param : green color up 
candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
#fills axis 2 between df_volume mdates = x df_volume.value = y
ax2.fill_between(df_volume.index.map(mdates.date2num) ,df_volume.values, 0)

plt.show()