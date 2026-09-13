'''
pandas datareader: extension of pandas to connect with APIs
        > install: pip install pandas-datareader
    - includes FRED, yahoo finance, world bank, etc.
    - FRED: series of data set from the federal reserve
    - yfinance: data also includes the financial reports
        > install: pip install yfinance

useful online data sources:
    - https://finviz.com/
    - https://www.koyfin.com/
    - https://ziggma.com/
    - https://valueline.com/
    - https://www.finra.org/
    - https://www.sec.gov/submit-filings
'''
import pandas_datareader.data as web
import yfinance as yf
import matplotlib.pyplot as plt

# You can now keep your existing code (just remove the 'yahoo' argument)
aapl_df = yf.download('AAPL',start='2020-01-01',end='2021-01-01')
print(aapl_df)

inflation_df = web.DataReader('T10YIE','fred',start='2004-01-01',end='2020-01-01')
print(inflation_df)
inflation_df.plot()
# plt.show()

# yfinance ticker object
aapl_ticker = yf.Ticker('AAPL')
print('BALANCE SHEET:\n{}'.format(aapl_ticker.get_balance_sheet()))
print('CORPORATE ACTIONS:\n{}'.format(aapl_ticker.actions))
