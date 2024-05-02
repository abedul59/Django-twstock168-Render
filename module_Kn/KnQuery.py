# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 08:43:37 2021

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


def KnQuery(stock_id): #税後淨利年增率
    headers = {'Referer':my_Referer,'user-agent': my_UserAgent}
    
    sheet_type = 'z/zc/zcq/zcq_' #ISQ 合併損益表 季表
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))


    bt1qN = dfs[2][1][0] #最新1季的名稱
    bt2qN = dfs[2][2][0] #最新2季的名稱
    bt3qN = dfs[2][3][0] #最新3季的名稱
    bt4qN = dfs[2][4][0] #最新4季的名稱
    bt5qN = dfs[2][5][0] #最新5季的名稱
    bt6qN = dfs[2][6][0] #最新6季的名稱
    bt7qN = dfs[2][7][0] #最新7季的名稱
    bt8qN = dfs[2][8][0] #最新8季的名稱

#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][70] #最新1季的合併總損益 税後淨利
#print(dfs[2][1][11])
    bt1q = float((dfs[2][1][64])) #最新1季的合併總損益 税前淨利 百萬
    bt2q = float((dfs[2][2][64])) #最新1季的合併總損益 税前淨利 百萬
    bt3q = float((dfs[2][3][64])) #最新1季的合併總損益 税前淨利 百萬
    bt4q = float((dfs[2][4][64])) #最新1季的合併總損益 税前淨利 百萬
    
    print(bt1q)


    sheet_type2 = 'z/zc/zcp/zcpa/zcpa_' #BSQ 表 季表
    url2 = bank_url + sheet_type2 + stock_id + '.djhtm'
    r = requests.get(url2, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))

    sh1q = float((dfs[2][1][92])) #最新1季的合併資產負債 股東權益總額 百萬
    sh2q = float((dfs[2][2][92])) #最新2季的合併資產負債 股東權益總額 百萬
    sh3q = float((dfs[2][3][92])) #最新3季的合併資產負債 股東權益總額 百萬
    sh4q = float((dfs[2][4][92])) #最新4季的合併資產負債 股東權益總額 百萬
    
    print(sh1q)
    #縮減小數後位數
    bt_roe1q = round(float(bt1q)/float(sh1q),4) #稅前ROE    
    if len(str(bt_roe1q)) > 3:
        bt_roe1qp = (str(bt_roe1q*100))[:4]+ "%"
    else:
        bt_roe1qp = str(bt_roe1q*100)+ "%"    
    

    bt_roe2q = round(float(bt2q)/float(sh2q),4) #稅前ROE
    if len(str(bt_roe2q)) > 3:
        bt_roe2qp = (str(bt_roe2q*100))[:4]+ "%"
    else:
        bt_roe2qp = str(bt_roe2q*100)+ "%"


    bt_roe3q = round(float(bt3q)/float(sh3q),4) #稅前ROE
    if len(str(bt_roe3q)) > 3:
        bt_roe3qp = (str(bt_roe3q*100))[:4]+ "%"
    else:
        bt_roe3qp = str(bt_roe3q*100)+ "%"

    bt_roe4q = round(float(bt4q)/float(sh4q),4) #稅前ROE
    if len(str(bt_roe4q)) > 3:
        bt_roe4qp = (str(bt_roe4q*100))[:4]+ "%"
    else:
        bt_roe4qp = str(bt_roe4q*100)+ "%"



    bt_roe1_4sum = bt_roe1q + bt_roe2q +bt_roe3q + bt_roe4q

    
    print(bt_roe1q)
    
    #bt_roe1qp = str(bt_roe1q*100)+ "%"
    #bt_roe2qp = str(bt_roe2q*100)+ "%"
    #bt_roe3qp = str(bt_roe3q*100)+ "%"
    #bt_roe4qp = str(bt_roe4q*100)+ "%"
    if len(str(bt_roe1_4sum)) > 3:
        bt_roe1_4sump = (str(bt_roe1_4sum*100))[:4]+ "%"
    else:
        bt_roe1_4sump = str(bt_roe1_4sum*100)+ "%"

    #bt_roe1_4sump =  str(bt_roe1_4sum*100) + "%"   
    print(bt_roe1qp)
    #####################################################

    sheet_type3 = 'z/zc/zcr/zcr_' #財務比率 表 季表
    url2 = bank_url + sheet_type3 + stock_id + '.djhtm'
    r = requests.get(url2, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))

    b1q = float((dfs[2][1][18])) #最新1季的每股淨值(F)(TSE公告數) 	
    
    print(b1q)
    
    
    url_y = 'https://tw.stock.yahoo.com/q/ts?s=' + stock_id

    r = requests.get(url_y)


    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))


#    yahoo_tradePrice = dfs[0][3] #yahoo成交價
#    yahoo_time= dfs[0][0] #yahoo成交時間
    yahoo_latest_tradePrice = float(dfs[0][3][6]) #yahoo最新成交價

    print(yahoo_latest_tradePrice)
    
    pb1q = round(float(yahoo_latest_tradePrice)/float(b1q),4)
    
    print(pb1q)
    
    #kn1 = round(bt_roe1/pb1,4)
    kn1_4sum = round(bt_roe1_4sum/pb1q,4)
    
    print(kn1_4sum)
    
    #kn1p = str(kn1*100) + "%"
    kn1_4sump = str(kn1_4sum*100) + "%"

    print(kn1_4sum)
    
    return bt1q, sh1q, bt_roe1_4sum, bt_roe1_4sump, b1q, yahoo_latest_tradePrice, pb1q, kn1_4sum, kn1_4sump, bt1qN, bt2qN, bt3qN, bt4qN, bt_roe1qp, bt_roe2qp, bt_roe3qp, bt_roe4qp
    
#KnQuery("2330")