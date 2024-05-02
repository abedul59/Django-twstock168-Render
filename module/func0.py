# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 12:23:41 2021

@author: green
"""



import pandas as pd 
import requests
from bs4 import BeautifulSoup


import random

a = 'https://www.google.com.tw'
b = 'https://tw.yahoo.com'
c = 'https://www.pchome.com.tw/'
d = 'https://djinfo.cathaysec.com.tw/'

my_Referer = random.choice([a,b,c])

my_UserAgent = 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'

#stock_id = "2002"
'''
bankA = 'https://djinfo.cathaysec.com.tw/' #國泰世華
bankB = 'http://jdata.yuanta.com.tw/' #元大
bankC = 'http://jsjustweb.jihsun.com.tw' #日盛
bankD = 'http://stockchannel.sinotrade.com.tw' #永豐金證券
bankE = 'http://djfubonholdingfund.fbs.com.tw' #富邦證券

my_Banks = random.choice([bankA, bankB, bankC, bankD, bankE])
'''
bank_url = 'https://djinfo.cathaysec.com.tw/'

#


def CFSQuery(stock_id):  #營業利益率評分標準
    headers = {'Referer':my_Referer,'user-agent': my_UserAgent}



    sheet_type = 'z/zc/zc3/zc3_' #現金流量表 季表
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))
    
    CFS_Time = []  #時間

    for i in range(1,9):
        CFS_Time.append(dfs[2][i][0])

    
    CFSitem = [None] * 15  #項目

 
   

            
    #, dfs[2][2][0], dfs[2][3][0], dfs[2][4][0], dfs[2][5][0]], dfs[2][6][0], dfs[2][7][0], dfs[2][8][0])

    CFSitem[0] = [] #營收淨額
    for i in range(1,9):
        CFSitem[0].append(dfs[2][i][3])

    CFSitem[1] = [] #銷貨成本
    for i in range(1,9):
        CFSitem[1].append(dfs[2][i][5])

    CFSitem[2] = [] #營業毛利
    for i in range(1,9):
        CFSitem[2].append(dfs[2][i][6])   
        
    CFSitem[3] = [] #營業費用
    for i in range(1,9):
        CFSitem[3].append(dfs[2][i][9])         
        
    CFSitem[4] = [] #研究發展費
    for i in range(1,9):
        CFSitem[4].append(dfs[2][i][12]) 

    CFSitem[5] = [] #營業利益
    for i in range(1,9):
        CFSitem[5].append(dfs[2][i][16])  

    CFSitem[6] = [] #營業外收入及支出
    for i in range(1,9):
        CFSitem[6].append(dfs[2][i][63]) 


    CFSitem[7] = [] #稅前淨利
    for i in range(1,9):
        CFSitem[7].append(dfs[2][i][64]) 

    CFSitem[8] = [] #合併總損益
    for i in range(1,9):
        CFSitem[8].append(dfs[2][i][70]) 

    CFSitem[9] = [] #本期綜合損益總額
    for i in range(1,9):
        CFSitem[9].append(dfs[2][i][91]) 

    CFSitem[10] = [] #歸屬母公司淨利（損）
    for i in range(1,9):
        CFSitem[10].append(dfs[2][i][92]) 

    CFSitem[11] = [] #歸屬非控制權益淨利（損）
    for i in range(1,9):
        CFSitem[11].append(dfs[2][i][93]) 

    CFSitem[12] = [] #每股盈餘
    for i in range(1,9):
        CFSitem[12].append(dfs[2][i][98]) 
    
    
    return CFS_Time, CFSitem


def ISQuery(stock_id):  #營業利益率評分標準
    headers = {'Referer':my_Referer,'user-agent': my_UserAgent}



    sheet_type = 'z/zc/zcq/zcq_' #ISQ 合併損益表 季表
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))
    
    IS_Time = []  #時間

    for i in range(1,9):
        IS_Time.append(dfs[2][i][0])

    
    ISitem = [None] * 15  #項目

 
   

            
    #, dfs[2][2][0], dfs[2][3][0], dfs[2][4][0], dfs[2][5][0]], dfs[2][6][0], dfs[2][7][0], dfs[2][8][0])

    ISitem[0] = [] #營收淨額
    for i in range(1,9):
        ISitem[0].append(dfs[2][i][3])

    ISitem[1] = [] #銷貨成本
    for i in range(1,9):
        ISitem[1].append(dfs[2][i][5])

    ISitem[2] = [] #營業毛利
    for i in range(1,9):
        ISitem[2].append(dfs[2][i][6])   
        
    ISitem[3] = [] #營業費用
    for i in range(1,9):
        ISitem[3].append(dfs[2][i][9])         
        
    ISitem[4] = [] #研究發展費
    for i in range(1,9):
        ISitem[4].append(dfs[2][i][12]) 

    ISitem[5] = [] #營業利益
    for i in range(1,9):
        ISitem[5].append(dfs[2][i][16])  

    ISitem[6] = [] #營業外收入及支出
    for i in range(1,9):
        ISitem[6].append(dfs[2][i][63]) 


    ISitem[7] = [] #稅前淨利
    for i in range(1,9):
        ISitem[7].append(dfs[2][i][64]) 

    ISitem[8] = [] #合併總損益
    for i in range(1,9):
        ISitem[8].append(dfs[2][i][70]) 

    ISitem[9] = [] #本期綜合損益總額
    for i in range(1,9):
        ISitem[9].append(dfs[2][i][91]) 

    ISitem[10] = [] #歸屬母公司淨利（損）
    for i in range(1,9):
        ISitem[10].append(dfs[2][i][92]) 

    ISitem[11] = [] #歸屬非控制權益淨利（損）
    for i in range(1,9):
        ISitem[11].append(dfs[2][i][93]) 

    ISitem[12] = [] #每股盈餘
    for i in range(1,9):
        ISitem[12].append(dfs[2][i][98]) 
    
    
    return IS_Time, ISitem