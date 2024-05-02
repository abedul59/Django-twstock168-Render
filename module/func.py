from django.conf import settings


######################################################以下為六大指標程式


import pandas as pd 
import requests
from bs4 import BeautifulSoup

#########

###########



##############################################

    
'''
def TWStock(stockid):
    import requests
    import time
#導入套件
    import datetime

    import numpy as np
    import matplotlib.pyplot as plt
#設定爬蟲股票代號
    sid = stockid + '.TW'

#設定爬蟲時間
    start = datetime.datetime.now() - datetime.timedelta(days=60)
    end = datetime.date.today()
#----------pandas_datareader套件教學--------------------------
#導入pandas_datareader
    import pandas as pd
 
    from pandas_datareader import data

# 取得股票資料
    stock_dr = data.get_data_yahoo(sid, start, end)
    #stock_dr.tail(10)

#線型圖，收盤價、5日均線、20日均線、60日均線
    stock_dr['Adj Close'].plot(figsize=(16, 8))
#stock_dr['Adj Close'].rolling(window=5).mean().plot(figsize=(16, 8), label='5_Day_Mean')
#stock_dr['Adj Close'].rolling(window=20).mean().plot(figsize=(16, 8), label='20_Day_Mean')
#stock_dr['Adj Close'].rolling(window=60).mean().plot(figsize=(16, 8), label='60_Day_Mean')

#顯示側標
    plt.legend(loc='upper right', shadow=True, fontsize='x-large')

#顯示標題
    plt.title(sid + ' 60 days Price Chart')
    plt.savefig('static/images/TWStock.png')  #很重要，要記得路徑。

    plt.close() #關掉之前的圖和數據 不然連續使用會重疊畫圖
    



def TWStockK(stockid): #成功版本mplfinance-0.12.4a0
    import requests
    import time
#導入套件
    import datetime

    import numpy as np
    import mplfinance as mpf
#設定爬蟲股票代號
    sid = stockid + '.TW'

#設定爬蟲時間
    start = datetime.datetime.now() - datetime.timedelta(days=60)
    end = datetime.date.today()
#----------pandas_datareader套件教學--------------------------
#導入pandas_datareader
    import pandas as pd
 
    from pandas_datareader import data

# 取得股票資料
    stock_dr = data.get_data_yahoo(sid, start, end)
    #stock_dr.tail(10)
    mpf.plot(stock_dr,type='candle',volume=True,savefig='static/images/TWStockKpic.png')







def TWStockKx(stockid, xdays): #成功版本mplfinance-0.12.4a0

    import datetime


    import mplfinance as mpf
#設定爬蟲股票代號

    sid = stockid + '.tw'

#設定爬蟲時間
    start = datetime.datetime.now() - datetime.timedelta(days=xdays)
    end = datetime.date.today()
#----------pandas_datareader套件教學--------------------------
#導入pandas_datareader
 
 
    from pandas_datareader import data

# 取得股票資料
    stock_dr = data.get_data_yahoo(sid, start, end)
        #stock_dr.tail(10)
    mpf.plot(stock_dr, type='candle',mav=(20,60),volume=True,savefig='static/images/TWStockKpicX.png')
'''
def TWStockKx(stockid, xdays): #成功版本mplfinance-0.12.4a0

    import datetime


    import mplfinance as mpf
#設定爬蟲股票代號

    sid = stockid + '.tw'

#設定爬蟲時間
    start = datetime.datetime.now() - datetime.timedelta(days=xdays)
    end = datetime.date.today()
#----------pandas_datareader套件教學--------------------------
#導入pandas_datareader
 
 
    from pandas_datareader import data

# 取得股票資料
    stock_dr = data.get_data_yahoo(sid, start, end)
        #stock_dr.tail(10)
    mpf.plot(stock_dr, type='candle',mav=(20,60),volume=True,savefig='static/images/TWStockKx.png')
             #TWStockKpicX.png')





##############################################
def USAStock(stockid):
    import requests
    import time
#導入套件
    import datetime

    import numpy as np
    import matplotlib.pyplot as plt
#設定爬蟲股票代號
    sid = stockid

#設定爬蟲時間
    start = datetime.datetime.now() - datetime.timedelta(days=60)
    end = datetime.date.today()
#----------pandas_datareader套件教學--------------------------
#導入pandas_datareader
    import pandas as pd
 
    from pandas_datareader import data

# 取得股票資料
    stock_dr = data.get_data_yahoo(sid, start, end)
    #stock_dr.tail(10)

#線型圖，收盤價、5日均線、20日均線、60日均線
    stock_dr['Adj Close'].plot(figsize=(16, 8))
#stock_dr['Adj Close'].rolling(window=5).mean().plot(figsize=(16, 8), label='5_Day_Mean')
#stock_dr['Adj Close'].rolling(window=20).mean().plot(figsize=(16, 8), label='20_Day_Mean')
#stock_dr['Adj Close'].rolling(window=60).mean().plot(figsize=(16, 8), label='60_Day_Mean')

#顯示側標
    plt.legend(loc='upper right', shadow=True, fontsize='x-large')

#顯示標題
    plt.title(sid + ' 60 days Price Chart')
    plt.savefig('static/images/USAStock_60d.png')  #很重要，要記得路徑。

    plt.close() #關掉之前的圖和數據 不然連續使用會重疊畫圖
    
    
def USAStockK(stockid): #成功版本mplfinance-0.12.4a0
    import requests
    import time
#導入套件
    import datetime

    import numpy as np
    import mplfinance as mpf
#設定爬蟲股票代號
    sid = stockid

#設定爬蟲時間
    start = datetime.datetime.now() - datetime.timedelta(days=60)
    end = datetime.date.today()
#----------pandas_datareader套件教學--------------------------
#導入pandas_datareader
    import pandas as pd
 
    from pandas_datareader import data

# 取得股票資料
    stock_dr = data.get_data_yahoo(sid, start, end)
    #stock_dr.tail(10)
    mpf.plot(stock_dr,type='candle',volume=True,savefig='static/images/USAStockK.png')


def USAStockKx(stockid, xdays): #成功版本mplfinance-0.12.4a0
    import requests
    import time
#導入套件
    import datetime

    import numpy as np
    import mplfinance as mpf
#設定爬蟲股票代號
    sid = stockid

#設定爬蟲時間
    start = datetime.datetime.now() - datetime.timedelta(days=xdays)
    end = datetime.date.today()
#----------pandas_datareader套件教學--------------------------
#導入pandas_datareader
    import pandas as pd
 
    from pandas_datareader import data

# 取得股票資料
    stock_dr = data.get_data_yahoo(sid, start, end)
    #stock_dr.tail(10)
    mpf.plot(stock_dr,type='candle',mav=(20,60),volume=True,savefig='static/images/USAStockK.png')

    