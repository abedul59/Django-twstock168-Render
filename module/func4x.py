# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 08:15:54 2020

@author: PCUSER
"""
bank_url = 'https://djinfo.cathaysec.com.tw/'


a = 'https://www.google.com.tw'
b = 'https://tw.yahoo.com'
c = 'https://www.pchome.com.tw/'
d = 'https://djinfo.cathaysec.com.tw/'

import random
my_Referer = random.choice([a,b,c])

my_UserAgent = 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'

def EPSach(stock_id):


    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup    
    
    
    #取得股票名
    bank_url0 = 'http://jdata.yuanta.com.tw/' #國泰世華
    sheet_type = 'z/zc/zca/zca_' #基本資料
    ###MoneyDJ
    url = bank_url0 + sheet_type + stock_id +'.djhtm'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs0 = pd.read_html(str(table))

#print(table)
    #stock_id_name = dfs[2][0][0][:-24] #股票代號和名稱
    stock_name = dfs0[2][0][0][0:3] #股票名稱
    test = stock_name.endswith('(')
    if test == True:
        stock_name = dfs0[2][0][0][0:2]
    else:
        stock_name = dfs0[2][0][0][0:3]
        
        stock_name = stock_name.strip()  #有的股票右側會殘留空格
        
        
    #年表
    bank_url = 'http://jdata.yuanta.com.tw/z/zc/zcq/zcq0.djhtm?b=Y&a=' #國泰世華
#sheet_type = 'z/zc/zcq/zcq_' #ISQ 合併損益表 季表

    url = bank_url + stock_id
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))

#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][98] #最新1年的合併總損益 每股盈餘

    eps1 = str(dfs[2][1][98]) #最新1年的合併總損益 每股盈餘 2019
    #eps2 = dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2018
    #eps3 = dfs[2][3][98] #最新3年的合併總損益 每股盈餘 2017
    #eps4 = dfs[2][4][98] #最新4年的合併總損益 每股盈餘 2017
    #eps5 = dfs[2][5][98] #最新5年的合併總損益 每股盈餘 2015
        
    #季表    
    bank_url2 = 'http://jdata.yuanta.com.tw/z/zc/zcq/zcq0.djhtm?b=Q&a=' #國泰世華
#sheet_type = 'z/zc/zcq/zcq_' #ISQ 合併損益表 季表

    url = bank_url2 + stock_id
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs2 = pd.read_html(str(table))


    epsq1N = str(dfs2[2][1][0]) #總損益 Q2每股盈餘 2021
    
    epsq1 = str(dfs2[2][1][98]) #總損益 Q2每股盈餘 2021
    epsq2 = str(dfs2[2][2][98]) #總損益 Q1每股盈餘 2021
    epsq3 = str(dfs2[2][3][98]) #總損益 Q3每股盈餘 2021
    epsAchieveRate = str(round((float(epsq1) + float(epsq2))/float(eps1),4)*100)+'%'
    #+'%'
    
    return eps1, epsq1, epsAchieveRate, stock_name, epsq2, epsq3, epsq1N




def StockCap(stock_id):   #計算股本變動


    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup    
    
    #http://dj.mybank.com.tw/z/zc/zcp/zcpa.djhtm?a=2330&b=1&c=Y
    #取得股票名
    bank_url0 = 'http://jdata.yuanta.com.tw/' #國泰世華
    sheet_type = 'z/zc/zca/zca_' #基本資料
    ###MoneyDJ
    url = bank_url0 + sheet_type + stock_id +'.djhtm'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs0 = pd.read_html(str(table))

#print(table)
    #stock_id_name = dfs[2][0][0][:-24] #股票代號和名稱
    stock_name = dfs0[2][0][0][0:3] #股票名稱
    test = stock_name.endswith('(')
    if test == True:
        stock_name = dfs0[2][0][0][0:2]
    else:
        stock_name = dfs0[2][0][0][0:3]
        
        stock_name = stock_name.strip()  #有的股票右側會殘留空格
        
        
    bank_url0 = 'http://jdata.yuanta.com.tw/' #國泰世華
    sheet_type = 'z/zc/zcp/zcpa_' #資產負債表
    ###MoneyDJ
    url = bank_url0 + sheet_type + stock_id +'.djhtm'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
        #table = soup.find_all('table')[0];
    table2 = soup.find_all(class_ = 'table-row') 
    #print(table2)
  
    xCap = table2[-14].text
    xCapList = xCap.split("\n")


    print(xCapList)

    cap1 = round(float(xCapList[2].replace(",", ""))/100,2) #最新一季股本（單位：百萬） 2020/7/4 要轉換成 億
    cap2 = round(float(xCapList[3].replace(",", ""))/100,2) #最新一季股本（單位：百萬） 2020/7/4 要轉換成 億
    cap3 = round(float(xCapList[4].replace(",", ""))/100,2) #最新一季股本（單位：百萬） 2020/7/4 要轉換成 億
    cap4 = round(float(xCapList[5].replace(",", ""))/100,2) #最新一季股本（單位：百萬） 2020/7/4 要轉換成 億
    cap5 = round(float(xCapList[6].replace(",", ""))/100,2) #最新一季股本（單位：百萬） 2020/7/4 要轉換成 億
    cap6 = round(float(xCapList[7].replace(",", ""))/100,2) #最新一季股本（單位：百萬） 2020/7/4 要轉換成 億
    cap7 = round(float(xCapList[8].replace(",", ""))/100,2) #最新一季股本（單位：百萬） 2020/7/4 要轉換成 億
    cap8 = round(float(xCapList[9].replace(",", ""))/100,2) #最新一季股本（單位：百萬） 2020/7/4 要轉換成 億


    #cap1 = int(dfs[2][1][80]) #最新一季股本（單位：百萬）
    #cap2 = int(dfs[2][2][80]) 
    #cap3 = int(dfs[2][3][80])
    #cap4 = int(dfs[2][4][80])
    #cap5 = int(dfs[2][5][80]) 
    #cap6 = int(dfs[2][6][80])
    #cap7 = int(dfs[2][7][80])
    #cap8 = int(dfs[2][8][80])
    
    latest_cap_YoY = str(round((cap1-cap5)/cap5,4)*100)+'%' 
    latest_cap_MoM = str(round((cap1-cap2)/cap2,4)*100)+'%'
        

    #+'%'
    
    return stock_name, cap1, cap2, cap3, cap4, cap5, cap6, cap7, cap8, latest_cap_YoY, latest_cap_MoM
    
    
    
def EPSnProfit(stock_id):
    
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup
    import random
    
    ################取得EPS
    #亂數抉擇銀行網址，避免封鎖
    headers = {'Referer':my_Referer,'user-agent': my_UserAgent}
    
    sheet_type = 'z/zc/zcq/zcq_' #ISQ 合併損益表 季表
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    #table = soup.find_all('table')[0];
    table2 = soup.find_all(class_ = 'table-row')   
    
    xEPS = table2[-9].text    
    xEPSList = xEPS.split("\n")
    
    print(xEPSList) 

#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][98] #最新1年的合併總損益 每股盈餘

    eps1 = float((xEPSList[2])) #最新1季的合併總損益 每股盈餘 
    eps2 = float((xEPSList[3])) #最新2季的合併總損益 每股盈餘 
    eps3 = float((xEPSList[4])) #最新3季的合併總損益 每股盈餘 
    eps4 = float((xEPSList[5])) #最新4季的合併總損益 每股盈餘 
    eps5 = float((xEPSList[6])) #最新5季的合併總損益 每股盈餘 
    eps6 = float((xEPSList[7])) #最新5季的合併總損益 每股盈餘
    eps7 = float((xEPSList[8])) #最新5季的合併總損益 每股盈餘
    eps8 = float((xEPSList[9])) #最新5季的合併總損益 每股盈餘
    
    epsGroup = [float(eps1), float(eps2), float(eps3), float(eps4), float(eps5), float(eps6), float(eps7), float(eps8)]

    eps8max = str(max(epsGroup))  #得到這八季最高值
    
    if (float(eps1) == float(eps8max)):
        epsNewHigh = 'Yes'
    else:
        epsNewHigh = 'No'
    
    #print(eps8max)
    
    
    ################取得營業利益率    

    headers = {'Referer':my_Referer,'user-agent': my_UserAgent}
    sheet_type = 'z/zc/zcr/zcr_' #FRQ 財務比率 季表
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    #url = bank_url_A  + sheet_type + stock_id + '.djhtm'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    #table = soup.find_all('table')[0];
    table2 = soup.find_all(class_ = 'table-row')   
    
    xYearSeasonTitle = table2[0].text
    xYearSeasonTitleList = xYearSeasonTitle.split("\n")

    xProfit = table2[9].text
    xProfitList = xProfit.split("\n")

    
    #print(table2)
    #print(len(table2))
    #print(xYearSeasonTitleList)
    #print(table2[9])

    #newest_Fin_Q = xYearSeasonTitleList[2] #最新1季的財報季份
#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][13] 最新一季稅後淨利率
    Prof1N = xYearSeasonTitleList[2]  #最新1季的營業利益率名稱
    Prof2N = xYearSeasonTitleList[3]  #最新2季的營業利益率名稱
    Prof3N = xYearSeasonTitleList[4]  #最新3季的營業利益率名稱
    Prof4N = xYearSeasonTitleList[5]  #最新4季的營業利益率名稱
    Prof5N = xYearSeasonTitleList[6]  #最新4季的營業利益率名稱
    Prof6N = xYearSeasonTitleList[7]  #最新4季的營業利益率名稱
    Prof7N = xYearSeasonTitleList[8]  #最新4季的營業利益率名稱
    Prof8N = xYearSeasonTitleList[9]  #最新4季的營業利益率名稱
    
    Prof1 = float(xProfitList[2])  #最新1季的營業利益率
    Prof2 = float(xProfitList[3])  #最新1季的營業利益率
    Prof3 = float(xProfitList[4])  #最新1季的營業利益率
    Prof4 = float(xProfitList[5])  #最新1季的營業利益率
    Prof5 = float(xProfitList[6]) #最新1季的營業利益率
    Prof6 = float(xProfitList[7])  #最新1季的營業利益率
    Prof7 = float(xProfitList[8])  #最新1季的營業利益率
    Prof8 = float(xProfitList[9])  #最新1季的營業利益率

    
    pProf1 = str(Prof1) +'%'
    pProf2 = str(Prof2) +'%'
    pProf3 = str(Prof3) +'%'
    pProf4 = str(Prof4) +'%'
    pProf5 = str(Prof5) +'%'
    pProf6 = str(Prof6) +'%'
    pProf7 = str(Prof7) +'%'
    pProf8 = str(Prof8) +'%'
    
    


    #Net4Average = (Net1+Net2+Net3+Net4)/4
    
    #pNet4Average = str(round(Net4Average*100,2))+'%'
    
    ProfGroup = [Prof1, Prof2, Prof3, Prof4, Prof5, Prof6, Prof7, Prof8]
    
    Prof8max = str(max(ProfGroup))
    
    if (Prof1 == float(Prof8max)):
        ProfNewHigh = 'Yes'
    else:
        ProfNewHigh = 'No'    
    
    #print(Prof8max)
    
    
    ################取得股票名稱
    bank_url0 = 'http://jdata.yuanta.com.tw/' #國泰世華
    sheet_type = 'z/zc/zca/zca_' #基本資料
    ###MoneyDJ
    url = bank_url0 + sheet_type + stock_id +'.djhtm'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs0 = pd.read_html(str(table))

#print(table)
    #stock_id_name = dfs[2][0][0][:-24] #股票代號和名稱
    stock_name = dfs0[2][0][0][0:3] #股票名稱
    test = stock_name.endswith('(')
    if test == True:
        stock_name = dfs0[2][0][0][0:2]
    else:
        stock_name = dfs0[2][0][0][0:3]
        
        stock_name = stock_name.strip()  #有的股票右側會殘留空格
    
    return eps1, eps2, eps3, eps4, eps5, eps6, eps7, eps8, Prof1N, Prof2N, Prof3N, Prof4N, Prof5N, Prof6N, Prof7N, Prof8N, Prof1, Prof2, Prof3, Prof4, Prof5, Prof6, Prof7, Prof8, pProf1, pProf2, pProf3, pProf4, pProf5, pProf6, pProf7, pProf8, eps8max, Prof8max, stock_name, epsNewHigh, ProfNewHigh


def InstituRate(stock_id):

    #籌碼安定度： 大戶 = 董監+法人持股總數佔股本比例
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup
    import random    
    
    #url_pool = ['http://dj.mybank.com.tw','http://jdata.yuanta.com.tw','http://jsjustweb.jihsun.com.tw','http://stockchannel.sinotrade.com.tw','http://www.emega.com.tw','http://djfubonholdingfund.fbs.com.tw','http://stocks.ftsi.com.tw','http://www.esunsec.com.tw','http://tcfhcsec.moneydj.com','http://kgieworld.moneydj.com','http://pscnetinvest.moneydj.com','http://web.tcsc.com.tw','http://just.honsec.com.tw','http://ycsc.moneydj.com','http://easyfun.concords.com.tw','http://just2.entrust.com.tw','http://newjust.masterlink.com.tw','http://jsinfo.wls.com.tw','http://stock.capital.com.tw']

    #url_chosen = random.choice(url_pool)
    
    #bank_url0 = url_chosen       
    #取得股票名
    bank_url0 = 'http://jdata.yuanta.com.tw/' #國泰世華
    sheet_type = 'z/zc/zca/zca_' #基本資料
    ###MoneyDJ
    url = bank_url0 + sheet_type + stock_id +'.djhtm'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs0 = pd.read_html(str(table))

#print(table)
    #stock_id_name = dfs[2][0][0][:-24] #股票代號和名稱
    stock_name = dfs0[2][0][0][0:3] #股票名稱
    test = stock_name.endswith('(')
    if test == True:
        stock_name = dfs0[2][0][0][0:2]
    else:
        stock_name = dfs0[2][0][0][0:3]
        
        stock_name = stock_name.strip()  #有的股票右側會殘留空格
        


#####################籌碼分佈        


    bank_url2 = 'http://jdata.yuanta.com.tw/' #國泰世華
    sheet_type = 'z/zc/zcj/zcj_' #籌碼分佈 

    url = bank_url2 + sheet_type + stock_id + '.djhtm'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))
    table = dfs[3]
    
    pBoard = table[3].iloc[2]  #董監持股，有百分比
    pForeign = table[3].iloc[3]  #外資持股
    pInvest = table[3].iloc[4]  #投信持股
    pSecurity = table[3].iloc[5]  #自營商持股

    Board = float(table[3].iloc[2][:-1])  #董監持股，去百分比
    Foreign = float(table[3].iloc[3][:-1])  #外資持股
    Invest = float(table[3].iloc[4][:-1])  #投信持股
    Security = float(table[3].iloc[5][:-1])  #自營商持股

    Big = Board + Foreign + Invest + Security #大戶比率
    Indiv = round(100 - Big,2)
    
    pBig = str(Big) + '%'
    pIndiv = str(Indiv) + '%' 

    print(pBig)    
    print(pIndiv)
    
    return stock_name, pBoard, pForeign, pInvest, pSecurity, pBig, pIndiv


def Dividend(stock_id):

    #籌碼安定度： 大戶 = 董監+法人持股總數佔股本比例
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup
    #import random    
    
    #url_pool = ['http://dj.mybank.com.tw','http://jdata.yuanta.com.tw','http://jsjustweb.jihsun.com.tw','http://stockchannel.sinotrade.com.tw','http://www.emega.com.tw','http://djfubonholdingfund.fbs.com.tw','http://stocks.ftsi.com.tw','http://www.esunsec.com.tw','http://tcfhcsec.moneydj.com','http://kgieworld.moneydj.com','http://pscnetinvest.moneydj.com','http://web.tcsc.com.tw','http://just.honsec.com.tw','http://ycsc.moneydj.com','http://easyfun.concords.com.tw','http://just2.entrust.com.tw','http://newjust.masterlink.com.tw','http://jsinfo.wls.com.tw','http://stock.capital.com.tw']

    #url_chosen = random.choice(url_pool)
    
    #bank_url0 = url_chosen       
    #取得股票名
    bank_url0 = 'http://jdata.yuanta.com.tw/' #國泰世華
    sheet_type = 'z/zc/zca/zca_' #基本資料
    ###MoneyDJ
    url = bank_url0 + sheet_type + stock_id +'.djhtm'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs0 = pd.read_html(str(table))

#print(table)
    #stock_id_name = dfs[2][0][0][:-24] #股票代號和名稱
    stock_name = dfs0[2][0][0][0:3] #股票名稱
    test = stock_name.endswith('(')
    if test == True:
        stock_name = dfs0[2][0][0][0:2]
    else:
        stock_name = dfs0[2][0][0][0:3]
        
        stock_name = stock_name.strip()  #有的股票右側會殘留空格
        


#####################籌碼分佈        
#https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2002
#https://medium.com/pythonstock/%E5%8F%B0%E7%81%A3%E8%82%A1%E5%B8%82%E8%B3%87%E8%A8%8A%E7%B6%B2-post%E7%88%AC%E8%9F%B2%E5%A4%A7%E5%85%AC%E9%96%8B-%E9%99%84-python%E7%A8%8B%E5%BC%8F%E7%A2%BC-e296238f9ef4
    if (stock_id == '2330'): #2330有分季的股利表格
        
        bank_url2 = 'https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=' #國泰世華
    #sheet_type = 'z/zc/zcj/zcj_' #籌碼分佈 
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
        url = bank_url2 + stock_id
        r = requests.post(url, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        table = soup.find_all('table');
        dfs = pd.read_html(str(table))
    #stab2017 = dfs[-2].iloc[3]  #2017
    #stab2019 = dfs[-2].iloc[1]  #2019    
    #stab2019name = dfs[-2].iloc[1].iloc[0]  #2019名稱 
        x2020div = float(dfs[-2].iloc[1].iloc[6])  #2020股票股利
        
        x2019div = float(dfs[-2].iloc[6].iloc[6])  #2019股票股利
        x2018div = float(dfs[-2].iloc[10].iloc[6])  #2018股票股利 
        x2017div = float(dfs[-2].iloc[11].iloc[6])  #2017股票股利 
        x2016div = float(dfs[-2].iloc[12].iloc[6])  #2016股票股利 
        x2015div = float(dfs[-2].iloc[13].iloc[6])  #2015股票股利
        #x2014div = float(dfs[-2].iloc[14].iloc[6])  #2014股票股利
        
        #x2021div = float(dfs[-2].iloc[0].iloc[6])  #2021股票股利
        
        s2020div = float(dfs[-2].iloc[1].iloc[3])  #2020現金股利        
        
        s2019div = float(dfs[-2].iloc[6].iloc[3])  #2019現金股利
        s2018div = float(dfs[-2].iloc[10].iloc[3])  #2018現金股利 
        s2017div = float(dfs[-2].iloc[11].iloc[3])  #2017現金股利 
        s2016div = float(dfs[-2].iloc[12].iloc[3])  #2016現金股利 
        s2015div = float(dfs[-2].iloc[13].iloc[3])  #2015現金股利
        #s2014div = float(dfs[-2].iloc[14].iloc[3])  #2014現金股利
        
        #s2021div = float(dfs[-2].iloc[0].iloc[3])  #2021現金股利
    
        return stock_name, s2020div, s2019div, s2018div, s2017div, s2016div, s2015div, x2020div, x2019div, x2018div, x2017div, x2016div, x2015div#, x2014div, s2014div
              
        
        
    else: 
        bank_url2 = 'https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=' #國泰世華
    #sheet_type = 'z/zc/zcj/zcj_' #籌碼分佈 
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
        url = bank_url2 + stock_id
        r = requests.post(url, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        table = soup.find_all('table');
        dfs = pd.read_html(str(table))
    #stab2017 = dfs[-2].iloc[3]  #2017
    #stab2019 = dfs[-2].iloc[1]  #2019    
    #stab2019name = dfs[-2].iloc[1].iloc[0]  #2019名稱 

        x2019div = float(dfs[-2].iloc[2].iloc[6])  #2019股票股利
        x2018div = float(dfs[-2].iloc[3].iloc[6])  #2018股票股利 
        x2017div = float(dfs[-2].iloc[4].iloc[6])  #2017股票股利 
        x2016div = float(dfs[-2].iloc[5].iloc[6])  #2016股票股利 
        x2015div = float(dfs[-2].iloc[6].iloc[6])  #2015股票股利
        #x2014div = float(dfs[-2].iloc[7].iloc[6])  #2014股票股利
        
        x2020div = float(dfs[-2].iloc[1].iloc[6])  #2020股票股利
        #x2021div = float(dfs[-2].iloc[0].iloc[6])  #2021股票股利


        s2019div = float(dfs[-2].iloc[2].iloc[3])  #2019現金股利
        s2018div = float(dfs[-2].iloc[3].iloc[3])  #2018現金股利 
        s2017div = float(dfs[-2].iloc[4].iloc[3])  #2017現金股利 
        s2016div = float(dfs[-2].iloc[5].iloc[3])  #2016現金股利 
        s2015div = float(dfs[-2].iloc[6].iloc[3])  #2015現金股利
        #s2014div = float(dfs[-2].iloc[7].iloc[3])  #2014現金股利
        
        s2020div = float(dfs[-2].iloc[1].iloc[3])  #2020現金股利
        #s2021div = float(dfs[-2].iloc[0].iloc[3])  #2021現金股利
    
        return stock_name, s2020div, s2019div, s2018div, s2017div, s2016div, s2015div, x2020div, x2019div, x2018div, x2017div, x2016div, x2015div#, x2014div, s2014div


'''
什麼是還原股價?

 就是 現金股利 及股票股利 加回

公司去年有賺錢的話, 今年會以 股票股利 或 現金股利

的方式發放給股東

因此每年公司發放股利的前一天稱為 除權息

而將股利加回來，就是還原股價

計算方式如下:

例如100元的股價

現金股利2元

股票股利3元

除權後股價:(100-2)/1.3=75.4

還原權值就是:75.4*1.3+2=100
'''