# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 12:34:48 2020

@author: Nicholas Huang 
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

def stock_Prof2_InvTO5(stock_id):  #營業利益率評分標準  #20211224 DJ大改版 無法再使用Pandas
    headers = {'Referer':my_Referer,'user-agent': my_UserAgent}
    sheet_type = 'z/zc/zcr/zcr_' #FRQ 財務比率 季表
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
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

    newest_Fin_Q = xYearSeasonTitleList[2] #最新1季的財報季份

    #b1N = dfs[2][1][1] #最新1季的名稱
    b1N = xYearSeasonTitleList[2] #最新1季的名稱
    b2N = xYearSeasonTitleList[3] #最新2季的名稱
    b3N = xYearSeasonTitleList[4] #最新3季的名稱
    b4N = xYearSeasonTitleList[5] #最新4季的名稱
    b5N = xYearSeasonTitleList[6] #最新5季的名稱
    b6N = xYearSeasonTitleList[7] #最新6季的名稱
    b7N = xYearSeasonTitleList[8] #最新7季的名稱
    b8N = xYearSeasonTitleList[9] #最新8季的名稱
    
    #print(b1N)
    

    #a9N = "近四季平均"
    #a10N = "最新1季季增率"
    #a11N = "最新2季季增率"
    #a12N = "最新3季季增率"
    #a13N = "最新4季季增率"

    ProfitN = []
    ProfitN.extend([b1N,b2N,b3N,b4N,b5N,b6N,b7N,b8N])
#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][10] 最新一季營益率
#print(dfs[2][1][10])

    b1 = float(xProfitList[2]) #float((dfs[2][1][10])) #最新1季的營益率
    b2 = float(xProfitList[3]) #float((dfs[2][2][10])) #最新2季的營益率 
    b3 = float(xProfitList[4]) #float((dfs[2][3][10])) #最新3季的營益率
    b4 = float(xProfitList[5]) #float((dfs[2][4][10])) #最新4季的營益率
    b5 = float(xProfitList[6]) #float((dfs[2][5][10])) #最新5季的營益率
    b6 = float(xProfitList[7]) #float((dfs[2][6][10])) #最新6季的營益率
    b7 = float(xProfitList[8]) #float((dfs[2][7][10])) #最新7季的營益率
    b8 = float(xProfitList[9]) # float((dfs[2][8][10])) #最新8季的營益率
    
    #print(b1)
    
    Profit = []
    Profit.extend([b1,b2,b3,b4,b5,b6,b7,b8])

#print(a1)

    b9 = round((b1+b2+b3+b4)/4,3) #四季平均
    #print(a9)
    b10 = round(float((b1-b2)/abs(b2)),3) #最新一季季增率
    #print(a10)
    b11 = float((b2-b3)/abs(b3)) #次新一季季增率
    #print(a11)
    b12 = float((b3-b4)/abs(b4)) #第3新一季季增率
    #print(a12)
    #a13 = float((a4-a5)/abs(a5)) #第4新一季季增率
    
    b10p = str(b10*100) + '%'
    #print(a13)

    if (b1 < 0):
        result2 = "C"      #最近一季為負

    elif (b9 < 0):
        result2 = "C"      #過去四季的平均為負
        
    elif (0 < b9 <= 5):
        result2 = "B"      #或不論漲跌幅，過去四季平均營益率在5%以下
        
    elif (b10 <= -0.2):
        result2 = "B"      #最近一季比上一季跌20%以上

    elif (b11 <= -0.2):
        result2 = "BB"     #過去四季曾出現季與季之間下跌20%以上，但不包括最近一季 1
        
    elif (b12 <= -0.2):
        result2 = "BB"     #過去四季曾出現季與季之間下跌20%以上，但不包括最近一季 2

    elif (15 >= b9 >= 10) and (b1 > b2) and (b2 > b3*0.8) and (b3 > b4*0.8):
        result2 = "AA"     #或過去四季皆維持穩定沒有下降，且平均在10-15%，最近一季呈現上升趨勢


    elif (15 >= b9 >= 10) and (b1 > b2*0.8) and (b2 > b3*0.8) and (b3 > b4*0.8): 
        result2 = "A"      #過去四季皆維持穩定沒有下降，且平均在10-15%

        
    elif (10 > b9 >= 5) and (b1 > b2) and (b2 > b3*0.8) and (b3 > b4*0.8):
        result2 = "A"      #或過去四季皆維持穩定沒有下跌，平均只有5-10%，但最近一季呈現上升趨勢



    elif (b9 > 15) and (b1 > b2*0.8) and (b2 > b3*0.8) and (b3 > b4*0.8):
        result2 = "AA"   #過去四季皆維持穩定沒有下跌，且平均在15%以上

      
        
    else:
        result2 = "BB"
        

    #############以下為存貨週轉率的部份################################
    xInv = table2[-35].text
    xInvList = xInv.split("\n")
    #print(xInvList)


    e1N = xYearSeasonTitleList[2] #最新1季的名稱
    e2N = xYearSeasonTitleList[3] #最新2季的名稱
    e3N = xYearSeasonTitleList[4] #最新3季的名稱
    e4N = xYearSeasonTitleList[5] #最新4季的名稱
    e5N = xYearSeasonTitleList[6] #最新5季的名稱
    e6N = xYearSeasonTitleList[7] #最新6季的名稱
    e7N = xYearSeasonTitleList[8] #最新7季的名稱
    e8N = xYearSeasonTitleList[9] #最新8季的名稱 
    
    

    InvTON = []
    InvTON.extend([e1N,e2N,e3N,e4N,e5N,e6N,e7N,e8N])
  
    e1 = float(xInvList[2]) #由左至右，第1欄數據 存貨週轉率 Inventory_turnover
    e2 = float(xInvList[3]) #由左至右，第2欄數據 存貨週轉率 Inventory_turnover
    e3 = float(xInvList[4]) #由左至右，第3欄數據 存貨週轉率 Inventory_turnover
    e4 = float(xInvList[5]) #由左至右，第4欄數據 存貨週轉率 Inventory_turnover
    e5 = float(xInvList[6]) #由左至右，第5欄數據 存貨週轉率 Inventory_turnover
    e6 = float(xInvList[7]) #由左至右，第6欄數據 存貨週轉率 Inventory_turnover
    e7 = float(xInvList[8]) #由左至右，第7欄數據 存貨週轉率 Inventory_turnover
    e8 = float(xInvList[9]) #由左至右，第8欄數據 存貨週轉率 Inventory_turnover
    #print(e1)
    InvTO = []
    InvTO.extend([e1,e2,e3,e4,e5,e6,e7,e8])

    e9  = float((e1+e2+e3+e4)/4) #四季平均
    #original
    ZeroCompany = ['6131','2471','2643','2743','3130','3546','4152','4550','4994','5604','6101','6482','6643','8473','6690','2719','8422','8446','8934','8477','9933','6172','8476','9943','2607','5210','6180','1439','2546','2701','2745','3264','3567','4157','4803','5364','5607','6169','6492','8077','8497','5287','6516','2543','9928','8926','8462','2642','6624','5344','5478','5704','1259','5703','1516','2617','2706','2904','3289','3587','4174','4946','5516','5609','6231','6542','8367','2516','3687','2724','8433','6592','6561','6179','8066','6533','2612','2736','5203','2707','2227','2636','2731','3083','3529','3629','4529','4953','5601','5706','6404','6625','8472','5201','6183','2702','1535','5209','3086','2404','6596','2712','2608','6111','2752','2616']
    
    try:  #排除存貨周轉率為零的問題
        e10 = float((e1-e2)/e2) #最新一季季增率
        e11 = float((e2-e3)/e3) #次新一季季增率
        e12 = float((e3-e4)/e4) #前新第三季季增率
        e13 = float((e4-e5)/e5) #前新第四季季增率
        
        
        
        if (stock_id in ZeroCompany):
            result5 = "不評分"
        
        elif (e10 <= -0.2):
            result5 = "C"    #最近一季出現20%以上的跌幅
        
        elif (e11 <= -0.2 or e12 <= -0.2):
            result5 = "B"    #最近四季曾經出現單季20%以上的跌幅
        

        elif (e10 < 0 and e11 < 0 and (e1-e3)/e3 <= -0.2): 
            result5 = "BB"   #最近四季出現連續兩季下跌，累積跌幅在20%以上
        
        elif (e11 < 0 and e12 < 0 and (e2-e4)/e4 <= -0.2): 
            result5 = "BB"   #最近四季出現連續兩季下跌，累積跌幅在20%以上

        elif (e9 < 1.5 and e10 > -0.2 and e11 > -0.2 and e12 > -0.2):
            result5 = "A"    #最近四季穩定不下降，且平均在1.5次以下

        elif (e9 >= 1.5 and e10 > -0.2 and e11 > -0.2 and e12 > -0.2):
            result5 = "AA"   #最近四季穩定不下降，且平均在1.5次以上

        
        else:
            result5 = "不評分"

    except:
        result5 = "不評分"



    return result2, ProfitN, Profit, b1N, b2N, b3N, b4N, b5N, b6N, b7N, b8N, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b10p, result5, InvTON, InvTO, e1N, e2N, e3N, e4N, e5N, e6N, e7N, e8N, e1, e2, e3, e4, e5, e6, e7, e8, newest_Fin_Q

############################################################################

def stock_NetInc3_EPS4(stock_id): #税後淨利年增率
    headers = {'Referer':my_Referer,'user-agent': my_UserAgent}
    
    sheet_type = 'z/zc/zcq/zcq_' #ISQ 合併損益表 季表
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    #table = soup.find_all('table')[0];
    table2 = soup.find_all(class_ = 'table-row')   
    
    xYearSeasonTitle = table2[0].text
    xYearSeasonTitleList = xYearSeasonTitle.split("\n")

    xNet = table2[-6].text    
    xNetList = xNet.split("\n")
    
    print(xNetList)   

    xEPS = table2[-9].text    
    xEPSList = xEPS.split("\n")
    
    print(xEPSList) 
    

    c1N = xYearSeasonTitleList[2] #最新1季的名稱
    c2N = xYearSeasonTitleList[3]  #最新2季的名稱
    c3N = xYearSeasonTitleList[4]  #最新3季的名稱
    c4N = xYearSeasonTitleList[5]  #最新4季的名稱
    c5N = xYearSeasonTitleList[6]  #最新5季的名稱
    c6N = xYearSeasonTitleList[7]  #最新6季的名稱
    c7N = xYearSeasonTitleList[8]  #最新7季的名稱
    c8N = xYearSeasonTitleList[9]  #最新8季的名稱

    NetIncomeN = []
    NetIncomeN.extend([c1N,c2N,c3N,c4N,c5N,c6N,c7N,c8N])

#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][70] #最新1季的合併總損益 税後淨利
#print(dfs[2][1][11])
    c1 = float((xNetList[2].replace(",",""))) #最新1季的合併總損益 税後淨利
    c2 = float((xNetList[3].replace(",",""))) #最新2季的合併總損益 税後淨利
    c3 = float((xNetList[4].replace(",",""))) #最新3季的合併總損益 税後淨利
    c4 = float((xNetList[5].replace(",",""))) #最新4季的合併總損益 税後淨利
    c5 = float((xNetList[6].replace(",",""))) #最新5季的合併總損益 税後淨利
    c6 = float((xNetList[7].replace(",",""))) #最新6季的合併總損益 税後淨利
    c7 = float((xNetList[8].replace(",",""))) #最新7季的合併總損益 税後淨利
    c8 = float((xNetList[9].replace(",",""))) #最新8季的合併總損益 税後淨利
    #print(c1)
    NetIncome = []
    NetIncome.extend([c1,c2,c3,c4,c5,c6,c7,c8])
#print(a1)
    c9 = float((c1-c5)/abs(c5)) #最新一季淨利年增率
#print(c9)
    c10 = float((c2-c6)/abs(c6)) #次新一季淨利年增率
#print(c10)
    c11 = float((c3-c7)/abs(c7)) #第3新一季淨利年增率
    #print(c11)
    c12 = float((c4-c8)/abs(c8)) #第4新一季淨利年增率
    
    
    pc9 = str(round(c9*100,2))+'%'
    pc10 = str(round(c10*100,2))+'%'
    pc11 = str(round(c11*100,2))+'%'

#print(c12)
#############計算負數的季數
    total = 0
    for n in [c9,c10,c11,c12]:
        if n < 0:
            total += 1
#print(total)
#################
    c13 = total #season_number_below0
#print(c13)

    if (c9 < 0 and c10 < 0):
        result3 = "C"     #最近兩季為負數
        
        
    elif (c9 < c10 < c11 and c9 < 0.5):
        result3 = "B"     #或近三季遞減（且最近一季税後淨利年增率低於50%）
        
    elif (c9 < 0):
        result3 = "B"     #最近一季出現負數

    elif (c13 >= 2):
        result3 = "B"     #或過去四季出現兩季負數
        


    elif (c9 > 0 and c10 > 0 and c11 > 0 and c9 > c10): 
        result3 = "AA"    #近三季皆為正數且最近一季呈現成長

    elif (c9 >= 0.5 and c10 >= 0.5 and c11 >= 0.5):
        result3 = "AA"    #或近三季皆在50%以上（遞減也無妨）

    elif (c9 > 0 and c10 > 0 and (c9-c10)/c10 > -0.5):
        result3 = "A"     #近兩季皆為正數且沒有出現大幅衰退

    elif (c10 < 0 and c9 > 0):
        result3 = "BB"    #或最近一季由負轉正
        
    elif (c9 > 0 and c10 > 0 and (c9-c10)/c10 <= -0.5):
        result3 = "BB"    #近兩季皆為正數但最近一季出現50%以上的衰退



        


        #如果同時滿足兩項評分，以較低評分為主。BB以下是這樣，A以上看情況。tivo的linebot有應證。
    #print (result3)


#########################以下為EPS指標的計算#########################


    d1N = xYearSeasonTitleList[2] #最新1季的名稱
    d2N = xYearSeasonTitleList[3] #最新2季的名稱
    d3N = xYearSeasonTitleList[4] #最新3季的名稱
    d4N = xYearSeasonTitleList[5] #最新4季的名稱
    d5N = xYearSeasonTitleList[6] #最新5季的名稱
    d6N = xYearSeasonTitleList[7] #最新6季的名稱
    d7N = xYearSeasonTitleList[8] #最新7季的名稱
    d8N = xYearSeasonTitleList[9] #最新8季的名稱

    EPSN = []
    EPSN.extend([d1N,d2N,d3N,d4N,d5N,d6N,d7N,d8N])


#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][98] #最新1季的合併總損益 每股盈餘
#dfs[2][1] #最新1季的合併總損益 税後淨利

#print (d1)

    d1 = float((xEPSList[2])) #最新1季的合併總損益 EPS
    d2 = float((xEPSList[3])) #最新2季的合併總損益 EPS
    d3 = float((xEPSList[4])) #最新3季的合併總損益 EPS
    d4 = float((xEPSList[5])) #最新4季的合併總損益 EPS
    d5 = float((xEPSList[6])) #最新5季的合併總損益 EPS
    d6 = float((xEPSList[7])) #最新6季的合併總損益 EPS
    d7 = float((xEPSList[8])) #最新7季的合併總損益 EPS
    d8 = float((xEPSList[9])) #最新8季的合併總損益 EPS

    EPS = []
    EPS.extend([d1,d2,d3,d4,d5,d6,d7,d8])

#print(EPS)

    #d9 = float((d1-d5)/d5) #最新一季年增率
#print(d9)
    #d10 = float((d2-d6)/d6) #次新一季年增率
#print(d10)
    #d11 = float((d3-d7)/d7) #第3新一季年增率
#print(d11)
    #d12 = float((d4-d8)/d8) #第4新一季年增率
#print(d12)
    d13  = d1+d2+d3+d4 #= season4Sum
#print(d13)

    if (d13 < 0):
        result4 = "C"   #最近四季累積虧損
        
    elif (d1 < 0):
        result4 = "B"   #或不管最近四季累積數，最近一季出現虧損者
        
    elif (1 > d13 > 0):
        result4 = "B"   #最近四季累積超過0元
        
    elif (3 >= d13 >= 1):
        result4 = "BB"  #最近四季累積1-3元

    elif (5 >= d13 > 3):
        result4 = "A"   #最近四季累積3-5元

    elif (d13 > 5):
        result4 = "AA"
        

    return result3, NetIncomeN, NetIncome, c1N, c2N, c3N, c4N, c5N, c6N, c7N, c8N, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, pc9, pc10, pc11, result4, EPSN, EPS, d1N, d2N, d3N, d4N, d5N, d6N, d7N, d8N, d1, d2, d3, d4, d5, d6, d7, d8
################################################################################


def stock_Cashflow6(stock_id): #(股票代碼, 股票名稱. 股票價格觸及下緣)
    headers = {'Referer':my_Referer,'user-agent': my_UserAgent}

    sheet_type = 'z/zc/zc3/zc3_' #合併現金流量表 季表
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
        #table = soup.find_all('table')[0];
    table2 = soup.find_all(class_ = 'table-row') 

  
    xYearSeasonTitle = table2[0].text
    xYearSeasonTitleList = xYearSeasonTitle.split("\n")

    xOpe = table2[54].text
    xOpeList = xOpe.split("\n")
    
    #print(xOpeList)

    xInv = table2[70].text
    xInvList = xInv.split("\n")
    
    #print(xInvList)
#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][54] #最新1季的合併現金流量 營運的現金流量
#dfs[2][1][70] #最新1季的合併現金流量 投資的現金流量

#print(dfs[2][1][11])
#print(dfs[2][1])
    
    f1N = xYearSeasonTitleList[2] #最新1季的名稱
    f2N = xYearSeasonTitleList[3] #最新2季的名稱
    f3N = xYearSeasonTitleList[4] #最新3季的名稱
    f4N = xYearSeasonTitleList[5] #最新4季的名稱
    f5N = xYearSeasonTitleList[6] #最新5季的名稱
    f6N = xYearSeasonTitleList[7] #最新6季的名稱
    f7N = xYearSeasonTitleList[8] #最新7季的名稱
    f8N = xYearSeasonTitleList[9] #最新8季的名稱

    CashFlowN = []
    CashFlowN.extend([f1N,f2N,f3N,f4N,f5N,f6N,f7N,f8N])
    

    f1 = int(xOpeList[2].replace(",","")) + int(xInvList[2].replace(",","")) #最新1季的自由現金流量
    
    #print(f1) 
    

    f2 = int(xOpeList[2].replace(",","")) + int(xInvList[2].replace(",","")) #最新2季的自由現金流量
    f3 = int(xOpeList[3].replace(",","")) + int(xInvList[3].replace(",","")) #最新3季的自由現金流量
    f4 = int(xOpeList[4].replace(",","")) + int(xInvList[4].replace(",","")) #最新4季的自由現金流量
    f5 = int(xOpeList[5].replace(",","")) + int(xInvList[5].replace(",","")) #最新5季的自由現金流量
    f6 = int(xOpeList[6].replace(",","")) + int(xInvList[6].replace(",","")) #最新6季的自由現金流量
    f7 = int(xOpeList[7].replace(",","")) + int(xInvList[7].replace(",","")) #最新7季的自由現金流量
    f8 = int(xOpeList[8].replace(",","")) + int(xInvList[8].replace(",","")) #最新8季的自由現金流量



    CashFlow = []
    CashFlow.extend([f1,f2,f3,f4,f5,f6,f7,f8])

#print(CashFlow)

    f9 = f1+f2+f3+f4 #前4季總和
#print(d9)
    f10 = f1+f2+f3+f4+f5+f6 #前6季總和
#print(d10)
    #f11 = f1+f2+f3+f4+f5+f6+f7+f8 #前8季總和
#print(d11)
    
    if (f9 < 0 and f10 < 0):
        result6 = "C"     #最近六季累積為負數且最近四季累積為負數
        
    elif (f9 < 0 and f10 > 0):
        result6 = "B"     #最近六季累積為正數且最近四季累積為負數
        
    elif (f9 > 0 and f10 < 0):
        result6 = "BB"     #最近六季累積為負數且最近四季累積為正數

    elif (f1 > 0 and f2 > 0 and f3 > 0 and f4 > 0 and f5 > 0 and f6 > 0):
        result6 = "AA"     #連續六季出現正數

    elif (f10 > 0 and f9 > 0):
        result6 = "A"     #最近六季累積為正數且最近四季累積為正數







#print (result6)
    return result6, CashFlowN, CashFlow, f1N, f2N, f3N, f4N, f5N, f6N, f7N, f8N, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10
    
 


def stock_Rev1(stock_id): #(股票代碼, 股票名稱. 股票價格觸及下緣) #營收評分標準
    headers = {'Referer':my_Referer,'user-agent': my_UserAgent}
    sheet_type = 'z/zc/zch/zch_' #Rev 營收   
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))

#dfs[2] 真正表格
#dfs[2][4] 營收年增率
#dfs[2][4][6] 最新一個月年增率
    #print(dfs[2][4][6])
    ###MoneyDJ
    newest_Rev_month = str(dfs[2][0][6]) #最新一個月的月份
    a1N = dfs[2][0][6] #最新1個月的名稱 
    a2N = dfs[2][0][7] #最新2個月的名稱 
    a3N = dfs[2][0][8] #最新3個月的名稱
    a4N = dfs[2][0][9] #最新4個月的名稱 
    a5N = dfs[2][0][10] #最新5個月的名稱 
    a6N = dfs[2][0][11] #最新6個月的名稱
    a7N = dfs[2][0][12] #最新7個月的名稱

    a1Nm = dfs[2][0][6][-2:] #最新1個月的名稱，只有月份兩個數字
    a2Nm = dfs[2][0][7][-2:] #最新2個月的名稱，只有月份兩個數字
    a3Nm = dfs[2][0][8][-2:] #最新3個月的名稱，只有月份兩個數字
    a4Nm = dfs[2][0][9][-2:] #最新4個月的名稱，只有月份兩個數字 
    a5Nm = dfs[2][0][10][-2:] #最新5個月的名稱，只有月份兩個數字 
    a6Nm = dfs[2][0][11][-2:] #最新6個月的名稱，只有月份兩個數字


    RevN = []
    RevN.extend([a1N,a2N,a3N,a4N,a5N,a6N])
    
    RevNm = []
    RevNm.extend([a1Nm,a2Nm,a3Nm,a4Nm,a5Nm,a6Nm])
    

        

    a1 = round(float((dfs[2][4][6])[:-1])/100,4) #最新1個月的營收年增率 
    a2 = round(float((dfs[2][4][7])[:-1])/100,4) #最新2個月的營收年增率 
    a3 = round(float((dfs[2][4][8])[:-1])/100,4) #最新3個月的營收年增率 
    a4 = round(float((dfs[2][4][9])[:-1])/100,4) #最新4個月的營收年增率 
    a5 = round(float((dfs[2][4][10])[:-1])/100,4) #最新5個月的營收年增率 
    a6 = round(float((dfs[2][4][11])[:-1])/100,4) #最新6個月的營收年增率 
    a7 = round(float((dfs[2][4][12])[:-1])/100,4) #最新7個月的營收年增率 

    Rev = []
    Rev.extend([a1,a2,a3,a4,a5,a6,a7])
    
    lu2_1n2 = round(float((dfs[2][6][6])[:-1])/100,4) #2月最新，1,2月的累積營收年增率
    lu3_1n2 = round(float((dfs[2][6][7])[:-1])/100,4) #3月最新，1,2月的累積營收年增率
    lu4_1n2 = round(float((dfs[2][6][8])[:-1])/100,4) #4月最新，1,2月的累積營收年增率
    lu5_1n2 = round(float((dfs[2][6][9])[:-1])/100,4) #5月最新，1,2月的累積營收年增率
    lu6_1n2 = round(float((dfs[2][6][10])[:-1])/100,4) #6月最新，1,2月的累積營收年增率 
    lu7_1n2 = round(float((dfs[2][6][11])[:-1])/100,4) #7月最新，1,2月的累積營收年增率     
    
    #if c in 
    
    na1 = str(round(a1*100,2))  #改為百分比的年增率
    na2 = str(round(a2*100,2))
    na3 = str(round(a3*100,2))
    na4 = str(round(a4*100,2))
    na5 = str(round(a5*100,2))
    na6 = str(round(a6*100,2))    
    na7 = str(round(a7*100,2))     

    a9 = (a1+a2+a3+a4+a5+a6)/6 #無農曆月份 6個月平均   小數
    na9 = str(round(a9*100,2))  #無農曆月份 6個月平均 百分比
    
    
    #print(a9)
    a10 = float((a1-a2)/a2) #最新一個月年增率和上個月比較
    na10 = str(round(a10*100,2)) #最新一個月年增率和上個月比較 百分比
    #print(a10)


    if a1Nm == "02":   #近六個內有一二月的判斷式，2月為最新月份
        luX = str(round(lu2_1n2*100,2))  #1,2月合併數據 改為百分比
        luX_MoM = float((lu2_1n2-a3)/a3) #1,2月跟12月的月增率比較
        nluX_MoM = str(round((float((lu2_1n2-a3)/a3))*100,2)) 
        #1,2月跟12月的月增率比較 改為百分比
        
        
        
        if ((lu2_1n2+a3+a4+a5+a6+a7)/6 < 0):
            result1 = "C"      #過去6個月平均數為負
    
        elif (lu2_1n2 < 0): #或最近一個月為負數，最新一個月是1,2月 #2021/3/3改為1,2月合併數據比較

        #elif (luX_MoM < 0): #或最近一個月為負數，最新一個月是1,2月 #2021/3/3改為1,2月合併數據比較

            result1 = "C"

        elif (lu2_1n2 < 0 or a3 < 0 or a4 < 0 or a5 < 0 or a6 < 0 or a7 < 0):

            result1 = "BB"         #過去六個月曾經出現單月負成長

        elif (lu2_1n2 < a3 < a4 and (lu2_1n2+a3+a4+a5+a6+a7)/6 > 0): #2,1,12,11月遞減的情況
            result1 = "B"      #過去六個月平均為正數，但最近三個月出現遞減（不論幅度）

        elif ((lu2_1n2+a3+a4+a5+a6+a7)/6 > 0.25 and 0 > (lu2_1n2-a3)/a3 >= -0.5):
            result1 = "A"      #或過去六個月平均超過25%，但最近一個月出現小幅衰退。（年增率較上個月下跌幅度在50%以內）   

        elif (lu2_1n2 > 0 and a3 > 0 and a4 > 0 and a5 >0 and a6 > 0 and a7 > 0 and 0.25 >= (lu2_1n2+a3+a4+a5+a6+a7)/6 >= 0.1 and lu2_1n2 >= a3):
            result1 = "A"      #過去六個月皆為正數平均10-25%，且最近一個月的年增率與上個月比較為增加或持平（>=0）            
            

        
        elif (lu2_1n2 > 0 and a3 > 0 and a4 > 0 and a5 >0 and a6 >0 and a7 > 0 and (lu2_1n2+a3+a4+a5+a6+a7)/6 > 0.25 and lu2_1n2 >= a3):
            result1 = "AA"     #過去六個月皆為正數且平均超過25%，且最近一個月的年增率與上個月比為增加或持平（>=0）
                        

        else:
            result1 = "BB"      #無法列為其他評等

###########################            

    elif a1Nm == "03":   #近六個內有一二月的判斷式，3月為最新月份
        
        luX = str(round(lu3_1n2*100,2))  #1,2月合併數據 改為百分比
        luX_MoM = float((a1-lu3_1n2)/lu3_1n2) #1,2月跟3月的月增率比較
        nluX_MoM = str(round((float((a1-lu3_1n2)/lu3_1n2))*100,2)) #1,2月跟3月的月增率比較 改為百分比
        
        if ((a1+lu3_1n2+a4+a5+a6+a7)/6 < 0):
            result1 = "C"      #過去6個月平均數為負
    
        elif (a1 < 0): #或最近一個月為負數，最新一個月是3月

            result1 = "C"

        elif (a1 < 0 or lu3_1n2 < 0 or a4 < 0 or a5 < 0 or a6 < 0 or a7 < 0): #3,2,1,12,11,10,9月

            result1 = "BB"         #過去六個月曾經出現單月負成長

        elif (a1 < lu3_1n2 < a4 and (a1+lu3_1n2+a4+a5+a6+a7)/6 > 0): #3,2,1月遞減的情況
            result1 = "B"      #過去六個月平均為正數，但最近三個月出現遞減（不論幅度）

        elif ((a1+lu3_1n2+a4+a5+a6+a7)/6 > 0.25 and 0 > (a1-lu3_1n2)/lu3_1n2 >= -0.5):
            result1 = "A"      #或過去六個月平均超過25%，但最近一個月出現小幅衰退。（年增率較上個月下跌幅度在50%以內）   

        elif (a1 > 0 and lu3_1n2 > 0 and a4 > 0 and a5 >0 and a6 > 0 and a7 > 0 and 0.25 >= (a1+lu3_1n2+a4+a5+a6+a7)/6 >= 0.1 and a1 >= lu3_1n2):
            result1 = "A"      #過去六個月皆為正數平均10-25%，且最近一個月的年增率與上個月比較為增加或持平（>=0）            





        elif (a1 > 0 and lu3_1n2 > 0 and a4 > 0 and a5 >0 and a6 >0  and a7 > 0 and (a1+lu3_1n2+a4+a5+a6+a7)/6 > 0.25 and a1 >= lu3_1n2):
            result1 = "AA"     #過去六個月皆為正數且平均超過25%，且最近一個月的年增率與上個月比為增加或持平（>=0）
                        

        else:
            result1 = "BB"      #無法列為其他評等

######################

    elif a1Nm == "04":   #近六個內有一二月的判斷式，4月為最新月份


        luX = str(round(lu4_1n2*100,2))  #1,2月合併數據 改為百分比
        luX_MoM = float((a1-lu4_1n2)/lu4_1n2) #1,2月跟3月的月增率比較（四月時沒有作用）
        nluX_MoM = None #1,2月跟3月的月增率比較 改為百分比 （四月時沒有作用）
  

        if ((a1+a2+lu4_1n2+a5+a6+a7)/6 < 0):
            result1 = "C"      #過去6個月平均數為負
    
        elif (a1 < 0): #或最近一個月為負數，最新一個月是4月

            result1 = "C"


        elif (a1 < 0 or a2 < 0 or lu4_1n2 < 0 or a5 < 0 or a6 < 0 or a7 < 0): #4,3,2,1,12,11,10,9月

            result1 = "BB"         #過去六個月曾經出現單月負成長

        elif (a1 < a2 < lu4_1n2 and (a1+a2+lu4_1n2+a5+a6+a7)/6 > 0): #4,3,2,1月遞減的情況
            result1 = "B"      #過去六個月平均為正數，但最近三個月出現遞減（不論幅度）

        elif ((a1+a2+lu4_1n2+a5+a6+a7)/6 > 0.25 and 0 > a10 >= -0.5):
            result1 = "A"      #或過去六個月平均超過25%，但最近一個月出現小幅衰退。（年增率較上個月下跌幅度在50%以內）   

        elif (a1 > 0 and a2 > 0 and lu4_1n2 > 0 and a5 >0 and a6 > 0 and a7 > 0 and 0.25 >= (a1+a2+lu4_1n2+a5+a6+a7)/6 >= 0.1 and a1 >= a2):
            result1 = "A"      #過去六個月皆為正數平均10-25%，且最近一個月的年增率與上個月比較為增加或持平（>=0）            







        elif (a1 > 0 and a2 > 0 and lu4_1n2 > 0  and a5 >0 and a6 >0 and a7 > 0 and (a1+a2+lu4_1n2+a5+a6+a7)/6 > 0.25 and a1 >= a2):
            result1 = "AA"     #過去六個月皆為正數且平均超過25%，且最近一個月的年增率與上個月比為增加或持平（>=0）
                        

        else:
            result1 = "BB"      #無法列為其他評等        

################

    elif a1Nm == "05":   #近六個內有一二月的判斷式，5月為最新月份

        luX = str(round(lu5_1n2*100,2))  #1,2月合併數據 改為百分比
        luX_MoM = None #1,2月跟3月的月增率比較（5月時沒有作用）
        nluX_MoM = None #1,2月跟3月的月增率比較 改為百分比 （四月時沒有作用）


        if ((a1+a2+a3+lu5_1n2+a6+a7)/6 < 0):
            result1 = "C"      #過去6個月平均數為負
    
        elif (a1 < 0): #或最近一個月為負數，最新一個月是5月

            result1 = "C"

        elif (a1 < 0 or a2 < 0 or a3 < 0 or lu5_1n2 < 0 or a6 < 0 or a7 < 0): #5,4,3,2,1,12,11月

            result1 = "BB"         #過去六個月曾經出現單月負成長


        elif (a1 < a2 < a3 and (a1+a2+a3+lu5_1n2+a6+a7)/6 > 0): #5,4,3月遞減的情況
            result1 = "B"      #過去六個月平均為正數，但最近三個月出現遞減（不論幅度）

        elif ((a1+a2+a3+lu5_1n2+a6+a7)/6 > 0.25 and 0 > a10 >= -0.5):
            result1 = "A"      #或過去六個月平均超過25%，但最近一個月出現小幅衰退。（年增率較上個月下跌幅度在50%以內）   

        elif (a1 > 0 and a2 > 0 and a3 > 0  and lu5_1n2 >0 and a6 > 0 and a7 > 0 and 0.25 >= (a1+a2+a3+lu5_1n2+a6+a7)/6 >= 0.1 and a1 >= a2):
            result1 = "A"      #過去六個月皆為正數平均10-25%，且最近一個月的年增率與上個月比較為增加或持平（>=0）            








        elif (a1 > 0 and a2 > 0 and a3 > 0  and lu5_1n2 >0 and a6 >0 and a7 > 0 and (a1+a2+a3+lu5_1n2+a6+a7)/6 > 0.25 and a1 >= a2):
            result1 = "AA"     #過去六個月皆為正數且平均超過25%，且最近一個月的年增率與上個月比為增加或持平（>=0）
                        

        else:
            result1 = "BB"      #無法列為其他評等

##########################

    elif a1Nm == "06":   #近六個內有一二月的判斷式，6月為最新月份

        luX = str(round(lu6_1n2*100,2))  #1,2月合併數據 改為百分比
        luX_MoM = None #1,2月跟3月的月增率比較（5月時沒有作用）
        nluX_MoM = None #1,2月跟3月的月增率比較 改為百分比 （四月時沒有作用）

        if ((a1+a2+a3+a4+lu6_1n2+a7)/6 < 0):
            result1 = "C"      #過去6個月平均數為負
    
        elif (a1 < 0): #或最近一個月為負數，最新一個月是6月

            result1 = "C"


        elif (a1 < 0 or a2 < 0 or a3 < 0 or a4 < 0 or lu6_1n2 < 0 or a7 < 0): #6,5,4,3,2,1,12月

            result1 = "BB"         #過去六個月曾經出現單月負成長

        elif (a1 < a2 < a3 and (a1+a2+a3+a4+lu6_1n2+a7)/6 > 0): #6,5,4月遞減的情況
            result1 = "B"      #過去六個月平均為正數，但最近三個月出現遞減（不論幅度）


        elif ((a1+a2+a3+a4+lu6_1n2+a7)/6 > 0.25 and 0 > a10 >= -0.5):
            result1 = "A"      #或過去六個月平均超過25%，但最近一個月出現小幅衰退。（年增率較上個月下跌幅度在50%以內）   

        elif (a1 > 0 and a2 > 0 and a3 > 0  and a4 >0 and lu6_1n2 >0 and a7 > 0 and 0.25 >= (a1+a2+a3+a4+lu6_1n2+a7)/6 >= 0.1 and a1 >= a2):
            result1 = "A"      #過去六個月皆為正數平均10-25%，且最近一個月的年增率與上個月比較為增加或持平（>=0）      






        elif (a1 > 0 and a2 > 0 and a3 > 0  and a4 >0 and lu6_1n2 >0 and a7 > 0 and (a1+a2+a3+a4+lu6_1n2+a7)/6 > 0.25 and a1 >= a2):
            result1 = "AA"     #過去六個月皆為正數且平均超過25%，且最近一個月的年增率與上個月比為增加或持平（>=0）
                        

        else:
            result1 = "BB"      #無法列為其他評等

    elif a1Nm == "07":   #近六個內有一二月的判斷式，7月為最新月份

        luX = str(round(lu7_1n2*100,2))  #1,2月合併數據 改為百分比
        luX_MoM = None #1,2月跟3月的月增率比較（5月時沒有作用）
        nluX_MoM = None #1,2月跟3月的月增率比較 改為百分比 （四月時沒有作用）


        if ((a1+a2+a3+a4+a5+lu7_1n2)/6 < 0):
            result1 = "C"      #過去6個月平均數為負
    
        elif (a1 < 0): #或最近一個月為負數，最新一個月是7月

            result1 = "C"

        elif (a1 < 0 or a2 < 0 or a3 < 0 or a4 < 0 or a5 < 0 or lu7_1n2 < 0): #7,6,5,4,3,2,1月

            result1 = "BB"         #過去六個月曾經出現單月負成長


        elif (a1 < a2 < a3 and (a1+a2+a3+a4+a5+lu7_1n2)/6 > 0): #7,6,5月遞減的情況
            result1 = "B"      #過去六個月平均為正數，但最近三個月出現遞減（不論幅度）


        elif ((a1+a2+a3+a4+a5+lu7_1n2)/6 > 0.25 and 0 > a10 >= -0.5):
            result1 = "A"      #或過去六個月平均超過25%，但最近一個月出現小幅衰退。（年增率較上個月下跌幅度在50%以內）   

        elif (a1 > 0 and a2 > 0 and a3 > 0  and a4 >0 and a5 > 0 and lu7_1n2 > 0 and 0.25 >= (a1+a2+a3+a4+a5+lu7_1n2)/6 >= 0.1 and a1 >= a2):
            result1 = "A"      #過去六個月皆為正數平均10-25%，且最近一個月的年增率與上個月比較為增加或持平（>=0）      






        elif (a1 > 0 and a2 > 0 and a3 > 0  and a4 >0 and a5 > 0 and lu7_1n2 > 0 and (a1+a2+a3+a4+a5+lu7_1n2)/6 > 0.25 and a1 >= a2):
            result1 = "AA"     #過去六個月皆為正數且平均超過25%，且最近一個月的年增率與上個月比為增加或持平（>=0）
                        

        else:
            result1 = "BB"      #無法列為其他評等

        
    else: #六個月內，沒有一二月的正常判斷式（8,9,10,11,12月）
        luX = None  #1,2月合併數據 改為百分比
        luX_MoM = None #1,2月跟3月的月增率比較
        nluX_MoM = None #1,2月跟3月的月增率比較 改為百分比
        
        if (a9 < 0):
            result1 = "C"      #過去6個月平均數為負
        
        elif (a1 < 0):
            result1 = "C"      #或最近一個月為負數

        elif (a1 < 0 or a2 < 0 or a3 < 0 or a4 < 0 or a5 < 0 or a6 < 0):

            result1 = "BB"         #過去六個月曾經出現單月負成長

        elif (a1 < a2 < a3 and a9 > 0):
            result1 = "B"      #過去六個月平均為正數，但最近三個月出現遞減（不論幅度）



        elif (a9 > 0.25 and 0 > a10 >= -0.5):
            result1 = "A"      #或過去六個月平均超過25%，但最近一個月出現小幅衰退。（年增率較上個月下跌幅度在50%以內）   



        elif (a1 > 0 and a2 > 0 and a3 > 0 and a4 > 0 and a5 >0 and a6 > 0 and 0.25 >= a9 >= 0.1 and a1 >= a2):
            result1 = "A"      #過去六個月皆為正數平均10-25%，且最近一個月的年增率與上個月比較為增加或持平（>=0）







        
        elif (a1 > 0 and a2 > 0 and a3 > 0 and a4 > 0 and a5 >0 and a6 >0 and a9 > 0.25 and a1 >= a2):
            result1 = "AA"     #過去六個月皆為正數且平均超過25%，且最近一個月的年增率與上個月比為增加或持平（>=0）
                        

        else:
            result1 = "BB"      #無法列為其他評等
    
    #print(a1_2)
    #print(result1)
    return result1, RevN, Rev, a1N, a2N, a3N, a4N, a5N, a6N, na1, na2, na3, na4, na5, na6, na9, na10, a7N, na7, newest_Rev_month, luX, nluX_MoM




###########################################################   

def stock6score(stock_id, st1, st2, st3, st4, st5, st6):  #由stock6改為stock6score 2020/5/7##計算六大指標平均 

    

##########計算六大指標平均
    if (st5 == "AA" or st5 == "A" or st5 == "BB" or st5 == "B" or st5 == "C"):  #存貨週轉率
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
            average6stock = str(round(int(total)/6,2))
    else:
        total = 0
        for i in [st1,st2,st3,st4,st6]:
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
            average6stock = str(round(int(total)/5,2))
            
    return average6stock

def CheckNewFnR(stock_id):
############Mdj營收最新月份
    
    headers = {'Referer': my_Referer,'user-agent': my_UserAgent}
    
    bank_url = 'https://djinfo.cathaysec.com.tw/' #國泰世華 #不能隨便改 會發生錯誤 2020/10/22
    sheet_type = 'z/zc/zch/zch_' #Rev 營收   
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.post(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))

    #dfs[2] 真正表格
    #dfs[2][4] 營收年增率
    newest_Rev_month = str(dfs[2][0][6]) #最新一個月的月份
################Mdj最新財報季份
    sheet_type = 'z/zc/zcr/zcr_' #FRQ 財務比率 季表
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.post(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))

#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][11] 最新一季營益率
#print(dfs[2][1][11])

    newest_Fin_Q = str(dfs[2][1][1]) #最新1季的財報季份
    
    
    return newest_Rev_month, newest_Fin_Q


def GetStockName(stock_id):  #由stock6改為stock6score 2020/5/7##計算六大指標平均 

    
####################取得股票名稱
    headers = {'Referer':my_Referer,'user-agent': my_UserAgent}

    bank_url = 'https://djinfo.cathaysec.com.tw/' #國泰世華 #不能隨便改 會發生錯誤 2020/10/22
    sheet_type = 'z/zc/zca/zca_' #基本資料
    ###MoneyDJ
    url = bank_url + sheet_type + stock_id +'.djhtm'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))

#print(table)
    #stock_id_name = dfs[2][0][0][:-24] #股票代號和名稱
    stock_name = dfs[2][0][0][0:3] #股票名稱
    test = stock_name.endswith('(')
    if test == True:
        stock_name = dfs[2][0][0][0:2]
    else:
        stock_name = dfs[2][0][0][0:3]
####################################
        
    #stock_description2 = '☆總大六大指標Mdj即時查詢評等☆' + '營益率指標為：' + st1 + '，' + '營收指標為：' + st2 + '，' + '税後淨利指標為：' + st3 + '，' + 'EPS指標為：' + st4 + '，' + '存貨週轉率指標為：' + st5 + '，' + '現金流量指標為：' + st6  + '，' + '六大指標平均為：' + average6stock  + '。' 
     #+ stock_id_name + '。'
    #print(stock_description)
    return stock_name