import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import datetime as dt

def make_daily_return_graph(etf):
  end = dt.datetime.now()
  start = dt.datetime(end.year - 20, end.month, end.day)
  df = yf.download(etf, start, end)
  df = df['Adj Close'].pct_change()
  fig = plt.figure()
  plt.plot(df)
  plt.title(f'{etf} Daily Returns Since Inception')
  plt.savefig(f'images/etf_daily_returns/{etf}.png', dpi=fig.dpi, bbox_inches='tight')