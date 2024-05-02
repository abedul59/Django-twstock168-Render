# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:58:08 2021

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
#1/1後第一件事，改上市上櫃html年份標記，下面的年份註解非必要改，改了比較好了解，模板if年份也要改，因為3/31前eps尚未更新完

def Price5y(stock_id):
    headers = {'Referer': my_Referer ,'user-agent': my_UserAgent}

    ######以下為判斷上市或上櫃，取得年度股價程式
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup    


    try:  #查詢上市年股價 （先上市，有些股票會上櫃轉上市，但上櫃還會留下資料，會抓錯。）
        twse_url = 'http://www.twse.com.tw/exchangeReport/FMNPTK?response=html&stockNo=' #國泰世華
        url = twse_url + stock_id 
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        table = soup.find_all('table')[0];
        dfs = pd.read_html(str(table))



        ls1  = dfs[0].iloc[-1] #2022/111年
        ls2  = dfs[0].iloc[-2] #2021/110年
        ls3  = dfs[0].iloc[-3] #109年
        ls4  = dfs[0].iloc[-4] #108年
        ls5  = dfs[0].iloc[-5] #107年
        ls6  = dfs[0].iloc[-6] #106年        

        H1 = ls1[4] #111年最高價
        L1 = ls1[6] #111年最低價

        H2 = ls2[4] #110年最高價
        L2 = ls2[6] #110年最低價

        H3 = ls3[4] #109年最高價
        L3 = ls3[6] #109年最低價

        H4 = ls4[4] #108年最高價
        L4 = ls4[6] #108年最低價

        H5 = ls5[4] #107年最高價
        L5 = ls5[6] #107年最低價

        H6 = ls6[4] #106年最高價
        L6 = ls6[6] #106年最低價


################################################接著取得上市股票EPS
#stock_id = "3034"
        bank_url0 = 'https://djinfo.cathaysec.com.tw/z/zc/zcq/zcq0.djhtm?b=Y&a=' #國泰世華
#sheet_type = 'z/zc/zcq/zcq_' #ISQ 合併損益表 季表

        url = bank_url0 + stock_id
        r = requests.get(url, headers=headers)
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
        #2023/3/7 3-4月間要改年分2022/2021
        
        if eps1N == '2022':  #在3/31前，Q4財報先出來的情況  年度轉換時還不適用。進入3月時才開始改
            
            eps1 = xEPSList[2] #dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2021
            eps2 = xEPSList[3] #dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2020
            eps3 = xEPSList[4] #dfs[2][3][98] #最新3年的合併總損益 每股盈餘 2019
            eps4 = xEPSList[5] #dfs[2][4][98] #最新4年的合併總損益 每股盈餘 2018
            eps5 = xEPSList[6] #dfs[2][5][98] #最新5年的合併總損益 每股盈餘 2017
            eps6 = xEPSList[7] #dfs[2][6][98] #最新5年的合併總損益 每股盈餘 2016
            
    ####2020/07/02 加入本益比成長率    
        #2021/1/6更改
            PER_H1 = round(float(H1)/float(eps1),2)  #110/2021本益比 高
            PER_L1 = round(float(L1)/float(eps1),2)  #110本益比 低 

            PER_H2 = round(float(H2)/float(eps2),2)  #109本益比 高
            PER_L2 = round(float(L2)/float(eps2),2)  #109本益比 低 

            PER_H3 = round(float(H3)/float(eps3),2)  #108本益比 高
            PER_L3 = round(float(L3)/float(eps3),2)  #108本益比 低 
            
            PER_H4 = round(float(H4)/float(eps4),2)  #107本益比 高
            PER_L4 = round(float(L4)/float(eps4),2)  #107本益比 低 
    
            PER_H5 = round(float(H5)/float(eps5),2)  #106本益比 高
            PER_L5 = round(float(L5)/float(eps5),2)  #106本益比 低 

            PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3 + PER_H4 + PER_H5)/5),2)
            PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3 + PER_L4 + PER_L5)/5),2)
#print(PER_H1)

            PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
            PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低  

          
        elif eps1N == '2021':  #3/31前，Q4財報還沒出來的情況 沒有2021的全年EPS
    ####2020/07/02 加入本益比成長率
            #2021EPS還沒出來的情況   #2021/12/31修改 欄位已改變 12/30最後交易日
            eps1 = xEPSList[2] #dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2020
            eps2 = xEPSList[3] #dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2019
            eps3 = xEPSList[4] #dfs[2][3][98] #最新3年的合併總損益 每股盈餘 2018
            eps4 = xEPSList[5] #dfs[2][4][98] #最新4年的合併總損益 每股盈餘 2017
            eps5 = xEPSList[6] #dfs[2][5][98] #最新5年的合併總損益 每股盈餘 2016
            eps6 = xEPSList[7] #dfs[2][6][98] #最新5年的合併總損益 每股盈餘 2015
            
        #2021/1/6更改  H1為2020高點
            PER_H1 = round(float(H2)/float(eps1),2)  #109/2020本益比 高
            PER_L1 = round(float(L2)/float(eps1),2)  #109本益比 低 

            PER_H2 = round(float(H3)/float(eps2),2)  #108本益比 高
            PER_L2 = round(float(L3)/float(eps2),2)  #108本益比 低 

            PER_H3 = round(float(H4)/float(eps3),2)  #107本益比 高
            PER_L3 = round(float(L4)/float(eps3),2)  #107本益比 低 

            PER_H4 = round(float(H5)/float(eps4),2)  #106本益比 高
            PER_L4 = round(float(L5)/float(eps4),2)  #106本益比 低 
    
            PER_H5 = round(float(H6)/float(eps5),2)  #105本益比 高
            PER_L5 = round(float(L6)/float(eps5),2)  #105本益比 低 

            PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3 + PER_H4 + PER_H5)/5),2)
            PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3 + PER_L4 + PER_L5)/5),2)

#print(PER_H1)
            PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
            PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低


    
    except:    #查詢上櫃年股價

################################################接著取得上市股票EPS
#stock_id = "3034"
        bank_url0 = 'https://djinfo.cathaysec.com.tw/z/zc/zcq/zcq0.djhtm?b=Y&a=' #國泰世華
#sheet_type = 'z/zc/zcq/zcq_' #ISQ 合併損益表 季表

        url = bank_url0 + stock_id
        r = requests.get(url, headers=headers)
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



#1/1後第一件事，改上市上櫃html年份標記，下面的年份註解非必要改，改了比較好了解，模板if年份也要改，因為3/31前eps尚未更新完


        payload = {'input_stock_code': stock_id} #股價空格 要填入代號
# 將查詢參數加入 POST 請求中
        r = requests.post("https://www.tpex.org.tw/web/stock/statistics/monthly/st42.php?l=zh-tw", data=payload, headers=headers)
#print(html.text) #以json格式呈現

        soup = BeautifulSoup(r.content, 'lxml')
        table = soup.find_all('table')[2];
        dfs = pd.read_html(str(table))

        #print(dfs)
        tablelen = len(dfs[0])
        
        #print(tablelen)


        if (tablelen == 6):  #原本 ==8  #去掉當年，只有過去5年資料  2022/2/18新增 2022/1/4 修改
            
            ls0 =  dfs[0].iloc[0] #當年 112年 #2023/1/6更改
            ls1 =  dfs[0].iloc[1] #111年
            ls2 =  dfs[0].iloc[2] #110年
            ls3 =  dfs[0].iloc[3] #109年
            ls4 =  dfs[0].iloc[4] #108年
            ls5 =  dfs[0].iloc[5] #107年
            ls6 =  None #105年
            
            #print(ls6)


            H0 = ls0[5] #112年目前已出現過的最高價
        #L0 = ls0[6] #109年目前已出現過的最低價

            H1 = ls1[5] #111/2022年最高價
            L1 = ls1[7] #111年最低價
             ############2020EPS尚未公佈
            H2 = ls2[5] #110年最高價
            L2 = ls2[7] #110年最低價

            H3 = ls3[5] #109年最高價
            L3 = ls3[7] #109年最低價

            H4 = ls4[5] #108年最高價
            L4 = ls4[7] #108年最低價
            
            H5 = ls5[5] #107年最高價
            L5 = ls5[7] #107年最低價

            H6 = None #106年最高價
            L6 = None #106年最低價
            #print(H0)
            
####################            
            


#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][98] #最新1年的合併總損益 每股盈餘
            if eps1N == '2021':  #在三月時，Q4財報先出來的情況
            
                eps1 = xEPSList[2] #dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2021
                eps2 = xEPSList[3] #dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2020
                eps3 = xEPSList[4] #dfs[2][3][98] #最新3年的合併總損益 每股盈餘 2019
                eps4 = xEPSList[5] #dfs[2][4][98] #最新4年的合併總損益 每股盈餘 2018
                eps5 = xEPSList[6] #dfs[2][5][98] #最新5年的合併總損益 每股盈餘 2017
                #eps6 = xEPSList[7] #dfs[2][6][98] #最新5年的合併總損益 每股盈餘 2016
    
    ####2020/07/02 加入本益比成長率
                PER_H1 = round(float(H1)/float(eps1),2)  #2021/110本益比 高
                PER_L1 = round(float(L1)/float(eps1),2)  #110本益比 低 

                PER_H2 = round(float(H2)/float(eps2),2)  #109本益比 高
                PER_L2 = round(float(L2)/float(eps2),2)  #109本益比 低 

                PER_H3 = round(float(H3)/float(eps3),2)  #108本益比 高
                PER_L3 = round(float(L3)/float(eps3),2)  #108本益比 低 

                PER_H4 = round(float(H4)/float(eps4),2)  #107本益比 高
                PER_L4 = round(float(L4)/float(eps4),2)  #107本益比 低 
    
                PER_H5 = round(float(H5)/float(eps5),2) #None  #106本益比 高
                PER_L5 = round(float(L5)/float(eps5),2) #None  #106本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3 + PER_H4 + PER_H5)/5),2)
                PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3 + PER_L4 + PER_H5)/5),2)

                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低
                
            elif eps1N == '2020':  #在三月時，Q4財報還沒出來的情況
            
                eps1 = xEPSList[2] #最新1年的合併總損益 每股盈餘 2020
                eps2 = xEPSList[3] #最新2年的合併總損益 每股盈餘 2019
                eps3 = xEPSList[4] #最新3年的合併總損益 每股盈餘 2018
                eps4 = xEPSList[5] #最新4年的合併總損益 每股盈餘 2017/106
                eps5 = None #最新5年的合併總損益 每股盈餘 2016/105
    
    ####2020/07/02 加入本益比成長率
                PER_H1 = round(float(H2)/float(eps1),2)  #2020/109本益比 高
                PER_L1 = round(float(L2)/float(eps1),2)  #109本益比 低 

                PER_H2 = round(float(H3)/float(eps2),2)  #108本益比 高
                PER_L2 = round(float(L3)/float(eps2),2)  #108本益比 低 

                PER_H3 = round(float(H4)/float(eps3),2)  #107本益比 高
                PER_L3 = round(float(L4)/float(eps3),2)  #107本益比 低 

                PER_H4 = round(float(H5)/float(eps4),2)  #106本益比 高
                PER_L4 = round(float(L5)/float(eps4),2)  #106本益比 低 
    
                PER_H5 = None  #105本益比 高
                PER_L5 = None  #105本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3 + PER_H4)/4),2)
                PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3 + PER_L4)/4),2)

                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低

        
        #2021/1/6更改
        if (tablelen == 5):  #原本 ==7 #去掉當年，只有過去四年資料
            
            ls0 =  dfs[0].iloc[0] #當年 111年 #2022/1/5更改
            ls1 =  dfs[0].iloc[1] #110年
            ls2 =  dfs[0].iloc[2] #109年
            ls3 =  dfs[0].iloc[3] #108年
            ls4 =  dfs[0].iloc[4] #107年
            ls5 =  None #dfs[0].iloc[5] #106年
            ls6 =  None #dfs[0].iloc[6] #105年


            H0 = ls0[5] #111年目前已出現過的最高價
        #L0 = ls0[6] #109年目前已出現過的最低價

            H1 = ls1[5] #110/2021年最高價
            L1 = ls1[7] #110年最低價
             ############2020EPS尚未公佈
            H2 = ls2[5] #109年最高價
            L2 = ls2[7] #109年最低價

            H3 = ls3[5] #108年最高價
            L3 = ls3[7] #108年最低價

            H4 = ls4[5] #107年最高價
            L4 = ls4[7] #107年最低價
            
            H5 = None #106年最高價
            L5 = None #106年最低價

            H6 = None #105年最高價
            L6 = None #105年最低價
            #print(H0)
            
####################            
            

#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][98] #最新1年的合併總損益 每股盈餘
            if eps1N == '2021':  #在三月時，Q4財報先出來的情況
            
                eps1 = xEPSList[2] #最新1年的合併總損益 每股盈餘 2021
                eps2 = xEPSList[3] #最新2年的合併總損益 每股盈餘 2020
                eps3 = xEPSList[4] #最新3年的合併總損益 每股盈餘 2019
                eps4 = xEPSList[5] #None #最新4年的合併總損益 每股盈餘 2018/107
                eps5 = None #最新5年的合併總損益 每股盈餘 2017/106
    
    ####2020/07/02 加入本益比成長率
                PER_H1 = round(float(H1)/float(eps1),2)  #2021/110本益比 高
                PER_L1 = round(float(L1)/float(eps1),2)  #110本益比 低 

                PER_H2 = round(float(H2)/float(eps2),2)  #109本益比 高
                PER_L2 = round(float(L2)/float(eps2),2)  #109本益比 低 

                PER_H3 = round(float(H3)/float(eps3),2)  #108本益比 高
                PER_L3 = round(float(L3)/float(eps3),2)  #108本益比 低 

                PER_H4 = round(float(H4)/float(eps4),2) #None  #107本益比 高
                PER_L4 = round(float(L4)/float(eps4),2)  #None  #107本益比 低 
    
                PER_H5 = None  #106本益比 高
                PER_L5 = None  #106本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3 + PER_H4)/4),2)
                PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3 + PER_L4)/4),2)

                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低

            elif eps1N == '2020':  #在三月時，Q4財報還沒出來的情況
            
                eps1 = xEPSList[2] #最新1年的合併總損益 每股盈餘 2020
                eps2 = xEPSList[3] #最新2年的合併總損益 每股盈餘 2019
                eps3 = xEPSList[4] #最新3年的合併總損益 每股盈餘 2018
                eps4 = None #最新4年的合併總損益 每股盈餘 2016/107
                eps5 = None #最新5年的合併總損益 每股盈餘 2015/106
    
    ####2020/07/02 加入本益比成長率
                PER_H1 = round(float(H2)/float(eps1),2)  #2020/109本益比 高
                PER_L1 = round(float(L2)/float(eps1),2)  #109本益比 低 

                PER_H2 = round(float(H3)/float(eps2),2)  #108本益比 高
                PER_L2 = round(float(L3)/float(eps2),2)  #108本益比 低 

                PER_H3 = round(float(H4)/float(eps3),2)  #107本益比 高
                PER_L3 = round(float(L4)/float(eps3),2)  #107本益比 低 

                PER_H4 = None  #106本益比 高
                PER_L4 = None  #106本益比 低 
    
                PER_H5 = None  #105本益比 高
                PER_L5 = None  #105本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3)/3),2)
                PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3)/3),2)

                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低

            
            
            
##############

        elif (tablelen == 4):  #原本 ==6 #去掉當年，只有過去三年資料
            
            ls0 =  dfs[0].iloc[0] #當年 111/2022年
            ls1 =  dfs[0].iloc[1] #110年
            ls2 =  dfs[0].iloc[2] #109年
            ls3 =  dfs[0].iloc[3] #108年
            ls4 =  dfs[0].iloc[4] #107年
            ls5 =  dfs[0].iloc[5] #106年
            #ls6 =  dfs[0].iloc[6] #104年

            H0 = ls0[5] #111年目前已出現過的最高價
        #L0 = ls0[6] #109年目前已出現過的最低價

            H1 = ls1[5] #110/2021年最高價
            L1 = ls1[7] #110年最低價

            H2 = ls2[5] #109年最高價
            L2 = ls2[7] #109年最低價

            H3 = ls3[5] #108年最高價
            L3 = ls3[7] #108年最低價

            H4 = None #107年最高價
            L4 = None #107年最低價
            
            H5 = None #106年最高價
            L5 = None #106年最低價

            H6 = None #105年最高價
            L6 = None #105年最低價
            #print(H0)



####################            
            


#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][98] #最新1年的合併總損益 每股盈餘
 
            if eps1N == '2021':  #在3/31前，Q4財報先出來的情況

                eps1 = xEPSList[2] #最新1年的合併總損益 每股盈餘 2021
                eps2 = xEPSList[3]#最新2年的合併總損益 每股盈餘 2020
                eps3 = xEPSList[4] #None #最新3年的合併總損益 每股盈餘 2019
                eps4 = None #最新4年的合併總損益 每股盈餘 2018
                eps5 = None #最新5年的合併總損益 每股盈餘 2017
    
    ####2020/07/02 加入本益比成長率
            #2021/1/6 更改
                PER_H1 = round(float(H1)/float(eps1),2)  #2021/110本益比 高
                PER_L1 = round(float(L1)/float(eps1),2)  #110本益比 低 

                PER_H2 = round(float(H2)/float(eps2),2)  #109本益比 高
                PER_L2 = round(float(L2)/float(eps2),2)  #109本益比 低 

                PER_H3 = round(float(H3)/float(eps3),2) #None  #108本益比 高
                PER_L3 = round(float(L3)/float(eps3),2) #None  #108本益比 低 

                PER_H4 = None  #107本益比 高
                PER_L4 = None  #107本益比 低 
    
                PER_H5 = None  #106本益比 高
                PER_L5 = None  #106本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3)/3),2)
                PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3)/3),2)

                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低

            elif eps1N == '2020':  #在三月時，Q4財報還沒出來的情況

                eps1 = xEPSList[2] #最新1年的合併總損益 每股盈餘 2020
                eps2 = xEPSList[3] #最新2年的合併總損益 每股盈餘 2019
                eps3 = None #最新3年的合併總損益 每股盈餘 2018
                eps4 = None #最新4年的合併總損益 每股盈餘 2017
                eps5 = None #最新5年的合併總損益 每股盈餘 2016
    
    ####2020/07/02 加入本益比成長率
            #2021/1/6 更改
                PER_H1 = round(float(H2)/float(eps1),2)  #2020/109本益比 高
                PER_L1 = round(float(L2)/float(eps1),2)  #109本益比 低 

                PER_H2 = round(float(H3)/float(eps2),2)  #108本益比 高
                PER_L2 = round(float(L3)/float(eps2),2)  #108本益比 低 

                PER_H3 = None  #107本益比 高
                PER_L3 = None  #107本益比 低 

                PER_H4 = None  #106本益比 高
                PER_L4 = None  #106本益比 低 
    
                PER_H5 = None  #105本益比 高
                PER_L5 = None  #105本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2)/2),2)
                PER_L_average = round(float((PER_L1 + PER_L2)/2),2)

                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低

            
            
            #2021/1/6 增加
#############################################
        elif (tablelen == 3): #原本 ==5 #去掉當年，只有過去2年資料
            
            #print("test")
            
            ls0 =  dfs[0].iloc[0] #當年 111/2022年
            ls1 =  dfs[0].iloc[1] #110年
            ls2 =  dfs[0].iloc[2] #109年
            ls3 =  None #108年
            ls4 =  None #107年
            ls5 =  None #106年
            ls6 =  None #105年

            H0 = ls0[5] #111年目前已出現過的最高價
        #L0 = ls0[6] #109年目前已出現過的最低價

            H1 = ls1[5] #110/2021年最高價
            L1 = ls1[7] #110年最低價

            H2 = ls2[5] #109年最高價
            L2 = ls2[7] #109年最低價

            H3 = None #108年最高價
            L3 = None #108年最低價

            H4 = None #107年最高價
            L4 = None #107年最低價
            
            H5 = None #106年最高價
            L5 = None #106年最低價

            H6 = None #105年最高價
            L6 = None #105年最低價
            #print(H1)

####################            
            

#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][98] #最新1年的合併總損益 每股盈餘
            if eps1N == '2021':  #在三月時，Q4財報先出來的情況

                eps1 = xEPSList[2] #最新1年的合併總損益 每股盈餘 2021
                eps2 = xEPSList[3] #None #最新2年的合併總損益 每股盈餘 2020
                eps3 = None #最新3年的合併總損益 每股盈餘 2019
                eps4 = None #最新4年的合併總損益 每股盈餘 2018
                eps5 = None #最新5年的合併總損益 每股盈餘 2017
    
    ####2020/07/02 加入本益比成長率
            #2021/1/6 更改
                PER_H1 = round(float(H1)/float(eps1),2)  #2021/110本益比 高
                PER_L1 = round(float(L1)/float(eps1),2)  #110本益比 低 

                PER_H2 = round(float(H2)/float(eps2),2)  #109本益比 高
                PER_L2 = round(float(L2)/float(eps2),2) #None  #109本益比 低 

                PER_H3 = None  #108本益比 高
                PER_L3 = None  #108本益比 低 

                PER_H4 = None  #107本益比 高
                PER_L4 = None  #107本益比 低 
    
                PER_H5 = None  #106本益比 高
                PER_L5 = None  #106本益比 低 

                PER_H_average =  round(float((PER_H1 + PER_H2)/2),2)
                PER_L_average = round(float((PER_L1 + PER_L2)/2),2)

                PER_H = PER_H_average #min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = PER_L_average #min(PER_L_average,PER_L1)  #本益比低點與最新孰低


            elif eps1N == '2020':  #在三月時，Q4財報還沒出來的情況

                eps1 = xEPSList[2] #最新1年的合併總損益 每股盈餘 2020
                eps2 = None #最新2年的合併總損益 每股盈餘 2019
                eps3 = None #最新3年的合併總損益 每股盈餘 2018
                eps4 = None #最新4年的合併總損益 每股盈餘 2017
                eps5 = None #最新5年的合併總損益 每股盈餘 2016
    
    ####2020/07/02 加入本益比成長率
            #2021/1/6 更改
                PER_H1 = round(float(H2)/float(eps1),2)  #2020/109本益比 高
                PER_L1 = round(float(L2)/float(eps1),2)  #109本益比 低 

                PER_H2 = None  #108本益比 高
                PER_L2 = None  #108本益比 低 

                PER_H3 = None  #107本益比 高
                PER_L3 = None  #107本益比 低 

                PER_H4 = None  #106本益比 高
                PER_L4 = None  #106本益比 低 
    
                PER_H5 = None  #105本益比 高
                PER_L5 = None  #105本益比 低 

                PER_H_average =  PER_H1 #round(float((PER_H1 + PER_H2)/2),2)
                PER_L_average = PER_L1 #round(float((PER_L1 + PER_L2)/2),2)

                PER_H = PER_H_average #min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = PER_L_average #min(PER_L_average,PER_L1)  #本益比低點與最新孰低


            
        elif (tablelen >= 7): #原本 >=9 #有6年以上歷史資料  含當年度有6年
    #ls0 = lastyear1 = dfs[0].iloc[2] #當年 2022/111年
            ls0 =  dfs[0].iloc[0] #原本[2]#當年2022/111年  2021/11/17整個編號有問題iloc
            ls1 =  dfs[0].iloc[1] #2021/110年            
            ls2 =  dfs[0].iloc[2] #109年
            ls3 =  dfs[0].iloc[3] #108年
            ls4 =  dfs[0].iloc[4] #107年
            ls5 =  dfs[0].iloc[5] #106年        
            ls6 =  dfs[0].iloc[6] #105年
            
            print(ls0, ls1)
           
        
            H0 = ls0[5] #111年目前已出現過的最高價
        #L0 = ls0[6] #109年目前已出現過的最低價

            H1 = ls1[5] #2021/110年最高價  原本[4]
            L1 = ls1[7] #110年最低價 原本[6]
            print(H1,L1)


            H2 = ls2[5] #2020/109年最高價
            L2 = ls2[7] #109年最低價

            H3 = ls3[5] #2019/108年最高價
            L3 = ls3[7] #108年最低價

            H4 = ls4[5] #2018/107年最高價
            L4 = ls4[7] #107年最低價

            H5 = ls5[5] #106年最高價
            L5 = ls5[7] #106年最低價

            H6 = ls6[5] #105年最高價
            L6 = ls6[7] #105年最低價
            #print(tablelen)




#dfs[2] 真
            if eps1N == '2021':  #在三月時，Q4財報先出來的情況

                eps1 = xEPSList[2] #最新1年的合併總損益 每股盈餘 2020
                eps2 = xEPSList[3] #最新2年的合併總損益 每股盈餘 2019
                eps3 = xEPSList[4] #最新3年的合併總損益 每股盈餘 2018
                eps4 = xEPSList[5] #最新4年的合併總損益 每股盈餘 2017
                eps5 = xEPSList[6] #最新5年的合併總損益 每股盈餘 2016
                
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

                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低

            elif eps1N == '2020':  #在三月時，Q4財報還沒出來的情況

                eps1 = xEPSList[2] #最新1年的合併總損益 每股盈餘 2020
                eps2 = xEPSList[3] #最新2年的合併總損益 每股盈餘 2019
                eps3 = xEPSList[4] #最新3年的合併總損益 每股盈餘 2018
                eps4 = xEPSList[5] #最新4年的合併總損益 每股盈餘 2017
                eps5 = xEPSList[6] #最新5年的合併總損益 每股盈餘 2016
                
                PER_H1 = round(float(H2)/float(eps1),2)  #2020/109本益比 高
                PER_L1 = round(float(L2)/float(eps1),2)  #109本益比 低 

                PER_H2 = round(float(H3)/float(eps2),2)  #108本益比 高
                PER_L2 = round(float(L3)/float(eps2),2)  #108本益比 低 
                
                PER_H3 = round(float(H4)/float(eps3),2)  #107本益比 高
                PER_L3 = round(float(L4)/float(eps3),2)  #107本益比 低 

                PER_H4 = round(float(H5)/float(eps4),2)  #106本益比 高
                PER_L4 = round(float(L5)/float(eps4),2)  #106本益比 低 
    
                PER_H5 = round(float(H6)/float(eps5),2)  #105本益比 高
                PER_L5 = round(float(L6)/float(eps5),2)  #105本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3 + PER_H4 + PER_H5)/5),2)
                PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3 + PER_L4 + PER_L5)/5),2)

                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低



    return H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, H6, L6, eps1N
#, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, New_up_profit, New_down_loss, risk_reward, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average, pNet1, pNet2, pNet3, pNet4, pNet4Average, H0, thisYear_Sum, theRest_Predict

#Price5y('2330')