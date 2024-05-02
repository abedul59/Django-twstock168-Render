# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 08:23:18 2020

@author: pcuser
"""


import random

a = 'https://www.google.com.tw'
b = 'https://tw.yahoo.com'
c = 'https://www.pchome.com.tw/'


my_Referer = random.choice([a,b,c])

my_UserAgent = 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'


###獲取營收公佈當日股價
def Daily_Price(stock_id, query_date, index_rev_date):
    headers = {'Referer': my_Referer ,'user-agent': my_UserAgent}

    ######以下為判斷上市或上櫃，取得年度股價程式
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup    


    #查詢上市年股價 （先上市，有些股票會上櫃轉上市，但上櫃還會留下資料，會抓錯。）
    twse_url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY_AVG?response=html&date=' 

    url = twse_url + query_date + '&stockNo=' + stock_id 
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))
    #print(dfs)
    
    rev_date_price  = dfs[0].iloc[index_rev_date][1]  #index_rev_date填入索引值
    
    #print(rev_date_price)
    
    return rev_date_price
    


def Daily_Price2(stock_id, dateX):#, month_id): #上櫃日股價查詢
    #import requests
    #import time
#導入套件
    #import datetime
#import pandas as pd
#pd.core.common.is_list_like = pd.api.types.is_list_like
    #import numpy as np

#設定爬蟲股票代號
    sid = stock_id + '.TWO'

#設定爬蟲時間
    #start = datetime.datetime.now() - datetime.timedelta(days=60)
    #end = datetime.date.today()

#----------pandas_datareader套件教學--------------------------
#導入pandas_datareader
    import pandas as pd
    pd.core.common.is_list_like = pd.api.types.is_list_like

    from pandas_datareader import data

# 取得股票資料
    stock_dr = data.get_data_yahoo(sid, dateX)
    
    #print(stock_dr)
    
    closeX = stock_dr.iloc[0][3]
    
    #print(stock_dr.iloc[0][3]) #
    
    return closeX

#Daily_Price2('6561', '2020-11-27')