import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from pypfopt import plotting
import datetime as dt
from holdings import stocks
import dataframe_image as dfi

def make_matrix():
  end = dt.datetime.now()
  start = dt.datetime(end.year - 20, end.month, end.day)
  df = yf.download(stocks, start, end)
  df = np.log(1+df['Adj Close'].pct_change())
  cov_table = df.cov()
  dfi.export(cov_table, 'images/cov_table.png', table_conversion='matplotlib')
  plotting.plot_covariance(df.corr(), plot_correlation=True, show_tickers=True)
  plt.savefig('images/correl_matrix.png')