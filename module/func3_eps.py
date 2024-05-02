# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 09:10:06 2021

@author: pcuser
"""

import pandas as pd 
import requests
from bs4 import BeautifulSoup


import random

a = 'https://www.google.com.tw'
b = 'https://tw.yahoo.com'
c = 'https://www.pchome.com.tw/'
d = 'https://dj.mybank.com.tw/'

my_Referer = random.choice([a,b,c])

my_UserAgent = 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'

#stock_id = "2002"
'''
bankA = 'http://dj.mybank.com.tw/' #國泰世華
bankB = 'http://jdata.yuanta.com.tw/' #元大
bankC = 'http://jsjustweb.jihsun.com.tw' #日盛
bankD = 'http://stockchannel.sinotrade.com.tw' #永豐金證券
bankE = 'http://djfubonholdingfund.fbs.com.tw' #富邦證券

my_Banks = random.choice([bankA, bankB, bankC, bankD, bankE])
'''
bank_url = 'http://dj.mybank.com.tw/'


def EPS_quarterlyGetter(stock_id):  #取得EPS
    headers = {'Referer':my_Referer,'user-agent': my_UserAgent}
    sheet_type = 'z/zc/zcr/zcr_' #FRQ 財務比率 季表
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))
    
    newest_Fin_Q = str(dfs[2][1][1]) #最新1季的財報季份

    b1N = dfs[2][1][1] #最新1季的名稱
    b2N = dfs[2][2][1] #最新2季的名稱
    b3N = dfs[2][3][1] #最新3季的名稱
    b4N = dfs[2][4][1] #最新4季的名稱
    #b5N = dfs[2][5][1] #最新5季的名稱
    #b6N = dfs[2][6][1] #最新6季的名稱
    #b7N = dfs[2][7][1] #最新7季的名稱
    #b8N = dfs[2][8][1] #最新8季的名稱
    

    b1 = float((dfs[2][1][25])) #最新1季的EPS
    b2 = float((dfs[2][2][25])) #最新2季的EPS
    b3 = float((dfs[2][3][25])) #最新3季的EPS
    b4 = float((dfs[2][4][25])) #最新4季的EPS
    #b5 = float((dfs[2][5][25])) #最新5季的EPS
    #b6 = float((dfs[2][6][25])) #最新6季的EPS
    #b7 = float((dfs[2][7][25])) #最新7季的EPS
    #b8 = float((dfs[2][8][25])) #最新8季的EPS
    
    print(b2)
    
    return b1N, b2N, b3N, b4N, b1, b2, b3, b4, newest_Fin_Q

#EPS_quarterlyGetter('5457')