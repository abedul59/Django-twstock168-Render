# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 17:04:20 2021

@author: pcuser
"""

import random

#from func3_eps import EPS_quarterlyGetter
a = 'https://www.google.com.tw'
b = 'https://tw.yahoo.com'
c = 'https://www.pchome.com.tw/'
d = 'https://dj.mybank.com.tw/'

my_Referer = random.choice([a,b,c,d])

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

def PERsegStable(stock_id):

    ######以下為判斷上市或上櫃，取得年度股價程式
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup    
    
    try:    #查詢上櫃年股價，失敗就換查上市股票

        payload = {'input_stock_code': stock_id} #股價空格 要填入代號
# 將查詢參數加入 get 請求中
        r = requests.post("https://www.tpex.org.tw/web/stock/statistics/monthly/st42.php?l=zh-tw", data=payload)
#print(html.text) #以json格式呈現

        soup = BeautifulSoup(r.content, 'lxml')
        table = soup.find_all('table')[2];
        dfs = pd.read_html(str(table))

        #print(dfs)

    #ls0 = lastyear1 = dfs[0].iloc[2] #當年 110年
        #ls0 =  dfs[0].iloc[2] #當年 110年

        ls1  = dfs[0].iloc[-1] #2020/109年
        ls2  = dfs[0].iloc[-2] #2019/108年
        ls3  = dfs[0].iloc[-3] #107年
        ls4  = dfs[0].iloc[-4] #106年
        ls5  = dfs[0].iloc[-5] #105年
        ls6  = dfs[0].iloc[-6] #104年        

        H1 = ls1[4] #109年最高價
        L1 = ls1[6] #109年最低價

        H2 = ls2[4] #2019/108年最高價
        L2 = ls2[6] #108年最低價

        H3 = ls3[4] #107年最高價
        L3 = ls3[6] #107年最低價

        H4 = ls4[4] #106年最高價
        L4 = ls4[6] #106年最低價

        H5 = ls5[4] #105年最高價
        L5 = ls5[6] #105年最低價

        H6 = ls6[4] #104年最高價
        L6 = ls6[6] #104年最低價
    
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



        ls1  = dfs[0].iloc[-1] #2020/109年
        ls2  = dfs[0].iloc[-2] #108年
        ls3  = dfs[0].iloc[-3] #107年
        ls4  = dfs[0].iloc[-4] #106年
        ls5  = dfs[0].iloc[-5] #105年

        H1 = ls1[4] #109年最高價
        L1 = ls1[6] #109年最低價

        H2 = ls2[4] #108年最高價
        L2 = ls2[6] #108年最低價

        H3 = ls3[4] #107年最高價
        L3 = ls3[6] #107年最低價

        H4 = ls4[4] #106年最高價
        L4 = ls4[6] #106年最低價

        H5 = ls5[4] #105年最高價
        L5 = ls5[6] #105年最低價

        #print(H5)
        #print(L5)
        '''        
        ##抓取上市今年最高價 一個月一個月抓，再算最大值
        twse_url2 = 'http://www.twse.com.tw/exchangeReport/FMSRFK?response=html&stockNo=' 
        url = twse_url2 + stock_id 
        r2 = requests.get(url)
        soup2 = BeautifulSoup(r2.content, 'lxml')
        table2 = soup2.find_all('table')[0];
        dfs2 = pd.read_html(str(table2))

        monthlen = len(dfs2[0]) #計算有幾個欄位（幾個月份）
    #dfs[0].iloc[m-1] #109年1月
        priceGroup = []

#try:      
        lm1  = dfs2[0].iloc[int(monthlen)-1][2] #109年最新的1個月最高價
        priceGroup.append(lm1)
        lm2  = dfs2[0].iloc[int(monthlen)-2][2] #109年最新的2個月最高價
        priceGroup.append(lm2)    
        lm3  = dfs2[0].iloc[int(monthlen)-3][2] #109年最新的3個月最高價
        priceGroup.append(lm3)
        lm4  = dfs2[0].iloc[int(monthlen)-4][2] #109年最新的4個月最高價
        priceGroup.append(lm4)
        lm5  = dfs2[0].iloc[int(monthlen)-5][2] #109年最新的5個月最高價
        priceGroup.append(lm5)
        lm6  = dfs2[0].iloc[int(monthlen)-6][2] #109年最新的6個月最高價
        priceGroup.append(lm6)
        lm7  = dfs2[0].iloc[int(monthlen)-7][2] #109年最新的7個月最高價
        priceGroup.append(lm7)
        lm8  = dfs2[0].iloc[int(monthlen)-8][2] #109年最新的8個月最高價
        priceGroup.append(lm8)
        lm9  = dfs2[0].iloc[int(monthlen)-9][2] #109年最新的9個月最高價
        priceGroup.append(lm9)
        lm10  = dfs2[0].iloc[int(monthlen)-10][2] #109年最新的10個月最高價
        priceGroup.append(lm10)
        lm11  = dfs2[0].iloc[int(monthlen)-11][2] #109年最新的11個月最高價
        priceGroup.append(lm11)
        lm12  = dfs2[0].iloc[int(monthlen)-12][2] #109年最新的12個月最高價
        priceGroup.append(lm12)     
    
        #thisYearMax = max(priceGroup)
        #H0 = str(thisYearMax)  #109年目前已出現過的最高價
        #print(priceGroup)
        #print(thisYearMax)
        '''
################################################接著取得EPS
#stock_id = "3034"
    bank_url = 'https://djinfo.cathaysec.com.tw/z/zc/zcq/zcq0.djhtm?b=Y&a=' #國泰世華
#sheet_type = 'z/zc/zcq/zcq_' #ISQ 合併損益表 季表

    url = bank_url + stock_id
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))

#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][98] #最新1年的合併總損益 每股盈餘
    
    eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2020
    eps2 = dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2019
    eps3 = dfs[2][3][98] #最新3年的合併總損益 每股盈餘 2018
    eps4 = dfs[2][4][98] #最新4年的合併總損益 每股盈餘 2017
    eps5 = dfs[2][5][98] #最新5年的合併總損益 每股盈餘 2016
    
    ####2020/07/02 加入EPS成長率
    
    #epsYoY1 = str(round((float(eps1)-float(eps2))/float(eps2),2)*100) + '%'    
    #epsYoY2 = str(round((float(eps2)-float(eps3))/float(eps3),2)*100) + '%'
    #epsYoY3 = str(round((float(eps3)-float(eps4))/float(eps4),2)*100) + '%'
    #epsYoY4 = str(round((float(eps4)-float(eps5))/float(eps5),2)*100) + '%'
    
    
    ####2020/07/02 加入本益比成長率
    PER_H1 = round(float(H1)/float(eps1),2)  #109本益比 高
    PER_L1 = round(float(L1)/float(eps1),2)  #109本益比 低 

    PER_H2 = round(float(H2)/float(eps2),2)  #108本益比 高
    PER_L2 = round(float(L2)/float(eps2),2)  #108本益比 低 

    PER_H3 = round(float(H3)/float(eps3),2)  #107本益比 高
    PER_L3 = round(float(L3)/float(eps3),2)  #107本益比 低 

    PER_H4 = round(float(H4)/float(eps4),2)  #106本益比 高
    PER_L4 = round(float(L4)/float(eps4),2)  #106本益比 低 
    
    PER_H5 = round(float(H5)/float(eps5),2)  #105本益比 高
    PER_L5 = round(float(L5)/float(eps5),2)  #105本益比 低 

    PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3 + PER_H4 + PER_H5)/5),2)
    PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3 + PER_L4 + PER_L5)/5),2)

    '''
#############2020/10/07 修改加入
    PER_H_average4 = round(float((PER_H1 + PER_H2 + PER_H3 + PER_H4)/4),2)
    PER_L_average4 = round(float((PER_L1 + PER_L2 + PER_L3 + PER_L4)/4),2)
    '''
#################

    #數值和平均值的波動值 高
    P_Hw1 = round(((PER_H1 - PER_H_average)/PER_H_average),4)
    P_Hw2 = round(((PER_H2 - PER_H_average)/PER_H_average),4)
    P_Hw3 = round(((PER_H3 - PER_H_average)/PER_H_average),4)
    P_Hw4 = round(((PER_H4 - PER_H_average)/PER_H_average),4)
    P_Hw5 = round(((PER_H5 - PER_H_average)/PER_H_average),4)
    
    #H_PERMax4 = max(PER_H1, PER_H2, PER_H3, PER_H4)   
    #H_PERMin4 = min(PER_H1, PER_H2, PER_H3, PER_H4)
    #數值和平均值的波動值 低
    P_Lw1 = round(((PER_L1 - PER_L_average)/PER_L_average),4)
    P_Lw2 = round(((PER_L2 - PER_L_average)/PER_L_average),4)
    P_Lw3 = round(((PER_L3 - PER_L_average)/PER_L_average),4)
    P_Lw4 = round(((PER_L4 - PER_L_average)/PER_L_average),4)
    P_Lw5 = round(((PER_L5 - PER_L_average)/PER_L_average),4)

    '''
    P_Hw1 = round(((PER_H1 - PER_H_average)/PER_H_average)*100,2)
    P_Hw2 = round(((PER_H2 - PER_H_average)/PER_H_average)*100,2)
    P_Hw3 = round(((PER_H3 - PER_H_average)/PER_H_average)*100,2)
    P_Hw4 = round(((PER_H4 - PER_H_average)/PER_H_average)*100,2)
    P_Hw5 = round(((PER_H5 - PER_H_average)/PER_H_average)*100,2)
    
    #H_PERMax4 = max(PER_H1, PER_H2, PER_H3, PER_H4)   
    #H_PERMin4 = min(PER_H1, PER_H2, PER_H3, PER_H4)
    #數值和平均值的波動值 低
    P_Lw1 = round(((PER_L1 - PER_L_average)/PER_L_average)*100,2)
    P_Lw2 = round(((PER_L2 - PER_L_average)/PER_L_average)*100,2)
    P_Lw3 = round(((PER_L3 - PER_L_average)/PER_L_average)*100,2)
    P_Lw4 = round(((PER_L4 - PER_L_average)/PER_L_average)*100,2)
    P_Lw5 = round(((PER_L5 - PER_L_average)/PER_L_average)*100,2)
    '''



    #L_PERMax4 = max(PER_L1, PER_L2, PER_L3, PER_L4)   
    #L_PERMin4 = min(PER_L1, PER_L2, PER_L3, PER_L4)   
##############
    '''    
    #總大的4年本益比區間高檔和低檔變動率
    P_Hx = str(round(((H_PERMax4 - H_PERMin4)/PER_H_average4)*100,2)) + '%'      #高檔區變動率
    P_Lx = str(round(((L_PERMax4 - L_PERMin4)/PER_L_average4)*100,2)) + '%'      #低檔區變動率 
    '''
    
    return PER_H1, PER_L1, PER_H2, PER_L2, PER_H3, PER_L3, PER_H4, PER_L4, PER_H5, PER_L5, PER_H_average, PER_L_average, P_Hw1, P_Hw2, P_Hw3, P_Hw4, P_Hw5, P_Lw1, P_Lw2, P_Lw3, P_Lw4, P_Lw5
#, PER_H_average4, PER_L_average4, P_Hx, P_Lx



def PERsegStable2(stock_id):

    ######以下為判斷上市或上櫃，取得年度股價程式
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup    
    
    try:    #查詢上櫃年股價，失敗就換查上市股票

        payload = {'input_stock_code': stock_id} #股價空格 要填入代號
# 將查詢參數加入 get 請求中
        r = requests.post("https://www.tpex.org.tw/web/stock/statistics/monthly/st42.php?l=zh-tw", data=payload)
#print(html.text) #以json格式呈現

        soup = BeautifulSoup(r.content, 'lxml')
        table = soup.find_all('table')[2];
        dfs = pd.read_html(str(table))

        #print(dfs)

    #ls0 = lastyear1 = dfs[0].iloc[2] #當年 110年
        ls0 =  dfs[0].iloc[2] #當年 110年
        ls1 =  dfs[0].iloc[3] #109年
        ls2 =  dfs[0].iloc[4] #108年
        ls3 =  dfs[0].iloc[5] #107年
        ls4 =  dfs[0].iloc[6] #106年
        ls5 =  dfs[0].iloc[7] #105年
        
        H0 = ls0[4] #110年目前已出現過的最高價
        #L0 = ls0[6] #110年目前已出現過的最低價

        H1 = ls1[4] #109年最高價
        L1 = ls1[6] #109年最低價

        H2 = ls2[4] #108年最高價
        L2 = ls2[6] #108年最低價

        H3 = ls3[4] #107年最高價
        L3 = ls3[6] #107年最低價

        H4 = ls4[4] #106年最高價
        L4 = ls4[6] #106年最低價

        H5 = ls5[4] #105年最高價
        L5 = ls5[6] #105年最低價
    
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



        ls1  = dfs[0].iloc[-1] #109年
        ls2  = dfs[0].iloc[-2] #108年
        ls3  = dfs[0].iloc[-3] #107年
        ls4  = dfs[0].iloc[-4] #106年
        ls5  = dfs[0].iloc[-5] #105年

        H1 = ls1[4] #2020/109年最高價
        L1 = ls1[6] #109年最低價

        H2 = ls2[4] #108年最高價
        L2 = ls2[6] #108年最低價

        H3 = ls3[4] #107年最高價
        L3 = ls3[6] #107年最低價

        H4 = ls4[4] #106年最高價
        L4 = ls4[6] #106年最低價

        H5 = ls5[4] #105年最高價
        L5 = ls5[6] #105年最低價

        #print(H5)
        #print(L5)
        '''
        ##抓取上市今年最高價 一個月一個月抓，再算最大值
        twse_url2 = 'http://www.twse.com.tw/exchangeReport/FMSRFK?response=html&stockNo=' 
        url = twse_url2 + stock_id 
        r2 = requests.get(url)
        soup2 = BeautifulSoup(r2.content, 'lxml')
        table2 = soup2.find_all('table')[0];
        dfs2 = pd.read_html(str(table2))

        monthlen = len(dfs2[0]) #計算有幾個欄位（幾個月份）
    #dfs[0].iloc[m-1] #109年1月
        priceGroup = []

#try:      
        lm1  = dfs2[0].iloc[int(monthlen)-1][2] #109年最新的1個月最高價
        priceGroup.append(lm1)
        lm2  = dfs2[0].iloc[int(monthlen)-2][2] #109年最新的2個月最高價
        priceGroup.append(lm2)    
        lm3  = dfs2[0].iloc[int(monthlen)-3][2] #109年最新的3個月最高價
        priceGroup.append(lm3)
        lm4  = dfs2[0].iloc[int(monthlen)-4][2] #109年最新的4個月最高價
        priceGroup.append(lm4)
        lm5  = dfs2[0].iloc[int(monthlen)-5][2] #109年最新的5個月最高價
        priceGroup.append(lm5)
        lm6  = dfs2[0].iloc[int(monthlen)-6][2] #109年最新的6個月最高價
        priceGroup.append(lm6)
        lm7  = dfs2[0].iloc[int(monthlen)-7][2] #109年最新的7個月最高價
        priceGroup.append(lm7)
        lm8  = dfs2[0].iloc[int(monthlen)-8][2] #109年最新的8個月最高價
        priceGroup.append(lm8)
        lm9  = dfs2[0].iloc[int(monthlen)-9][2] #109年最新的9個月最高價
        priceGroup.append(lm9)
        lm10  = dfs2[0].iloc[int(monthlen)-10][2] #109年最新的10個月最高價
        priceGroup.append(lm10)
        lm11  = dfs2[0].iloc[int(monthlen)-11][2] #109年最新的11個月最高價
        priceGroup.append(lm11)
        lm12  = dfs2[0].iloc[int(monthlen)-12][2] #109年最新的12個月最高價
        priceGroup.append(lm12)     
    
        thisYearMax = max(priceGroup)
        H0 = str(thisYearMax)  #109年目前已出現過的最高價
        #print(priceGroup)
        #print(thisYearMax)
        '''
################################################接著取得EPS
#stock_id = "3034"
    bank_url = 'https://djinfo.cathaysec.com.tw/z/zc/zcq/zcq0.djhtm?b=Y&a=' #國泰世華
#sheet_type = 'z/zc/zcq/zcq_' #ISQ 合併損益表 季表

    url = bank_url + stock_id
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
        #table = soup.find_all('table')[0];
    table2 = soup.find_all(class_ = 'table-row') 


    xYearSeasonTitle = table2[0].text
    xYearSeasonTitleList = xYearSeasonTitle.split("\n")

    xEPS = table2[-1].text
    xEPSList = xEPS.split("\n")
#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
    print(xYearSeasonTitle)
    eps1N = xYearSeasonTitleList[2] #dfs[2][1][0] #最新1年的名稱 2020
    print(xEPSList)
        ######2021/03/13 Q4財報出來大修改  20211224 MoneyDJ大改版

#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][98] #最新1年的合併總損益 每股盈餘

    eps1 = xEPSList[2] #最新1年的合併總損益 每股盈餘 2020
    eps2 = xEPSList[3] #最新2年的合併總損益 每股盈餘 2019
    eps3 = xEPSList[4] #最新3年的合併總損益 每股盈餘 2018
    eps4 = xEPSList[5] #最新4年的合併總損益 每股盈餘 2017
    eps5 = xEPSList[6] #最新5年的合併總損益 每股盈餘 2016
    
    ####2020/07/02 加入EPS成長率
    
    epsYoY1 = str(round((float(eps1)-float(eps2))/float(eps2),2)*100) + '%'    
    epsYoY2 = str(round((float(eps2)-float(eps3))/float(eps3),2)*100) + '%'
    epsYoY3 = str(round((float(eps3)-float(eps4))/float(eps4),2)*100) + '%'
    epsYoY4 = str(round((float(eps4)-float(eps5))/float(eps5),2)*100) + '%'
    
    
    ####2020/07/02 加入本益比成長率
    PER_H1 = round(float(H1)/float(eps1),2)  #2020/109本益比 高
    PER_L1 = round(float(L1)/float(eps1),2)  #109本益比 低 

    PER_H2 = round(float(H2)/float(eps2),2)  #108本益比 高
    PER_L2 = round(float(L2)/float(eps2),2)  #108本益比 低 

    PER_H3 = round(float(H3)/float(eps3),2)  #107本益比 高
    PER_L3 = round(float(L3)/float(eps3),2)  #107本益比 低 

    PER_H4 = round(float(H4)/float(eps4),2)  #106本益比 高
    PER_L4 = round(float(L4)/float(eps4),2)  #106本益比 低 
    
    PER_H5 = round(float(H5)/float(eps5),2)  #105本益比 高
    PER_L5 = round(float(L5)/float(eps5),2)  #105本益比 低 

    PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3 + PER_H4 + PER_H5)/5),2)
    PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3 + PER_L4 + PER_L5)/5),2)

#############2020/10/07 修改加入
    PER_H_average4 = round(float((PER_H1 + PER_H2 + PER_H3 + PER_H4)/4),2)
    PER_L_average4 = round(float((PER_L1 + PER_L2 + PER_L3 + PER_L4)/4),2)

#################

    #數值和平均值的波動值 高
    P_Hw1 = round(((PER_H1 - PER_H_average)/PER_H_average)*100,2)
    P_Hw2 = round(((PER_H2 - PER_H_average)/PER_H_average)*100,2)
    P_Hw3 = round(((PER_H3 - PER_H_average)/PER_H_average)*100,2)
    P_Hw4 = round(((PER_H4 - PER_H_average)/PER_H_average)*100,2)
    P_Hw5 = round(((PER_H5 - PER_H_average)/PER_H_average)*100,2)

    H_PERMax4 = max(PER_H1, PER_H2, PER_H3, PER_H4)   
    H_PERMin4 = min(PER_H1, PER_H2, PER_H3, PER_H4)
    #數值和平均值的波動值 低
    P_Lw1 = round(((PER_L1 - PER_L_average)/PER_L_average)*100,2)
    P_Lw2 = round(((PER_L2 - PER_L_average)/PER_L_average)*100,2)
    P_Lw3 = round(((PER_L3 - PER_L_average)/PER_L_average)*100,2)
    P_Lw4 = round(((PER_L4 - PER_L_average)/PER_L_average)*100,2)
    P_Lw5 = round(((PER_L5 - PER_L_average)/PER_L_average)*100,2)

    L_PERMax4 = max(PER_L1, PER_L2, PER_L3, PER_L4)   
    L_PERMin4 = min(PER_L1, PER_L2, PER_L3, PER_L4)   
##############
    
    #總大的4年本益比區間高檔和低檔變動率
    P_Hx = str(round(((H_PERMax4 - H_PERMin4)/PER_H_average4)*100,2)) + '%'      #高檔區變動率
    P_Lx = str(round(((L_PERMax4 - L_PERMin4)/PER_L_average4)*100,2)) + '%'      #低檔區變動率 

    print(P_Hx, P_Lx)    
    return PER_H1, PER_L1, PER_H2, PER_L2, PER_H3, PER_L3, PER_H4, PER_L4, PER_H5, PER_L5, PER_H_average, PER_L_average, P_Hw1, P_Hw2, P_Hw3, P_Hw4, P_Hw5, P_Lw1, P_Lw2, P_Lw3, P_Lw4, P_Lw5, PER_H_average4, PER_L_average4, P_Hx, P_Lx
#

