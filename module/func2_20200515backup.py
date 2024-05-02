# -*- coding: utf-8 -*-
"""
Created on Wed May  6 08:29:58 2020

@author: Farland
"""
from django.conf import settings

import pandas as pd 
import requests
from bs4 import BeautifulSoup


#stock_id = "2002"
bank_url = 'http://dj.mybank.com.tw/' #國泰世華

def stock_Prof(stock_id):
    sheet_type = 'z/zc/zcr/zcr_' #FRQ 財務比率 季表
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))


    a1N = dfs[2][1][1] #最新1季的名稱
    a2N = dfs[2][2][1] #最新2季的名稱
    a3N = dfs[2][3][1] #最新3季的名稱
    a4N = dfs[2][4][1] #最新4季的名稱
    a5N = dfs[2][5][1] #最新5季的名稱
    a6N = dfs[2][6][1] #最新6季的名稱
    a7N = dfs[2][7][1] #最新7季的名稱
    a8N = dfs[2][8][1] #最新8季的名稱
    
    a9N = "近四季平均"
    a10N = "最新1季季增率"
    a11N = "最新2季季增率"
    a12N = "最新3季季增率"
    a13N = "最新4季季增率"

    ProfitN = []
    ProfitN.extend([a1N,a2N,a3N,a4N,a5N,a6N,a7N,a8N])
#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][10] 最新一季營益率
#print(dfs[2][1][10])

    a1 = float((dfs[2][1][10])) #最新1季的營益率
    a2 = float((dfs[2][2][10])) #最新2季的營益率 
    a3 = float((dfs[2][3][10])) #最新3季的營益率
    a4 = float((dfs[2][4][10])) #最新4季的營益率
    a5 = float((dfs[2][5][10])) #最新5季的營益率
    a6 = float((dfs[2][6][10])) #最新6季的營益率
    a7 = float((dfs[2][7][10])) #最新7季的營益率
    a8 = float((dfs[2][8][10])) #最新8季的營益率

    Profit = []
    Profit.extend([a1,a2,a3,a4,a5,a6,a7,a8])

#print(a1)

    a9 = latest_4season_average = (a1+a2+a3+a4)/4 #四季平均
    #print(a9)
    a10 = latest_month_gain_loss = float((a1-a2)/abs(a2)) #最新一個月月增率
    #print(a10)
    a11 = second_latest_month_gain_loss = float((a2-a3)/abs(a3)) #次新一個月月增率
    #print(a11)
    a12 = third_latest_month_gain_loss = float((a3-a4)/abs(a4)) #第3新一個月月增率
    #print(a12)
    a13 = fourth_latest_month_gain_loss = float((a4-a5)/abs(a5)) #第4新一個月月增率
    #print(a13)

    if a1 < 0:
        result1 = "C"

    elif a9 < 0:
        result1 = "C"
        
    elif a10 <= -0.2 or a9 <= 0.05:
        result1 = "B"
        
    elif a9 >= 0.1: 
        result1 = "A"    
    
    elif a9 >= 0.05 and a10 > 0:
        result1 = "A"        
        
    elif (a9 >= 0.15):
        result1 = "AA"
        
    elif a9 >= 0.1 and a10 > 0:
        result1 = "AA"

    elif a11 <= -0.2 or a12 <= -0.2 or a13 <= -0.2:
        result1 = "BB"

    else:
        result1 = "BB"

    return result1, ProfitN, Profit, a1N, a2N, a3N, a4N, a5N, a6N, a7N, a8N, a1, a2, a3, a4, a5, a6, a7, a8

################################################################

def stock_Rev(stock_id): #(股票代碼, 股票名稱. 股票價格觸及下緣)
    sheet_type = 'z/zc/zch/zch_' #Rev 營收   
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))

#dfs[2] 真正表格
#dfs[2][4] 營收年增率
#dfs[2][4][6] 最新一個月年增率
    #print(dfs[2][4][6])
    ###MoneyDJ
    b1N = dfs[2][0][6] #最新1個月的名稱 
    b2N = dfs[2][0][7] #最新2個月的名稱 
    b3N = dfs[2][0][8] #最新3個月的名稱
    b4N = dfs[2][0][9] #最新4個月的名稱 
    b5N = dfs[2][0][10] #最新5個月的名稱 
    b6N = dfs[2][0][11] #最新6個月的名稱 

    RevN = []
    RevN.extend([b1N,b2N,b3N,b4N,b5N,b6N])

    b1 = round(float((dfs[2][4][6])[:-1])/100,4) #最新1個月的營收年增率 
    b2 = round(float((dfs[2][4][7])[:-1])/100,4) #最新2個月的營收年增率 
    b3 = round(float((dfs[2][4][8])[:-1])/100,4) #最新3個月的營收年增率 
    b4 = round(float((dfs[2][4][9])[:-1])/100,4) #最新4個月的營收年增率 
    b5 = round(float((dfs[2][4][10])[:-1])/100,4) #最新5個月的營收年增率 
    b6 = round(float((dfs[2][4][11])[:-1])/100,4) #最新6個月的營收年增率 

    Rev = []
    Rev.extend([b1,b2,b3,b4,b5,b6])

    b9 = latest_6month_average = (b1+b2+b3+b4+b5+b6)/6 #四季平均
    #print(b9)
    b10 = latest_month_gain_loss = float((b1-b2)/abs(b2)) #最新一個月月增率
    #print(b10)

    if b9 < 0 or b1 < 0:
        result2 = "C"

    elif b1 < b2 < b3 and b9 > 0:
        result2 = "B"
        
    elif b1 or b2 or b3 or b4 or b5 or b6 < 0:
        result2 = "BB"
        
    elif b9 >= 0.1 and b10 >= 0:
        result2 = "A"     
        
    elif b9 >= 0.25 and b10 >= 0:
        result2 = "AA"

    else:
        result2 = "BB"

    return result2, RevN, Rev, b1N, b2N, b3N, b4N, b5N, b6N, b1, b2, b3, b4, b5, b6 
    #print (result1)
##############################################################


def stock_NetInc(stock_id): #(股票代碼, 股票名稱. 股票價格觸及下緣)
    sheet_type = 'z/zc/zcq/zcq_' #ISQ 合併損益表 季表
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))


    c1N = dfs[2][1][0] #最新1季的名稱
    c2N = dfs[2][2][0] #最新2季的名稱
    c3N = dfs[2][3][0] #最新3季的名稱
    c4N = dfs[2][4][0] #最新4季的名稱
    c5N = dfs[2][5][0] #最新5季的名稱
    c6N = dfs[2][6][0] #最新6季的名稱
    c7N = dfs[2][7][0] #最新7季的名稱
    c8N = dfs[2][8][0] #最新8季的名稱

    NetIncomeN = []
    NetIncomeN.extend([c1N,c2N,c3N,c4N,c5N,c6N,c7N,c8N])

#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][70] #最新1季的合併總損益 税後淨利
#print(dfs[2][1][11])
    c1 = float((dfs[2][1][70])) #最新1季的合併總損益 税後淨利
    c2 = float((dfs[2][2][70])) #最新2季的合併總損益 税後淨利
    c3 = float((dfs[2][3][70])) #最新3季的合併總損益 税後淨利
    c4 = float((dfs[2][4][70])) #最新4季的合併總損益 税後淨利
    c5 = float((dfs[2][5][70])) #最新5季的合併總損益 税後淨利
    c6 = float((dfs[2][6][70])) #最新6季的合併總損益 税後淨利
    c7 = float((dfs[2][7][70])) #最新7季的合併總損益 税後淨利
    c8 = float((dfs[2][8][70])) #最新8季的合併總損益 税後淨利
#print(c2)
    NetIncome = []
    NetIncome.extend([c1,c2,c3,c4,c5,c6,c7,c8])
#print(a1)
    c9 = latest_YoY = float((c1-c5)/abs(c5)) #最新一季年增率
#print(c9)
    c10 = second_latest_YoY = float((c2-c6)/abs(c6)) #次新一季年增率
#print(c10)
    c11 = third_YoY = float((c3-c7)/abs(c7)) #第3新一季年增率
    #print(c11)
    c12 = fourth_YoY = float((c4-c8)/abs(c8)) #第4新一季年增率
#print(c12)
#############計算負數的季數
    total = 0
    for n in [c1,c2,c3,c4]:
        if n < 0:
            total += 1
#print(total)
#################
    c13 = season_number_below0 = total
#print(c13)

    if c1 < 0 and c2 < 0:
        result3 = "C"

    elif c1 < 0 or c13 >= 2:
        result3 = "B"

    elif (c1 < c2 < c3) and (c9 < 0.5 or c10 < 0.5 or c11 < 0.5):
        result3 = "B" 

    elif c1 > 0 and c2 > 0 and (c1-c2)/abs(c2) < -0.5:
        result3 = "BB"
        
    elif c1 > 0 and c2 < 0 and c3 < 0 and c4 < 0:
        result3 = "BB"

    elif c1 > 0 and c2 > 0 and (c1-c2)/abs(c2) > -0.5:
        result3 = "A"

    elif c1 > 0 and c2 > 0 and c3 > 0 and c1 > c2: 
        result3 = "AA"
    
    elif c1 >= 0.5 and c2 >= 0.5 and c3 >= 0.5:
        result3 = "AA"

    #print (result3)

    return result3, NetIncomeN, NetIncome, c1N, c2N, c3N, c4N, c5N, c6N, c7N, c8N, c1, c2, c3, c4, c5, c6, c7, c8
###########################################################
def stock_EPS(stock_id):

    sheet_type = 'z/zc/zcq/zcq_' #ISQ 合併損益表 季表
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))


    d1N = dfs[2][1][0] #最新1季的名稱
    d2N = dfs[2][2][0] #最新2季的名稱
    d3N = dfs[2][3][0] #最新3季的名稱
    d4N = dfs[2][4][0] #最新4季的名稱
    d5N = dfs[2][5][0] #最新5季的名稱
    d6N = dfs[2][6][0] #最新6季的名稱
    d7N = dfs[2][7][0] #最新7季的名稱
    d8N = dfs[2][8][0] #最新8季的名稱

    EPSN = []
    EPSN.extend([d1N,d2N,d3N,d4N,d5N,d6N,d7N,d8N])


#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][98] #最新1季的合併總損益 每股盈餘
#dfs[2][1] #最新1季的合併總損益 税後淨利

#print (d1)

    d1 = float((dfs[2][1][98])) #最新1季的合併總損益 EPS
    d2 = float((dfs[2][2][98])) #最新2季的合併總損益 EPS
    d3 = float((dfs[2][3][98])) #最新3季的合併總損益 EPS
    d4 = float((dfs[2][4][98])) #最新4季的合併總損益 EPS
    d5 = float((dfs[2][5][98])) #最新5季的合併總損益 EPS
    d6 = float((dfs[2][6][98])) #最新6季的合併總損益 EPS
    d7 = float((dfs[2][7][98])) #最新7季的合併總損益 EPS
    d8 = float((dfs[2][8][98])) #最新8季的合併總損益 EPS

    EPS = []
    EPS.extend([d1,d2,d3,d4,d5,d6,d7,d8])

#print(EPS)

    d9 = latest_YoY = float((d1-d5)/abs(d5)) #最新一季年增率
#print(d9)
    d10 = second_YoY = float((d2-d6)/abs(d6)) #次新一季年增率
#print(d10)
    d11 = third_YoY = float((d3-d7)/abs(d7)) #第3新一季年增率
#print(d11)
    d12 = fourth_YoY = float((d4-d8)/abs(d8)) #第4新一季年增率
#print(d12)
    d13 = season4Sum = d1+d2+d3+d4
#print(d13)

    if d13 < 0:
        result4 = "C"

    elif d13 > 0 or d1 < 0:
        result4 = "B"

    elif d13 >= 1:
        result4 = "BB"

    elif d13 >= 3:
        result4 = "A"

    elif d13 > 5:
        result4 = "AA"

    #print (result4)
    return result4, EPSN, EPS, d1N, d2N, d3N, d4N, d5N, d6N, d7N, d8N, d1, d2, d3, d4, d5, d6, d7, d8
#, EPSN, EPS

##############################################################

def stock_InvTO(stock_id): #(股票代碼)
    
    ###MoneyDJ
    sheet_type = 'z/zc/zcr/zcr_' #FRQ 財務比率表 季
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))

#print(table)
#stock_id_name = dfs[2][1] #由左至右，第一欄數據

    e1N = dfs[2][1][1] #最新1季的名稱
    e2N = dfs[2][2][1] #最新2季的名稱
    e3N = dfs[2][3][1] #最新3季的名稱
    e4N = dfs[2][4][1] #最新4季的名稱
    e5N = dfs[2][5][1] #最新5季的名稱
    e6N = dfs[2][6][1] #最新6季的名稱
    e7N = dfs[2][7][1] #最新7季的名稱
    e8N = dfs[2][8][1] #最新8季的名稱

    InvTON = []
    InvTON.extend([e1N,e2N,e3N,e4N,e5N,e6N,e7N,e8N])
    
    e1 = float(dfs[2][1][52]) #由左至右，第1欄數據 存貨週轉率 Inventory_turnover
    e2 = float(dfs[2][2][52]) #由左至右，第2欄數據 存貨週轉率 Inventory_turnover
    e3 = float(dfs[2][3][52]) #由左至右，第3欄數據 存貨週轉率 Inventory_turnover
    e4 = float(dfs[2][4][52]) #由左至右，第4欄數據 存貨週轉率 Inventory_turnover
    e5 = float(dfs[2][5][52]) #由左至右，第5欄數據 存貨週轉率 Inventory_turnover
    e6 = float(dfs[2][6][52]) #由左至右，第6欄數據 存貨週轉率 Inventory_turnover
    e7 = float(dfs[2][7][52]) #由左至右，第7欄數據 存貨週轉率 Inventory_turnover
    e8 = float(dfs[2][8][52]) #由左至右，第8欄數據 存貨週轉率 Inventory_turnover

    InvTO = []
    InvTO.extend([e1,e2,e3,e4,e5,e6,e7,e8])

    e9 = latest_4season_average = float((e1+e2+e3+e4)/4) #四季平均
    e10 = latest_gain_loss = float((e1-e2)/e2) #最新一季漲跌幅
    e11 = second_gain_loss = float((e2-e3)/e3) #次新一季漲跌幅
    e12 = third_gain_loss = float((e3-e4)/e4) #前三季漲跌幅
    e13 = fourth_gain_loss = float((e4-e5)/e5) #前四季漲跌幅
    #print(e9)

    #print(InvTO)   

#
    if e10 < -0.2:
        result5 = "C"
      
    elif e11 < -0.2 or e12 < -0.2 or e13 < -0.2:
        result5 = "B"

    elif e11 < -0.2 and e12 < -0.2: 
        result5 = "BB"
        
    elif e11 < -0.2 and e13 < -0.2:
        result5 = "BB"
        
    elif e12 < -0.2 and e13 < -0.2:        
        result5 = "BB" 
        
    elif e10 < -0.2 and e11 < -0.2:
        result5 = "BB"    
    
    elif e10 < -0.2 and e12 < -0.2:
        result5 = "BB"
        
    elif e10 < -0.2 and e13 < -0.2:
        result5 = "BB"

    elif e9 < 1.5 and e10 > -0.2 and e11 > -0.2 and e12 > -0.2 and e13 > -0.2:
        result5 = "A"
       
    elif e9 > 1.5 and e10 > -0.2 and e11 > -0.2 and e12 > -0.2 and e13 > -0.2:
        result5 = "AA"

    else:
        result5 = "不評分"      

    return result5, InvTON, InvTO, e1N, e2N, e3N, e4N, e5N, e6N, e7N, e8N, e1, e2, e3, e4, e5, e6, e7, e8
##########################################################
def stock_Cashflow(stock_id): #(股票代碼, 股票名稱. 股票價格觸及下緣)
    sheet_type = 'z/zc/zc3/zc3_' #合併現金流量表 季表
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))

#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][54] #最新1季的合併現金流量 營運的現金流量
#dfs[2][1][70] #最新1季的合併現金流量 投資的現金流量

#print(dfs[2][1][11])
#print(dfs[2][1])

    f1N = dfs[2][1][0] #最新1季的名稱
    f2N = dfs[2][2][0] #最新2季的名稱
    f3N = dfs[2][3][0] #最新3季的名稱
    f4N = dfs[2][4][0] #最新4季的名稱
    f5N = dfs[2][5][0] #最新5季的名稱
    f6N = dfs[2][6][0] #最新6季的名稱
    f7N = dfs[2][7][0] #最新7季的名稱
    f8N = dfs[2][8][0] #最新8季的名稱

    CashFlowN = []
    CashFlowN.extend([f1N,f2N,f3N,f4N,f5N,f6N,f7N,f8N])
    

    f1 = int((dfs[2][1][54])) + int((dfs[2][1][70])) #最新1季的自由現金流量
    f2 = int((dfs[2][2][54])) + int((dfs[2][2][70])) #最新2季的自由現金流量
    f3 = int((dfs[2][3][54])) + int((dfs[2][3][70])) #最新3季的自由現金流量
    f4 = int((dfs[2][4][54])) + int((dfs[2][4][70])) #最新4季的自由現金流量
    f5 = int((dfs[2][5][54])) + int((dfs[2][5][70])) #最新5季的自由現金流量
    f6 = int((dfs[2][6][54])) + int((dfs[2][6][70])) #最新6季的自由現金流量
    f7 = int((dfs[2][7][54])) + int((dfs[2][7][70])) #最新7季的自由現金流量
    f8 = int((dfs[2][8][54])) + int((dfs[2][8][70])) #最新8季的自由現金流量

#print (f1)

    CashFlow = []
    CashFlow.extend([f1,f2,f3,f4,f5,f6,f7,f8])

#print(CashFlow)

    f9 = season4sum = f1+f2+f3+f4 #前4季總和
#print(d9)
    f10 = season6sum = f1+f2+f3+f4+f5+f6 #前6季總和
#print(d10)
    f11 = season8sum = f1+f2+f3+f4+f5+f6+f7+f8 #前8季總和
#print(d11)
    
    if f10 < 0:
        result6 = "C"

    elif f10 < 0:
        result6 = "B"

    elif f9 > 0:
        result6 = "BB"

    elif f10 > 0:
        result6 = "A"

    elif f1 > 0 and f2 > 0 and f3 > 0 and f4 > 0 and f5 > 0 and f6 > 0:
        result6 = "AA"

#print (result6)
    return result6, CashFlowN, CashFlow, f1N, f2N, f3N, f4N, f5N, f6N, f7N, f8N, f1, f2, f3, f4, f5, f6, f7, f8
   
##########################################################
######################################################以上為六大指標程式
######################################################以下為股價程式

import pandas as pd 
import requests
from bs4 import BeautifulSoup


#stock_id = "3034"

def stockdef(stock_id): #(股票代碼, 股票名稱. 股票價格觸及下緣)
    bank_url = 'http://dj.mybank.com.tw/' #國泰世華
    sheet_type = 'z/zc/zca/zca_' #基本資料
    ###MoneyDJ
    url = bank_url + sheet_type + stock_id +'.djhtm'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))

#print(table)
    #stock_id_name = dfs[2][0][0][:-24] #股票代號和名稱
    #stock_name = dfs[2][0][0][0:3] #股票名稱
    latest_trade_date = dfs[2][0][0][-13:-8] #最近交易日
    open = dfs[2][1][1] #開盤價
    high = dfs[2][3][1] #最高價
    low  = dfs[2][5][1] #最低價
    close  = dfs[2][7][1] #收盤價
    
    
    
    thisYearGain = dfs[2][1][7][:-2] #今年以來的漲幅
    #thisMonthGain = dfs[2][1][9] #這個月以來的漲幅 
    
############Mdj營收最新月份
    sheet_type = 'z/zc/zch/zch_' #Rev 營收   
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))

    #dfs[2] 真正表格
    #dfs[2][4] 營收年增率
    newest_Rev_month = dfs[2][0][6] #最新一個月的月份
################Mdj最新財報季份
    sheet_type = 'z/zc/zcr/zcr_' #FRQ 財務比率 季表
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))

#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][11] 最新一季營益率
#print(dfs[2][1][11])

    newest_Fin_Q = (dfs[2][1][1]) #最新1季的財報季份
    
    
########################Yahoo奇摩股市   
    
    url = 'https://tw.stock.yahoo.com/q/ts?s=' + stock_id
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))

    stock_id_name = dfs[0][1][3][:-8] #股票代號和名稱
    yahoo_tradePrice = dfs[0][3] #yahoo成交價
    yahoo_time= dfs[0][0] #yahoo成交時間
    yahoo_latest_tradePrice = dfs[0][3][6] #yahoo最新成交價
    yahoo_latest_time = dfs[0][0][6] #yahoo最新成交時間
    
    #hour = dfs[0][0][6][1:2]
    #minute = dfs[0][0][6][3:4]
    
    #new_yahoo_latest_time = hour + '：' + minute

    #print(yahoo_latest_time)
    #print(yahoo_latest_tradePrice)
    
    price4 = '開盤價：' + open  + '；' + '收盤價：' + close  + '；' + '最高價：' + high  + '；' + '最低價：' + low  + '。'
    

    
    stock_description = '☆' + stock_id_name + '。' + 'Mdj資料日期：' + latest_trade_date + '，' + price4 + '今年漲幅：' + thisYearGain + '％。' + '最新營收月份：' + newest_Rev_month + '，'  + '最新財報季數：' + newest_Fin_Q + '，' + 'Yh即時價：' +  str(yahoo_latest_tradePrice) + '。' + '即時時間：' +  str(yahoo_latest_time) + '。' 
    #print(stock_description)
    return stock_description, latest_trade_date, open, close, high, low, thisYearGain, newest_Rev_month, stock_id_name, yahoo_latest_tradePrice  

###########################################################
##############################################################
    
def stock6score(stock_id):  #由stock6改為stock6score 2020/5/7

    
         
    #前三個變數沿用之前的，後面為後來增修
    st1, dt1N, dt1, a1N, a2N, a3N, a4N, a5N, a6N, a7N, a8N, a1, a2, a3, a4, a5, a6, a7, a8 = stock_Prof(stock_id)
    #print('營益率指標為：' + st1) #營益率指標函數
 
    st2, dt2N, dt2, b1N, b2N, b3N, b4N, b5N, b6N, b1, b2, b3, b4, b5, b6 = stock_Rev(stock_id)  #營收指標函數
    #print('營收指標為：' + st2)
    
    st3, dt3N, dt3, c1N, c2N, c3N, c4N, c5N, c6N, c7N, c8N, c1, c2, c3, c4, c5, c6, c7, c8 = stock_NetInc(stock_id)
    #print('税後淨利指標為：' + st3) #税後淨利指標函數

    st4, dt4N, dt4, d1N, d2N, d3N, d4N, d5N, d6N, d7N, d8N, d1, d2, d3, d4, d5, d6, d7, d8 = stock_EPS(stock_id)  #EPS指標函數
    #print('EPS指標為：' + st4)

    st5, dt5N, dt5, e1N, e2N, e3N, e4N, e5N, e6N, e7N, e8N, e1, e2, e3, e4, e5, e6, e7, e8 = stock_InvTO(stock_id)  #存貨週轉率指標函數
    #print('存貨週轉率指標為：' + st5)
    
    st6, dt6N, dt6, f1N, f2N, f3N, f4N, f5N, f6N, f7N, f8N, f1, f2, f3, f4, f5, f6, f7, f8 = stock_Cashflow(stock_id)  #現金流量指標函數
    #print('現金流量指標為：' + st6)

##########計算六大指標平均    
    total = 0
    for i in [st1,st2,st3,st4,st5,st6]:
        if i == "AA":
            score = 4
        elif i == "A":
            score = 3
        elif i == "BB":
            score = 2
        elif i == "B":
            score = 1
        elif i == "C":
            score = 0
        total += score
    average6stock = str(round(int(total)/6,1))
##########計算六大指標平均    
    
    stock_description2 = '☆總大六大指標Mdj即時查詢評等☆' + '營益率指標為：' + st1 + '，' + '營收指標為：' + st2 + '，' + '税後淨利指標為：' + st3 + '，' + 'EPS指標為：' + st4 + '，' + '存貨週轉率指標為：' + st5 + '，' + '現金流量指標為：' + st6  + '，' + '六大指標平均為：' + average6stock  + '。' 
     #+ stock_id_name + '。'
    #print(stock_description)
    return stock_description2, average6stock

######################################################以上為股價程式



##################以下為本益比區間程式
def PERseg(stock_id):

    ######以下為判斷上市或上櫃，取得年度股價程式
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup    
    
    try:    #查詢上櫃年股價

        payload = {'input_stock_code': stock_id} #股價空格 要填入代號
# 將查詢參數加入 POST 請求中
        r = requests.post("https://www.tpex.org.tw/web/stock/statistics/monthly/st42.php?l=zh-tw", data=payload)
#print(html.text) #以json格式呈現

        soup = BeautifulSoup(r.content, 'lxml')
        table = soup.find_all('table')[2];
        dfs = pd.read_html(str(table))

        #print(dfs)

    #ls0 = lastyear1 = dfs[0].iloc[2] #當年 109年

        ls1 =  dfs[0].iloc[3] #108年
        ls2 =  dfs[0].iloc[4] #107年
        ls3 =  dfs[0].iloc[5] #106年
        ls4 =  dfs[0].iloc[6] #105年
        ls5 =  dfs[0].iloc[7] #104年

        H1 = ls1[4] #108年最高價
        L1 = ls1[6] #108年最低價

        H2 = ls2[4] #107年最高價
        L2 = ls2[6] #107年最低價

        H3 = ls3[4] #106年最高價
        L3 = ls3[6] #106年最低價

        H4 = ls4[4] #105年最高價
        L4 = ls4[6] #105年最低價

        H5 = ls5[4] #104年最高價
        L5 = ls5[6] #104年最低價
    
        #print(H5)
        #print(L5)
##########
    except:  #查詢上市年股價
        twse_url = 'http://www.twse.com.tw/exchangeReport/FMNPTK?response=html&stockNo=' #國泰世華
        url = twse_url + stock_id 
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'lxml')
        table = soup.find_all('table')[0];
        dfs = pd.read_html(str(table))

#xxx = dfs[0].iloc[-1,-5] #-1為最新年度 -5為最高價
#yyy = dfs[0].iloc[-1,-3] #-1為最新年度 -5為最高價
#zzz = dfs[0].iloc[-1] #最後一列 最新年度 所有資料
#xxx = lastyear1[0] #年度
#yyy = lastyear1[4] #最高價
#zzz = lastyear1[6] #最高價

        ls1  = dfs[0].iloc[-1] #108年
        ls2  = dfs[0].iloc[-2] #107年
        ls3  = dfs[0].iloc[-3] #106年
        ls4  = dfs[0].iloc[-4] #105年
        ls5  = dfs[0].iloc[-5] #104年

        H1 = ls1[4] #108年最高價
        L1 = ls1[6] #108年最低價

        H2 = ls2[4] #107年最高價
        L2 = ls2[6] #107年最低價

        H3 = ls3[4] #106年最高價
        L3 = ls3[6] #106年最低價

        H4 = ls4[4] #105年最高價
        L4 = ls4[6] #105年最低價

        H5 = ls5[4] #104年最高價
        L5 = ls5[6] #104年最低價

        #print(H5)
        #print(L5)


################################################取得EPS
#stock_id = "3034"
    bank_url = 'http://dj.mybank.com.tw/z/zc/zcq/zcq0.djhtm?b=Y&a=' #國泰世華
#sheet_type = 'z/zc/zcq/zcq_' #ISQ 合併損益表 季表

    url = bank_url + stock_id
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))

#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][98] #最新1年的合併總損益 每股盈餘

    eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2019
    eps2 = dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2018
    eps3 = dfs[2][3][98] #最新3年的合併總損益 每股盈餘 2017
    eps4 = dfs[2][4][98] #最新4年的合併總損益 每股盈餘 2017
    eps5 = dfs[2][5][98] #最新5年的合併總損益 每股盈餘 2015

    PER_H1 = round(float(H1)/float(eps1),2)  #107本益比 高
    PER_L1 = round(float(L1)/float(eps1),2)  #107本益比 低 

    PER_H2 = round(float(H2)/float(eps2),2)  #106本益比 高
    PER_L2 = round(float(L2)/float(eps2),2)  #106本益比 低 

    PER_H3 = round(float(H3)/float(eps3),2)  #105本益比 高
    PER_L3 = round(float(L3)/float(eps3),2)  #105本益比 低 

    PER_H4 = round(float(H4)/float(eps4),2)  #104本益比 高
    PER_L4 = round(float(L4)/float(eps4),2)  #104本益比 低 
    
    PER_H5 = round(float(H5)/float(eps5),2)  #103本益比 高
    PER_L5 = round(float(L5)/float(eps5),2)  #103本益比 低 

    PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3 + PER_H4 + PER_H5)/5),2)
    PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3 + PER_L4 + PER_L5)/5),2)


#print(PER_H1)

##############################################取得營收

    PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
    PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低


#print(PER_H)
#print(PER_L)

############################
    sheet_type = 'z/zc/zch/zch_' #Rev 營收
    #stock_id = "3034"
    bank_url = 'http://dj.mybank.com.tw/' #國泰世華
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))

    rYoY1N = dfs[2][0][6] #最新一個月名稱
    rYoY2N = dfs[2][0][7]
    rYoY3N = dfs[2][0][8]
    rYoY4N = dfs[2][0][9]
    rYoY5N = dfs[2][0][10]
    rYoY6N = dfs[2][0][11]

#目前2020/5/12
    rYoY1 = round(float(dfs[2][4][6][:-1])/100,4) #最新一個月年增率
    rYoY2 = round(float(dfs[2][4][7][:-1])/100,4)
    rYoY3 = round(float(dfs[2][4][8][:-1])/100,4)
    rYoY4 = round(float(dfs[2][4][9][:-1])/100,4)
    rYoY5 = round(float(dfs[2][4][10][:-1])/100,4)
    rYoY6 = round(float(dfs[2][4][11][:-1])/100,4)

    rYoY6Average  = (rYoY1+rYoY2+rYoY3+rYoY4+rYoY5+rYoY6)/6 #最新六個月營收平均
#print(rYoY6Average)

    RevYoY = round(min(rYoY6Average,rYoY1),4) #兩者擇一較低

    #return H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average 

#######以下開始預估未來一整年的營收

#print(RevYoY)
    
    r1N = dfs[2][0][6] #千元 改 億  #最新一個月營收的名稱 109/4
    r2N = dfs[2][0][7]  #109/3
    r3N = dfs[2][0][8]  #109/2
    r4N = dfs[2][0][9]  #109/1
    r5N = dfs[2][0][10]  #108/12
    r6N = dfs[2][0][11]  #108/11
    r7N = dfs[2][0][12]  #108/10
    r8N = dfs[2][0][13]  #108/9
    r9N = dfs[2][0][14]  #108/8
    r10N = dfs[2][0][15]  #108/7
    r11N = dfs[2][0][16]  #108/6
    r12N = dfs[2][0][17]  #108/5




#######



    r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 109/4
    r2 = int(dfs[2][1][7])/100000  #109/3
    r3 = int(dfs[2][1][8])/100000  #109/2
    r4 = int(dfs[2][1][9])/100000  #109/1
    


#print(r1)
    #r1_9Sum = Jan_Sep_Sum = r1+r2+r3+r4+r5+r6+r7+r8+r9 #今年1-9月營收
    r1_4Sum = Jan_Sep_Sum = r1+r2+r3+r4 #今年1-4月營收
#print(r1_9Sum)


    r5 = int(dfs[2][1][10])/100000  #108/12
    r6 = int(dfs[2][1][11])/100000  #108/11
    r7 = int(dfs[2][1][12])/100000  #108/10
    r8 = int(dfs[2][1][13])/100000  #108/9
    r9 = int(dfs[2][1][14])/100000  #108/8
    r10 = int(dfs[2][1][15])/100000  #108/7
    r11 = int(dfs[2][1][16])/100000  #108/6
    r12 = int(dfs[2][1][17])/100000  #108/5

    #r10_12Sum_Predict = (r10+r11+r12)*(1+RevYoY) #預估今年10-12月營收
    r5_12Sum_Predict = (r5+r6+r7+r8+r9+r10+r11+r12)*(1+RevYoY) #預估今年10-12月營收

#print(r10_12Sum_Predict)

    Rev_Predict = round(r1_4Sum + r5_12Sum_Predict, 4) #預估今年全年營收

#print(Rev_Predict)

##################################取得稅後淨利率

    bank_url = 'http://dj.mybank.com.tw/' #國泰世華
    sheet_type = 'z/zc/zcr/zcr_' #FRQ 財務比率 季表

    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))

#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][13] 最新一季稅後淨利率
    Net1N = dfs[2][1][1] #最新1季的稅後淨利率名稱
    Net2N = dfs[2][2][1] #最新1季的稅後淨利率名稱
    Net3N = dfs[2][3][1] #最新1季的稅後淨利率名稱
    Net4N = dfs[2][4][1] #最新1季的稅後淨利率名稱


    Net1 = round(float((dfs[2][1][12]))/100,4) #最新1季的稅後淨利率
    Net2 = round(float((dfs[2][2][12]))/100,4) #最新1季的稅後淨利率
    Net3 = round(float((dfs[2][3][12]))/100,4) #最新1季的稅後淨利率
    Net4 = round(float((dfs[2][4][12]))/100,4) #最新1季的稅後淨利率

    Net4Average = (Net1+Net2+Net3+Net4)/4

#print(Net4Average)

###############預估 淨利 EPS
    Net_Predict = round(Rev_Predict*Net4Average,6)

#print(Net_Predict)

################取得股本
    bank_url = 'http://dj.mybank.com.tw/' #國泰世華
    sheet_type = 'z/zc/zca/zca_' #基本資料

    url = bank_url + sheet_type + stock_id +'.djhtm'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))

#print(table)
#stock_id_name = dfs[2][0][0][:-24] #股票代號和名稱
    #stock_name = dfs[2][0][0][0:3] #股票名稱
#latest_trade_date = dfs[2][0][0][-13:-8] #最近交易日
#open = dfs[2][1][1] #開盤價
#high = dfs[2][3][1] #最高價
#low  = dfs[2][5][1] #最低價
#close  = dfs[2][7][1] #收盤價
    capital_stock = float(dfs[2][1][13]) #Basic表股本 單位：億
#print(capital_stock)
####################計算預估EPS
    Predict_EPS = round(Net_Predict/capital_stock*10,2)
#print(Predict_EPS)

    Predict_high_price = round(Predict_EPS*PER_H,2)
    Predict_low_price = round(Predict_EPS*PER_L,2)

#print(Predict_high_price)  #預估股價高點
#print(Predict_low_price)  #預估股價低點
########################取得目前股價
#    url = 'https://tw.stock.yahoo.com/q/ts?s=' + stock_id
#    r = requests.get(url)
#    soup = BeautifulSoup(r.content, 'html.parser')
#    table = soup.find_all('table')[0];
#    dfs = pd.read_html(str(table))

#    yahoo_tradePriceX = float(dfs[0][3][6]) #yahoo成交價
    #print(yahoo_tradePrice)
##################

    url = 'https://tw.stock.yahoo.com/q/ts?s=' + stock_id
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))


#    yahoo_tradePrice = dfs[0][3] #yahoo成交價
#    yahoo_time= dfs[0][0] #yahoo成交時間
    yahoo_latest_tradePrice = float(dfs[0][3][6]) #yahoo最新成交價
#    yahoo_latest_time = dfs[0][0][6] #yahoo最新成交時間    
    
    
##############    

    up_profit = round((Predict_high_price - yahoo_latest_tradePrice)/yahoo_latest_tradePrice,2)
    down_loss = round((Predict_low_price - yahoo_latest_tradePrice)/yahoo_latest_tradePrice,2)

#print(up_profit)
#print(down_loss)

    New_up_profit = str(up_profit*100) + '%'
    New_down_loss = str(down_loss*100) + '%'

#print(New_up_profit)
#print(New_down_loss)

    risk_reward = round(up_profit/down_loss,2)

    #print(risk_reward)
    #stock_description3 = '☆本益比區間快速查詢☆' + 'Yh即時價為：' + str(yahoo_latest_tradePrice) + '，' + '預估高點為：' + str(Predict_high_price) + '，'  + '預估低點為：' + str(Predict_low_price) + '，' + '預估利潤為：' + str(New_up_profit) + '，' + '可能損失為：' + str(New_down_loss) + '，' + '風險報酬倍數為：' + str(risk_reward) + '。' 
     #+ stock_id_name + '。'

    #print(stock_description3)
    return H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, up_profit, down_loss, risk_reward
########################test
def stock_detail(stock_id):
    
    url = 'https://tw.stock.yahoo.com/q/ts?s=' + stock_id
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))

    stock_id_name = dfs[0][1][3][:-8] #股票代號和名稱
    
    st1, dt1N, dt1 = stock_Prof(stock_id)
    #print('營益率指標為：' + st1) #營益率指標函數
    st2, dt2N, dt2 = stock_Rev(stock_id)  #營收指標函數
    #print('營收指標為：' + st2)
    st3, dt3N, dt3 = stock_NetInc(stock_id)
    #print('税後淨利指標為：' + st3) #税後淨利指標函數
    st4, dt4N, dt4 = stock_EPS(stock_id)  #EPS指標函數
    #print('EPS指標為：' + st4)
    st5, dt5N, dt5 = stock_InvTO(stock_id)  #存貨週轉率指標函數
    #print('存貨週轉率指標為：' + st5)
    st6, dt6N, dt6 = stock_Cashflow(stock_id)  #現金流量指標函數
    #print('現金流量指標為：' + st6)
    



    stock_description4 = stock_id_name + '。' + '☆總大六大指標細節☆' + '營益率詳細為：' + str(dt1N) + str(dt1) + '；營收詳細為：' + str(dt2N) + str(dt2) + '；稅後淨利詳細為：' + str(dt3N) + str(dt3) + '；EPS詳細為：' + str(dt4N) + str(dt4) + '；存貨周轉率詳細為：' + str(dt5N) + str(dt5) + '；自由現金流量詳細為：' + str(dt6N) + str(dt6) + '。'
    #+ '，' + '營收指標為：' + st2 + '，' + '税後淨利指標為：' + st3 + '，' + 'EPS指標為：' + st4 + '，' + '存貨週轉率指標為：' + st5 + '，' + '現金流量指標為：' + st6  + '，' + '六大指標平均為：' + average6stock  + '。' 

    return stock_description4

