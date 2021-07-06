import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from pypfopt import plotting
import datetime as dt
from risk_report import stocks


end = dt.datetime.now()
start = dt.datetime(end.year - 20, end.month, end.day)

df = yf.download(stocks, start, end)

df = np.log(1+df['Adj Close'].pct_change())
print(df)

plotting.plot_covariance(df.corr(), plot_correlation=True, show_tickers=True)
plt.savefig('correl_matrix.png')