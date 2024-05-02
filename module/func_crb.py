# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 08:36:14 2022

@author: green
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 19:01:58 2022

@author: pcuser
"""

import random

a = 'https://www.google.com.tw'
b = 'https://tw.yahoo.com'
c = 'https://www.pchome.com.tw/'


my_Referer = random.choice([a,b,c])

my_UserAgent = 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'

def getCRB():
    headers = {'Referer': my_Referer ,'user-agent': my_UserAgent}

    ######以下為判斷上市或上櫃，取得年度股價程式
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup    


    cnyes_url = 'https://www.stockq.org/index/CRB.php' 

    url = cnyes_url 
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    table = soup.find_all('table')[9]  #7變成9  2023/7/21
    print(table)
    dfs = pd.read_html(str(table))
    #print(dfs[0])
 
    table2 = soup.find_all('table')[11] #9變成11  2023/7/21
    #print(table2)
    dfs2 = pd.read_html(str(table2))    
    
    
    CRBindex = dfs[0].iloc[1][0]
    CRBhalfyear = dfs2[0].iloc[2][5]
    CRBoneyear = dfs2[0].iloc[2][7]    
    
    
    #USBond3mYieldClose = dfs[0].iloc[0][8]
    #USBond10yYieldClose = dfs[0].iloc[6][8]    
    
    print(CRBindex)
    print(CRBhalfyear)
    print(CRBoneyear)
    #print(USBond10yYieldClose)
    
    return CRBindex, CRBhalfyear, CRBoneyear


#getCRB()