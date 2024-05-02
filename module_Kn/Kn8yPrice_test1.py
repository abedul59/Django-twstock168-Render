# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 17:00:24 2021

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
bankA = 'http://dj.mybank.com.tw/' #國泰世華
bankB = 'http://jdata.yuanta.com.tw/' #元大
bankC = 'http://jsjustweb.jihsun.com.tw' #日盛
bankD = 'http://stockchannel.sinotrade.com.tw' #永豐金證券
bankE = 'http://djfubonholdingfund.fbs.com.tw' #富邦證券

my_Banks = random.choice([bankA, bankB, bankC, bankD, bankE])



'''

    
#############################################################以下為本益比區間程式
def Kn8yPrice(stock_id):
    headers = {'Referer': my_Referer ,'user-agent': my_UserAgent}
    ######以下為判斷上市或上櫃，取得年度股價程式
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup    

        #TSE沒有當年度，例如今年2021，只有2020以前
    try:  #查詢上市年股價 （先上市，有些股票會上櫃轉上市，但上櫃還會留下資料，會抓錯。）
        twse_url = 'http://www.twse.com.tw/exchangeReport/FMNPTK?response=html&stockNo=' #國泰世華
        url = twse_url + stock_id 
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        table = soup.find_all('table')[0];
        dfs = pd.read_html(str(table))


        try:
            ls1 = dfs[0].iloc[-1] #2020/109年

            H1 = ls1[4] #109/2020年最高價
            L1 = ls1[6] #109年最低價
        except:
            H1 = "N/A" #109/2020年最高價
            L1 = "N/A" #109年最低價
        
        try:
            ls2 = dfs[0].iloc[-2] #2019/108年

            H2 = ls2[4] #2019/108年最高價
            L2 = ls2[6] #108年最低價
        except:
            H2 = "N/A" #2019/108年最高價
            L2 = "N/A" #108年最低價
            
        try:
            ls3  = dfs[0].iloc[-3] #107年

            H3 = ls3[4] #107年最高價
            L3 = ls3[6] #107年最低價            
        except:
            H3 = "N/A" #107年最高價
            L3 = "N/A" #107年最低價 

        try:            
            ls4  = dfs[0].iloc[-4] #106年
        
            H4 = ls4[4] #106年最高價
            L4 = ls4[6] #106年最低價
        except:
            H4 = "N/A" #106年最高價
            L4 = "N/A" #106年最低價            
        
        try:
            ls5  = dfs[0].iloc[-5] #105年
            
            H5 = ls5[4] #105年最高價
            L5 = ls5[6] #105年最低價   
        except:
            H5 = "N/A" #105年最高價
            L5 = "N/A" #105年最低價            
            
            
        try:            
            ls6  = dfs[0].iloc[-6] #104年

            H6 = ls6[4] #104年最高價
            L6 = ls6[6] #104年最低價            
        except:
            H6 = "N/A" #104年最高價
            L6 = "N/A" #104年最低價

        try:
            ls7  = dfs[0].iloc[-7] #103年

            H7 = ls7[4] #103年最高價
            L7 = ls7[6] #103年最低價 
        except:
            H7 = "N/A" #103年最高價
            L7 = "N/A" #103年最低價             
        
        try:            
            ls8  = dfs[0].iloc[-8] #102年

            H8 = ls8[4] #102年最高價
            L8 = ls8[6] #102年最低價     
        except:
            H8 = "N/A" #102年最高價
            L8 = "N/A" #102年最低價                 
            
            
        try:    
            ls9  = dfs[0].iloc[-9] #101年  

            H9 = ls9[4] #101年最高價
            L9 = ls9[6] #101年最低價
        except:
            H9 = "N/A" #101年最高價
            L9 = "N/A" #101年最低價


##################################################################


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
        

    
    
    except:    #查詢上櫃年股價
################################################
#stock_id = "3034"
        bank_url0 = 'http://dj.mybank.com.tw/z/zc/zcq/zcq0.djhtm?b=Y&a=' #國泰世華
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

            
        #elif (tablelen >= 9):  #有五年以上歷史資料
    #ls0 = lastyear1 = dfs[0].iloc[2] #當年 2021/110年
        try:
            ls0 =  dfs[0].iloc[2] #當年2021/110年

            H0 = ls0[4] #110/2021年目前已出現過的最高價
            L0 = ls0[6] #110年目前已出現過的最低價
        except:
            H0 = 0 #110/2021年目前已出現過的最高價
            L0 = 0 #110年目前已出現過的最低價
            
        try:
            ls1 =  dfs[0].iloc[3] #2020/109年  
            
            H1 = ls1[4] #2020/109年最高價
            L1 = ls1[6] #109年最低價 
        except:
            H1 = 0 #2020/109年最高價
            L1 = 0 #109年最低價             
            
        try:
            ls2 =  dfs[0].iloc[4] #108年

            H2 = ls2[4] #2019/108年最高價
            L2 = ls2[6] #108年最低價 
        except:
            H2 = 0 #2019/108年最高價
            L2 = 0 #108年最低價             
            
        try:
            ls3 =  dfs[0].iloc[5] #107年
            
            H3 = ls3[4] #2018/107年最高價
            L3 = ls3[6] #107年最低價
        except:
            H3 = 0 #2018/107年最高價
            L3 = 0 #107年最低價            
            
            
            
        try:
            ls4 =  dfs[0].iloc[6] #106年
            
            H4 = ls4[4] #2017/106年最高價
            L4 = ls4[6] #106年最低價
        except:
            H4 = 0 #2017/106年最高價
            L4 = 0 #106年最低價            
            
            
            
        try:
            ls5 =  dfs[0].iloc[7] #105年   
            
            H5 = ls5[4] #105年最高價
            L5 = ls5[6] #105年最低價     
        except:
            H5 = 0 #105年最高價
            L5 = 0 #105年最低價                
            
        try:
            ls6 =  dfs[0].iloc[8] #104年
            
            H6 = ls6[4] #104年最高價
            L6 = ls6[6] #104年最低價
        except:
            H6 = 0 #104年最高價
            L6 = 0 #104年最低價            
            
        try:
            ls7 =  dfs[0].iloc[9] #103年
            
            H7 = ls7[4] #103年最高價
            L7 = ls7[6] #103年最低價
        except:
            H7 = 0 #103年最高價
            L7 = 0 #103年最低價            
            
        try:
            ls8 =  dfs[0].iloc[10] #102年

            H8 = ls8[4] #102年最高價
            L8 = ls8[6] #102年最低價  
        except:
            H8 = 0 #102年最高價
            L8 = 0 #102年最低價              
            
            
        try:
            ls9 =  dfs[0].iloc[11] #101年
                       
            H9 = ls9[4] #101年最高價
            L9 = ls9[6] #101年最低價
        except:
            H9 = 0 #101年最高價
            L9 = 0 #101年最低價            

            #print(tablelen)

################################################
    bank_url = "https://dj.mybank.com.tw/"
    sheet_type = 'z/zc/zcq/zcq0.djhtm?b=Y&a=' #ISQ 合併損益表 年表
    url = bank_url + sheet_type + stock_id
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))


    bt1N = dfs[2][1][0] #最新1年的名稱
    bt2N = dfs[2][2][0] #最新2年的名稱
    bt3N = dfs[2][3][0] #最新3年的名稱
    bt4N = dfs[2][4][0] #最新4年的名稱
    bt5N = dfs[2][5][0] #最新5年的名稱
    bt6N = dfs[2][6][0] #最新6年的名稱
    bt7N = dfs[2][7][0] #最新7年的名稱
    bt8N = dfs[2][8][0] #最新8年的名稱

#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][70] #最新1季的合併總損益 税後淨利
#print(dfs[2][1][11])
    bt1 = float((dfs[2][1][64])) #最新1年的合併總損益 税前淨利 百萬
    bt2 = float((dfs[2][2][64])) #最新2年的合併總損益 税前淨利 百萬
    bt3 = float((dfs[2][3][64])) #最新3年的合併總損益 税前淨利 百萬
    bt4 = float((dfs[2][4][64])) #最新4年的合併總損益 税前淨利 百萬
        
    bt5 = float((dfs[2][5][64])) #最新5年的合併總損益 税前淨利 百萬
    bt6 = float((dfs[2][6][64])) #最新6年的合併總損益 税前淨利 百萬
    bt7 = float((dfs[2][7][64])) #最新7年的合併總損益 税前淨利 百萬
    bt8 = float((dfs[2][8][64])) #最新8年的合併總損益 税前淨利 百萬        
    print(bt1)
        #############################################################

    sheet_type2 = 'z/zc/zcp/zcpa/zcpa0.djhtm?b=Y&a=' #BSQ 表 年表
    url2 = bank_url + sheet_type2 + stock_id
    r = requests.get(url2, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))
        
    sh1 = float((dfs[2][1][92])) #最新1年的合併資產負債 股東權益總額 百萬
    sh2 = float((dfs[2][2][92])) #最新2年的合併資產負債 股東權益總額 百萬
    sh3 = float((dfs[2][3][92])) #最新3年的合併資產負債 股東權益總額 百萬
    sh4 = float((dfs[2][4][92])) #最新4年的合併資產負債 股東權益總額 百萬

    sh5 = float((dfs[2][5][92])) #最新5年的合併資產負債 股東權益總額 百萬
    sh6 = float((dfs[2][6][92])) #最新6年的合併資產負債 股東權益總額 百萬
    sh7 = float((dfs[2][7][92])) #最新7年的合併資產負債 股東權益總額 百萬
    sh8 = float((dfs[2][8][92])) #最新8年的合併資產負債 股東權益總額 百萬    
    print(sh1)

    bt_roe1 = round(float(bt1)/float(sh1),4) #稅前ROE
    bt_roe2 = round(float(bt2)/float(sh2),4) #稅前ROE
    bt_roe3 = round(float(bt3)/float(sh3),4) #稅前ROE
    bt_roe4 = round(float(bt4)/float(sh4),4) #稅前ROE

    bt_roe5 = round(float(bt5)/float(sh5),4) #稅前ROE
    bt_roe6 = round(float(bt6)/float(sh6),4) #稅前ROE
    bt_roe7 = round(float(bt7)/float(sh7),4) #稅前ROE
    bt_roe8 = round(float(bt8)/float(sh8),4) #稅前ROE    
    print(bt_roe1)

    bt_roe1p = str(bt_roe1*100)+ "%"
    bt_roe2p = str(bt_roe2*100)+ "%"
    bt_roe3p = str(bt_roe3*100)+ "%"
    bt_roe4p = str(bt_roe4*100)+ "%"

    bt_roe5p = str(bt_roe5*100)+ "%"
    bt_roe6p = str(bt_roe6*100)+ "%"
    bt_roe7p = str(bt_roe7*100)+ "%"
    bt_roe8p = str(bt_roe8*100)+ "%"        
    print(bt_roe1p)

################################################
    sheet_type3 = 'z/zc/zcr/zcr0.djhtm?b=Y&a=' #財務比率 表 年表
    url2 = bank_url + sheet_type3 + stock_id
    r = requests.get(url2, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))
        
    b1 = float((dfs[2][1][18])) #最新1年的每股淨值(F)(TSE公告數) 	
    b2 = float((dfs[2][2][18])) #最新2年的每股淨值(F)(TSE公告數) 
    b3 = float((dfs[2][3][18])) #最新3年的每股淨值(F)(TSE公告數) 
    b4 = float((dfs[2][4][18])) #最新4年的每股淨值(F)(TSE公告數) 

    b5 = float((dfs[2][5][18])) #最新5年的每股淨值(F)(TSE公告數) 	
    b6 = float((dfs[2][6][18])) #最新6年的每股淨值(F)(TSE公告數) 
    b7 = float((dfs[2][7][18])) #最新7年的每股淨值(F)(TSE公告數) 
    b8 = float((dfs[2][8][18])) #最新8年的每股淨值(F)(TSE公告數) 
    
    print(b1)

    pb1_H = round(float(H1)/float(b1),4)
    pb1_L = round(float(L1)/float(b1),4)    
    
    try:
        pb2_H = round(float(H2)/float(b2),4)
        pb2_L = round(float(L2)/float(b2),4)  
    except:
        pb2_H = round(float(H2)/float(b2),4)
        pb2_L = round(float(L2)/float(b2),4)          
    
    
    try:
        pb3_H = round(float(H3)/float(b3),4)
        pb3_L = round(float(L3)/float(b3),4)
    except:
        pb3_H = 0
        pb3_L = 0       
    
    try:
        pb4_H = round(float(H4)/float(b4),4)
        pb4_L = round(float(L4)/float(b4),4)  
    except:
        pb4_H = 0
        pb4_L = 0 
        
    try:
        pb5_H = round(float(H5)/float(b5),4)
        pb5_L = round(float(L5)/float(b5),4)    
    except:
        pb5_H = 0
        pb5_L = 0        
        
    try:
        pb6_H = round(float(H6)/float(b6),4)
        pb6_L = round(float(L6)/float(b6),4)
    except:
        pb6_H = 0
        pb6_L = 0        
    
    try:
        pb7_H = round(float(H7)/float(b7),4)
        pb7_L = round(float(L7)/float(b7),4)  
    except:
        pb7_H = 0
        pb7_L = 0          
        
    try:    
        pb8_H = round(float(H8)/float(b8),4)
        pb8_L = round(float(L8)/float(b8),4) 
    except:
        pb8_H = 0
        pb8_L = 0        
    print(pb1_H)



    kn1_H = round(bt_roe1/pb1_H,4)
    kn1_L = round(bt_roe1/pb1_L,4)    
    
    try:
        kn2_H = round(bt_roe1/pb2_H,4)
        kn2_L = round(bt_roe1/pb2_L,4) 
    except:
        kn2_H = 0
        kn2_L = 0         
    
    try:
        kn3_H = round(bt_roe1/pb3_H,4)
        kn3_L = round(bt_roe1/pb3_L,4)
    except:
        kn3_H = 0
        kn3_L = 0        
    
    try:
        kn4_H = round(bt_roe1/pb4_H,4)
        kn4_L = round(bt_roe1/pb4_L,4)
    except:
        kn4_H = 0
        kn4_L = 0     

    try:
        kn5_H = round(bt_roe1/pb5_H,4)
        kn5_L = round(bt_roe1/pb5_L,4)
    except:
        kn5_H = 0
        kn5_L = 0

    try:    
        kn6_H = round(bt_roe1/pb6_H,4)
        kn6_L = round(bt_roe1/pb6_L,4)
    except:
        kn6_H = 0
        kn6_L = 0
        
    try:
        kn7_H = round(bt_roe1/pb7_H,4)
        kn7_L = round(bt_roe1/pb7_L,4)
    except:
        kn7_H = 0
        kn7_L = 0
        
    try:
        kn8_H = round(bt_roe1/pb8_H,4)
        kn8_L = round(bt_roe1/pb8_L,4)
    except:
        kn8_H = round(bt_roe1/pb8_H,4)
        kn8_L = round(bt_roe1/pb8_L,4)        
    print(kn1_H)

    kn1_Hp = str(kn1_H*100) + "%"
    kn1_Lp = str(kn1_L*100) + "%"
    kn2_Hp = str(kn2_H*100) + "%"
    kn2_Lp = str(kn2_L*100) + "%"        
    kn3_Hp = str(kn3_H*100) + "%"
    kn3_Lp = str(kn3_L*100) + "%"
    kn4_Hp = str(kn4_H*100) + "%"
    kn4_Lp = str(kn4_L*100) + "%"

    kn5_Hp = str(kn5_H*100) + "%"
    kn5_Lp = str(kn5_L*100) + "%"
    kn6_Hp = str(kn6_H*100) + "%"
    kn6_Lp = str(kn6_L*100) + "%"        
    kn7_Hp = str(kn7_H*100) + "%"
    kn7_Lp = str(kn7_L*100) + "%"
    kn8_Hp = str(kn8_H*100) + "%"
    kn8_Lp = str(kn8_L*100) + "%"   
        
    print(kn1_Hp)
    #print(risk_reward)
    
    return H0, H1, H2, H3, H4, H5, H6, H7, H8, H9, L0, L1, L2, L3, L4, L5, L6, L7, L8, L9, bt1N, bt2N, bt3N, bt4N, bt5N, bt6N, bt7N, bt8N, bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, sh1, sh2, sh3, sh4, sh5, sh6, sh7, sh8, bt_roe1p, bt_roe2p, bt_roe3p, bt_roe4p, bt_roe5p, bt_roe6p, bt_roe7p, bt_roe8p, b1, b2, b3, b4, b5, b6, b7, b8, kn1_Hp, kn1_Lp, kn2_Hp, kn2_Lp, kn3_Hp, kn3_Lp, kn4_Hp, kn4_Lp, kn5_Hp, kn5_Lp, kn6_Hp, kn6_Lp, kn7_Hp, kn7_Lp, kn8_Hp, kn8_Lp
Kn8yPrice("1240")