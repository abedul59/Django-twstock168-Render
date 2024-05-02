# -*- coding: utf-8 -*-
"""
Created on Sat May 16 12:58:13 2020

@author: Farland
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
            ls6 =  None #104年
            
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

            H6 = None #104年最高價
            L6 = None #104年最低價
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
                eps5 = None #最新5年的合併總損益 每股盈餘 2015/104
    
    ####2020/07/02 加入本益比成長率
                PER_H1 = round(float(H1)/float(eps1),2)  #2020/109本益比 高
                PER_L1 = round(float(L1)/float(eps1),2)  #109本益比 低 

                PER_H2 = round(float(H2)/float(eps2),2)  #108本益比 高
                PER_L2 = round(float(L2)/float(eps2),2)  #108本益比 低 

                PER_H3 = round(float(H3)/float(eps3),2)  #107本益比 高
                PER_L3 = round(float(L3)/float(eps3),2)  #107本益比 低 

                PER_H4 = round(float(H4)/float(eps4),2)  #106本益比 高
                PER_L4 = round(float(L4)/float(eps4),2)  #106本益比 低 
    
                PER_H5 = None  #104本益比 高
                PER_L5 = None  #104本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3 + PER_H4)/4),2)
                PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3 + PER_L4)/4),2)

                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低
                
            elif eps1N == '2019':  #在三月時，Q4財報還沒出來的情況
            
                eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2019
                eps2 = dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2018
                eps3 = dfs[2][3][98] #最新3年的合併總損益 每股盈餘 2017
                eps4 = dfs[2][4][98] #最新4年的合併總損益 每股盈餘 2016/105
                eps5 = None #最新5年的合併總損益 每股盈餘 2015/104
    
    ####2020/07/02 加入本益比成長率
                PER_H1 = round(float(H2)/float(eps1),2)  #2019/108本益比 高
                PER_L1 = round(float(L2)/float(eps1),2)  #108本益比 低 

                PER_H2 = round(float(H3)/float(eps2),2)  #107本益比 高
                PER_L2 = round(float(L3)/float(eps2),2)  #107本益比 低 

                PER_H3 = round(float(H4)/float(eps3),2)  #106本益比 高
                PER_L3 = round(float(L4)/float(eps3),2)  #106本益比 低 

                PER_H4 = round(float(H5)/float(eps4),2)  #105本益比 高
                PER_L4 = round(float(L5)/float(eps4),2)  #105本益比 低 
    
                PER_H5 = None  #104本益比 高
                PER_L5 = None  #104本益比 低 

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
            
            H5 = None #105年最高價
            L5 = None #105年最低價

            H6 = None #104年最高價
            L6 = None #104年最低價
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
                eps4 = None #最新4年的合併總損益 每股盈餘 2017/106
                eps5 = None #最新5年的合併總損益 每股盈餘 2016/105
    
    ####2020/07/02 加入本益比成長率
                PER_H1 = round(float(H1)/float(eps1),2)  #2020/109本益比 高
                PER_L1 = round(float(L1)/float(eps1),2)  #109本益比 低 

                PER_H2 = round(float(H2)/float(eps2),2)  #108本益比 高
                PER_L2 = round(float(L2)/float(eps2),2)  #108本益比 低 

                PER_H3 = round(float(H3)/float(eps3),2)  #107本益比 高
                PER_L3 = round(float(L3)/float(eps3),2)  #107本益比 低 

                PER_H4 = None  #106本益比 高
                PER_L4 = None  #106本益比 低 
    
                PER_H5 = None  #105本益比 高
                PER_L5 = None  #105本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3)/3),2)
                PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3)/3),2)

                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低

            elif eps1N == '2019':  #在三月時，Q4財報還沒出來的情況
            
                eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2019
                eps2 = dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2018
                eps3 = dfs[2][3][98] #最新3年的合併總損益 每股盈餘 2017
                eps4 = None #最新4年的合併總損益 每股盈餘 2016/105
                eps5 = None #最新5年的合併總損益 每股盈餘 2015/104
    
    ####2020/07/02 加入本益比成長率
                PER_H1 = round(float(H2)/float(eps1),2)  #2019/108本益比 高
                PER_L1 = round(float(L2)/float(eps1),2)  #108本益比 低 

                PER_H2 = round(float(H3)/float(eps2),2)  #107本益比 高
                PER_L2 = round(float(L3)/float(eps2),2)  #107本益比 低 

                PER_H3 = round(float(H4)/float(eps3),2)  #106本益比 高
                PER_L3 = round(float(L4)/float(eps3),2)  #106本益比 低 

                PER_H4 = None  #105本益比 高
                PER_L4 = None  #105本益比 低 
    
                PER_H5 = None  #104本益比 高
                PER_L5 = None  #104本益比 低 

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

            H4 = None #106年最高價
            L4 = None #106年最低價
            
            H5 = None #105年最高價
            L5 = None #105年最低價

            H6 = None #104年最高價
            L6 = None #104年最低價
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
                eps3 = None #最新3年的合併總損益 每股盈餘 2018
                eps4 = None #最新4年的合併總損益 每股盈餘 2017
                eps5 = None #最新5年的合併總損益 每股盈餘 2016
    
    ####2020/07/02 加入本益比成長率
            #2021/1/6 更改
                PER_H1 = round(float(H1)/float(eps1),2)  #2020/109本益比 高
                PER_L1 = round(float(L1)/float(eps1),2)  #109本益比 低 

                PER_H2 = round(float(H2)/float(eps2),2)  #108本益比 高
                PER_L2 = round(float(L2)/float(eps2),2)  #108本益比 低 

                PER_H3 = None  #106本益比 高
                PER_L3 = None  #106本益比 低 

                PER_H4 = None  #105本益比 高
                PER_L4 = None  #105本益比 低 
    
                PER_H5 = None  #104本益比 高
                PER_L5 = None  #104本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2)/2),2)
                PER_L_average = round(float((PER_L1 + PER_L2)/2),2)

                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低

            elif eps1N == '2019':  #在三月時，Q4財報還沒出來的情況

                eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2019
                eps2 = dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2018
                eps3 = None #最新3年的合併總損益 每股盈餘 2017
                eps4 = None #最新4年的合併總損益 每股盈餘 2016
                eps5 = None #最新5年的合併總損益 每股盈餘 2015
    
    ####2020/07/02 加入本益比成長率
            #2021/1/6 更改
                PER_H1 = round(float(H2)/float(eps1),2)  #2019/108本益比 高
                PER_L1 = round(float(L2)/float(eps1),2)  #108本益比 低 

                PER_H2 = round(float(H3)/float(eps2),2)  #107本益比 高
                PER_L2 = round(float(L3)/float(eps2),2)  #107本益比 低 

                PER_H3 = None  #106本益比 高
                PER_L3 = None  #106本益比 低 

                PER_H4 = None  #105本益比 高
                PER_L4 = None  #105本益比 低 
    
                PER_H5 = None  #104本益比 高
                PER_L5 = None  #104本益比 低 

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
            ls3 =  None #107年
            ls4 =  None #106年
            ls5 =  None #105年
            ls6 =  None #104年

            H0 = ls0[4] #110年目前已出現過的最高價
        #L0 = ls0[6] #109年目前已出現過的最低價

            H1 = ls1[4] #109/2020年最高價
            L1 = ls1[6] #109年最低價

            H2 = ls2[4] #108年最高價
            L2 = ls2[6] #108年最低價

            H3 = None #107年最高價
            L3 = None #107年最低價

            H4 = None #106年最高價
            L4 = None #106年最低價
            
            H5 = None #105年最高價
            L5 = None #105年最低價

            H6 = None #104年最高價
            L6 = None #104年最低價
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
                eps2 = None #最新2年的合併總損益 每股盈餘 2019
                eps3 = None #最新3年的合併總損益 每股盈餘 2018
                eps4 = None #最新4年的合併總損益 每股盈餘 2017
                eps5 = None #最新5年的合併總損益 每股盈餘 2016
    
    ####2020/07/02 加入本益比成長率
            #2021/1/6 更改
                PER_H1 = round(float(H1)/float(eps1),2)  #2020/109本益比 高
                PER_L1 = round(float(L1)/float(eps1),2)  #109本益比 低 

                PER_H2 = None  #107本益比 高
                PER_L2 = None  #107本益比 低 

                PER_H3 = None  #106本益比 高
                PER_L3 = None  #106本益比 低 

                PER_H4 = None  #105本益比 高
                PER_L4 = None  #105本益比 低 
    
                PER_H5 = None  #104本益比 高
                PER_L5 = None  #104本益比 低 

                PER_H_average =  PER_H1 #round(float((PER_H1 + PER_H2)/2),2)
                PER_L_average = PER_L1 #round(float((PER_L1 + PER_L2)/2),2)

                PER_H = PER_H_average #min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = PER_L_average #min(PER_L_average,PER_L1)  #本益比低點與最新孰低


            elif eps1N == '2019':  #在三月時，Q4財報還沒出來的情況

                eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2019
                eps2 = None #最新2年的合併總損益 每股盈餘 2018
                eps3 = None #最新3年的合併總損益 每股盈餘 2017
                eps4 = None #最新4年的合併總損益 每股盈餘 2017
                eps5 = None #最新5年的合併總損益 每股盈餘 2015
    
    ####2020/07/02 加入本益比成長率
            #2021/1/6 更改
                PER_H1 = round(float(H2)/float(eps1),2)  #2019/108本益比 高
                PER_L1 = round(float(L2)/float(eps1),2)  #108本益比 低 

                PER_H2 = None  #107本益比 高
                PER_L2 = None  #107本益比 低 

                PER_H3 = None  #106本益比 高
                PER_L3 = None  #106本益比 低 

                PER_H4 = None  #105本益比 高
                PER_L4 = None  #105本益比 低 
    
                PER_H5 = None  #104本益比 高
                PER_L5 = None  #104本益比 低 

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

      


    
#############################################################以下為本益比區間程式
def PERseg(stock_id, month_id):
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
              
        ##抓取上市今年最高價 一個月一個月抓，再算最大值
        twse_url2 = 'http://www.twse.com.tw/exchangeReport/FMSRFK?response=html&stockNo=' 
        url = twse_url2 + stock_id 
        r2 = requests.get(url, headers=headers)
        soup2 = BeautifulSoup(r2.content, 'lxml')
        table2 = soup2.find_all('table')[0];
        dfs2 = pd.read_html(str(table2))

        monthlen = len(dfs2[0]) #計算有幾個欄位（幾個月份）
        
        print(monthlen)
    #dfs[0].iloc[m-1] #109年1月
        priceGroup = []

        if monthlen == 1 :   ##不分流會發生錯誤#20210201
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)
            print(lm1)
        elif monthlen == 2 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)
            #print(lm1)        
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)
            #print(lm2)        
        elif monthlen == 3 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)       
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)          
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3)        
        elif monthlen == 4 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)       
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)          
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
        elif monthlen == 5 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)       
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)          
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
            lm5  = dfs2[0].iloc[int(monthlen)-5][2] #110年最新的5個月最高價
            priceGroup.append(lm5)
        elif monthlen == 6 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)       
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)          
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
            lm5  = dfs2[0].iloc[int(monthlen)-5][2] #110年最新的5個月最高價
            priceGroup.append(lm5)
            lm6  = dfs2[0].iloc[int(monthlen)-6][2] #110年最新的6個月最高價
            priceGroup.append(lm6)
        elif monthlen == 7 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)       
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)          
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
            lm5  = dfs2[0].iloc[int(monthlen)-5][2] #110年最新的5個月最高價
            priceGroup.append(lm5)
            lm6  = dfs2[0].iloc[int(monthlen)-6][2] #110年最新的6個月最高價
            priceGroup.append(lm6)
            lm7  = dfs2[0].iloc[int(monthlen)-7][2] #110年最新的7個月最高價
            priceGroup.append(lm7)
        elif monthlen == 8 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)       
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)          
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
            lm5  = dfs2[0].iloc[int(monthlen)-5][2] #110年最新的5個月最高價
            priceGroup.append(lm5)
            lm6  = dfs2[0].iloc[int(monthlen)-6][2] #110年最新的6個月最高價
            priceGroup.append(lm6)
            lm7  = dfs2[0].iloc[int(monthlen)-7][2] #110年最新的7個月最高價
            priceGroup.append(lm7)
            lm8  = dfs2[0].iloc[int(monthlen)-8][2] #110年最新的8個月最高價
            priceGroup.append(lm8)

        elif monthlen == 9 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)       
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)          
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
            lm5  = dfs2[0].iloc[int(monthlen)-5][2] #110年最新的5個月最高價
            priceGroup.append(lm5)
            lm6  = dfs2[0].iloc[int(monthlen)-6][2] #110年最新的6個月最高價
            priceGroup.append(lm6)
            lm7  = dfs2[0].iloc[int(monthlen)-7][2] #110年最新的7個月最高價
            priceGroup.append(lm7)
            lm8  = dfs2[0].iloc[int(monthlen)-8][2] #110年最新的8個月最高價
            priceGroup.append(lm8)
            lm9  = dfs2[0].iloc[int(monthlen)-9][2] #110年最新的9個月最高價
            priceGroup.append(lm9)

        elif monthlen == 10 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)       
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)          
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
            lm5  = dfs2[0].iloc[int(monthlen)-5][2] #110年最新的5個月最高價
            priceGroup.append(lm5)
            lm6  = dfs2[0].iloc[int(monthlen)-6][2] #110年最新的6個月最高價
            priceGroup.append(lm6)
            lm7  = dfs2[0].iloc[int(monthlen)-7][2] #110年最新的7個月最高價
            priceGroup.append(lm7)
            lm8  = dfs2[0].iloc[int(monthlen)-8][2] #110年最新的8個月最高價
            priceGroup.append(lm8)
            lm9  = dfs2[0].iloc[int(monthlen)-9][2] #110年最新的9個月最高價
            priceGroup.append(lm9)
            lm10  = dfs2[0].iloc[int(monthlen)-10][2] #110年最新的10個月最高價
            priceGroup.append(lm10)
        elif monthlen == 11 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)       
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)          
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
            lm5  = dfs2[0].iloc[int(monthlen)-5][2] #110年最新的5個月最高價
            priceGroup.append(lm5)
            lm6  = dfs2[0].iloc[int(monthlen)-6][2] #110年最新的6個月最高價
            priceGroup.append(lm6)
            lm7  = dfs2[0].iloc[int(monthlen)-7][2] #110年最新的7個月最高價
            priceGroup.append(lm7)
            lm8  = dfs2[0].iloc[int(monthlen)-8][2] #110年最新的8個月最高價
            priceGroup.append(lm8)
            lm9  = dfs2[0].iloc[int(monthlen)-9][2] #110年最新的9個月最高價
            priceGroup.append(lm9)
            lm10  = dfs2[0].iloc[int(monthlen)-10][2] #110年最新的10個月最高價
            priceGroup.append(lm10)
            lm11  = dfs2[0].iloc[int(monthlen)-11][2] #110年最新的11個月最高價
            priceGroup.append(lm11)
        elif monthlen == 12 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)       
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)          
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
            lm5  = dfs2[0].iloc[int(monthlen)-5][2] #110年最新的5個月最高價
            priceGroup.append(lm5)
            lm6  = dfs2[0].iloc[int(monthlen)-6][2] #110年最新的6個月最高價
            priceGroup.append(lm6)
            lm7  = dfs2[0].iloc[int(monthlen)-7][2] #110年最新的7個月最高價
            priceGroup.append(lm7)
            lm8  = dfs2[0].iloc[int(monthlen)-8][2] #110年最新的8個月最高價
            priceGroup.append(lm8)
            lm9  = dfs2[0].iloc[int(monthlen)-9][2] #110年最新的9個月最高價
            priceGroup.append(lm9)
            lm10  = dfs2[0].iloc[int(monthlen)-10][2] #110年最新的10個月最高價
            priceGroup.append(lm10)
            lm11  = dfs2[0].iloc[int(monthlen)-11][2] #110年最新的11個月最高價
            priceGroup.append(lm11)
            lm12  = dfs2[0].iloc[int(monthlen)-12][2] #110年最新的12個月最高價
            priceGroup.append(lm12)     
    
        thisYearMax = max(priceGroup)
        H0 = str(thisYearMax)  #110年目前已出現過的最高價
        #print(priceGroup)
        #print(thisYearMax)
        
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
            ls6 =  None #104年
            
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

            H6 = None #104年最高價
            L6 = None #104年最低價
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
                eps5 = None #最新5年的合併總損益 每股盈餘 2015/104
    
    ####2020/07/02 加入本益比成長率
                PER_H1 = round(float(H1)/float(eps1),2)  #2020/109本益比 高
                PER_L1 = round(float(L1)/float(eps1),2)  #109本益比 低 

                PER_H2 = round(float(H2)/float(eps2),2)  #108本益比 高
                PER_L2 = round(float(L2)/float(eps2),2)  #108本益比 低 

                PER_H3 = round(float(H3)/float(eps3),2)  #107本益比 高
                PER_L3 = round(float(L3)/float(eps3),2)  #107本益比 低 

                PER_H4 = round(float(H4)/float(eps4),2)  #106本益比 高
                PER_L4 = round(float(L4)/float(eps4),2)  #106本益比 低 
    
                PER_H5 = None  #104本益比 高
                PER_L5 = None  #104本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3 + PER_H4)/4),2)
                PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3 + PER_L4)/4),2)

                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低
                
            elif eps1N == '2019':  #在三月時，Q4財報還沒出來的情況
            
                eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2019
                eps2 = dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2018
                eps3 = dfs[2][3][98] #最新3年的合併總損益 每股盈餘 2017
                eps4 = dfs[2][4][98] #最新4年的合併總損益 每股盈餘 2016/105
                eps5 = None #最新5年的合併總損益 每股盈餘 2015/104
    
    ####2020/07/02 加入本益比成長率
                PER_H1 = round(float(H2)/float(eps1),2)  #2019/108本益比 高
                PER_L1 = round(float(L2)/float(eps1),2)  #108本益比 低 

                PER_H2 = round(float(H3)/float(eps2),2)  #107本益比 高
                PER_L2 = round(float(L3)/float(eps2),2)  #107本益比 低 

                PER_H3 = round(float(H4)/float(eps3),2)  #106本益比 高
                PER_L3 = round(float(L4)/float(eps3),2)  #106本益比 低 

                PER_H4 = round(float(H5)/float(eps4),2)  #105本益比 高
                PER_L4 = round(float(L5)/float(eps4),2)  #105本益比 低 
    
                PER_H5 = None  #104本益比 高
                PER_L5 = None  #104本益比 低 

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
            
            H5 = None #105年最高價
            L5 = None #105年最低價

            H6 = None #104年最高價
            L6 = None #104年最低價
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
                eps4 = None #最新4年的合併總損益 每股盈餘 2017/106
                eps5 = None #最新5年的合併總損益 每股盈餘 2016/105
    
    ####2020/07/02 加入本益比成長率
                PER_H1 = round(float(H1)/float(eps1),2)  #2020/109本益比 高
                PER_L1 = round(float(L1)/float(eps1),2)  #109本益比 低 

                PER_H2 = round(float(H2)/float(eps2),2)  #108本益比 高
                PER_L2 = round(float(L2)/float(eps2),2)  #108本益比 低 

                PER_H3 = round(float(H3)/float(eps3),2)  #107本益比 高
                PER_L3 = round(float(L3)/float(eps3),2)  #107本益比 低 

                PER_H4 = None  #106本益比 高
                PER_L4 = None  #106本益比 低 
    
                PER_H5 = None  #105本益比 高
                PER_L5 = None  #105本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3)/3),2)
                PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3)/3),2)

                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低

            elif eps1N == '2019':  #在三月時，Q4財報還沒出來的情況
            
                eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2019
                eps2 = dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2018
                eps3 = dfs[2][3][98] #最新3年的合併總損益 每股盈餘 2017
                eps4 = None #最新4年的合併總損益 每股盈餘 2016/105
                eps5 = None #最新5年的合併總損益 每股盈餘 2015/104
    
    ####2020/07/02 加入本益比成長率
                PER_H1 = round(float(H2)/float(eps1),2)  #2019/108本益比 高
                PER_L1 = round(float(L2)/float(eps1),2)  #108本益比 低 

                PER_H2 = round(float(H3)/float(eps2),2)  #107本益比 高
                PER_L2 = round(float(L3)/float(eps2),2)  #107本益比 低 

                PER_H3 = round(float(H4)/float(eps3),2)  #106本益比 高
                PER_L3 = round(float(L4)/float(eps3),2)  #106本益比 低 

                PER_H4 = None  #105本益比 高
                PER_L4 = None  #105本益比 低 
    
                PER_H5 = None  #104本益比 高
                PER_L5 = None  #104本益比 低 

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

            H4 = None #106年最高價
            L4 = None #106年最低價
            
            H5 = None #105年最高價
            L5 = None #105年最低價

            H6 = None #104年最高價
            L6 = None #104年最低價
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
                eps3 = None #最新3年的合併總損益 每股盈餘 2018
                eps4 = None #最新4年的合併總損益 每股盈餘 2017
                eps5 = None #最新5年的合併總損益 每股盈餘 2016
    
    ####2020/07/02 加入本益比成長率
            #2021/1/6 更改
                PER_H1 = round(float(H1)/float(eps1),2)  #2020/109本益比 高
                PER_L1 = round(float(L1)/float(eps1),2)  #109本益比 低 

                PER_H2 = round(float(H2)/float(eps2),2)  #108本益比 高
                PER_L2 = round(float(L2)/float(eps2),2)  #108本益比 低 

                PER_H3 = None  #106本益比 高
                PER_L3 = None  #106本益比 低 

                PER_H4 = None  #105本益比 高
                PER_L4 = None  #105本益比 低 
    
                PER_H5 = None  #104本益比 高
                PER_L5 = None  #104本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2)/2),2)
                PER_L_average = round(float((PER_L1 + PER_L2)/2),2)

                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低

            elif eps1N == '2019':  #在三月時，Q4財報還沒出來的情況

                eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2019
                eps2 = dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2018
                eps3 = None #最新3年的合併總損益 每股盈餘 2017
                eps4 = None #最新4年的合併總損益 每股盈餘 2016
                eps5 = None #最新5年的合併總損益 每股盈餘 2015
    
    ####2020/07/02 加入本益比成長率
            #2021/1/6 更改
                PER_H1 = round(float(H2)/float(eps1),2)  #2019/108本益比 高
                PER_L1 = round(float(L2)/float(eps1),2)  #108本益比 低 

                PER_H2 = round(float(H3)/float(eps2),2)  #107本益比 高
                PER_L2 = round(float(L3)/float(eps2),2)  #107本益比 低 

                PER_H3 = None  #106本益比 高
                PER_L3 = None  #106本益比 低 

                PER_H4 = None  #105本益比 高
                PER_L4 = None  #105本益比 低 
    
                PER_H5 = None  #104本益比 高
                PER_L5 = None  #104本益比 低 

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
            ls3 =  None #107年
            ls4 =  None #106年
            ls5 =  None #105年
            ls6 =  None #104年

            H0 = ls0[4] #110年目前已出現過的最高價
        #L0 = ls0[6] #109年目前已出現過的最低價

            H1 = ls1[4] #109/2020年最高價
            L1 = ls1[6] #109年最低價

            H2 = ls2[4] #108年最高價
            L2 = ls2[6] #108年最低價

            H3 = None #107年最高價
            L3 = None #107年最低價

            H4 = None #106年最高價
            L4 = None #106年最低價
            
            H5 = None #105年最高價
            L5 = None #105年最低價

            H6 = None #104年最高價
            L6 = None #104年最低價
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
                eps2 = None #最新2年的合併總損益 每股盈餘 2019
                eps3 = None #最新3年的合併總損益 每股盈餘 2018
                eps4 = None #最新4年的合併總損益 每股盈餘 2017
                eps5 = None #最新5年的合併總損益 每股盈餘 2016
    
    ####2020/07/02 加入本益比成長率
            #2021/1/6 更改
                PER_H1 = round(float(H1)/float(eps1),2)  #2020/109本益比 高
                PER_L1 = round(float(L1)/float(eps1),2)  #109本益比 低 

                PER_H2 = None  #107本益比 高
                PER_L2 = None  #107本益比 低 

                PER_H3 = None  #106本益比 高
                PER_L3 = None  #106本益比 低 

                PER_H4 = None  #105本益比 高
                PER_L4 = None  #105本益比 低 
    
                PER_H5 = None  #104本益比 高
                PER_L5 = None  #104本益比 低 

                PER_H_average =  PER_H1 #round(float((PER_H1 + PER_H2)/2),2)
                PER_L_average = PER_L1 #round(float((PER_L1 + PER_L2)/2),2)

                PER_H = PER_H_average #min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = PER_L_average #min(PER_L_average,PER_L1)  #本益比低點與最新孰低


            elif eps1N == '2019':  #在三月時，Q4財報還沒出來的情況

                eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2019
                eps2 = None #最新2年的合併總損益 每股盈餘 2018
                eps3 = None #最新3年的合併總損益 每股盈餘 2017
                eps4 = None #最新4年的合併總損益 每股盈餘 2017
                eps5 = None #最新5年的合併總損益 每股盈餘 2015
    
    ####2020/07/02 加入本益比成長率
            #2021/1/6 更改
                PER_H1 = round(float(H2)/float(eps1),2)  #2019/108本益比 高
                PER_L1 = round(float(L2)/float(eps1),2)  #108本益比 低 

                PER_H2 = None  #107本益比 高
                PER_L2 = None  #107本益比 低 

                PER_H3 = None  #106本益比 高
                PER_L3 = None  #106本益比 低 

                PER_H4 = None  #105本益比 高
                PER_L4 = None  #105本益比 低 
    
                PER_H5 = None  #104本益比 高
                PER_L5 = None  #104本益比 低 

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
##########
########################2021/2/28新增單季EPS計算 取代整年營收估EPS計算
    bank_url = 'https://djinfo.cathaysec.com.tw/' #國泰世華
    headers = {'Referer':my_Referer,'user-agent': my_UserAgent}
    sheet_type = 'z/zc/zcr/zcr_' #FRQ 財務比率 季表
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs5 = pd.read_html(str(table))
    
    #newest_Fin_Q = str(dfs5[2][1][1]) #最新1季的財報季份

    epsq1N = dfs5[2][1][1] #最新1季的名稱
    #epsq2N = dfs5[2][2][1] #最新2季的名稱
    #epsq3N = dfs5[2][3][1] #最新3季的名稱
    #epsq4N = dfs5[2][4][1] #最新4季的名稱
    #epsq5N = dfs5[2][5][1] #最新5季的名稱
    #epsq6N = dfs5[2][6][1] #最新6季的名稱
    #epsq7N = dfs5[2][7][1] #最新7季的名稱
    #epsq8N = dfs5[2][8][1] #最新8季的名稱
    

    epsq1 = float((dfs5[2][1][25])) #最新1季的EPS
    epsq2 = float((dfs5[2][2][25])) #最新2季的EPS
    epsq3 = float((dfs5[2][3][25])) #最新3季的EPS
    epsq4 = float((dfs5[2][4][25])) #最新4季的EPS
    epsq5 = float((dfs5[2][5][25])) #最新5季的EPS
    epsq6 = float((dfs5[2][6][25])) #最新6季的EPS
    epsq7 = float((dfs5[2][7][25])) #最新7季的EPS
    epsq8 = float((dfs5[2][8][25])) #最新8季的EPS


#print(PER_H)
#print(PER_L)
##############################################取得營收
############################
    sheet_type = 'z/zc/zch/zch_' #Rev 營收
    #stock_id = "3034"
    bank_url = 'https://djinfo.cathaysec.com.tw/' #國泰世華
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
    
    pYoY1 = str(round(rYoY1*100,2))+'%'
    pYoY2 = str(round(rYoY2*100,2))+'%'
    pYoY3 = str(round(rYoY3*100,2))+'%'
    pYoY4 = str(round(rYoY4*100,2))+'%'
    pYoY5 = str(round(rYoY5*100,2))+'%'
    pYoY6 = str(round(rYoY6*100,2))+'%'
    
    

    rYoY6Average  = (rYoY1+rYoY2+rYoY3+rYoY4+rYoY5+rYoY6)/6 #最新六個月營收平均
#print(rYoY6Average)
    pYoY6Average = str(round(rYoY6Average*100,2))+'%'

    RevYoY = round(min(rYoY6Average,rYoY1),4) #兩者擇一較低
    
    pRevYoY = str(round(RevYoY*100,2))+'%'

    #return H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average 



##############################以下開始預估未來一整年的營收，

#print(RevYoY)
    if (month_id == '4'): 
        ##########################月份名稱############
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
        ##########################各月份營收############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 109/4
        r2 = int(dfs[2][1][7])/100000  #109/3
        r3 = int(dfs[2][1][8])/100000  #109/2
        r4 = int(dfs[2][1][9])/100000  #109/1
    
    #r1_9Sum = Jan_Sep_Sum = r1+r2+r3+r4+r5+r6+r7+r8+r9 #今年1-9月營收
        thisYear_Sum = r1+r2+r3+r4 #今年1-4月營收

        r5 = int(dfs[2][1][10])/100000  #108/12
        r6 = int(dfs[2][1][11])/100000  #108/11
        r7 = int(dfs[2][1][12])/100000  #108/10
        r8 = int(dfs[2][1][13])/100000  #108/9
        r9 = int(dfs[2][1][14])/100000  #108/8
        r10 = int(dfs[2][1][15])/100000  #108/7
        r11 = int(dfs[2][1][16])/100000  #108/6
        r12 = int(dfs[2][1][17])/100000  #108/5

    #r10_12Sum_Predict = (r10+r11+r12)*(1+RevYoY) #預估今年10-12月營收
        theRest_Predict = (r5+r6+r7+r8+r9+r10+r11+r12)*(1+RevYoY) #預估今年10-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #預估今年全年營收

        if epsq1N == '2020.4Q' :
            Q4_Rev_Predict = None
        else:            
            Q4_Rev_Predict = r5+r6+r7 #2020/10,11,12月營收

    elif (month_id == '1'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 110/1

    
        thisYear_Sum = r1 #今年已公布營收 1月營收
        
        r2 = int(dfs[2][1][7])/100000  #109/12
        r3 = int(dfs[2][1][8])/100000  #109/11
        r4 = int(dfs[2][1][9])/100000  #109/10
        r5 = int(dfs[2][1][10])/100000  #109/9
        r6 = int(dfs[2][1][11])/100000  #109/8
        r7 = int(dfs[2][1][12])/100000  #109/7
        r8 = int(dfs[2][1][13])/100000  #109/6
        r9 = int(dfs[2][1][14])/100000  #109/5
        r10 = int(dfs[2][1][15])/100000  #109/4
        r11 = int(dfs[2][1][16])/100000  #109/3
        r12 = int(dfs[2][1][17])/100000  #109/2


        theRest_Predict = (r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12)*(1+RevYoY) #預估今年10-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #預估今年全年營收

        ###2021/2/28新增單季eps
        #估計2020Q4 EPS 因為尚未公佈
        Q4_Rev_Predict = r2+r3+r4 #2020/10,11,12月營收

    elif (month_id == '2'):  #3月整個月都會在公佈前一年Q4營收，會同時有Q3和Q4財報並存現象
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
    
        thisYear_Sum = r1+r2 #今年已公布營收 1-2月營收
        
        
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000  
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000
        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000


        theRest_Predict = (r3+r4+r5+r6+r7+r8+r9+r10+r11+r12)*(1+RevYoY) #預估今年10-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #預估今年全年營收

        if epsq1N == '2020.4Q' :
            Q4_Rev_Predict = None
        else:            
            Q4_Rev_Predict = r3+r4+r5 #2020/10,11,12月營收

    elif (month_id == '3'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        
        thisYear_Sum = r1+r2+r3 #今年已公布營收 1-3月營收
        
        

        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000  
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000
        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000


        theRest_Predict = (r4+r5+r6+r7+r8+r9+r10+r11+r12)*(1+RevYoY) #預估今年4-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #預估今年全年營收

        if epsq1N == '2020.4Q' :
            Q4_Rev_Predict = None
        else:            
            Q4_Rev_Predict = r4+r5+r6 #2020/10,11,12月營收

    elif (month_id == '5'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        
        thisYear_Sum = r1+r2+r3+r4+r5 #今年已公布營收 1-5月營收
        
        


        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000  
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000
        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000


        theRest_Predict = (r6+r7+r8+r9+r10+r11+r12)*(1+RevYoY) #預估今年6-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #預估今年全年營收

        if epsq1N == '2020.4Q' :
            Q4_Rev_Predict = None
        else:            
            Q4_Rev_Predict = r6+r7+r8 #2020/10,11,12月營收


    elif (month_id == '6'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        
        thisYear_Sum = r1+r2+r3+r4+r5+r6 #今年已公布營收 1-6月營收
        
        
        r7 = int(dfs[2][1][12])/100000  
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000
        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000


        theRest_Predict = (r7+r8+r9+r10+r11+r12)*(1+RevYoY) #預估今年7-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #預估今年全年營收

    elif (month_id == '7'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000 
        
        thisYear_Sum = r1+r2+r3+r4+r5+r6+r7 #今年已公布營收 1-7月營收
        
         
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000
        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000


        theRest_Predict = (r8+r9+r10+r11+r12)*(1+RevYoY) #預估今年8-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #預估今年全年營收

    elif (month_id == '8'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000 
        r8 = int(dfs[2][1][13])/100000
        
        thisYear_Sum = r1+r2+r3+r4+r5+r6+r7+r8 #今年已公布營收 1-7月營收
        
        
        r9 = int(dfs[2][1][14])/100000
        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000


        theRest_Predict = (r9+r10+r11+r12)*(1+RevYoY) #預估今年9-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #預估今年全年營收



########################################暑假過後，只能估算明年的數字
    elif (month_id == '9'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000 
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000 
       
        thisYear_Sum = r1+r2+r3+r4+r5+r6+r7+r8+r9 #今年已公布營收 1-9月營收
        
        

        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000


        theRest_Predict = (r10+r11+r12)*(1+RevYoY) #預估今年10-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #預估明年全年營收

    elif (month_id == '10'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000 
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000 
        r10 = int(dfs[2][1][15])/100000
        
        thisYear_Sum = r1+r2+r3+r4+r5+r6+r7+r8+r9+r10 #今年已公布營收 1-10月營收
        
        
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000


        theRest_Predict = (r11+r12)*(1+RevYoY) #預估今年11-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #預估明年全年營收

    elif (month_id == '11'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000 
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000 
        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        
        thisYear_Sum = r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11 #今年已公布營收 1-11月營收
        
        

        r12 = int(dfs[2][1][17])/100000


        theRest_Predict = (r12)*(1+RevYoY) #預估今年12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #預估明年全年營收

    elif (month_id == '12'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000 
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000 
        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000
        
        thisYear_Sum = r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12 #去年已公布營收 1-12月營收
        #其實是lastYear_Sum 因為名字要一致 才不出錯
        

        


        theRest_Predict = thisYear_Sum*(1+RevYoY) #預估今年全年營收


        Rev_Predict = round(theRest_Predict, 4) #預估今年全年營收

        Q4_Rev_Predict = r1+r2+r3 #2020/10,11,12月營收
##################################取得稅後淨利率

    bank_url = 'https://djinfo.cathaysec.com.tw/' #國泰世華
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
    
    pNet1 = str(round(Net1*100,2))+'%'
    pNet2 = str(round(Net2*100,2))+'%'
    pNet3 = str(round(Net3*100,2))+'%'
    pNet4 = str(round(Net4*100,2))+'%'

    Net4Average = (Net1+Net2+Net3+Net4)/4
    
    pNet4Average = str(round(Net4Average*100,2))+'%'

#print(Net4Average)

###############預估 淨利 EPS
    Net_Predict = round(Rev_Predict*Net4Average,6)
    #2021/2/28新增  20210726省略下面if..else...
    #if epsq1N == '2020.4Q' :
        
        #Q4_Net_Predict = None
        
    #else:
        #Q4_Net_Predict = None
        #round(Q4_Rev_Predict*Net4Average,6)  #暫時省略20210726
#print(Net_Predict)

####################################################取得股本


    bank_url0 = 'https://djinfo.cathaysec.com.tw/' #國泰世華
    sheet_type = 'z/zc/zcp/zcpa_' 
    ###MoneyDJ
    url = bank_url0 + sheet_type + stock_id +'.djhtm'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))

    cap1 = round(float(dfs[2][1][80])/100,2) #最新一季股本（單位：百萬） 2020/7/4 要轉換成 億
#print(table)
#stock_id_name = dfs[2][0][0][:-24] #股票代號和名稱
    #stock_name = dfs[2][0][0][0:3] #股票名稱
#latest_trade_date = dfs[2][0][0][-13:-8] #最近交易日
#open = dfs[2][1][1] #開盤價
#high = dfs[2][3][1] #最高價
#low  = dfs[2][5][1] #最低價
#close  = dfs[2][7][1] #收盤價
    capital_stock = cap1 #本來Basic表股本 單位：億
#print(capital_stock)
####################計算預估EPS
    Predict_EPS = round(Net_Predict/capital_stock*10,2) #2021
    #2021/2/28新增  3/12更改Q3 Q4並存情況   2021/7/26省略if...else的部份 注意EPS季份
    Predict_EPS0 = epsq2 + epsq3 + epsq4 + epsq5    
    
    #if epsq1N == '2020.4Q' :
        #Predict_EPS0 = epsq1 + epsq2 + epsq3 + epsq4
    #else:
        #Q4_Predict_EPS = round(Q4_Net_Predict/capital_stock*10,2) #估算2020/Q4 eps
        #Predict_EPS0 = epsq1 + epsq2 + epsq3 + Q4_Predict_EPS #估2020全年EPS 2021/3/31前 尚未公佈
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
    
    
#######################################    

    up_profit = round((Predict_high_price - yahoo_latest_tradePrice)/yahoo_latest_tradePrice,2)
    down_loss = round((Predict_low_price - yahoo_latest_tradePrice)/yahoo_latest_tradePrice,2)

#print(up_profit)
#print(down_loss)

    New_up_profit = str(up_profit*100) + '%'
    New_down_loss = str(down_loss*100) + '%'

#print(New_up_profit)
#print(New_down_loss)

    #risk_reward = round(abs(up_profit)/abs(down_loss),2)
    risk_reward = round(abs(up_profit/down_loss),2)
    
    #print(risk_reward)
    
    return H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, New_up_profit, New_down_loss, risk_reward, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average, pNet1, pNet2, pNet3, pNet4, pNet4Average, H0, thisYear_Sum, theRest_Predict, H6, L6, Predict_EPS0, eps1N
#, epsYoY1, epsYoY2, epsYoY3, epsYoY4, PER_H_YoY1, PER_H_YoY2, PER_H_YoY3, PER_H_YoY4, PEG_H1, PEG_H2, PEG_H3, PEG_H4, PEG_L1, PEG_L2, PEG_L3, PEG_L4 



##############################################
    


def PERsegPEG(stock_id, month_id):
    headers = {'Referer': my_Referer,'user-agent': my_UserAgent}

    ######以下為判斷上市或上櫃，取得年度股價程式
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup    



       

##########
    try:  #查詢上市年股價
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

        H1 = ls1[4] #2020/109年最高價
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

#try:      
  
        if monthlen == 1 :   ##不分流會發生錯誤#20210201
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)
            print(lm1)
        elif monthlen == 2 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)
            #print(lm1)        
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)
            #print(lm2)        
        elif monthlen == 3 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)       
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)          
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3)        
        elif monthlen == 4 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)       
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)          
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
        elif monthlen == 5 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)       
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)          
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
            lm5  = dfs2[0].iloc[int(monthlen)-5][2] #110年最新的5個月最高價
            priceGroup.append(lm5)
        elif monthlen == 6 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)       
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)          
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
            lm5  = dfs2[0].iloc[int(monthlen)-5][2] #110年最新的5個月最高價
            priceGroup.append(lm5)
            lm6  = dfs2[0].iloc[int(monthlen)-6][2] #110年最新的6個月最高價
            priceGroup.append(lm6)
        elif monthlen == 7 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)       
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)          
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
            lm5  = dfs2[0].iloc[int(monthlen)-5][2] #110年最新的5個月最高價
            priceGroup.append(lm5)
            lm6  = dfs2[0].iloc[int(monthlen)-6][2] #110年最新的6個月最高價
            priceGroup.append(lm6)
            lm7  = dfs2[0].iloc[int(monthlen)-7][2] #110年最新的7個月最高價
            priceGroup.append(lm7)
        elif monthlen == 8 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)       
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)          
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
            lm5  = dfs2[0].iloc[int(monthlen)-5][2] #110年最新的5個月最高價
            priceGroup.append(lm5)
            lm6  = dfs2[0].iloc[int(monthlen)-6][2] #110年最新的6個月最高價
            priceGroup.append(lm6)
            lm7  = dfs2[0].iloc[int(monthlen)-7][2] #110年最新的7個月最高價
            priceGroup.append(lm7)
            lm8  = dfs2[0].iloc[int(monthlen)-8][2] #110年最新的8個月最高價
            priceGroup.append(lm8)

        elif monthlen == 9 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)       
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)          
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
            lm5  = dfs2[0].iloc[int(monthlen)-5][2] #110年最新的5個月最高價
            priceGroup.append(lm5)
            lm6  = dfs2[0].iloc[int(monthlen)-6][2] #110年最新的6個月最高價
            priceGroup.append(lm6)
            lm7  = dfs2[0].iloc[int(monthlen)-7][2] #110年最新的7個月最高價
            priceGroup.append(lm7)
            lm8  = dfs2[0].iloc[int(monthlen)-8][2] #110年最新的8個月最高價
            priceGroup.append(lm8)
            lm9  = dfs2[0].iloc[int(monthlen)-9][2] #110年最新的9個月最高價
            priceGroup.append(lm9)

        elif monthlen == 10 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)       
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)          
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
            lm5  = dfs2[0].iloc[int(monthlen)-5][2] #110年最新的5個月最高價
            priceGroup.append(lm5)
            lm6  = dfs2[0].iloc[int(monthlen)-6][2] #110年最新的6個月最高價
            priceGroup.append(lm6)
            lm7  = dfs2[0].iloc[int(monthlen)-7][2] #110年最新的7個月最高價
            priceGroup.append(lm7)
            lm8  = dfs2[0].iloc[int(monthlen)-8][2] #110年最新的8個月最高價
            priceGroup.append(lm8)
            lm9  = dfs2[0].iloc[int(monthlen)-9][2] #110年最新的9個月最高價
            priceGroup.append(lm9)
            lm10  = dfs2[0].iloc[int(monthlen)-10][2] #110年最新的10個月最高價
            priceGroup.append(lm10)
        elif monthlen == 11 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)       
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)          
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
            lm5  = dfs2[0].iloc[int(monthlen)-5][2] #110年最新的5個月最高價
            priceGroup.append(lm5)
            lm6  = dfs2[0].iloc[int(monthlen)-6][2] #110年最新的6個月最高價
            priceGroup.append(lm6)
            lm7  = dfs2[0].iloc[int(monthlen)-7][2] #110年最新的7個月最高價
            priceGroup.append(lm7)
            lm8  = dfs2[0].iloc[int(monthlen)-8][2] #110年最新的8個月最高價
            priceGroup.append(lm8)
            lm9  = dfs2[0].iloc[int(monthlen)-9][2] #110年最新的9個月最高價
            priceGroup.append(lm9)
            lm10  = dfs2[0].iloc[int(monthlen)-10][2] #110年最新的10個月最高價
            priceGroup.append(lm10)
            lm11  = dfs2[0].iloc[int(monthlen)-11][2] #110年最新的11個月最高價
            priceGroup.append(lm11)
        elif monthlen == 12 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)       
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)          
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
            lm5  = dfs2[0].iloc[int(monthlen)-5][2] #110年最新的5個月最高價
            priceGroup.append(lm5)
            lm6  = dfs2[0].iloc[int(monthlen)-6][2] #110年最新的6個月最高價
            priceGroup.append(lm6)
            lm7  = dfs2[0].iloc[int(monthlen)-7][2] #110年最新的7個月最高價
            priceGroup.append(lm7)
            lm8  = dfs2[0].iloc[int(monthlen)-8][2] #110年最新的8個月最高價
            priceGroup.append(lm8)
            lm9  = dfs2[0].iloc[int(monthlen)-9][2] #110年最新的9個月最高價
            priceGroup.append(lm9)
            lm10  = dfs2[0].iloc[int(monthlen)-10][2] #110年最新的10個月最高價
            priceGroup.append(lm10)
            lm11  = dfs2[0].iloc[int(monthlen)-11][2] #110年最新的11個月最高價
            priceGroup.append(lm11)
            lm12  = dfs2[0].iloc[int(monthlen)-12][2] #110年最新的12個月最高價
            priceGroup.append(lm12)     
    
        thisYearMax = max(priceGroup)
        H0 = str(thisYearMax)  #110年目前已出現過的最高價
        #print(priceGroup)
        #print(thisYearMax)
        from decimal import Decimal, ROUND_HALF_UP

################################################接著取得上市股票EPS
        bank_url = 'https://djinfo.cathaysec.com.tw/z/zc/zcq/zcq0.djhtm?b=Y&a=' #國泰世華
#sheet_type = 'z/zc/zcq/zcq_' #ISQ 合併損益表 季表

        url = bank_url + stock_id
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
    
    ####2020/07/02 加入EPS成長率   2020/10/22修改成decimal函數處理四捨五入
            epsYoY1 = str((Decimal((float(eps1)-float(eps2))/float(eps2)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
            epsYoY2 = str((Decimal((float(eps2)-float(eps3))/float(eps3)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
            epsYoY3 = str((Decimal((float(eps3)-float(eps4))/float(eps4)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
            epsYoY4 = str((Decimal((float(eps4)-float(eps5))/float(eps5)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
        
    #epsYoY1 = str(round((float(eps1)-float(eps2))/float(eps2),2)*100) + '%'    
    #epsYoY2 = str(round((float(eps2)-float(eps3))/float(eps3),2)*100) + '%'
    #epsYoY3 = str(round((float(eps3)-float(eps4))/float(eps4),2)*100) + '%'
    #epsYoY4 = str(round((float(eps4)-float(eps5))/float(eps5),2)*100) + '%'
    
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


            PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
            PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低


    ####2020/07/02 加入本益比高點成長率
            PER_H_YoY1  = str(round((PER_H1-PER_H2)/PER_H2,4)*100) + '%'
            PER_H_YoY2  = str(round((PER_H2-PER_H3)/PER_H3,4)*100) + '%'
            PER_H_YoY3  = str(round((PER_H3-PER_H4)/PER_H4,4)*100) + '%'
            PER_H_YoY4  = str(round((PER_H4-PER_H5)/PER_H5,4)*100) + '%'
        
######################2020/07/02 加入PEG
    ##########PEG高點
 
            PEG_H1 = round(PER_H1/round((float(eps1)-float(eps2))/float(eps2),4)/100,2)
            PEG_H2 = round(PER_H2/round((float(eps2)-float(eps3))/float(eps3),4)/100,2)
            PEG_H3 = round(PER_H3/round((float(eps3)-float(eps4))/float(eps4),4)/100,2)
            PEG_H4 = round(PER_H4/round((float(eps4)-float(eps5))/float(eps5),4)/100,2) 
    
    ##########PEG低點


            PEG_L1 = round(PER_L1/round((float(eps1)-float(eps2))/float(eps2),4)/100,2)
            PEG_L2 = round(PER_L2/round((float(eps2)-float(eps3))/float(eps3),4)/100,2)
            PEG_L3 = round(PER_L3/round((float(eps3)-float(eps4))/float(eps4),4)/100,2)
            PEG_L4 = round(PER_L4/round((float(eps4)-float(eps5))/float(eps5),4)/100,2)  



        elif eps1N == '2019':  #在三月時，Q4財報還沒出來的情況
            eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2019
            eps2 = dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2018
            eps3 = dfs[2][3][98] #最新3年的合併總損益 每股盈餘 2017
            eps4 = dfs[2][4][98] #最新4年的合併總損益 每股盈餘 2017
            eps5 = dfs[2][5][98] #最新5年的合併總損益 每股盈餘 2015
    
    ####2020/07/02 加入EPS成長率   2020/10/22修改成decimal函數處理四捨五入
            epsYoY1 = str((Decimal((float(eps1)-float(eps2))/float(eps2)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
            epsYoY2 = str((Decimal((float(eps2)-float(eps3))/float(eps3)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
            epsYoY3 = str((Decimal((float(eps3)-float(eps4))/float(eps4)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
            epsYoY4 = str((Decimal((float(eps4)-float(eps5))/float(eps5)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
        
    #epsYoY1 = str(round((float(eps1)-float(eps2))/float(eps2),2)*100) + '%'    
    #epsYoY2 = str(round((float(eps2)-float(eps3))/float(eps3),2)*100) + '%'
    #epsYoY3 = str(round((float(eps3)-float(eps4))/float(eps4),2)*100) + '%'
    #epsYoY4 = str(round((float(eps4)-float(eps5))/float(eps5),2)*100) + '%'
    
    ####2020/07/02 加入本益比成長率
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


    ####2020/07/02 加入本益比高點成長率
            PER_H_YoY1  = str(round((PER_H1-PER_H2)/PER_H2,4)*100) + '%'
            PER_H_YoY2  = str(round((PER_H2-PER_H3)/PER_H3,4)*100) + '%'
            PER_H_YoY3  = str(round((PER_H3-PER_H4)/PER_H4,4)*100) + '%'
            PER_H_YoY4  = str(round((PER_H4-PER_H5)/PER_H5,4)*100) + '%'
        
######################2020/07/02 加入PEG
    ##########PEG高點
 
            PEG_H1 = round(PER_H1/round((float(eps1)-float(eps2))/float(eps2),4)/100,2)
            PEG_H2 = round(PER_H2/round((float(eps2)-float(eps3))/float(eps3),4)/100,2)
            PEG_H3 = round(PER_H3/round((float(eps3)-float(eps4))/float(eps4),4)/100,2)
            PEG_H4 = round(PER_H4/round((float(eps4)-float(eps5))/float(eps5),4)/100,2) 
    
    ##########PEG低點


            PEG_L1 = round(PER_L1/round((float(eps1)-float(eps2))/float(eps2),4)/100,2)
            PEG_L2 = round(PER_L2/round((float(eps2)-float(eps3))/float(eps3),4)/100,2)
            PEG_L3 = round(PER_L3/round((float(eps3)-float(eps4))/float(eps4),4)/100,2)
            PEG_L4 = round(PER_L4/round((float(eps4)-float(eps5))/float(eps5),4)/100,2)  

    except:    #查詢上櫃年股價，失敗就換查上市股票

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

        tablelen = len(dfs[0])

        #2021/2/18更改
        if (tablelen == 8):  #去掉當年，只有過去5年資料 沒有104
            
            ls0 =  dfs[0].iloc[2] #當年 110年 #2021/1/6更改
            ls1 =  dfs[0].iloc[3] #109年
            ls2 =  dfs[0].iloc[4] #108年
            ls3 =  dfs[0].iloc[5] #107年
            ls4 =  dfs[0].iloc[6] #106年
            ls5 =  dfs[0].iloc[7] #105年
            ls6 =  None #104年


            H0 = ls0[4] #110年目前已出現過的最高價
        #L0 = ls0[6] #109年目前已出現過的最低價

            H1 = ls1[4] #109/2020年最高價
            L1 = ls1[6] #109年最低價
             ############2020EPS尚未公佈
            H2 = ls2[4] #2019/108年最高價
            L2 = ls2[6] #108年最低價

            H3 = ls3[4] #107年最高價
            L3 = ls3[6] #107年最低價

            H4 = ls4[4] #106年最高價
            L4 = ls4[6] #106年最低價
            
            H5 = ls5[4] #105年最高價
            L5 = ls5[6] #105年最低價

            H6 = None #104年最高價
            L6 = None #104年最低價
            print(H0)
            
####################            
            ##########################2021/2/1增添修改
##########################################接著取得EPS
            from decimal import Decimal, ROUND_HALF_UP
                        
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
                eps5 = None #最新5年的合併總損益 每股盈餘 2016/105
    
    ####2020/07/02 加入EPS成長率   2020/10/22修改成decimal函數處理四捨五入
                epsYoY1 = str((Decimal((float(eps1)-float(eps2))/float(eps2)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
                epsYoY2 = str((Decimal((float(eps2)-float(eps3))/float(eps3)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
                epsYoY3 = str((Decimal((float(eps3)-float(eps4))/float(eps4)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
                epsYoY4 = None
  
                PER_H1 = round(float(H1)/float(eps1),2)  #2020/109本益比 高
                PER_L1 = round(float(L1)/float(eps1),2)  #109本益比 低 

                PER_H2 = round(float(H2)/float(eps2),2)  #108本益比 高
                PER_L2 = round(float(L2)/float(eps2),2)  #108本益比 低 

                PER_H3 = round(float(H3)/float(eps3),2)  #107本益比 高
                PER_L3 = round(float(L3)/float(eps3),2)  #107本益比 低 

                PER_H4 = round(float(H4)/float(eps4),2)  #106本益比 高
                PER_L4 = round(float(L4)/float(eps4),2)  #106本益比 低 
    
                PER_H5 = None  #105本益比 高
                PER_L5 = None  #105本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3 + PER_H4)/4),2)
                PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3 + PER_L4)/4),2)
                        
                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低

    ####2020/07/02 加入本益比成長率
                PER_H_YoY1  = str(round((PER_H1-PER_H2)/PER_H2,4)*100) + '%'
                PER_H_YoY2  = str(round((PER_H2-PER_H3)/PER_H3,4)*100) + '%'
                PER_H_YoY3  = str(round((PER_H3-PER_H4)/PER_H4,4)*100) + '%'
                PER_H_YoY4  = None
        
######################2020/07/02 加入PEG
    ##########PEG高點     
                PEG_H1 = round(PER_H1/round((float(eps1)-float(eps2))/float(eps2),4)/100,2)
                PEG_H2 = round(PER_H2/round((float(eps2)-float(eps3))/float(eps3),4)/100,2)
                PEG_H3 = round(PER_H3/round((float(eps3)-float(eps4))/float(eps4),4)/100,2)
                PEG_H4 = None 
    
    ##########PEG低點
                PEG_L1 = round(PER_L1/round((float(eps1)-float(eps2))/float(eps2),4)/100,2)
                PEG_L2 = round(PER_L2/round((float(eps2)-float(eps3))/float(eps3),4)/100,2)
                PEG_L3 = round(PER_L3/round((float(eps3)-float(eps4))/float(eps4),4)/100,2)
                PEG_L4 = None 

            elif eps1N == '2019':  #在三月時，Q4財報還沒出來的情況
            
                eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2019
                eps2 = dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2018
                eps3 = dfs[2][3][98] #最新3年的合併總損益 每股盈餘 2017
                eps4 = dfs[2][4][98] #最新4年的合併總損益 每股盈餘 2016/105
                eps5 = None #最新5年的合併總損益 每股盈餘 2015/104
    
    ####2020/07/02 加入EPS成長率   2020/10/22修改成decimal函數處理四捨五入
                epsYoY1 = str((Decimal((float(eps1)-float(eps2))/float(eps2)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
                epsYoY2 = str((Decimal((float(eps2)-float(eps3))/float(eps3)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
                epsYoY3 = str((Decimal((float(eps3)-float(eps4))/float(eps4)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
                epsYoY4 = None
  
                PER_H1 = round(float(H2)/float(eps1),2)  #2019/108本益比 高
                PER_L1 = round(float(L2)/float(eps1),2)  #108本益比 低 

                PER_H2 = round(float(H3)/float(eps2),2)  #107本益比 高
                PER_L2 = round(float(L3)/float(eps2),2)  #107本益比 低 

                PER_H3 = round(float(H4)/float(eps3),2)  #106本益比 高
                PER_L3 = round(float(L4)/float(eps3),2)  #106本益比 低 

                PER_H4 = round(float(H5)/float(eps4),2)  #105本益比 高
                PER_L4 = round(float(L5)/float(eps4),2)  #105本益比 低 
    
                PER_H5 = None  #104本益比 高
                PER_L5 = None  #104本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3 + PER_H4)/4),2)
                PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3 + PER_L4)/4),2)
                        
                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低

    ####2020/07/02 加入本益比成長率
                PER_H_YoY1  = str(round((PER_H1-PER_H2)/PER_H2,4)*100) + '%'
                PER_H_YoY2  = str(round((PER_H2-PER_H3)/PER_H3,4)*100) + '%'
                PER_H_YoY3  = str(round((PER_H3-PER_H4)/PER_H4,4)*100) + '%'
                PER_H_YoY4  = None
        
######################2020/07/02 加入PEG
    ##########PEG高點     
                PEG_H1 = round(PER_H1/round((float(eps1)-float(eps2))/float(eps2),4)/100,2)
                PEG_H2 = round(PER_H2/round((float(eps2)-float(eps3))/float(eps3),4)/100,2)
                PEG_H3 = round(PER_H3/round((float(eps3)-float(eps4))/float(eps4),4)/100,2)
                PEG_H4 = None 
    
    ##########PEG低點
                PEG_L1 = round(PER_L1/round((float(eps1)-float(eps2))/float(eps2),4)/100,2)
                PEG_L2 = round(PER_L2/round((float(eps2)-float(eps3))/float(eps3),4)/100,2)
                PEG_L3 = round(PER_L3/round((float(eps3)-float(eps4))/float(eps4),4)/100,2)
                PEG_L4 = None  
            





        
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
            H2 = ls2[4] #2019/108年最高價
            L2 = ls2[6] #108年最低價

            H3 = ls3[4] #107年最高價
            L3 = ls3[6] #107年最低價

            H4 = ls4[4] #106年最高價
            L4 = ls4[6] #106年最低價
            
            H5 = None #105年最高價
            L5 = None #105年最低價

            H6 = None #104年最高價
            L6 = None #104年最低價
            print(H0)
            
####################            
            ##########################2021/2/1增添修改
##########################################接著取得EPS
            from decimal import Decimal, ROUND_HALF_UP
                        
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
                eps4 = None #最新4年的合併總損益 每股盈餘 2017/106
                eps5 = None #最新5年的合併總損益 每股盈餘 2016/105
    
    ####2020/07/02 加入EPS成長率   2020/10/22修改成decimal函數處理四捨五入
                epsYoY1 = str((Decimal((float(eps1)-float(eps2))/float(eps2)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
                epsYoY2 = str((Decimal((float(eps2)-float(eps3))/float(eps3)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
                epsYoY3 = None
                epsYoY4 = None
  
                PER_H1 = round(float(H1)/float(eps1),2)  #2020/109本益比 高
                PER_L1 = round(float(L1)/float(eps1),2)  #109本益比 低 

                PER_H2 = round(float(H2)/float(eps2),2)  #108本益比 高
                PER_L2 = round(float(L2)/float(eps2),2)  #108本益比 低 

                PER_H3 = round(float(H3)/float(eps3),2)  #107本益比 高
                PER_L3 = round(float(L3)/float(eps3),2)  #107本益比 低 

                PER_H4 = None  #106本益比 高
                PER_L4 = None  #106本益比 低 
    
                PER_H5 = None  #105本益比 高
                PER_L5 = None  #105本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3)/3),2)
                PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3)/3),2)

                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低

    ####2020/07/02 加入本益比成長率
                PER_H_YoY1  = str(round((PER_H1-PER_H2)/PER_H2,4)*100) + '%'
                PER_H_YoY2  = str(round((PER_H2-PER_H3)/PER_H3,4)*100) + '%'
                PER_H_YoY3  = None
                PER_H_YoY4  = None
        
######################2020/07/02 加入PEG
    ##########PEG高點     
                PEG_H1 = round(PER_H1/round((float(eps1)-float(eps2))/float(eps2),4)/100,2)
                PEG_H2 = round(PER_H2/round((float(eps2)-float(eps3))/float(eps3),4)/100,2)
                PEG_H3 = None
                PEG_H4 = None 
    
    ##########PEG低點
                PEG_L1 = round(PER_L1/round((float(eps1)-float(eps2))/float(eps2),4)/100,2)
                PEG_L2 = round(PER_L2/round((float(eps2)-float(eps3))/float(eps3),4)/100,2)
                PEG_L3 = None
                PEG_L4 = None  
            
            elif eps1N == '2019':  #在三月時，Q4財報還沒出來的情況

                eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2019
                eps2 = dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2018
                eps3 = dfs[2][3][98] #最新3年的合併總損益 每股盈餘 2017
                eps4 = None #最新4年的合併總損益 每股盈餘 2016/105
                eps5 = None #最新5年的合併總損益 每股盈餘 2015/104
    
    ####2020/07/02 加入EPS成長率   2020/10/22修改成decimal函數處理四捨五入
                epsYoY1 = str((Decimal((float(eps1)-float(eps2))/float(eps2)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
                epsYoY2 = str((Decimal((float(eps2)-float(eps3))/float(eps3)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
                epsYoY3 = None
                epsYoY4 = None
  
                PER_H1 = round(float(H2)/float(eps1),2)  #2019/108本益比 高
                PER_L1 = round(float(L2)/float(eps1),2)  #108本益比 低 

                PER_H2 = round(float(H3)/float(eps2),2)  #107本益比 高
                PER_L2 = round(float(L3)/float(eps2),2)  #107本益比 低 

                PER_H3 = round(float(H4)/float(eps3),2)  #106本益比 高
                PER_L3 = round(float(L4)/float(eps3),2)  #106本益比 低 

                PER_H4 = None  #105本益比 高
                PER_L4 = None  #105本益比 低 
    
                PER_H5 = None  #104本益比 高
                PER_L5 = None  #104本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3)/3),2)
                PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3)/3),2)

                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低

    ####2020/07/02 加入本益比成長率
                PER_H_YoY1  = str(round((PER_H1-PER_H2)/PER_H2,4)*100) + '%'
                PER_H_YoY2  = str(round((PER_H2-PER_H3)/PER_H3,4)*100) + '%'
                PER_H_YoY3  = None
                PER_H_YoY4  = None
        
######################2020/07/02 加入PEG
    ##########PEG高點     
                PEG_H1 = round(PER_H1/round((float(eps1)-float(eps2))/float(eps2),4)/100,2)
                PEG_H2 = round(PER_H2/round((float(eps2)-float(eps3))/float(eps3),4)/100,2)
                PEG_H3 = None
                PEG_H4 = None 
    
    ##########PEG低點
                PEG_L1 = round(PER_L1/round((float(eps1)-float(eps2))/float(eps2),4)/100,2)
                PEG_L2 = round(PER_L2/round((float(eps2)-float(eps3))/float(eps3),4)/100,2)
                PEG_L3 = None
                PEG_L4 = None  
            
            
            
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

            H4 = None #106年最高價
            L4 = None #106年最低價
            
            H5 = None #105年最高價
            L5 = None #105年最低價

            H6 = None #104年最高價
            L6 = None #104年最低價
            print(H0)



####################            
####################            
            ##########################2021/2/1增添修改
##########################################接著取得EPS
            from decimal import Decimal, ROUND_HALF_UP            
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
                eps3 = None #最新3年的合併總損益 每股盈餘 2018
                eps4 = None #最新4年的合併總損益 每股盈餘 2017
                eps5 = None #最新5年的合併總損益 每股盈餘 2016
            
    ####2020/07/02 加入EPS成長率   2020/10/22修改成decimal函數處理四捨五入
                epsYoY1 = str((Decimal((float(eps1)-float(eps2))/float(eps2)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
                epsYoY2 = None
                epsYoY3 = None
                epsYoY4 = None
            
    ####2020/07/02 加入本益比成長率
  
    
            #2021/1/6 更改
                PER_H1 = round(float(H1)/float(eps1),2)  #2020/109本益比 高
                PER_L1 = round(float(L1)/float(eps1),2)  #109本益比 低 
                
                PER_H2 = round(float(H2)/float(eps2),2)  #108本益比 高
                PER_L2 = round(float(L2)/float(eps2),2)  #108本益比 低 

                PER_H3 = None  #106本益比 高
                PER_L3 = None  #106本益比 低 

                PER_H4 = None  #105本益比 高
                PER_L4 = None  #105本益比 低 
    
                PER_H5 = None  #104本益比 高
                PER_L5 = None  #104本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2)/2),2)
                PER_L_average = round(float((PER_L1 + PER_L2)/2),2)

                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低
    ####2020/07/02 加入本益比成長率
                PER_H_YoY1  = str(round((PER_H1-PER_H2)/PER_H2,4)*100) + '%'
                PER_H_YoY2  = None
                PER_H_YoY3  = None
                PER_H_YoY4  = None
        
######################2020/07/02 加入PEG
    ##########PEG高點     
                PEG_H1 = round(PER_H1/round((float(eps1)-float(eps2))/float(eps2),4)/100,2)
                PEG_H2 = None
                PEG_H3 = None
                PEG_H4 = None
    
    ##########PEG低點
                PEG_L1 = round(PER_L1/round((float(eps1)-float(eps2))/float(eps2),4)/100,2)
                PEG_L2 = None
                PEG_L3 = None
                PEG_L4 = None            
            
            elif eps1N == '2019':  #在三月時，Q4財報還沒出來的情況


                eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2019
                eps2 = dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2018
                eps3 = None #最新3年的合併總損益 每股盈餘 2017
                eps4 = None #最新4年的合併總損益 每股盈餘 2016
                eps5 = None #最新5年的合併總損益 每股盈餘 2015
            
    ####2020/07/02 加入EPS成長率   2020/10/22修改成decimal函數處理四捨五入
                epsYoY1 = str((Decimal((float(eps1)-float(eps2))/float(eps2)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
                epsYoY2 = None
                epsYoY3 = None
                epsYoY4 = None
            
    ####2020/07/02 加入本益比成長率
  
    
            #2021/1/6 更改
                PER_H1 = round(float(H2)/float(eps1),2)  #2019/108本益比 高
                PER_L1 = round(float(L2)/float(eps1),2)  #108本益比 低 
                
                PER_H2 = round(float(H3)/float(eps2),2)  #107本益比 高
                PER_L2 = round(float(L3)/float(eps2),2)  #107本益比 低 

                PER_H3 = None  #106本益比 高
                PER_L3 = None  #106本益比 低 

                PER_H4 = None  #105本益比 高
                PER_L4 = None  #105本益比 低 
    
                PER_H5 = None  #104本益比 高
                PER_L5 = None  #104本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2)/2),2)
                PER_L_average = round(float((PER_L1 + PER_L2)/2),2)

                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低
    ####2020/07/02 加入本益比成長率
                PER_H_YoY1  = str(round((PER_H1-PER_H2)/PER_H2,4)*100) + '%'
                PER_H_YoY2  = None
                PER_H_YoY3  = None
                PER_H_YoY4  = None
        
######################2020/07/02 加入PEG
    ##########PEG高點     
                PEG_H1 = round(PER_H1/round((float(eps1)-float(eps2))/float(eps2),4)/100,2)
                PEG_H2 = None
                PEG_H3 = None
                PEG_H4 = None
    
    ##########PEG低點
                PEG_L1 = round(PER_L1/round((float(eps1)-float(eps2))/float(eps2),4)/100,2)
                PEG_L2 = None
                PEG_L3 = None
                PEG_L4 = None  

            
            
            #2021/1/6 增加
#############################################
        elif (tablelen == 5):  #去掉當年，只有過去2年資料
            
            ls0 =  dfs[0].iloc[2] #當年 110/2021年
            ls1 =  dfs[0].iloc[3] #109年
            ls2 =  dfs[0].iloc[4] #108年
            ls3 =  None #107年
            ls4 =  None #106年
            ls5 =  None #105年
            ls6 =  None #104年

            H0 = ls0[4] #110年目前已出現過的最高價
        #L0 = ls0[6] #109年目前已出現過的最低價

            H1 = ls1[4] #109/2020年最高價
            L1 = ls1[6] #109年最低價

            H2 = ls2[4] #108年最高價
            L2 = ls2[6] #108年最低價

            H3 = None #107年最高價
            L3 = None #107年最低價

            H4 = None #106年最高價
            L4 = None #106年最低價
            
            H5 = None #105年最高價
            L5 = None #105年最低價

            H6 = None #104年最高價
            L6 = None #104年最低價
            print(H1)

####################            
            ##########################2021/2/1增添修改
##########################################接著取得EPS
            from decimal import Decimal, ROUND_HALF_UP
            
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
                eps2 = None #最新2年的合併總損益 每股盈餘 2019
                eps3 = None #最新3年的合併總損益 每股盈餘 2018
                eps4 = None #最新4年的合併總損益 每股盈餘 2017
                eps5 = None #最新5年的合併總損益 每股盈餘 2016
    

    ####2020/07/02 加入EPS成長率   2020/10/22修改成decimal函數處理四捨五入
                epsYoY1 = None
                epsYoY2 = None
                epsYoY3 = None
                epsYoY4 = None
       
            #2021/1/6 更改
                PER_H1 = round(float(H1)/float(eps1),2)  #2020/109本益比 高
                PER_L1 = round(float(L1)/float(eps1),2)  #109本益比 低 

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

    ####2020/07/02 加入本益比成長率
                PER_H_YoY1  = None
                PER_H_YoY2  = None
                PER_H_YoY3  = None
                PER_H_YoY4  = None
        
######################2020/07/02 加入PEG
    ##########PEG高點     
                PEG_H1 = None
                PEG_H2 = None
                PEG_H3 = None
                PEG_H4 = None 
    
    ##########PEG低點
                PEG_L1 = None 
                PEG_L2 = None 
                PEG_L3 = None 
                PEG_L4 = None 


            elif eps1N == '2019':  #在三月時，Q4財報還沒出來的情況


                eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2019
                eps2 = None #最新2年的合併總損益 每股盈餘 2018
                eps3 = None #最新3年的合併總損益 每股盈餘 2017
                eps4 = None #最新4年的合併總損益 每股盈餘 2017
                eps5 = None #最新5年的合併總損益 每股盈餘 2015
    

    ####2020/07/02 加入EPS成長率   2020/10/22修改成decimal函數處理四捨五入
                epsYoY1 = None
                epsYoY2 = None
                epsYoY3 = None
                epsYoY4 = None
       
            #2021/1/6 更改
                PER_H1 = round(float(H2)/float(eps1),2)  #2019/108本益比 高
                PER_L1 = round(float(L2)/float(eps1),2)  #108本益比 低 

                PER_H2 = None  #107本益比 高
                PER_L2 = None  #107本益比 低 

                PER_H3 = None  #106本益比 高
                PER_L3 = None  #106本益比 低 

                PER_H4 = None  #105本益比 高
                PER_L4 = None  #105本益比 低 
    
                PER_H5 = None  #104本益比 高
                PER_L5 = None  #104本益比 低 

                PER_H_average =  PER_H1 #round(float((PER_H1 + PER_H2)/2),2)
                PER_L_average = PER_L1 #round(float((PER_L1 + PER_L2)/2),2)

                PER_H = PER_H_average #min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = PER_L_average #min(PER_L_average,PER_L1)  #本益比低點與最新孰低

    ####2020/07/02 加入本益比成長率
                PER_H_YoY1  = None
                PER_H_YoY2  = None
                PER_H_YoY3  = None
                PER_H_YoY4  = None
        
######################2020/07/02 加入PEG
    ##########PEG高點     
                PEG_H1 = None
                PEG_H2 = None
                PEG_H3 = None
                PEG_H4 = None 
    
    ##########PEG低點
                PEG_L1 = None 
                PEG_L2 = None 
                PEG_L3 = None 
                PEG_L4 = None 

   
            
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
            ##########################2021/2/1增添修改
##########################################接著取得EPS
            from decimal import Decimal, ROUND_HALF_UP


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
                eps4 = dfs[2][4][98] #最新4年的合併總損益 每股盈餘 2017
                eps5 = dfs[2][5][98] #最新5年的合併總損益 每股盈餘 2016
    
    ####2020/07/02 加入EPS成長率   2020/10/22修改成decimal函數處理四捨五入
                epsYoY1 = str((Decimal((float(eps1)-float(eps2))/float(eps2)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
                epsYoY2 = str((Decimal((float(eps2)-float(eps3))/float(eps3)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
                epsYoY3 = str((Decimal((float(eps3)-float(eps4))/float(eps4)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
                epsYoY4 = str((Decimal((float(eps4)-float(eps5))/float(eps5)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
        
    #epsYoY1 = str(round((float(eps1)-float(eps2))/float(eps2),2)*100) + '%'    
    #epsYoY2 = str(round((float(eps2)-float(eps3))/float(eps3),2)*100) + '%'
    #epsYoY3 = str(round((float(eps3)-float(eps4))/float(eps4),2)*100) + '%'
    #epsYoY4 = str(round((float(eps4)-float(eps5))/float(eps5),2)*100) + '%'
        
    
    ####2020/07/02 加入本益比成長率
                PER_H1 = round(float(H1)/float(eps1),2)  #2019/108本益比 高  H2為109年
                PER_L1 = round(float(L1)/float(eps1),2)  #108本益比 低 

                PER_H2 = round(float(H2)/float(eps2),2)  #107本益比 高
                PER_L2 = round(float(L2)/float(eps2),2)  #107本益比 低 

                PER_H3 = round(float(H3)/float(eps3),2)  #106本益比 高
                PER_L3 = round(float(L3)/float(eps3),2)  #106本益比 低 

                PER_H4 = round(float(H4)/float(eps4),2)  #105本益比 高
                PER_L4 = round(float(L4)/float(eps4),2)  #105本益比 低 
    
                PER_H5 = round(float(H5)/float(eps5),2)  #104本益比 高
                PER_L5 = round(float(L5)/float(eps5),2)  #104本益比 低 

                PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3 + PER_H4 + PER_H5)/5),2)
                PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3 + PER_L4 + PER_L5)/5),2)


                PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
                PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低

    ####2020/07/02 加入本益比成長率
                PER_H_YoY1  = str(round((PER_H1-PER_H2)/PER_H2,4)*100) + '%'
                PER_H_YoY2  = str(round((PER_H2-PER_H3)/PER_H3,4)*100) + '%'
                PER_H_YoY3  = str(round((PER_H3-PER_H4)/PER_H4,4)*100) + '%'
                PER_H_YoY4  = str(round((PER_H4-PER_H5)/PER_H5,4)*100) + '%'
        
######################2020/07/02 加入PEG
    ##########PEG高點     
                PEG_H1 = round(PER_H1/round((float(eps1)-float(eps2))/float(eps2),4)/100,2)
                PEG_H2 = round(PER_H2/round((float(eps2)-float(eps3))/float(eps3),4)/100,2)
                PEG_H3 = round(PER_H3/round((float(eps3)-float(eps4))/float(eps4),4)/100,2)
                PEG_H4 = round(PER_H4/round((float(eps4)-float(eps5))/float(eps5),4)/100,2) 
    
    ##########PEG低點
                PEG_L1 = round(PER_L1/round((float(eps1)-float(eps2))/float(eps2),4)/100,2)
                PEG_L2 = round(PER_L2/round((float(eps2)-float(eps3))/float(eps3),4)/100,2)
                PEG_L3 = round(PER_L3/round((float(eps3)-float(eps4))/float(eps4),4)/100,2)
                PEG_L4 = round(PER_L4/round((float(eps4)-float(eps5))/float(eps5),4)/100,2)  



            elif eps1N == '2019':  #在三月時，Q4財報還沒出來的情況

                eps1 = dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2019
                eps2 = dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2018
                eps3 = dfs[2][3][98] #最新3年的合併總損益 每股盈餘 2017
                eps4 = dfs[2][4][98] #最新4年的合併總損益 每股盈餘 2017
                eps5 = dfs[2][5][98] #最新5年的合併總損益 每股盈餘 2015
    
    ####2020/07/02 加入EPS成長率   2020/10/22修改成decimal函數處理四捨五入
                epsYoY1 = str((Decimal((float(eps1)-float(eps2))/float(eps2)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
                epsYoY2 = str((Decimal((float(eps2)-float(eps3))/float(eps3)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
                epsYoY3 = str((Decimal((float(eps3)-float(eps4))/float(eps4)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
                epsYoY4 = str((Decimal((float(eps4)-float(eps5))/float(eps5)).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
        
    #epsYoY1 = str(round((float(eps1)-float(eps2))/float(eps2),2)*100) + '%'    
    #epsYoY2 = str(round((float(eps2)-float(eps3))/float(eps3),2)*100) + '%'
    #epsYoY3 = str(round((float(eps3)-float(eps4))/float(eps4),2)*100) + '%'
    #epsYoY4 = str(round((float(eps4)-float(eps5))/float(eps5),2)*100) + '%'
        
    
    ####2020/07/02 加入本益比成長率
                PER_H1 = round(float(H2)/float(eps1),2)  #2019/108本益比 高  H2為109年
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

    ####2020/07/02 加入本益比成長率
                PER_H_YoY1  = str(round((PER_H1-PER_H2)/PER_H2,4)*100) + '%'
                PER_H_YoY2  = str(round((PER_H2-PER_H3)/PER_H3,4)*100) + '%'
                PER_H_YoY3  = str(round((PER_H3-PER_H4)/PER_H4,4)*100) + '%'
                PER_H_YoY4  = str(round((PER_H4-PER_H5)/PER_H5,4)*100) + '%'
        
######################2020/07/02 加入PEG
    ##########PEG高點     
                PEG_H1 = round(PER_H1/round((float(eps1)-float(eps2))/float(eps2),4)/100,2)
                PEG_H2 = round(PER_H2/round((float(eps2)-float(eps3))/float(eps3),4)/100,2)
                PEG_H3 = round(PER_H3/round((float(eps3)-float(eps4))/float(eps4),4)/100,2)
                PEG_H4 = round(PER_H4/round((float(eps4)-float(eps5))/float(eps5),4)/100,2) 
    
    ##########PEG低點
                PEG_L1 = round(PER_L1/round((float(eps1)-float(eps2))/float(eps2),4)/100,2)
                PEG_L2 = round(PER_L2/round((float(eps2)-float(eps3))/float(eps3),4)/100,2)
                PEG_L3 = round(PER_L3/round((float(eps3)-float(eps4))/float(eps4),4)/100,2)
                PEG_L4 = round(PER_L4/round((float(eps4)-float(eps5))/float(eps5),4)/100,2)  

        #print(L5)    
######
########################2021/2/28新增單季EPS計算 取代整年營收估EPS計算
    bank_url = 'https://djinfo.cathaysec.com.tw/' #國泰世華
    headers = {'Referer':my_Referer,'user-agent': my_UserAgent}
    sheet_type = 'z/zc/zcr/zcr_' #FRQ 財務比率 季表
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs5 = pd.read_html(str(table))
    
    #newest_Fin_Q = str(dfs5[2][1][1]) #最新1季的財報季份

    epsq1N = dfs5[2][1][1] #最新1季的名稱
    #epsq2N = dfs5[2][2][1] #最新2季的名稱
    #epsq3N = dfs5[2][3][1] #最新3季的名稱
    #epsq4N = dfs5[2][4][1] #最新4季的名稱
    #epsq5N = dfs5[2][5][1] #最新5季的名稱
    #epsq6N = dfs5[2][6][1] #最新6季的名稱
    #epsq7N = dfs5[2][7][1] #最新7季的名稱
    #epsq8N = dfs5[2][8][1] #最新8季的名稱
    

    epsq1 = float((dfs5[2][1][25])) #最新1季的EPS
    epsq2 = float((dfs5[2][2][25])) #最新2季的EPS
    epsq3 = float((dfs5[2][3][25])) #最新3季的EPS
    epsq4 = float((dfs5[2][4][25])) #最新4季的EPS
    #epsq5 = float((dfs5[2][5][25])) #最新5季的EPS
    #epsq6 = float((dfs5[2][6][25])) #最新6季的EPS
    #epsq7 = float((dfs5[2][7][25])) #最新7季的EPS
    #epsq8 = float((dfs5[2][8][25])) #最新8季的EPS




##############################################取得營收
############################
    sheet_type = 'z/zc/zch/zch_' #Rev 營收
    #stock_id = "3034"
    bank_url = 'https://djinfo.cathaysec.com.tw/' #國泰世華
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url, headers=headers)
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
    
    pYoY1 = str(round(rYoY1*100,2))+'%'
    pYoY2 = str(round(rYoY2*100,2))+'%'
    pYoY3 = str(round(rYoY3*100,2))+'%'
    pYoY4 = str(round(rYoY4*100,2))+'%'
    pYoY5 = str(round(rYoY5*100,2))+'%'
    pYoY6 = str(round(rYoY6*100,2))+'%'
    
    

    rYoY6Average  = (rYoY1+rYoY2+rYoY3+rYoY4+rYoY5+rYoY6)/6 #最新六個月營收平均
#print(rYoY6Average)
    pYoY6Average = str(round(rYoY6Average*100,2))+'%'

    RevYoY = round(min(rYoY6Average,rYoY1),4) #兩者擇一較低
    
    pRevYoY = str(round(RevYoY*100,2))+'%'

    #return H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average 

##############################以下開始預估未來一整年的營收，

#print(RevYoY)
    if (month_id == '4'): 
        ##########################月份名稱############
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
        r13N = dfs[2][0][18]  #108/4
        r14N = dfs[2][0][19]  #108/3
        r15N = dfs[2][0][20]  #108/2
        r16N = dfs[2][0][21]  #108/1
        ##########################各月份營收############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 109/4
        r2 = int(dfs[2][1][7])/100000  #109/3
        r3 = int(dfs[2][1][8])/100000  #109/2
        r4 = int(dfs[2][1][9])/100000  #109/1
    
    #r1_9Sum = Jan_Sep_Sum = r1+r2+r3+r4+r5+r6+r7+r8+r9 #今年1-9月營收
        thisYear_Sum = r1+r2+r3+r4 #今年1-4月營收

        r5 = int(dfs[2][1][10])/100000  #108/12
        r6 = int(dfs[2][1][11])/100000  #108/11
        r7 = int(dfs[2][1][12])/100000  #108/10
        r8 = int(dfs[2][1][13])/100000  #108/9
        r9 = int(dfs[2][1][14])/100000  #108/8
        r10 = int(dfs[2][1][15])/100000  #108/7
        r11 = int(dfs[2][1][16])/100000  #108/6
        r12 = int(dfs[2][1][17])/100000  #108/5
        r13 = int(dfs[2][1][18])/100000  #108/4
        r14 = int(dfs[2][1][19])/100000  #108/3
        r15 = int(dfs[2][1][20])/100000  #108/2
        r16 = int(dfs[2][1][21])/100000  #108/1

        Rev_LastYear = r5+r6+r7+r8+r9+r10+r11+r12+r13+r14+r15+r16  #在2021/2/19 計算2020 營收和EPS


    #r10_12Sum_Predict = (r10+r11+r12)*(1+RevYoY) #預估今年10-12月營收
        theRest_Predict = (r5+r6+r7+r8+r9+r10+r11+r12)*(1+RevYoY) #預估2021年5-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #用去年營收 預估今年2021全年營收 20200924修改

        if epsq1N == '2020.4Q' :
            Q4_Rev_Predict = None
        else:            
            Q4_Rev_Predict = r5+r6+r7 #2020/10,11,12月營收

    elif (month_id == '1'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱 1月
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        r13N = dfs[2][0][18]         
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 2021/01

    
        thisYear_Sum = r1 #今年已公布營收 1月營收
        
        r2 = int(dfs[2][1][7])/100000   #2020/12
        r3 = int(dfs[2][1][8])/100000 
        r4 = int(dfs[2][1][9])/100000  
        r5 = int(dfs[2][1][10])/100000  
        r6 = int(dfs[2][1][11])/100000  
        r7 = int(dfs[2][1][12])/100000  
        r8 = int(dfs[2][1][13])/100000 
        r9 = int(dfs[2][1][14])/100000  
        r10 = int(dfs[2][1][15])/100000  
        r11 = int(dfs[2][1][16])/100000  
        r12 = int(dfs[2][1][17])/100000  
        r13 = int(dfs[2][1][18])/100000 

        Rev_LastYear = r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r13  #在2021/2/19 計算2020 營收和EPS 因為尚未公佈

        theRest_Predict = (r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12)*(1+RevYoY) 

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #用去年營收 預估今年2021全年營收 20200924修改

        Q4_Rev_Predict = r2+r3+r4 #2020/10,11,12月營收


    elif (month_id == '2'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        r13N = dfs[2][0][18]  
        r14N = dfs[2][0][19]          
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
    
        thisYear_Sum = r1+r2 #今年已公布營收 1-2月營收
        
        
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000  
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000
        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000
        r13 = int(dfs[2][1][18])/100000
        r14 = int(dfs[2][1][19])/100000
        
        Rev_LastYear = r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r13+r14  #在2021/2/19 計算2020 營收和EPS 因為尚未公佈


        theRest_Predict = (r3+r4+r5+r6+r7+r8+r9+r10+r11+r12)*(1+RevYoY) #預估2021年3-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #用去年營收 預估今年2021全年營收 20200924修改

        if epsq1N == '2020.4Q' :
            Q4_Rev_Predict = None
        else:            
            Q4_Rev_Predict = r3+r4+r5 #2020/10,11,12月營收

    elif (month_id == '3'):  #第四季(Q4)財報及年報：隔年3/31前
    #第一季(Q1)財報：5/15前
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        r13N = dfs[2][0][18]  
        r14N = dfs[2][0][19]  
        r15N = dfs[2][0][20]  

        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        
        thisYear_Sum = r1+r2+r3 #今年已公布營收 1-3月營收
        
        

        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000  
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000
        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000
        r13 = int(dfs[2][1][18])/100000
        r14 = int(dfs[2][1][19])/100000
        r15 = int(dfs[2][1][20])/100000

        Rev_LastYear = r4+r5+r6+r7+r8+r9+r10+r11+r12+r13+r14+r15  #在2021/2/19 計算2020 營收和EPS 因為尚未公佈


        theRest_Predict = (r4+r5+r6+r7+r8+r9+r10+r11+r12)*(1+RevYoY) #預估今年4-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #用去年營收 預估今年2021全年營收 20200924修改

        if epsq1N == '2020.4Q' :
            Q4_Rev_Predict = None
        else:            
            Q4_Rev_Predict = r4+r5+r6 #2020/10,11,12月營收


    elif (month_id == '5'): #第一季(Q1)財報：5/15前
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        r13N = dfs[2][0][18] 
        r14N = dfs[2][0][19] 
        r15N = dfs[2][0][20] 
        r16N = dfs[2][0][21] 
        r17N = dfs[2][0][22] 

        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        
        thisYear_Sum = r1+r2+r3+r4+r5 #今年已公布營收 1-5月營收
        
        


        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000  
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000
        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000
        r13 = int(dfs[2][1][18])/100000
        r14 = int(dfs[2][1][19])/100000
        r15 = int(dfs[2][1][20])/100000
        r16 = int(dfs[2][1][21])/100000
        r17 = int(dfs[2][1][22])/100000

        Rev_LastYear = r6+r7+r8+r9+r10+r11+r12+r13+r14+r15+r16+r17  #在2021/2/19 計算2020 營收和EPS


        theRest_Predict = (r6+r7+r8+r9+r10+r11+r12)*(1+RevYoY) #預估今年6-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #用去年營收 預估今年2021全年營收 20200924修改

        if epsq1N == '2020.4Q' :
            Q4_Rev_Predict = None
        else:            
            Q4_Rev_Predict = r6+r7+r8 #2020/10,11,12月營收

    elif (month_id == '6'):  
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        
        thisYear_Sum = r1+r2+r3+r4+r5+r6 #今年已公布營收 1-6月營收
        
        
        r7 = int(dfs[2][1][12])/100000  
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000
        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000


        theRest_Predict = (r7+r8+r9+r10+r11+r12)*(1+RevYoY) #預估今年7-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #用去年營收 預估今年2021全年營收 20200924修改

    elif (month_id == '7'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000 
        
        thisYear_Sum = r1+r2+r3+r4+r5+r6+r7 #今年已公布營收 1-7月營收
        
         
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000
        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000


        theRest_Predict = (r8+r9+r10+r11+r12)*(1+RevYoY) #預估今年8-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #用去年營收 預估今年2021全年營收 20200924修改

    elif (month_id == '8'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000 
        r8 = int(dfs[2][1][13])/100000
        
        thisYear_Sum = r1+r2+r3+r4+r5+r6+r7+r8 #今年已公布營收 1-7月營收
        
        
        r9 = int(dfs[2][1][14])/100000
        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000


        theRest_Predict = (r9+r10+r11+r12)*(1+RevYoY) #預估今年9-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #用去年營收 預估今年2021全年營收 20200924修改



########################################暑假過後，只能估算明年的數字
    elif (month_id == '9'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱  9月
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  #1月
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  #10月
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000 
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000 
       
        thisYear_Sum = r1+r2+r3+r4+r5+r6+r7+r8+r9 #今年已公布營收 1-9月營收
        
        

        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000


        theRest_Predict = (r10+r11+r12)*(1+RevYoY) #預估今年10-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4)*(1+RevYoY) #用今年營收 預估明年2021全年營收 20200924修改

    elif (month_id == '10'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000 
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000 
        r10 = int(dfs[2][1][15])/100000
        
        thisYear_Sum = r1+r2+r3+r4+r5+r6+r7+r8+r9+r10 #今年已公布營收 1-10月營收
        
        
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000


        theRest_Predict = (r11+r12)*(1+RevYoY) #預估今年11-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4)*(1+RevYoY) #用今年營收 預估明年2021全年營收 20200924修改

    elif (month_id == '11'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000 
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000 
        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        
        thisYear_Sum = r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11 #今年已公布營收 1-11月營收
        
        

        r12 = int(dfs[2][1][17])/100000


        theRest_Predict = (r12)*(1+RevYoY) #預估今年12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4)*(1+RevYoY) #用今年營收 預估明年2021全年營收 20200924修改

    elif (month_id == '12'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000 
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000 
        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000
        
        thisYear_Sum = r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12 #去年已公布營收 1-12月營收
        
        

        


        theRest_Predict = 0 ##用去年2020營收 預估今年2021全年營收 20200924修改

        Rev_Predict = round(thisYear_Sum, 4)*(1+RevYoY) #預估2021年全年營收



##################################取得稅後淨利率

    bank_url = 'https://djinfo.cathaysec.com.tw/' #國泰世華
    sheet_type = 'z/zc/zcr/zcr_' #FRQ 財務比率 季表

    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url, headers=headers)
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
    
    pNet1 = str(round(Net1*100,2))+'%'
    pNet2 = str(round(Net2*100,2))+'%'
    pNet3 = str(round(Net3*100,2))+'%'
    pNet4 = str(round(Net4*100,2))+'%'

    Net4Average = (Net1+Net2+Net3+Net4)/4
    
    pNet4Average = str(round(Net4Average*100,2))+'%'

#print(Net4Average)

###############預估 淨利 EPS  ###2021/3/31公佈2020年報後 必須修改 不用估算 直接抓EPS
    #Net_Predict0 = round(Rev_LastYear*Net4Average,6)  #估算2020 #暫時省略20210726

    #Q4_Net_Predict = round(Q4_Rev_Predict*Net4Average,6) #估算2020 Q4 淨利


    Net_Predict = round(Rev_Predict*Net4Average,6)  #估算2021

    #2021/2/28新增
    if epsq1N == '2020.4Q' :
        
        Q4_Net_Predict = None
        
    else:
        Q4_Net_Predict = None
        #round(Q4_Rev_Predict*Net4Average,6)  #暫時省略20210726
#print(Net_Predict)

####################################################取得股本
    bank_url0 = 'https://djinfo.cathaysec.com.tw/' #國泰世華
    sheet_type = 'z/zc/zcp/zcpa_' 
    ###MoneyDJ
    url = bank_url0 + sheet_type + stock_id +'.djhtm'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))

    cap1 = round(float(dfs[2][1][80])/100,2) #最新一季股本（單位：百萬） 2020/7/4 要轉換成 億
#print(table)
#stock_id_name = dfs[2][0][0][:-24] #股票代號和名稱
    #stock_name = dfs[2][0][0][0:3] #股票名稱
#latest_trade_date = dfs[2][0][0][-13:-8] #最近交易日
#open = dfs[2][1][1] #開盤價
#high = dfs[2][3][1] #最高價
#low  = dfs[2][5][1] #最低價
#close  = dfs[2][7][1] #收盤價
    capital_stock = cap1 #本來Basic表股本 單位：億
#print(capital_stock)
####################計算預估EPS 2021/2/2修改
    #Q4_Predict_EPS = round(Q4_Net_Predict/capital_stock*10,2) #估算2020/Q4 eps
    

    #Predict_EPSq = epsq1 + epsq2 + epsq3 + Q4_Predict_EPS
    #round(Net_Predict0/capital_stock*10,2) #2020年預估值，在2021四月財報公佈之前  q為?
    #print(Predict_EPSq)
    Predict_EPS = round(Net_Predict/capital_stock*10,2)   #2021

    #2021/2/28新增  2021/5/29 更改
    if epsq1N == '2020.4Q' :
        Predict_EPSq = epsq1 + epsq2 + epsq3 + epsq4
        print(epsq1, epsq2, epsq3, epsq4)
        print(Predict_EPSq)

#####################
        PER_Hq = round(float(H1)/float(Predict_EPSq),2)  #H1為2020高點   計算2020年本益比高點
        PER_Lq = round(float(L1)/float(Predict_EPSq),2)  #L1為2020低點   計算2020年本益比低點
    
    #預測的EPS成長率 2021/2/2修改   3/14更改 配合Q4財報更新  注意不要重複 eps1改eps2
        epsYoYq = str(round((float(Predict_EPSq)-float(eps2))/float(eps1),3)*100) + '%'  #2020年預估值，在2021四月財報公佈之前  q為?
    
        epsYoY0 = str(round((float(Predict_EPS)-float(Predict_EPSq))/float(Predict_EPSq),3)*100) + '%'  #2021

    #預測出來的新價格的PEG 2021/2/2修改
        print(eps1, Predict_EPSq)
        
        PEG_Hq = round(PER_Hq/round((float(Predict_EPSq)-float(eps2))/float(eps2),4)/100,2)  #2020年預估值，在2021四月財報公佈之前  q為?
        PEG_Lq = round(PER_Lq/round((float(Predict_EPSq)-float(eps2))/float(eps2),4)/100,2)
            
        PEG_H0 = round(PER_H/round((float(Predict_EPS)-float(Predict_EPSq))/float(Predict_EPSq),4)/100,2)  #2021
        PEG_L0 = round(PER_L/round((float(Predict_EPS)-float(Predict_EPSq))/float(Predict_EPSq),4)/100,2)

    if epsq1N == '2021.1Q' :   #2021/5/29增加
        
        #Q4_Predict_EPS = round(Q4_Net_Predict/capital_stock*10,2) #估算2020/Q4 eps
        Predict_EPSq = epsq1 + epsq2 + epsq3 + epsq4 #5/15前公佈2021Q1財報

        #print(Q4_Predict_EPS)
    
        print(epsq1,epsq2,epsq3,epsq4)
#print(Predict_EPS)

            #PER_H1 = round(float(H2)/float(eps1),2)  #2019/108本益比 高  H2為109年
            #PER_L1 = round(float(L2)/float(eps1),2)  #108本益比 低 
#########################################
        PER_Hq = round(float(H1)/float(Predict_EPSq),2)  #H1為2020高點   計算2020年本益比高點，2021年四月前估算
        PER_Lq = round(float(L1)/float(Predict_EPSq),2)  #L1為2020低點   計算2020年本益比低點，2021年四月前估算
    
    #預測的EPS成長率 2021/2/2修改
        epsYoYq = str(round((float(Predict_EPSq)-float(eps1))/float(eps1),3)*100) + '%'  #2020年預估值，在2021四月財報公佈之前  q為?
    
        epsYoY0 = str(round((float(Predict_EPS)-float(Predict_EPSq))/float(Predict_EPSq),3)*100) + '%'  #2021

    #預測出來的新價格的PEG 2021/2/2修改
        print(eps1, Predict_EPSq)
        
        PEG_Hq = round(PER_Hq/round((float(Predict_EPSq)-float(eps1))/float(eps1),4)/100,2)  #2020年預估值，在2021四月財報公佈之前  q為?
        PEG_Lq = round(PER_Lq/round((float(Predict_EPSq)-float(eps1))/float(eps1),4)/100,2)
            
        PEG_H0 = round(PER_H/round((float(Predict_EPS)-float(Predict_EPSq))/float(Predict_EPSq),4)/100,2)  #2021
        PEG_L0 = round(PER_L/round((float(Predict_EPS)-float(Predict_EPSq))/float(Predict_EPSq),4)/100,2)

        
    else:
        Q4_Predict_EPS = round(Q4_Net_Predict/capital_stock*10,2) #估算2020/Q4 eps
        Predict_EPSq = epsq1 + epsq2 + epsq3 + Q4_Predict_EPS #估2020全年EPS 2021/3/31前 尚未公佈

        print(Q4_Predict_EPS)
    
        print(epsq1,epsq2,epsq3)
#print(Predict_EPS)

            #PER_H1 = round(float(H2)/float(eps1),2)  #2019/108本益比 高  H2為109年
            #PER_L1 = round(float(L2)/float(eps1),2)  #108本益比 低 
#########################################
        PER_Hq = round(float(H1)/float(Predict_EPSq),2)  #H1為2020高點   計算2020年本益比高點，2021年四月前估算
        PER_Lq = round(float(L1)/float(Predict_EPSq),2)  #L1為2020低點   計算2020年本益比低點，2021年四月前估算
    
    #預測的EPS成長率 2021/2/2修改
        epsYoYq = str(round((float(Predict_EPSq)-float(eps1))/float(eps1),3)*100) + '%'  #2020年預估值，在2021四月財報公佈之前  q為?
    
        epsYoY0 = str(round((float(Predict_EPS)-float(Predict_EPSq))/float(Predict_EPSq),3)*100) + '%'  #2021

    #預測出來的新價格的PEG 2021/2/2修改
        print(eps1, Predict_EPSq)
        
        PEG_Hq = round(PER_Hq/round((float(Predict_EPSq)-float(eps1))/float(eps1),4)/100,2)  #2020年預估值，在2021四月財報公佈之前  q為?
        PEG_Lq = round(PER_Lq/round((float(Predict_EPSq)-float(eps1))/float(eps1),4)/100,2)
            
        PEG_H0 = round(PER_H/round((float(Predict_EPS)-float(Predict_EPSq))/float(Predict_EPSq),4)/100,2)  #2021
        PEG_L0 = round(PER_L/round((float(Predict_EPS)-float(Predict_EPSq))/float(Predict_EPSq),4)/100,2)



    Predict_high_price = round(Predict_EPS*PER_H,2)
    Predict_low_price = round(Predict_EPS*PER_L,2)


    #計算PEG為1時，股價是多少？  #2021
    PEG1_PredictPrice = Predict_EPS*100*round((float(Predict_EPS)-float(Predict_EPSq))/float(Predict_EPSq),3)    
    #計算PEG為0.67時，股價是多少？  #2021
    PEG067_PredictPrice = Predict_EPS*67*round((float(Predict_EPS)-float(Predict_EPSq))/float(Predict_EPSq),3)    

    print(round((float(Predict_EPS)-float(Predict_EPSq))/float(Predict_EPSq),3))
    
    print(Predict_EPS)

    url = 'https://tw.stock.yahoo.com/q/ts?s=' + stock_id
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))


#    yahoo_tradePrice = dfs[0][3] #yahoo成交價
#    yahoo_time= dfs[0][0] #yahoo成交時間
    yahoo_latest_tradePrice = float(dfs[0][3][6]) #yahoo最新成交價
#    yahoo_latest_time = dfs[0][0][6] #yahoo最新成交時間    
    
    
#######################################    

    up_profit = round((Predict_high_price - yahoo_latest_tradePrice)/yahoo_latest_tradePrice,2)
    down_loss = round((Predict_low_price - yahoo_latest_tradePrice)/yahoo_latest_tradePrice,2)

#print(up_profit)
#print(down_loss)

    New_up_profit = str(up_profit*100) + '%'
    New_down_loss = str(down_loss*100) + '%'

#print(New_up_profit)
#print(New_down_loss)

    #risk_reward = round(abs(up_profit)/abs(down_loss),2)
    risk_reward = round(abs(up_profit/down_loss),2)
    
    return H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, New_up_profit, New_down_loss, risk_reward, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average, pNet1, pNet2, pNet3, pNet4, pNet4Average, H0, epsYoY1, epsYoY2, epsYoY3, epsYoY4, PER_H_YoY1, PER_H_YoY2, PER_H_YoY3, PER_H_YoY4, PEG_H1, PEG_H2, PEG_H3, PEG_H4, PEG_L1, PEG_L2, PEG_L3, PEG_L4, epsYoY0, PEG_H0, PEG_L0, PEG1_PredictPrice, PEG067_PredictPrice, thisYear_Sum, theRest_Predict, H6, L6, Predict_EPSq, PER_Hq, PER_Lq, epsYoYq, PEG_Hq, PEG_Lq, eps1N

 
    
#################################################################################

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
        
        H0 = ls0[4] #111年目前已出現過的最高價
        #L0 = ls0[6] #111年目前已出現過的最低價

        H1 = ls1[4] #110年最高價
        L1 = ls1[6] #110年最低價

        H2 = ls2[4] #109年最高價
        L2 = ls2[6] #109年最低價

        H3 = ls3[4] #108年最高價
        L3 = ls3[6] #108年最低價

        H4 = ls4[4] #107年最高價
        L4 = ls4[6] #107年最低價

        H5 = ls5[4] #106年最高價
        L5 = ls5[6] #106年最低價
    
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



        ls1  = dfs[0].iloc[-1] #110年
        ls2  = dfs[0].iloc[-2] #109年
        ls3  = dfs[0].iloc[-3] #108年
        ls4  = dfs[0].iloc[-4] #107年
        ls5  = dfs[0].iloc[-5] #106年

        H1 = ls1[4] #2021/110年最高價
        L1 = ls1[6] #110年最低價

        H2 = ls2[4] #109年最高價
        L2 = ls2[6] #109年最低價

        H3 = ls3[4] #108年最高價
        L3 = ls3[6] #108年最低價

        H4 = ls4[4] #107年最高價
        L4 = ls4[6] #107年最低價

        H5 = ls5[4] #106年最高價
        L5 = ls5[6] #106年最低價

        #print(H5)
        #print(L5)
  
################################################接著取得EPS
#stock_id = "3034"
    bank_url = 'https://djinfo.cathaysec.com.tw/z/zc/zcq/zcq0.djhtm?b=Y&a=' #國泰世華
#sheet_type = 'z/zc/zcq/zcq_' #ISQ 合併損益表 季表

    url = bank_url + stock_id
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    #table = soup.find_all('table')[0];
    table2 = soup.find_all(class_ = 'table-row') 


    #xYearSeasonTitle = table2[0].text
    #xYearSeasonTitleList = xYearSeasonTitle.split("\n")

    xEPS = table2[-1].text
    xEPSList = xEPS.split("\n")

#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][98] #最新1年的合併總損益 每股盈餘

    eps1 = xEPSList[2] #最新1年的合併總損益 每股盈餘 2021/110
    eps2 = xEPSList[3] #最新2年的合併總損益 每股盈餘 2020
    eps3 = xEPSList[4] #最新3年的合併總損益 每股盈餘 2019
    eps4 = xEPSList[5] #最新4年的合併總損益 每股盈餘 2018
    eps5 = xEPSList[6] #最新5年的合併總損益 每股盈餘 2017
    
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



