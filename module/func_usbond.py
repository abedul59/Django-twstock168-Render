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



def getUSBondYield3m():
    headers = {'Referer': my_Referer ,'user-agent': my_UserAgent}

    ######以下為判斷上市或上櫃，取得年度股價程式
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    #urllib3.disable_warnings()  

    #3M
    cnyes_url = 'https://www.cnyes.com/futures/html5chart/TB3MY.html' 

    url = cnyes_url 
    r = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(r.content, 'lxml')
    table = soup.find_all('table')[0]
    print(table)
    dfs = pd.read_html(str(table))
    print(dfs[0])
    #一週 一個月	三個月	六個月 今年以來	一年	三年	五年
    table2 = dfs[0]
    Lists3m = [table2.iloc[3][0],table2.iloc[3][1],table2.iloc[3][3],table2.iloc[3][5],table2.iloc[0][1]] #最後一個為最新殖利率
    print(table2.iloc[3])
    #print(table2.iloc[3][0])
    print(Lists3m)
    
    print(table2.iloc[0][1])
    return Lists3m

def getUSBondYield6m():
    headers = {'Referer': my_Referer ,'user-agent': my_UserAgent}

    ######以下為判斷上市或上櫃，取得年度股價程式
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup    
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    #urllib3.disable_warnings() 
    #6M
    cnyes_url = 'https://www.cnyes.com/futures/html5chart/TB6MY.html' 

    url = cnyes_url 
    r = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(r.content, 'lxml')
    table = soup.find_all('table')[0]
    #print(table)
    dfs = pd.read_html(str(table))
    #print(dfs[0])
    #一週 一個月	三個月	六個月 今年以來	一年	三年	五年
    table2 = dfs[0]
    Lists6m = [table2.iloc[3][0],table2.iloc[3][1],table2.iloc[3][3],table2.iloc[3][5],table2.iloc[0][1]] #最後一個為最新殖利率
    print(table2.iloc[3])
    #print(table2.iloc[3][0])
    print(Lists6m)
    return Lists6m    


def getUSBondYield2y():
    headers = {'Referer': my_Referer ,'user-agent': my_UserAgent}

    ######以下為判斷上市或上櫃，取得年度股價程式
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup    
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    #urllib3.disable_warnings() 
    #6M
    cnyes_url = 'https://www.cnyes.com/futures/html5chart/US2YY.html' 

    url = cnyes_url 
    r = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(r.content, 'lxml')
    table = soup.find_all('table')[0]
    #print(table)
    dfs = pd.read_html(str(table))
    #print(dfs[0])
    #一週 一個月	三個月	六個月 今年以來	一年	三年	五年
    table2 = dfs[0]
    Lists2y = [table2.iloc[3][0],table2.iloc[3][1],table2.iloc[3][3],table2.iloc[3][5],table2.iloc[0][1]] #最後一個為最新殖利率
    print(table2.iloc[3])
    #print(table2.iloc[3][0])
    print(Lists2y)
    return Lists2y   


def getUSBondYield3y():
    headers = {'Referer': my_Referer ,'user-agent': my_UserAgent}

    ######以下為判斷上市或上櫃，取得年度股價程式
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup    
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    #urllib3.disable_warnings() 
    #6M
    cnyes_url = 'https://www.cnyes.com/futures/html5chart/US3YY.html' 

    url = cnyes_url 
    r = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(r.content, 'lxml')
    table = soup.find_all('table')[0]
    #print(table)
    dfs = pd.read_html(str(table))
    #print(dfs[0])
    #一週 一個月	三個月	六個月 今年以來	一年	三年	五年
    table2 = dfs[0]
    Lists3y = [table2.iloc[3][0],table2.iloc[3][1],table2.iloc[3][3],table2.iloc[3][5],table2.iloc[0][1]] #最後一個為最新殖利率
    print(table2.iloc[3])
    #print(table2.iloc[3][0])
    print(Lists3y)
    return Lists3y   


def getUSBondYield5y():
    headers = {'Referer': my_Referer ,'user-agent': my_UserAgent}

    ######以下為判斷上市或上櫃，取得年度股價程式
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup    
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    #urllib3.disable_warnings() 
    #6M
    cnyes_url = 'https://www.cnyes.com/futures/html5chart/US5YY.html' 

    url = cnyes_url 
    r = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(r.content, 'lxml')
    table = soup.find_all('table')[0]
    #print(table)
    dfs = pd.read_html(str(table))
    #print(dfs[0])
    #一週 一個月	三個月	六個月 今年以來	一年	三年	五年
    table2 = dfs[0]
    Lists5y = [table2.iloc[3][0],table2.iloc[3][1],table2.iloc[3][3],table2.iloc[3][5],table2.iloc[0][1]] #最後一個為最新殖利率
    print(table2.iloc[3])
    #print(table2.iloc[3][0])
    print(Lists5y)
    return Lists5y 

def getUSBondYield7y():
    headers = {'Referer': my_Referer ,'user-agent': my_UserAgent}

    ######以下為判斷上市或上櫃，取得年度股價程式
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup    
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    #urllib3.disable_warnings() 
    #6M
    cnyes_url = 'https://www.cnyes.com/futures/html5chart/US7YY.htmll' 

    url = cnyes_url 
    r = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(r.content, 'lxml')
    table = soup.find_all('table')[0]
    #print(table)
    dfs = pd.read_html(str(table))
    #print(dfs[0])
    #一週 一個月	三個月	六個月 今年以來	一年	三年	五年
    table2 = dfs[0]
    Lists7y = [table2.iloc[3][0],table2.iloc[3][1],table2.iloc[3][3],table2.iloc[3][5],table2.iloc[0][1]] #最後一個為最新殖利率
    print(table2.iloc[3])
    #print(table2.iloc[3][0])
    print(Lists7y)
    return Lists7y 

def getUSBondYield10y():
    headers = {'Referer': my_Referer ,'user-agent': my_UserAgent}

    ######以下為判斷上市或上櫃，取得年度股價程式
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup    
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    #urllib3.disable_warnings() 
    #6M
    cnyes_url = 'https://www.cnyes.com/futures/html5chart/US10YY.html' 

    url = cnyes_url 
    r = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(r.content, 'lxml')
    table = soup.find_all('table')[0]
    #print(table)
    dfs = pd.read_html(str(table))
    #print(dfs[0])
    #一週 一個月	三個月	六個月 今年以來	一年	三年	五年
    table2 = dfs[0]
    Lists10y = [table2.iloc[3][0],table2.iloc[3][1],table2.iloc[3][3],table2.iloc[3][5],table2.iloc[0][1]] #最後一個為最新殖利率
    print(table2.iloc[3])
    #print(table2.iloc[3][0])
    print(Lists10y)
    return Lists10y

def getUSBondYield30y():
    headers = {'Referer': my_Referer ,'user-agent': my_UserAgent}

    ######以下為判斷上市或上櫃，取得年度股價程式
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup    
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    #urllib3.disable_warnings() 
    #6M
    cnyes_url = 'https://www.cnyes.com/futures/html5chart/US30YY.html' 

    url = cnyes_url 
    r = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(r.content, 'lxml')
    table = soup.find_all('table')[0]
    #print(table)
    dfs = pd.read_html(str(table))
    #print(dfs[0])
    #一週 一個月	三個月	六個月 今年以來	一年	三年	五年
    table2 = dfs[0]
    Lists30y = [table2.iloc[3][0],table2.iloc[3][1],table2.iloc[3][3],table2.iloc[3][5],table2.iloc[0][1]] #最後一個為最新殖利率
    print(table2.iloc[3])
    #print(table2.iloc[3][0])
    print(Lists30y)
    return Lists30y

    
def getUSBondYieldALL():
    headers = {'Referer': my_Referer ,'user-agent': my_UserAgent}

    ######以下為判斷上市或上櫃，取得年度股價程式
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup    


    #cnyes_url = 'https://www.cnyes.com/bond/' 

    #url = cnyes_url 
    #r = requests.get(url, headers=headers)
    #soup = BeautifulSoup(r.content, 'lxml')
    #table = soup.find_all('table')[0]
    #print(table)
    #dfs = pd.read_html(str(table))
    #print(dfs[0])
    
    #USBond3mYieldClose = dfs[0].iloc[0][8]
    #USBond6mYieldClose = dfs[0].iloc[1][8]    
    #USBond2yYieldClose = dfs[0].iloc[2][8]  
    #USBond3yYieldClose = dfs[0].iloc[3][8]      
    #USBond5yYieldClose = dfs[0].iloc[4][8]  
    #USBond7yYieldClose = dfs[0].iloc[5][8]      
    #USBond10yYieldClose = dfs[0].iloc[6][8]    
    #USBond30yYieldClose = dfs[0].iloc[7][8]    

    USBond3mYieldClose = getUSBondYield3m()[-1] 
    USBond6mYieldClose = getUSBondYield6m()[-1]   
    USBond2yYieldClose = getUSBondYield2y()[-1]  
    USBond3yYieldClose = getUSBondYield3y()[-1]     
    USBond5yYieldClose = getUSBondYield5y()[-1] 
    USBond7yYieldClose = getUSBondYield7y()[-1]     
    USBond10yYieldClose = getUSBondYield10y()[-1]   
    USBond30yYieldClose = getUSBondYield30y()[-1]

        
    print(USBond3mYieldClose)
    print(USBond6mYieldClose)    
    print(USBond2yYieldClose)     
    print(USBond3yYieldClose) 
    print(USBond5yYieldClose) 
    print(USBond7yYieldClose)     
    print(USBond10yYieldClose)
    print(USBond30yYieldClose)

    
    return USBond3mYieldClose, USBond6mYieldClose, USBond2yYieldClose, USBond3yYieldClose, USBond5yYieldClose, USBond7yYieldClose, USBond10yYieldClose, USBond30yYieldClose


def getUSBondYield():
    headers = {'Referer': my_Referer ,'user-agent': my_UserAgent}

    ######以下為判斷上市或上櫃，取得年度股價程式
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup    
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    #urllib3.disable_warnings() 

    cnyes_url = 'https://www.cnyes.com/bond/' 

    url = cnyes_url 
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    table = soup.find_all('table')[0]
    print(table)
    dfs = pd.read_html(str(table))
    print(dfs[0])
    
    USBond3mYieldClose = dfs[0].iloc[0][8]
    USBond10yYieldClose = dfs[0].iloc[6][8]    
    
    print(USBond3mYieldClose)
    print(USBond10yYieldClose)
    
    return USBond3mYieldClose, USBond10yYieldClose

#getUSBondYield3m()
#getUSBondYield6m()
#getUSBondYield2y()
#getUSBondYield3y()
#getUSBondYield5y()
#getUSBondYield7y()
#getUSBondYield10y()
#getUSBondYield30y()
getUSBondYieldALL()

#getUSBondYieldALL()