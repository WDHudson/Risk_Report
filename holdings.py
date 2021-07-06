holdings = [
  {
    'name': 'EGFIX',
    'description': "The Edgewood Growth Fund is a growth equity mutual fund with an institutional and retail share class. The fund pursues long-term capital growth through a portfolio of 22 stocks of mid-to-large size companies. These companies are distinguished by their financial strength, levels of profitability, strong management, and ability to deliver long-term earnings power. The Fund's performance is typically benchmarked against the S&P 500 Growth Index over a full-market cycle.",
    'weight': 0.1087
  },
  {
    'name': 'AKRIX',
    'description': "The Akre Focus Fund (Institutional share: “AKRIX;” Retail share: “AKREX”) was launched on August 31, 2009, and currently has net assets of approximately $16.9 billion as of June 30, 2021. The Fund is non-diversified and maintains a focused portfolio of investments. These companies meet specific standards related to the business itself, the people who manage it, and the discipline they demonstrate when it comes to reinvesting free cash flow.",
    'weight': 0.1087
  },
  {
    'name': 'MBB',
    'description': "The iShares MBS ETF (MBB) seeks to track the investment results of an index composed of investment-grade mortgage-backed pass-through securities issued and/or guaranteed by U.S. government agencies.",
    'weight': 0.0529
  },
  {
    'name': 'IEF',
    'description': "he iShares 7-10 Year Treasury Bond ETF (IEF) seeks to track the investment results of an index composed of U.S. Treasury bonds with remaining maturities between seven and ten years.",
    'weight': 0.0297
  },
  {
    'name': 'PSK',
    'description': "The SPDR ICE Preferred Securities ETF (PSK) seeks to provide investment results that, before fees and expenses, correspond generally to the total return performance of the ICE Exchange-Listed Fixed & Adjustable Rate Preferred Securities Index. The ETF seeks to provide exposure to preferred securities that are non-convert. The Index holdings are required to be rated investment grade by either Moody’s Investors Service, Inc. or Standard & Poor’s Financial Services, LLC.",
    'weight': 0.0731
  },
  {
    'name': 'QQQ',
    'description': "Invesco QQQ is an exchange-traded fund that tracks the Nasdaq-100 Index™. The Index includes the 100 largest non-financial companies listed on the Nasdaq based on market cap.",
    'weight': 0.3768
  },
  {
    'name': 'QQQJ',
    'description': "The Invesco NASDAQ Next Gen 100 Fund (Fund) is based on the NASDAQ Next Generation 100 Index (Index). The Fund will invest at least 90% of its total assets in the securities that comprise the Index by investing in the 101st to the 200th largest companies on the NASDAQ. As a result, the portfolio may be concentrated in mid-capitalization stocks. The Index is comprised of securities of the next generation of Nasdaq-listed non-financial companies; that is, the largest 100 Nasdaq-listed companies outside of the NASDAQ-100 Index.",
    'weight': 0.0515
  },
  # {
  #   'name': 'RSP',
  #   'weight': 0.0528
  # },
  {
    'name': 'PDO',
    'description': "The fund utilizes an opportunistic approach to pursue high conviction income-generating ideas across both public and private credit markets to seek current income as a primary objective and capital appreciation as a secondary objective. In managing the fund, PIMCO employs a dynamic asset allocation strategy across multiple fixed income sectors based on, among other things, market conditions, valuation assessments, economic outlook, credit market trends and other economic factors. With PIMCO’s macroeconomic analysis as the basis for top-down investment decisions, including geographic and credit sector emphasis, PIMCO manages the fund with a focus on seeking income generating investment ideas across multiple fixed income sectors, with an emphasis on seeking opportunities in developed and emerging global credit markets.",
    'weight': 0.0341
  }
]

stocks = []
for stock in holdings:
  stocks.append(stock['name'])

weights = []
for etf in holdings:
  weights.append(etf['weight'])