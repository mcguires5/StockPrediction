from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import fix_yahoo_finance as yf
import numpy as np
from datetime import datetime
import matplotlib.dates as mdates

yf.pdr_override() # <== that's all it takes :-)

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y')


# download Panel
data = pdr.get_data_yahoo(["SPY"], start="2017-01-01", end="2018-04-30")
CloseDates = data['Close']
dates = np.asarray(CloseDates.axes[0])
dates = dates.astype(datetime)
close_values = CloseDates.values


plt.plot(dates, close_values)
plt.show()
print("Done")