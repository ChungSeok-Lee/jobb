import datetime as dt
import os
from pandas_datareader import data as pdr


tickers = ['NKE','JPM','KO','GNL','AAPL','SBUX','T','MA','PG','OHI','COST','VZ','MS','MSFT',
'V','JNJ','MCD','BA','BAC','PEP','WMT','INTC','WFC','HON','DPZ','QCOM','BLK','GILD','MMM',
'UNH','AMGN','HD','ADI','ROST','SWKS','K','EL','GS','DIS','O','SPY','IVV','VOO','QQQ','DIV',
'SOXX','XLF','IBB','VIG','EWQ','ARKQ']


if not os.path.exists('stock_dfs'):
    os.makedirs('stock_dfs')
start = dt.datetime(2010, 1, 1)
end = dt.datetime.now()
for ticker in tickers:
    print(ticker)
    if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
        df = pdr.get_data_yahoo(ticker, start, end)
        df.reset_index(inplace=True)
        df.set_index("Date", inplace=True)
        df.to_csv('stock_dfs/{}.csv'.format(ticker))
    else:
        print('Already have {}'.format(ticker))