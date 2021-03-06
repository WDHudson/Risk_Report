# Implement the Monte Carlo Method to simulate a stock portfolio
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from pandas_datareader import data as pdr
from holdings import stocks, weights
import yfinance as yf
import dataframe_image as dfi

def run_monte_carlo():
    # import data
    today = dt.datetime.today()
    endDate = dt.datetime.now()
    startDate = endDate - dt.timedelta(days=20*365)
    def get_data(stocks, start, end):
        stockData = yf.download(stocks, start='2000-01-01', end=today)
        stockData = stockData['Adj Close']
        returns = stockData.pct_change()
        meanReturns = returns.mean()
        covMatrix = returns.cov()
        # print(covMatrix)
        return meanReturns, covMatrix


    meanReturns, covMatrix = get_data(stocks, startDate, endDate)
    mc_sims = 10000 # number of simulations
    T = 253 #timeframe in days

    meanM = np.full(shape=(T, len(weights)), fill_value=meanReturns)
    meanM = meanM.T

    portfolio_sims = np.full(shape=(T, mc_sims), fill_value=0.0)

    initialPortfolio = 100000

    for m in range(0, mc_sims):
        # MC loops
        Z = np.random.normal(size=(T, len(weights)))
        L = np.linalg.cholesky(covMatrix)
        dailyReturns = meanM + np.inner(L, Z)
        portfolio_sims[:,m] = np.cumprod(np.inner(weights, dailyReturns.T)+1)*initialPortfolio

    fig = plt.figure()
    plt.plot(portfolio_sims)
    plt.ylabel('Portfolio Value ($)')
    plt.xlabel('Days')
    plt.title('Monte Carlo simulation of ETF portfolio')
    plt.savefig('images/monte_carlo.png', dpi=fig.dpi, bbox_inches="tight")

    def mcVaR(returns, alpha=5):
        """ Input: pandas series of returns
            Output: percentile on return distribution to a given confidence level alpha
        """
        if isinstance(returns, pd.Series):
            return np.percentile(returns, alpha)
        else:
            raise TypeError("Expected a pandas data series.")

    def mcCVaR(returns, alpha=5):
        """ Input: pandas series of returns
            Output: CVaR or Expected Shortfall to a given confidence level alpha
        """
        if isinstance(returns, pd.Series):
            belowVaR = returns <= mcVaR(returns, alpha=alpha)
            return returns[belowVaR].mean()
        else:
            raise TypeError("Expected a pandas data series.")

    portResults = pd.Series(portfolio_sims[-1,:])

    VaR = initialPortfolio - mcVaR(portResults, alpha=5)
    CVaR = initialPortfolio - mcCVaR(portResults, alpha=5)

    data = [['VaR with 95 percent confidence:', '${}'.format(round(VaR,2))], ['CVaR with 95 percent confidence:', '${}'.format(round(CVaR,2))]]
    df = pd.DataFrame(data, columns = ['', ''])
    # Removes index column
    dfi.export(df, 'images/conf_interval_table.png', table_conversion='matplotlib')