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


def stock_Prof(stock_id):  #營業利益率評分標準
    headers = {'Referer':'https://accounts.pixiv.net/loginlang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index','user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    sheet_type = 'z/zc/zcr/zcr_' #FRQ 財務比率 季表
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url, headers=headers)
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

    a9 = round((a1+a2+a3+a4)/4,3) #四季平均
    #print(a9)
    a10 = round(float((a1-a2)/abs(a2)),3) #最新一季季增率
    #print(a10)
    a11 = float((a2-a3)/abs(a3)) #次新一季季增率
    #print(a11)
    a12 = float((a3-a4)/abs(a4)) #第3新一季季增率
    #print(a12)
    a13 = float((a4-a5)/abs(a5)) #第4新一季季增率
    
    a10p = str(a10*100) + '%'
    #print(a13)

    if (a1 < 0):
        result1 = "C"      #最近一季為負

    elif (a9 < 0):
        result1 = "C"      #過去四季的平均為負
        
    elif (0 < a9 <= 5):
        result1 = "B"      #或不論漲跌幅，過去四季平均營益率在5%以下
        
    elif (a10 <= -0.2):
        result1 = "B"      #最近一季比上一季跌20%以上

    elif (a11 <= -0.2):
        result1 = "BB"     #過去四季曾出現季與季之間下跌20%以上，但不包括最近一季 1
        
    elif (a12 <= -0.2):
        result1 = "BB"     #過去四季曾出現季與季之間下跌20%以上，但不包括最近一季 2

    elif (15 >= a9 >= 10) and (a1 > a2) and (a2 > a3*0.8) and (a3 > a4*0.8):
        result1 = "AA"     #或過去四季皆維持穩定沒有下降，且平均在10-15%，最近一季呈現上升趨勢


    elif (15 >= a9 >= 10) and (a1 > a2*0.8) and (a2 > a3*0.8) and (a3 > a4*0.8): 
        result1 = "A"      #過去四季皆維持穩定沒有下降，且平均在10-15%

        
    elif (10 > a9 >= 5) and (a1 > a2) and (a2 > a3*0.8) and (a3 > a4*0.8):
        result1 = "A"      #或過去四季皆維持穩定沒有下跌，平均只有5-10%，但最近一季呈現上升趨勢



    elif (a9 > 15) and (a1 > a2*0.8) and (a2 > a3*0.8) and (a3 > a4*0.8):
        result1 = "AA"   #過去四季皆維持穩定沒有下跌，且平均在15%以上

      
        
    else:
        result1 = "BB"
        

    return result1, ProfitN, Profit, a1N, a2N, a3N, a4N, a5N, a6N, a7N, a8N, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a10p

################################################################

def stock_Rev(stock_id): #(股票代碼, 股票名稱. 股票價格觸及下緣) #營收評分標準
    headers = {'Referer':'https://accounts.pixiv.net/loginlang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index','user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
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
    b1N = dfs[2][0][6] #最新1個月的名稱 
    b2N = dfs[2][0][7] #最新2個月的名稱 
    b3N = dfs[2][0][8] #最新3個月的名稱
    b4N = dfs[2][0][9] #最新4個月的名稱 
    b5N = dfs[2][0][10] #最新5個月的名稱 
    b6N = dfs[2][0][11] #最新6個月的名稱

    b1Nm = dfs[2][0][6][-2:] #最新1個月的名稱，只有月份兩個數字
    b2Nm = dfs[2][0][7][-2:] #最新2個月的名稱，只有月份兩個數字
    b3Nm = dfs[2][0][8][-2:] #最新3個月的名稱，只有月份兩個數字
    b4Nm = dfs[2][0][9][-2:] #最新4個月的名稱，只有月份兩個數字 
    b5Nm = dfs[2][0][10][-2:] #最新5個月的名稱，只有月份兩個數字 
    b6Nm = dfs[2][0][11][-2:] #最新6個月的名稱，只有月份兩個數字


    RevN = []
    RevN.extend([b1N,b2N,b3N,b4N,b5N,b6N])
    
    RevNm = []
    RevNm.extend([b1Nm,b2Nm,b3Nm,b4Nm,b5Nm,b6Nm])
    

        

    b1 = round(float((dfs[2][4][6])[:-1])/100,4) #最新1個月的營收年增率 
    b2 = round(float((dfs[2][4][7])[:-1])/100,4) #最新2個月的營收年增率 
    b3 = round(float((dfs[2][4][8])[:-1])/100,4) #最新3個月的營收年增率 
    b4 = round(float((dfs[2][4][9])[:-1])/100,4) #最新4個月的營收年增率 
    b5 = round(float((dfs[2][4][10])[:-1])/100,4) #最新5個月的營收年增率 
    b6 = round(float((dfs[2][4][11])[:-1])/100,4) #最新6個月的營收年增率 

    Rev = []
    Rev.extend([b1,b2,b3,b4,b5,b6])
    
    lu2_1n2 = round(float((dfs[2][6][6])[:-1])/100,4) #2月最新，1,2月的累積營收年增率
    lu3_1n2 = round(float((dfs[2][6][7])[:-1])/100,4) #3月最新，1,2月的累積營收年增率
    lu4_1n2 = round(float((dfs[2][6][8])[:-1])/100,4) #4月最新，1,2月的累積營收年增率
    lu5_1n2 = round(float((dfs[2][6][9])[:-1])/100,4) #5月最新，1,2月的累積營收年增率
    lu6_1n2 = round(float((dfs[2][6][10])[:-1])/100,4) #6月最新，1,2月的累積營收年增率 
    lu7_1n2 = round(float((dfs[2][6][11])[:-1])/100,4) #7月最新，1,2月的累積營收年增率     
    
    #if c in 
    
    nb1 = str(round(b1*100,2))  #改為百分比的年增率
    nb2 = str(round(b2*100,2))
    nb3 = str(round(b3*100,2))
    nb4 = str(round(b4*100,2))
    nb5 = str(round(b5*100,2))
    nb6 = str(round(b6*100,2))    
    

    b9 = (b1+b2+b3+b4+b5+b6)/6 #6個月平均   小數
    nb9 = str(round(b9*100,2))  #6個月平均 百分比
    #print(b9)
    b10 = float((b1-b2)/b2) #最新一個月年增率和上個月比較
    nb10 = str(round(b10*100,2)) #最新一個月年增率和上個月比較 百分比
    #print(b10)


    if b1Nm == "02":   #近六個內有一二月的判斷式，2月為最新月份
        if (b9 < 0):
            result2 = "C"      #過去6個月平均數為負
    
        elif (lu2_1n2 < 0): #或最近一個月為負數，最新一個月是1,2月

            result2 = "C"

        elif (lu2_1n2 < 0 or b3 < 0 or b4 < 0 or b5 < 0 or b6 < 0):

            result2 = "BB"         #過去六個月曾經出現單月負成長

        elif (b9 > 0.25 and 0 > b10 >= -0.5):
            result2 = "A"      #或過去六個月平均超過25%，但最近一個月出現小幅衰退。（年增率較上個月下跌幅度在50%以內）   

        elif (b1 > 0 and b2 > 0 and b3 > 0 and b4 > 0 and b5 >0 and b6 > 0 and 0.25 >= b9 >= 0.1 and b1 >= b2):
            result2 = "A"      #過去六個月皆為正數平均10-25%，且最近一個月的年增率與上個月比較為增加或持平（>=0）            
            

        elif (lu2_1n2 < b3 and b1 < b2 < b3 and b9 > 0): #2,1,12,11月遞減的情況
            result2 = "B"      #過去六個月平均為正數，但最近三個月出現遞減（不論幅度）



        
        elif (lu2_1n2 > 0 and b3 > 0 and b4 > 0 and b5 >0 and b6 >0 and b9 > 0.25 and lu2_1n2 >= b3):
            result2 = "AA"     #過去六個月皆為正數且平均超過25%，且最近一個月的年增率與上個月比為增加或持平（>=0）
                        

        else:
            result2 = "BB"      #無法列為其他評等
            

    elif b1Nm == "03":   #近六個內有一二月的判斷式，3月為最新月份
        if (b9 < 0):
            result2 = "C"      #過去6個月平均數為負
    
        elif (b1 < 0): #或最近一個月為負數，最新一個月是3月

            result2 = "C"

        elif (b1 < 0 or lu3_1n2 < 0 or b4 < 0 or b5 < 0 or b6 < 0): #3,2,1,12,11,10月

            result2 = "BB"         #過去六個月曾經出現單月負成長

        elif (b9 > 0.25 and 0 > b10 >= -0.5):
            result2 = "A"      #或過去六個月平均超過25%，但最近一個月出現小幅衰退。（年增率較上個月下跌幅度在50%以內）   

        elif (b1 > 0 and lu3_1n2 > 0 and b4 > 0 and b5 >0 and b6 > 0 and 0.25 >= b9 >= 0.1 and b1 >= lu3_1n2):
            result2 = "A"      #過去六個月皆為正數平均10-25%，且最近一個月的年增率與上個月比較為增加或持平（>=0）            


        elif (b1 < lu3_1n2 and b1 < b2 < b3 and b9 > 0): #3,2,1月遞減的情況
            result2 = "B"      #過去六個月平均為正數，但最近三個月出現遞減（不論幅度）




        elif (b1 > 0 and lu3_1n2 > 0 and b4 > 0 and b5 >0 and b6 >0 and b9 > 0.25 and b1 >= lu3_1n2):
            result2 = "AA"     #過去六個月皆為正數且平均超過25%，且最近一個月的年增率與上個月比為增加或持平（>=0）
                        

        else:
            result2 = "BB"      #無法列為其他評等

    elif b1Nm == "04":   #近六個內有一二月的判斷式，4月為最新月份
        if (b9 < 0):
            result2 = "C"      #過去6個月平均數為負
    
        elif (b1 < 0): #或最近一個月為負數，最新一個月是4月

            result2 = "C"


        elif (b1 < 0 or b2 < 0 or lu4_1n2 < 0 or b5 < 0 or b6 < 0): #4,3,2,1,12,11,10月

            result2 = "BB"         #過去六個月曾經出現單月負成長

        elif (b9 > 0.25 and 0 > b10 >= -0.5):
            result2 = "A"      #或過去六個月平均超過25%，但最近一個月出現小幅衰退。（年增率較上個月下跌幅度在50%以內）   

        elif (b1 > 0 and b2 > 0 and lu4_1n2 > 0 and b5 >0 and b6 > 0 and 0.25 >= b9 >= 0.1 and b1 >= b2):
            result2 = "A"      #過去六個月皆為正數平均10-25%，且最近一個月的年增率與上個月比較為增加或持平（>=0）            


        elif (b1 < b2 < lu4_1n2 and b9 > 0): #4,3,2,1月遞減的情況
            result2 = "B"      #過去六個月平均為正數，但最近三個月出現遞減（不論幅度）




        elif (b1 > 0 and b2 > 0 and lu4_1n2 > 0  and b5 >0 and b6 >0 and b9 > 0.25 and b1 >= b2):
            result2 = "AA"     #過去六個月皆為正數且平均超過25%，且最近一個月的年增率與上個月比為增加或持平（>=0）
                        

        else:
            result2 = "BB"      #無法列為其他評等        

    elif b1Nm == "05":   #近六個內有一二月的判斷式，5月為最新月份
        if (b9 < 0):
            result2 = "C"      #過去6個月平均數為負
    
        elif (b1 < 0): #或最近一個月為負數，最新一個月是5月

            result2 = "C"

        elif (b1 < 0 or b2 < 0 or b3 < 0 or lu5_1n2 < 0 or b6 < 0): #5,4,3,2,1,12月

            result2 = "BB"         #過去六個月曾經出現單月負成長

        elif (b9 > 0.25 and 0 > b10 >= -0.5):
            result2 = "A"      #或過去六個月平均超過25%，但最近一個月出現小幅衰退。（年增率較上個月下跌幅度在50%以內）   

        elif (b1 > 0 and b2 > 0 and b3 > 0  and lu5_1n2 >0 and b6 > 0 and 0.25 >= b9 >= 0.1 and b1 >= b2):
            result2 = "A"      #過去六個月皆為正數平均10-25%，且最近一個月的年增率與上個月比較為增加或持平（>=0）            



        elif (b1 < b2 < b3 and b9 > 0): #5,4,3月遞減的情況
            result2 = "B"      #過去六個月平均為正數，但最近三個月出現遞減（不論幅度）




        elif (b1 > 0 and b2 > 0 and b3 > 0  and lu5_1n2 >0 and b6 >0 and b9 > 0.25 and b1 >= b2):
            result2 = "AA"     #過去六個月皆為正數且平均超過25%，且最近一個月的年增率與上個月比為增加或持平（>=0）
                        

        else:
            result2 = "BB"      #無法列為其他評等

    elif b1Nm == "06":   #近六個內有一二月的判斷式，6月為最新月份
        if (b9 < 0):
            result2 = "C"      #過去6個月平均數為負
    
        elif (b1 < 0): #或最近一個月為負數，最新一個月是6月

            result2 = "C"


        elif (b1 < 0 or b2 < 0 or b3 < 0 or b4 < 0 or lu6_1n2 < 0): #6,5,4,3,2,1月

            result2 = "BB"         #過去六個月曾經出現單月負成長

        elif (b9 > 0.25 and 0 > b10 >= -0.5):
            result2 = "A"      #或過去六個月平均超過25%，但最近一個月出現小幅衰退。（年增率較上個月下跌幅度在50%以內）   

        elif (b1 > 0 and b2 > 0 and b3 > 0  and b4 >0 and lu6_1n2 >0 and 0.25 >= b9 >= 0.1 and b1 >= b2):
            result2 = "A"      #過去六個月皆為正數平均10-25%，且最近一個月的年增率與上個月比較為增加或持平（>=0）      


        elif (b1 < b2 < b3 and b9 > 0): #6,5,4月遞減的情況
            result2 = "B"      #過去六個月平均為正數，但最近三個月出現遞減（不論幅度）




        elif (b1 > 0 and b2 > 0 and b3 > 0  and b4 >0 and lu6_1n2 >0 and b9 > 0.25 and b1 >= b2):
            result2 = "AA"     #過去六個月皆為正數且平均超過25%，且最近一個月的年增率與上個月比為增加或持平（>=0）
                        

        else:
            result2 = "BB"      #無法列為其他評等

    elif b1Nm == "07":   #近六個內有一二月的判斷式，7月為最新月份
        if (b9 < 0):
            result2 = "C"      #過去6個月平均數為負
    
        elif (b1 < 0): #或最近一個月為負數，最新一個月是7月

            result2 = "C"

        elif (b1 < 0 or b2 < 0 or b3 < 0 or b4 < 0 or b5 < 0 or lu7_1n2 < 0): #7,6,5,4,3,2月

            result2 = "BB"         #過去六個月曾經出現單月負成長

        elif (b9 > 0.25 and 0 > b10 >= -0.5):
            result2 = "A"      #或過去六個月平均超過25%，但最近一個月出現小幅衰退。（年增率較上個月下跌幅度在50%以內）   

        elif (b1 > 0 and b2 > 0 and b3 > 0  and b4 >0 and b5 > 0 and lu7_1n2 > 0 and 0.25 >= b9 >= 0.1 and b1 >= b2):
            result2 = "A"      #過去六個月皆為正數平均10-25%，且最近一個月的年增率與上個月比較為增加或持平（>=0）      


        elif (b1 < b2 < b3 and b9 > 0): #7,6,5月遞減的情況
            result2 = "B"      #過去六個月平均為正數，但最近三個月出現遞減（不論幅度）




        elif (b1 > 0 and b2 > 0 and b3 > 0  and b4 >0 and b5 > 0 and lu7_1n2 > 0 and b9 > 0.25 and b1 >= b2):
            result2 = "AA"     #過去六個月皆為正數且平均超過25%，且最近一個月的年增率與上個月比為增加或持平（>=0）
                        

        else:
            result2 = "BB"      #無法列為其他評等

        
    else: #六個月內，沒有一二月的正常判斷式（8,9,10,11,12月）

        if (b9 < 0):
            result2 = "C"      #過去6個月平均數為負
        
        elif (b1 < 0):
            result2 = "C"      #或最近一個月為負數

        elif (b1 < 0 or b2 < 0 or b3 < 0 or b4 < 0 or b5 < 0 or b6 < 0):

            result2 = "BB"         #過去六個月曾經出現單月負成長

        elif (b9 > 0.25 and 0 > b10 >= -0.5):
            result2 = "A"      #或過去六個月平均超過25%，但最近一個月出現小幅衰退。（年增率較上個月下跌幅度在50%以內）   

        elif (b1 > 0 and b2 > 0 and b3 > 0 and b4 > 0 and b5 >0 and b6 > 0 and 0.25 >= b9 >= 0.1 and b1 >= b2):
            result2 = "A"      #過去六個月皆為正數平均10-25%，且最近一個月的年增率與上個月比較為增加或持平（>=0）



        elif (b1 < b2 < b3 and b9 > 0):
            result2 = "B"      #過去六個月平均為正數，但最近三個月出現遞減（不論幅度）



        
        elif (b1 > 0 and b2 > 0 and b3 > 0 and b4 > 0 and b5 >0 and b6 >0 and b9 > 0.25 and b1 >= b2):
            result2 = "AA"     #過去六個月皆為正數且平均超過25%，且最近一個月的年增率與上個月比為增加或持平（>=0）
                        

        else:
            result2 = "BB"      #無法列為其他評等
    
    #print(b1_2)
    #print(result2)
    return result2, RevN, Rev, b1N, b2N, b3N, b4N, b5N, b6N, nb1, nb2, nb3, nb4, nb5, nb6, nb9, nb10

##############################################################
################################################################

def stock_Revnew(stock_id, newestRev_id): #(股票代碼, 股票名稱. 股票價格觸及下緣)
    headers = {'Referer':'https://accounts.pixiv.net/loginlang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index','user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

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
    b1N = dfs[2][0][6] #最新1個月的名稱 
    b2N = dfs[2][0][7] #最新2個月的名稱 
    b3N = dfs[2][0][8] #最新3個月的名稱
    b4N = dfs[2][0][9] #最新4個月的名稱 
    b5N = dfs[2][0][10] #最新5個月的名稱 
    b6N = dfs[2][0][11] #最新6個月的名稱 

    RevN = []
    RevN.extend([b1N,b2N,b3N,b4N,b5N,b6N])
    
    #############
    b0 = round(float(newestRev_id),4) #自己輸入的最新營收數字
    #################

    b1 = round(float((dfs[2][4][6])[:-1])/100,4) #最新1個月的營收年增率 
    b2 = round(float((dfs[2][4][7])[:-1])/100,4) #最新2個月的營收年增率 
    b3 = round(float((dfs[2][4][8])[:-1])/100,4) #最新3個月的營收年增率 
    b4 = round(float((dfs[2][4][9])[:-1])/100,4) #最新4個月的營收年增率 
    b5 = round(float((dfs[2][4][10])[:-1])/100,4) #最新5個月的營收年增率 
    b6 = round(float((dfs[2][4][11])[:-1])/100,4) #最新6個月的營收年增率 

    Rev = []
    Rev.extend([b0,b1,b2,b3,b4,b5])

    ###以下有些許改動  2020/05/30
    
    b9  = (b0+b1+b2+b3+b4+b5)/6 #6個月四季平均
    #print(b9)
    b10 = float((b0-b1)/b1) #最新一個月月增率
    #print(b10)
    #以下公式尚未根據格局修改2020/06/26
    if (b9 < 0):
        result2 = "C"
        
    elif (b0 < 0):
        result2 = "C"
        
    elif (b9 >= 0.25 and b10 >= 0):
        result2 = "AA"

    elif (b9 >= 0.1 and b10 >= 0):
        result2 = "A"

    elif (b1 or b2 or b3 or b4 or b5 or b0 < 0):
        result2 = "BB"
        
    elif (b0 < b1 < b2 and b9 > 0):
        result2 = "B"
        
    else:
        result2 = "BB"

    return result2, RevN, Rev, b1N, b2N, b3N, b4N, b5N, b6N, b1, b2, b3, b4, b5, b6, b0 
    #print (result1)
##############################################################

def stock_NetInc(stock_id): #税後淨利年增率
    headers = {'Referer':'https://accounts.pixiv.net/loginlang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index','user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    
    sheet_type = 'z/zc/zcq/zcq_' #ISQ 合併損益表 季表
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url, headers=headers)
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
    c13 = season_number_below0 = total
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

    return result3, NetIncomeN, NetIncome, c1N, c2N, c3N, c4N, c5N, c6N, c7N, c8N, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, pc9, pc10, pc11
###########################################################
def stock_EPS(stock_id):
    headers = {'Referer':'https://accounts.pixiv.net/loginlang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index','user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

    sheet_type = 'z/zc/zcq/zcq_' #ISQ 合併損益表 季表
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url, headers=headers)
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

    d9 = float((d1-d5)/d5) #最新一季年增率
#print(d9)
    d10 = float((d2-d6)/d6) #次新一季年增率
#print(d10)
    d11 = float((d3-d7)/d7) #第3新一季年增率
#print(d11)
    d12 = float((d4-d8)/d8) #第4新一季年增率
#print(d12)
    d13 = season4Sum = d1+d2+d3+d4
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
        




    #print (result4)
    return result4, EPSN, EPS, d1N, d2N, d3N, d4N, d5N, d6N, d7N, d8N, d1, d2, d3, d4, d5, d6, d7, d8
#, EPSN, EPS

##############################################################

def stock_InvTO(stock_id): #(股票代碼)
    headers = {'Referer':'https://accounts.pixiv.net/loginlang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index','user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    
    ###MoneyDJ
    sheet_type = 'z/zc/zcr/zcr_' #FRQ 財務比率表 季
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url, headers=headers)
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

    return result5, InvTON, InvTO, e1N, e2N, e3N, e4N, e5N, e6N, e7N, e8N, e1, e2, e3, e4, e5, e6, e7, e8
##########################################################
def stock_Cashflow(stock_id): #(股票代碼, 股票名稱. 股票價格觸及下緣)
    headers = {'Referer':'https://accounts.pixiv.net/loginlang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index','user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

    sheet_type = 'z/zc/zc3/zc3_' #合併現金流量表 季表
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url, headers=headers)
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

    f9 = f1+f2+f3+f4 #前4季總和
#print(d9)
    f10 = f1+f2+f3+f4+f5+f6 #前6季總和
#print(d10)
    f11 = f1+f2+f3+f4+f5+f6+f7+f8 #前8季總和
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
   
##########################################################
######################################################以上為六大指標程式
######################################################以下為股價程式

import pandas as pd 
import requests
from bs4 import BeautifulSoup


#stock_id = "3034"

def stockdef(stock_id): #(股票代碼, 股票名稱. 股票價格觸及下緣)
    headers = {'Referer':'https://accounts.pixiv.net/loginlang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index','user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

    bank_url = 'http://dj.mybank.com.tw/' #國泰世華
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
    r = requests.get(url, headers=headers)
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
    r = requests.get(url, headers=headers)
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
    return stock_description, latest_trade_date, open, close, high, low, thisYearGain, newest_Rev_month, stock_id_name, yahoo_latest_tradePrice, stock_name  

###########################################################
##############################################################
    
def stock6score(stock_id):  #由stock6改為stock6score 2020/5/7##計算六大指標平均 

    
         
    #前三個變數沿用之前的，後面為後來增修
    st1, dt1N, dt1, a1N, a2N, a3N, a4N, a5N, a6N, a7N, a8N, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a10p = stock_Prof(stock_id)
    #print('營益率指標為：' + st1) #營益率指標函數
 
    st2, dt2N, dt2, b1N, b2N, b3N, b4N, b5N, b6N, b1, b2, b3, b4, b5, b6, nb9, nb10 = stock_Rev(stock_id)  #營收指標函數
    #print('營收指標為：' + st2)
    
    st3, dt3N, dt3, c1N, c2N, c3N, c4N, c5N, c6N, c7N, c8N, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, pc9, pc10, pc11 = stock_NetInc(stock_id)
    #print('税後淨利指標為：' + st3) #税後淨利指標函數

    st4, dt4N, dt4, d1N, d2N, d3N, d4N, d5N, d6N, d7N, d8N, d1, d2, d3, d4, d5, d6, d7, d8 = stock_EPS(stock_id)  #EPS指標函數
    #print('EPS指標為：' + st4)

    st5, dt5N, dt5, e1N, e2N, e3N, e4N, e5N, e6N, e7N, e8N, e1, e2, e3, e4, e5, e6, e7, e8 = stock_InvTO(stock_id)  #存貨週轉率指標函數
    #print('存貨週轉率指標為：' + st5)
    
    st6, dt6N, dt6, f1N, f2N, f3N, f4N, f5N, f6N, f7N, f8N, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10 = stock_Cashflow(stock_id)  #現金流量指標函數
    #print('現金流量指標為：' + st6)

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

####################取得股票名稱
    headers = {'Referer':'https://accounts.pixiv.net/loginlang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index','user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

    bank_url = 'http://dj.mybank.com.tw/' #國泰世華
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
        
    stock_description2 = '☆總大六大指標Mdj即時查詢評等☆' + '營益率指標為：' + st1 + '，' + '營收指標為：' + st2 + '，' + '税後淨利指標為：' + st3 + '，' + 'EPS指標為：' + st4 + '，' + '存貨週轉率指標為：' + st5 + '，' + '現金流量指標為：' + st6  + '，' + '六大指標平均為：' + average6stock  + '。' 
     #+ stock_id_name + '。'
    #print(stock_description)
    return stock_description2, average6stock, stock_name

######################################################以上為股價程式

##############################################################
    
def stock6scorenew(stock_id, newestRev_id):  #newestRev_id 營收部份要自己輸入最新的數字

    
         
    #前三個變數沿用之前的，後面為後來增修
    st1, dt1N, dt1, a1N, a2N, a3N, a4N, a5N, a6N, a7N, a8N, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = stock_Prof(stock_id)
    #print('營益率指標為：' + st1) #營益率指標函數
 
    st2, dt2N, dt2, b1N, b2N, b3N, b4N, b5N, b6N, b1, b2, b3, b4, b5, b6, b0 = stock_Revnew(stock_id, newestRev_id)  #營收指標函數 自己輸入最新的數字
    #print('營收指標為：' + st2)
    
    st3, dt3N, dt3, c1N, c2N, c3N, c4N, c5N, c6N, c7N, c8N, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, pc9, pc10, pc11 = stock_NetInc(stock_id)
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
    average6stock = str(round(int(total)/6,2))
##########計算六大指標平均    
    
    stock_description2 = '☆總大六大指標Mdj即時查詢評等☆' + '營益率指標為：' + st1 + '，' + '營收指標為：' + st2 + '，' + '税後淨利指標為：' + st3 + '，' + 'EPS指標為：' + st4 + '，' + '存貨週轉率指標為：' + st5 + '，' + '現金流量指標為：' + st6  + '，' + '六大指標平均為：' + average6stock  + '。' 
     #+ stock_id_name + '。'
    #print(stock_description)
    return stock_description2, average6stock

######################################################以上為股價程式

#
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

def CheckNewFnR(stock_id):
############Mdj營收最新月份
    
    headers = {'Referer':'https://accounts.pixiv.net/loginlang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index','user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    
    bank_url = 'http://dj.mybank.com.tw/' #國泰世華
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