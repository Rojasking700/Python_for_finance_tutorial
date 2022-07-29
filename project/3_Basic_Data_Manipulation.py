
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style 
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

df = pd.read_csv('tsla.csv', parse_dates = True, index_col=0 )

df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean() # gets the rolling avg of adjusted cose for a 100 days  

# df.dropna(inplace=True)

print(df.head())

# graphs 
# First parameter = graphsize 6x1:
# second param = start position 0,0 (top corner)
# Third how many rows it will span 5
# Fourth how many columns it will span 
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1) 
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1) #doesnt acutally shaer axix

# plots simple line that takes Xs and Ys
ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.plot(df.index, df['Volume'])

plt.show()