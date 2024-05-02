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


def Price5yDB(stock_id):
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
        '''        
        ##抓取上市今年最高價 一個月一個月抓，再算最大值
        twse_url2 = 'http://www.twse.com.tw/exchangeReport/FMSRFK?response=html&stockNo=' 
        url = twse_url2 + stock_id 
        r2 = requests.get(url, headers=headers)
        soup2 = BeautifulSoup(r2.content, 'lxml')
        table2 = soup2.find_all('table')[0];
        dfs2 = pd.read_html(str(table2))

        monthlen = len(dfs2[0]) #計算有幾個欄位（幾個月份）
    #dfs[0].iloc[m-1] #109年1月
        priceGroup = []

  
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
################################################接著取得上市股票EPS
#stock_id = "3034"
        bank_url0 = 'https://djinfo.cathaysec.com.tw/z/zc/zcq/zcq0.djhtm?b=Y&a=' #國泰世華
#sheet_type = 'z/zc/zcq/zcq_' #ISQ 合併損益表 季表

        url = bank_url0 + stock_id
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find_all('table')[0];
        dfs = pd.read_html(str(table))

#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][98] #最新1年的合併總損益 每股盈餘

        eps1N = dfs[2][1][0] #最新1年的名稱 2020
        print(eps1N)
        ######2021/03/13 Q4財報出來大修改
        if eps1N == '2020':  #在三月時，Q4財報先出來的情況
            
            eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2020
            eps2 = dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2019
            eps3 = dfs[2][3][98] #最新3年的合併總損益 每股盈餘 2018
            eps4 = dfs[2][4][98] #最新4年的合併總損益 每股盈餘 2017
            eps5 = dfs[2][5][98] #最新5年的合併總損益 每股盈餘 2016
            eps6 = dfs[2][6][98] #最新5年的合併總損益 每股盈餘 2015
            
    ####2020/07/02 加入本益比成長率    
        #2021/1/6更改
            PER_H1 = round(float(H1)/float(eps1),2)  #109/2020本益比 高
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
#print(PER_H1)

            PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
            PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低  

          
        elif eps1N == '2019':  #在三月時，Q4財報還沒出來的情況
    ####2020/07/02 加入本益比成長率
            #2020EPS還沒出來的情況
            eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2019
            eps2 = dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2018
            eps3 = dfs[2][3][98] #最新3年的合併總損益 每股盈餘 2017
            eps4 = dfs[2][4][98] #最新4年的合併總損益 每股盈餘 2016
            eps5 = dfs[2][5][98] #最新5年的合併總損益 每股盈餘 2015
            #eps6 = dfs[2][6][98] #最新5年的合併總損益 每股盈餘 2015
            
        #2021/1/6更改  H1為2020高點
            PER_H1 = round(float(H2)/float(eps1),2)  #108/2019本益比 高
            PER_L1 = round(float(L2)/float(eps1),2)  #108本益比 低 

            PER_H2 = round(float(H3)/float(eps2),2)  #107本益比 高
            PER_L2 = round(float(L3)/float(eps2),2)  #107本益比 低 

            PER_H3 = round(float(H4)/float(eps3),2)  #106本益比 高
            PER_L3 = round(float(L4)/float(eps3),2)  #106本益比 低 

            PER_H4 = round(float(H5)/float(eps4),2)  #105本益比 高
            PER_L4 = round(float(L5)/float(eps4),2)  #105本益比 低 
    
            PER_H5 = round(float(H6)/float(eps5),2)  #104本益比 高
            PER_L5 = round(float(L6)/float(eps5),2)  #104本益比 低 

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
        table = soup.find_all('table')[0];
        dfs = pd.read_html(str(table))

#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][98] #最新1年的合併總損益 每股盈餘

        eps1N = dfs[2][1][0] #最新1年的名稱 2020
        print(eps1N)





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



        if (tablelen == 8):  #去掉當年，只有過去5年資料  2021/2/18新增
            
            ls0 =  dfs[0].iloc[2] #當年 110年 #2021/1/6更改
            ls1 =  dfs[0].iloc[3] #109年
            ls2 =  dfs[0].iloc[4] #108年
            ls3 =  dfs[0].iloc[5] #107年
            ls4 =  dfs[0].iloc[6] #106年
            ls5 =  dfs[0].iloc[7] #105年
            ls6 =  "N/A" #104年
            
            #print(ls6)


            H0 = ls0[4] #110年目前已出現過的最高價
        #L0 = ls0[6] #109年目前已出現過的最低價

            H1 = ls1[4] #109/2020年最高價
            L1 = ls1[6] #109年最低價
             ############2020EPS尚未公佈
            H2 = ls2[4] #108年最高價
            L2 = ls2[6] #108年最低價

            H3 = ls3[4] #107年最高價
            L3 = ls3[6] #107年最低價

            H4 = ls4[4] #106年最高價
            L4 = ls4[6] #106年最低價
            
            H5 = ls5[4] #105年最高價
            L5 = ls5[4] #105年最低價

            H6 = "N/A" #104年最高價
            L6 = "N/A" #104年最低價
            #print(H0)
            
####################            
            
            bank_url0 = 'https://djinfo.cathaysec.com.tw/z/zc/zcq/zcq0.djhtm?b=Y&a=' #國泰世華
#sheet_type = 'z/zc/zcq/zcq_' #ISQ 合併損益表 季表

            url = bank_url0 + stock_id
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.content, 'html.parser')
            table = soup.find_all('table')[0];
            dfs = pd.read_html(str(table))

#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][98] #最新1年的合併總損益 每股盈餘
            if eps1N == '2020':  #在三月時，Q4財報先出來的情況
            
                eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2020
                eps2 = dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2019
                eps3 = dfs[2][3][98] #最新3年的合併總損益 每股盈餘 2018
                eps4 = dfs[2][4][98] #最新4年的合併總損益 每股盈餘 2017/106
                eps5 = "N/A" #最新5年的合併總損益 每股盈餘 2015/104
    
    ####2020/07/02 加入本益比成長率
                PER_H1 = round(float(H1)/float(eps1),2)  #2020/109本益比 高
                PER_L1 = round(float(L1)/float(eps1),2)  #109本益比 低 

                PER_H2 = round(float(H2)/float(eps2),2)  #108本益比 高
                PER_L2 = round(float(L2)/float(eps2),2)  #108本益比 低 

                PER_H3 = round(float(H3)/float(eps3),2)  #107本益比 高
                PER_L3 = round(float(L3)/float(eps3),2)  #107本益比 低 

                PER_H4 = round(float(H4)/float(eps4),2)  #106本益比 高
                PER_L4 = round(float(L4)/float(eps4),2)  #106本益比 低 
    
                PER_H5 = "N/A"  #104本益比 高
                PER_L5 = "N/A"  #104本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3 + PER_H4)/4),2)
                PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3 + PER_L4)/4),2)

                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低
                
            elif eps1N == '2019':  #在三月時，Q4財報還沒出來的情況
            
                eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2019
                eps2 = dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2018
                eps3 = dfs[2][3][98] #最新3年的合併總損益 每股盈餘 2017
                eps4 = dfs[2][4][98] #最新4年的合併總損益 每股盈餘 2016/105
                eps5 = "N/A" #最新5年的合併總損益 每股盈餘 2015/104
    
    ####2020/07/02 加入本益比成長率
                PER_H1 = round(float(H2)/float(eps1),2)  #2019/108本益比 高
                PER_L1 = round(float(L2)/float(eps1),2)  #108本益比 低 

                PER_H2 = round(float(H3)/float(eps2),2)  #107本益比 高
                PER_L2 = round(float(L3)/float(eps2),2)  #107本益比 低 

                PER_H3 = round(float(H4)/float(eps3),2)  #106本益比 高
                PER_L3 = round(float(L4)/float(eps3),2)  #106本益比 低 

                PER_H4 = round(float(H5)/float(eps4),2)  #105本益比 高
                PER_L4 = round(float(L5)/float(eps4),2)  #105本益比 低 
    
                PER_H5 = "N/A"  #104本益比 高
                PER_L5 = "N/A"  #104本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3 + PER_H4)/4),2)
                PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3 + PER_L4)/4),2)

                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低

        
        #2021/1/6更改
        if (tablelen == 7):  #去掉當年，只有過去四年資料
            
            ls0 =  dfs[0].iloc[2] #當年 110年 #2021/1/6更改
            ls1 =  dfs[0].iloc[3] #109年
            ls2 =  dfs[0].iloc[4] #108年
            ls3 =  dfs[0].iloc[5] #107年
            ls4 =  dfs[0].iloc[6] #106年
            ls5 =  dfs[0].iloc[7] #105年
            ls6 =  dfs[0].iloc[8] #104年


            H0 = ls0[4] #110年目前已出現過的最高價
        #L0 = ls0[6] #109年目前已出現過的最低價

            H1 = ls1[4] #109/2020年最高價
            L1 = ls1[6] #109年最低價
             ############2020EPS尚未公佈
            H2 = ls2[4] #108年最高價
            L2 = ls2[6] #108年最低價

            H3 = ls3[4] #107年最高價
            L3 = ls3[6] #107年最低價

            H4 = ls4[4] #106年最高價
            L4 = ls4[6] #106年最低價
            
            H5 = "N/A" #105年最高價
            L5 = "N/A" #105年最低價

            H6 = "N/A" #104年最高價
            L6 = "N/A" #104年最低價
            #print(H0)
            
####################            
            
            bank_url0 = 'https://djinfo.cathaysec.com.tw/z/zc/zcq/zcq0.djhtm?b=Y&a=' #國泰世華
#sheet_type = 'z/zc/zcq/zcq_' #ISQ 合併損益表 季表

            url = bank_url0 + stock_id
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.content, 'html.parser')
            table = soup.find_all('table')[0];
            dfs = pd.read_html(str(table))

#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][98] #最新1年的合併總損益 每股盈餘
            if eps1N == '2020':  #在三月時，Q4財報先出來的情況
            
                eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2020
                eps2 = dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2019
                eps3 = dfs[2][3][98] #最新3年的合併總損益 每股盈餘 2018
                eps4 = "N/A" #最新4年的合併總損益 每股盈餘 2017/106
                eps5 = "N/A" #最新5年的合併總損益 每股盈餘 2016/105
    
    ####2020/07/02 加入本益比成長率
                PER_H1 = round(float(H1)/float(eps1),2)  #2020/109本益比 高
                PER_L1 = round(float(L1)/float(eps1),2)  #109本益比 低 

                PER_H2 = round(float(H2)/float(eps2),2)  #108本益比 高
                PER_L2 = round(float(L2)/float(eps2),2)  #108本益比 低 

                PER_H3 = round(float(H3)/float(eps3),2)  #107本益比 高
                PER_L3 = round(float(L3)/float(eps3),2)  #107本益比 低 

                PER_H4 = "N/A"  #106本益比 高
                PER_L4 = "N/A"  #106本益比 低 
    
                PER_H5 = "N/A"  #105本益比 高
                PER_L5 = "N/A"  #105本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3)/3),2)
                PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3)/3),2)

                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低

            elif eps1N == '2019':  #在三月時，Q4財報還沒出來的情況
            
                eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2019
                eps2 = dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2018
                eps3 = dfs[2][3][98] #最新3年的合併總損益 每股盈餘 2017
                eps4 = "N/A" #最新4年的合併總損益 每股盈餘 2016/105
                eps5 = "N/A" #最新5年的合併總損益 每股盈餘 2015/104
    
    ####2020/07/02 加入本益比成長率
                PER_H1 = round(float(H2)/float(eps1),2)  #2019/108本益比 高
                PER_L1 = round(float(L2)/float(eps1),2)  #108本益比 低 

                PER_H2 = round(float(H3)/float(eps2),2)  #107本益比 高
                PER_L2 = round(float(L3)/float(eps2),2)  #107本益比 低 

                PER_H3 = round(float(H4)/float(eps3),2)  #106本益比 高
                PER_L3 = round(float(L4)/float(eps3),2)  #106本益比 低 

                PER_H4 = "N/A"  #105本益比 高
                PER_L4 = "N/A"  #105本益比 低 
    
                PER_H5 = "N/A"  #104本益比 高
                PER_L5 = "N/A"  #104本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3)/3),2)
                PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3)/3),2)

                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低

            
            
            
##############

        elif (tablelen == 6):  #去掉當年，只有過去三年資料
            
            ls0 =  dfs[0].iloc[2] #當年 110/2021年
            ls1 =  dfs[0].iloc[3] #109年
            ls2 =  dfs[0].iloc[4] #108年
            ls3 =  dfs[0].iloc[5] #107年
            ls4 =  dfs[0].iloc[6] #106年
            ls5 =  dfs[0].iloc[7] #105年
            ls6 =  dfs[0].iloc[8] #104年

            H0 = ls0[4] #110年目前已出現過的最高價
        #L0 = ls0[6] #109年目前已出現過的最低價

            H1 = ls1[4] #109/2020年最高價
            L1 = ls1[6] #109年最低價

            H2 = ls2[4] #108年最高價
            L2 = ls2[6] #108年最低價

            H3 = ls3[4] #107年最高價
            L3 = ls3[6] #107年最低價

            H4 = "N/A" #106年最高價
            L4 = "N/A" #106年最低價
            
            H5 = "N/A" #105年最高價
            L5 = "N/A" #105年最低價

            H6 = "N/A" #104年最高價
            L6 = "N/A" #104年最低價
            #print(H0)



####################            
            
            bank_url0 = 'https://djinfo.cathaysec.com.tw/z/zc/zcq/zcq0.djhtm?b=Y&a=' #國泰世華
#sheet_type = 'z/zc/zcq/zcq_' #ISQ 合併損益表 季表

            url = bank_url0 + stock_id
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.content, 'html.parser')
            table = soup.find_all('table')[0];
            dfs = pd.read_html(str(table))

#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][98] #最新1年的合併總損益 每股盈餘
 
            if eps1N == '2020':  #在三月時，Q4財報先出來的情況

                eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2020
                eps2 = dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2019
                eps3 = "N/A" #最新3年的合併總損益 每股盈餘 2018
                eps4 = "N/A" #最新4年的合併總損益 每股盈餘 2017
                eps5 = "N/A" #最新5年的合併總損益 每股盈餘 2016
    
    ####2020/07/02 加入本益比成長率
            #2021/1/6 更改
                PER_H1 = round(float(H1)/float(eps1),2)  #2020/109本益比 高
                PER_L1 = round(float(L1)/float(eps1),2)  #109本益比 低 

                PER_H2 = round(float(H2)/float(eps2),2)  #108本益比 高
                PER_L2 = round(float(L2)/float(eps2),2)  #108本益比 低 

                PER_H3 = "N/A"  #106本益比 高
                PER_L3 = "N/A"  #106本益比 低 

                PER_H4 = "N/A"  #105本益比 高
                PER_L4 = "N/A"  #105本益比 低 
    
                PER_H5 = "N/A"  #104本益比 高
                PER_L5 = "N/A"  #104本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2)/2),2)
                PER_L_average = round(float((PER_L1 + PER_L2)/2),2)

                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低

            elif eps1N == '2019':  #在三月時，Q4財報還沒出來的情況

                eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2019
                eps2 = dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2018
                eps3 = "N/A" #最新3年的合併總損益 每股盈餘 2017
                eps4 = "N/A" #最新4年的合併總損益 每股盈餘 2016
                eps5 = "N/A" #最新5年的合併總損益 每股盈餘 2015
    
    ####2020/07/02 加入本益比成長率
            #2021/1/6 更改
                PER_H1 = round(float(H2)/float(eps1),2)  #2019/108本益比 高
                PER_L1 = round(float(L2)/float(eps1),2)  #108本益比 低 

                PER_H2 = round(float(H3)/float(eps2),2)  #107本益比 高
                PER_L2 = round(float(L3)/float(eps2),2)  #107本益比 低 

                PER_H3 = "N/A"  #106本益比 高
                PER_L3 = "N/A"  #106本益比 低 

                PER_H4 = "N/A"  #105本益比 高
                PER_L4 = "N/A"  #105本益比 低 
    
                PER_H5 = "N/A"  #104本益比 高
                PER_L5 = "N/A"  #104本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2)/2),2)
                PER_L_average = round(float((PER_L1 + PER_L2)/2),2)

                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低

            
            
            #2021/1/6 增加
#############################################
        elif (tablelen == 5):  #去掉當年，只有過去2年資料
            
            ls0 =  dfs[0].iloc[2] #當年 110/2021年
            ls1 =  dfs[0].iloc[3] #109年
            ls2 =  dfs[0].iloc[4] #108年
            ls3 =  "N/A" #107年
            ls4 =  "N/A" #106年
            ls5 =  "N/A" #105年
            ls6 =  "N/A" #104年

            H0 = ls0[4] #110年目前已出現過的最高價
        #L0 = ls0[6] #109年目前已出現過的最低價

            H1 = ls1[4] #109/2020年最高價
            L1 = ls1[6] #109年最低價

            H2 = ls2[4] #108年最高價
            L2 = ls2[6] #108年最低價

            H3 = "N/A" #107年最高價
            L3 = "N/A" #107年最低價

            H4 = "N/A" #106年最高價
            L4 = "N/A" #106年最低價
            
            H5 = "N/A" #105年最高價
            L5 = "N/A" #105年最低價

            H6 = "N/A" #104年最高價
            L6 = "N/A" #104年最低價
            #print(H1)

####################            
            
            bank_url0 = 'https://djinfo.cathaysec.com.tw/z/zc/zcq/zcq0.djhtm?b=Y&a=' #國泰世華
#sheet_type = 'z/zc/zcq/zcq_' #ISQ 合併損益表 季表

            url = bank_url0 + stock_id
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.content, 'html.parser')
            table = soup.find_all('table')[0];
            dfs = pd.read_html(str(table))

#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][98] #最新1年的合併總損益 每股盈餘
            if eps1N == '2020':  #在三月時，Q4財報先出來的情況

                eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2020
                eps2 = "N/A" #最新2年的合併總損益 每股盈餘 2019
                eps3 = "N/A" #最新3年的合併總損益 每股盈餘 2018
                eps4 = "N/A" #最新4年的合併總損益 每股盈餘 2017
                eps5 = "N/A" #最新5年的合併總損益 每股盈餘 2016
    
    ####2020/07/02 加入本益比成長率
            #2021/1/6 更改
                PER_H1 = round(float(H1)/float(eps1),2)  #2020/109本益比 高
                PER_L1 = round(float(L1)/float(eps1),2)  #109本益比 低 

                PER_H2 = "N/A"  #107本益比 高
                PER_L2 = "N/A"  #107本益比 低 

                PER_H3 = "N/A"  #106本益比 高
                PER_L3 = "N/A"  #106本益比 低 

                PER_H4 = "N/A"  #105本益比 高
                PER_L4 = "N/A"  #105本益比 低 
    
                PER_H5 = "N/A"  #104本益比 高
                PER_L5 = "N/A"  #104本益比 低 

                PER_H_average =  PER_H1 #round(float((PER_H1 + PER_H2)/2),2)
                PER_L_average = PER_L1 #round(float((PER_L1 + PER_L2)/2),2)

                PER_H = PER_H_average #min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = PER_L_average #min(PER_L_average,PER_L1)  #本益比低點與最新孰低


            elif eps1N == '2019':  #在三月時，Q4財報還沒出來的情況

                eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2019
                eps2 = "N/A" #最新2年的合併總損益 每股盈餘 2018
                eps3 = "N/A" #最新3年的合併總損益 每股盈餘 2017
                eps4 = "N/A" #最新4年的合併總損益 每股盈餘 2017
                eps5 = "N/A" #最新5年的合併總損益 每股盈餘 2015
    
    ####2020/07/02 加入本益比成長率
            #2021/1/6 更改
                PER_H1 = round(float(H2)/float(eps1),2)  #2019/108本益比 高
                PER_L1 = round(float(L2)/float(eps1),2)  #108本益比 低 

                PER_H2 = "N/A"  #107本益比 高
                PER_L2 = "N/A"  #107本益比 低 

                PER_H3 = "N/A"  #106本益比 高
                PER_L3 = "N/A"  #106本益比 低 

                PER_H4 = "N/A"  #105本益比 高
                PER_L4 = "N/A"  #105本益比 低 
    
                PER_H5 = "N/A"  #104本益比 高
                PER_L5 = "N/A"  #104本益比 低 

                PER_H_average =  PER_H1 #round(float((PER_H1 + PER_H2)/2),2)
                PER_L_average = PER_L1 #round(float((PER_L1 + PER_L2)/2),2)

                PER_H = PER_H_average #min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = PER_L_average #min(PER_L_average,PER_L1)  #本益比低點與最新孰低


            
        elif (tablelen >= 9):  #有五年以上歷史資料
    #ls0 = lastyear1 = dfs[0].iloc[2] #當年 2021/110年
            ls0 =  dfs[0].iloc[2] #當年2021/110年
            ls1 =  dfs[0].iloc[3] #2020/109年            
            ls2 =  dfs[0].iloc[4] #108年
            ls3 =  dfs[0].iloc[5] #107年
            ls4 =  dfs[0].iloc[6] #107年
            ls5 =  dfs[0].iloc[7] #105年        
            ls6 =  dfs[0].iloc[8] #104年
           
        
            H0 = ls0[4] #109年目前已出現過的最高價
        #L0 = ls0[6] #109年目前已出現過的最低價

            H1 = ls1[4] #2020/109年最高價
            L1 = ls1[6] #109年最低價


            H2 = ls2[4] #2019/108年最高價
            L2 = ls2[6] #108年最低價

            H3 = ls3[4] #2018/107年最高價
            L3 = ls3[6] #107年最低價

            H4 = ls4[4] #2017/106年最高價
            L4 = ls4[6] #106年最低價

            H5 = ls5[4] #105年最高價
            L5 = ls5[6] #105年最低價

            H6 = ls6[4] #104年最高價
            L6 = ls6[6] #104年最低價
            #print(tablelen)


            bank_url0 = 'https://djinfo.cathaysec.com.tw/z/zc/zcq/zcq0.djhtm?b=Y&a=' #國泰世華
#sheet_type = 'z/zc/zcq/zcq_' #ISQ 合併損益表 季表

            url = bank_url0 + stock_id
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.content, 'html.parser')
            table = soup.find_all('table')[0];
            dfs = pd.read_html(str(table))

#dfs[2] 真
            if eps1N == '2020':  #在三月時，Q4財報先出來的情況

                eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2020
                eps2 = dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2019
                eps3 = dfs[2][3][98] #最新3年的合併總損益 每股盈餘 2018
                eps4 = dfs[2][4][98] #最新4年的合併總損益 每股盈餘 2017
                eps5 = dfs[2][5][98] #最新5年的合併總損益 每股盈餘 2016
                
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

            elif eps1N == '2019':  #在三月時，Q4財報還沒出來的情況

                eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2019
                eps2 = dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2018
                eps3 = dfs[2][3][98] #最新3年的合併總損益 每股盈餘 2017
                eps4 = dfs[2][4][98] #最新4年的合併總損益 每股盈餘 2017
                eps5 = dfs[2][5][98] #最新5年的合併總損益 每股盈餘 2015
                
                PER_H1 = round(float(H2)/float(eps1),2)  #2019/108本益比 高
                PER_L1 = round(float(L2)/float(eps1),2)  #108本益比 低 

                PER_H2 = round(float(H3)/float(eps2),2)  #107本益比 高
                PER_L2 = round(float(L3)/float(eps2),2)  #107本益比 低 
                
                PER_H3 = round(float(H4)/float(eps3),2)  #106本益比 高
                PER_L3 = round(float(L4)/float(eps3),2)  #106本益比 低 

                PER_H4 = round(float(H5)/float(eps4),2)  #105本益比 高
                PER_L4 = round(float(L5)/float(eps4),2)  #105本益比 低 
    
                PER_H5 = round(float(H6)/float(eps5),2)  #104本益比 高
                PER_L5 = round(float(L6)/float(eps5),2)  #104本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3 + PER_H4 + PER_H5)/5),2)
                PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3 + PER_L4 + PER_L5)/5),2)

                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低
            #print(H1)


    return H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, H6, L6, eps1N
#, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, New_up_profit, New_down_loss, risk_reward, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average, pNet1, pNet2, pNet3, pNet4, pNet4Average, H0, thisYear_Sum, theRest_Predict
