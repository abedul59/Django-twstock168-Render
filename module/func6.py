# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 17:14:34 2020

@author: Nicholas
"""

def BigSharHo1000p(stock_id):  #神秘金字塔 超過1000張大股東比率

    
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup
    #import random    
    
    #url_pool = ['http://dj.mybank.com.tw','http://jdata.yuanta.com.tw','http://jsjustweb.jihsun.com.tw','http://stockchannel.sinotrade.com.tw','http://www.emega.com.tw','http://djfubonholdingfund.fbs.com.tw','http://stocks.ftsi.com.tw','http://www.esunsec.com.tw','http://tcfhcsec.moneydj.com','http://kgieworld.moneydj.com','http://pscnetinvest.moneydj.com','http://web.tcsc.com.tw','http://just.honsec.com.tw','http://ycsc.moneydj.com','http://easyfun.concords.com.tw','http://just2.entrust.com.tw','http://newjust.masterlink.com.tw','http://jsinfo.wls.com.tw','http://stock.capital.com.tw']

    #url_chosen = random.choice(url_pool)
    
    #bank_url0 = url_chosen       
    #取得股票名
    bank_url0 = 'https://djinfo.cathaysec.com.tw/' #國泰世華
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
        
#######################    
    
    #神秘金字塔 
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup
    import random
    import time    
    
    #url_pool = ['http://dj.mybank.com.tw','http://jdata.yuanta.com.tw','http://jsjustweb.jihsun.com.tw','http://stockchannel.sinotrade.com.tw','http://www.emega.com.tw','http://djfubonholdingfund.fbs.com.tw','http://stocks.ftsi.com.tw','http://www.esunsec.com.tw','http://tcfhcsec.moneydj.com','http://kgieworld.moneydj.com','http://pscnetinvest.moneydj.com','http://web.tcsc.com.tw','http://just.honsec.com.tw','http://ycsc.moneydj.com','http://easyfun.concords.com.tw','http://just2.entrust.com.tw','http://newjust.masterlink.com.tw','http://jsinfo.wls.com.tw','http://stock.capital.com.tw']

    #url_chosen = random.choice(url_pool)
    
    #bank_url0 = url_chosen       
    #取得股票名


    with requests.Session() as s:
        headers = {'Referer':'https://accounts.pixiv.net/loginlang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index','user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
        #proxies = {'http': 'http://10.10.1.10:3128','https': 'http://10.10.1.10:1080'}	    
        page = s.get('https://norway.twsthr.info/StockHolders.aspx', headers=headers)#, proxies=proxies)
        soup = BeautifulSoup(page.content, 'lxml')
        
        payload_loginPage = {
		    'txtStock': stock_id,
		    'btnQuery': 'Query',

	    }

	    #payload_loginPage["__VIEWSTATE"] = soup.select_one("#__VIEWSTATE")["/wEPDwUJODE3NDE5NDE0ZGQtkmiE92Nmg1+bmd1dLv7LI2sBgg=="]
	    #payload_loginPage["__VIEWSTATEGENERATOR"] = soup.select_one("#__VIEWSTATEGENERATOR")["B22D0476"]
	    #payload_loginPage["__EVENTVALIDATION"] = soup.select_one("#__EVENTVALIDATION")["/wEdAAT5lSNx2nS0euqUKRLwxs8lprT8jKN33hsBogQbG0vXougPUnnQ1NWw7q+TtnLeKzOvMSGXfUsv7Cj7V5DYQf+eEps2ruUuy1HJhEr56pP7mYZC+Mo="]
        #以下隱藏資訊的value不用輸入，直接帶入即可
        payload_loginPage["__VIEWSTATE"] = soup.select_one("#__VIEWSTATE")["value"]
        payload_loginPage["__VIEWSTATEGENERATOR"] = soup.select_one("#__VIEWSTATEGENERATOR")["value"]
        payload_loginPage["__EVENTVALIDATION"] = soup.select_one("#__EVENTVALIDATION")["value"]
        page2 = s.post('https://norway.twsthr.info/StockHolders.aspx', data=payload_loginPage, headers=headers)#, proxies=proxies)
        soup2 = BeautifulSoup(page2.content, 'lxml')
        
    time.sleep(random.randint(3,6))
    table = soup2.select('#Details')  #  真正表格數據 id = Details 


    dfs0 = pd.read_html(str(table))
    table2 = dfs0[0]   #0為正確表格
    #xx = table2[0]  #2為資料月份 8平均價 9週轉率
    #test = table2.iloc[0]  #0為標題
    #test2 = table2.iloc[1]  #1為最新週
    #test3 = table2.iloc[1].iloc[2]  
    #2為最新週日期
    #3為集保總張數
    #4為總股東人數
    #5為平均張數/人
    #6為>400張大股東持有張數
    #7為>400張大股東持有百分比
    #8為>400張大股東人數
    #12為>1000張人數
    #13為>1000張大股東持有百分比
    #14為 收盤價
    w01title = str(table2.iloc[1].iloc[2])
    w01over1000p = str(table2.iloc[1].iloc[13])
    w01close = str(table2.iloc[1].iloc[14])
    #不知為何，每一週跳一個空格？iloc[1,3,5,7]...
    w02title = str(table2.iloc[3].iloc[2])
    w02over1000p = str(table2.iloc[3].iloc[13])
    w02close = str(table2.iloc[3].iloc[14])

    w03title = str(table2.iloc[5].iloc[2])
    w03over1000p = str(table2.iloc[5].iloc[13])     
    w03close = str(table2.iloc[5].iloc[14])


    w04title = str(table2.iloc[7].iloc[2])
    w04over1000p = str(table2.iloc[7].iloc[13])
    w04close = str(table2.iloc[7].iloc[14])


    w05title = str(table2.iloc[9].iloc[2])
    w05over1000p = str(table2.iloc[9].iloc[13])
    w05close = str(table2.iloc[9].iloc[14])


    w06title = str(table2.iloc[11].iloc[2])
    w06over1000p = str(table2.iloc[11].iloc[13])
    w06close = str(table2.iloc[11].iloc[14])


    w07title = str(table2.iloc[13].iloc[2])
    w07over1000p = str(table2.iloc[13].iloc[13])
    w07close = str(table2.iloc[13].iloc[14])

    
    w08title = str(table2.iloc[15].iloc[2])
    w08over1000p = str(table2.iloc[15].iloc[13])
    w08close = str(table2.iloc[15].iloc[14])

    
    w09title = str(table2.iloc[17].iloc[2])
    w09over1000p = str(table2.iloc[17].iloc[13])
    w09close = str(table2.iloc[17].iloc[14])

    
    w10title = str(table2.iloc[19].iloc[2])
    w10over1000p = str(table2.iloc[19].iloc[13])
    w10close = str(table2.iloc[19].iloc[14])


    w11title = str(table2.iloc[21].iloc[2])
    w11over1000p = str(table2.iloc[21].iloc[13])
    w11close = str(table2.iloc[21].iloc[14])

    w12title = str(table2.iloc[23].iloc[2])
    w12over1000p = str(table2.iloc[23].iloc[13])
    w12close = str(table2.iloc[23].iloc[14])

    w13title = str(table2.iloc[25].iloc[2])
    w13over1000p = str(table2.iloc[25].iloc[13])
    w13close = str(table2.iloc[25].iloc[14])

    w14title = str(table2.iloc[27].iloc[2])
    w14over1000p = str(table2.iloc[27].iloc[13])
    w14close = str(table2.iloc[27].iloc[14])

    w15title = str(table2.iloc[29].iloc[2])
    w15over1000p = str(table2.iloc[29].iloc[13])
    w15close = str(table2.iloc[29].iloc[14])

    w16title = str(table2.iloc[31].iloc[2])
    w16over1000p = str(table2.iloc[31].iloc[13])
    w16close = str(table2.iloc[31].iloc[14])

    w17title = str(table2.iloc[33].iloc[2])
    w17over1000p = str(table2.iloc[33].iloc[13])
    w17close = str(table2.iloc[33].iloc[14])

    w18title = str(table2.iloc[35].iloc[2])
    w18over1000p = str(table2.iloc[35].iloc[13])
    w18close = str(table2.iloc[35].iloc[14])

    w19title = str(table2.iloc[37].iloc[2])
    w19over1000p = str(table2.iloc[37].iloc[13])
    w19close = str(table2.iloc[37].iloc[14])

    w20title = str(table2.iloc[39].iloc[2])
    w20over1000p = str(table2.iloc[39].iloc[13])    
    w20close = str(table2.iloc[39].iloc[14])
    
    stock_message = '☆集保庫存-大於1000張大股東持有百分比快速查詢（太頻繁查詢會被擋而發生錯誤，請隔3-4分鐘以上）☆\n\n☆股票代號：' + stock_id + '，' + '股票名稱：' + stock_name + '☆\n\n' + \
    ' 日期 ' + '  :  ' + '持股比率' + ' : ' + '收盤價' + '\n' + \
    w01title + ' : ' + w01over1000p + '%' + ' : ' + w01close + '\n' + \
    w02title + ' : ' + w02over1000p + '%' + ' : ' + w02close + '\n' + \
    w03title + ' : ' + w03over1000p + '%' + ' : ' + w03close + '\n' + \
    w04title + ' : ' + w04over1000p + '%' + ' : ' + w04close + '\n' + \
    w05title + ' : ' + w05over1000p + '%' + ' : ' + w05close + '\n' + \
    w06title + ' : ' + w06over1000p + '%' + ' : ' + w06close + '\n' + \
    w07title + ' : ' + w07over1000p + '%' + ' : ' + w07close + '\n' + \
    w08title + ' : ' + w08over1000p + '%' + ' : ' + w08close + '\n' + \
    w09title + ' : ' + w09over1000p + '%' + ' : ' + w09close + '\n' + \
    w10title + ' : ' + w10over1000p + '%' + ' : ' + w10close + '\n' + \
    w11title + ' : ' + w11over1000p + '%' + ' : ' + w11close + '\n' + \
    w12title + ' : ' + w12over1000p + '%' + ' : ' + w12close + '\n' + \
    w13title + ' : ' + w13over1000p + '%' + ' : ' + w13close + '\n' + \
    w14title + ' : ' + w14over1000p + '%' + ' : ' + w14close + '\n' + \
    w15title + ' : ' + w15over1000p + '%' + ' : ' + w15close + '\n' + \
    w16title + ' : ' + w16over1000p + '%' + ' : ' + w16close + '\n' + \
    w17title + ' : ' + w17over1000p + '%' + ' : ' + w17close + '\n' + \
    w18title + ' : ' + w18over1000p + '%' + ' : ' + w18close + '\n' + \
    w19title + ' : ' + w19over1000p + '%' + ' : ' + w19close + '\n' + \
    w20title + ' : ' + w20over1000p + '%' + ' : ' + w20close + '\n\n' + '☆六大指標智慧系統☆有更多功能可測試，包括EPS達成率、股本變動率、本益比區間穩定率等功能和眾多資料庫☆ https://twstock168.herokuapp.com'
  
    
    
    return stock_message



def BigSharHo400p(stock_id):  #神秘金字塔 超過1000張大股東比率

    
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup
    #import random    
    
    #url_pool = ['http://dj.mybank.com.tw','http://jdata.yuanta.com.tw','http://jsjustweb.jihsun.com.tw','http://stockchannel.sinotrade.com.tw','http://www.emega.com.tw','http://djfubonholdingfund.fbs.com.tw','http://stocks.ftsi.com.tw','http://www.esunsec.com.tw','http://tcfhcsec.moneydj.com','http://kgieworld.moneydj.com','http://pscnetinvest.moneydj.com','http://web.tcsc.com.tw','http://just.honsec.com.tw','http://ycsc.moneydj.com','http://easyfun.concords.com.tw','http://just2.entrust.com.tw','http://newjust.masterlink.com.tw','http://jsinfo.wls.com.tw','http://stock.capital.com.tw']

    #url_chosen = random.choice(url_pool)
    
    #bank_url0 = url_chosen       
    #取得股票名
    bank_url0 = 'https://djinfo.cathaysec.com.tw/' #國泰世華
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
        
#######################    
    
    #神秘金字塔 
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup
    import random
    import time    
    
    #url_pool = ['http://dj.mybank.com.tw','http://jdata.yuanta.com.tw','http://jsjustweb.jihsun.com.tw','http://stockchannel.sinotrade.com.tw','http://www.emega.com.tw','http://djfubonholdingfund.fbs.com.tw','http://stocks.ftsi.com.tw','http://www.esunsec.com.tw','http://tcfhcsec.moneydj.com','http://kgieworld.moneydj.com','http://pscnetinvest.moneydj.com','http://web.tcsc.com.tw','http://just.honsec.com.tw','http://ycsc.moneydj.com','http://easyfun.concords.com.tw','http://just2.entrust.com.tw','http://newjust.masterlink.com.tw','http://jsinfo.wls.com.tw','http://stock.capital.com.tw']

    #url_chosen = random.choice(url_pool)
    
    #bank_url0 = url_chosen       
    #取得股票名


    with requests.Session() as s:
        headers = {'Referer':'https://accounts.pixiv.net/loginlang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index','user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
        #proxies = {'http': 'http://10.10.1.10:3128','https': 'http://10.10.1.10:1080'}	    
        page = s.get('https://norway.twsthr.info/StockHolders.aspx', headers=headers)#, proxies=proxies)
        soup = BeautifulSoup(page.content, 'lxml')
        
        payload_loginPage = {
		    'txtStock': stock_id,
		    'btnQuery': 'Query',

	    }

	    #payload_loginPage["__VIEWSTATE"] = soup.select_one("#__VIEWSTATE")["/wEPDwUJODE3NDE5NDE0ZGQtkmiE92Nmg1+bmd1dLv7LI2sBgg=="]
	    #payload_loginPage["__VIEWSTATEGENERATOR"] = soup.select_one("#__VIEWSTATEGENERATOR")["B22D0476"]
	    #payload_loginPage["__EVENTVALIDATION"] = soup.select_one("#__EVENTVALIDATION")["/wEdAAT5lSNx2nS0euqUKRLwxs8lprT8jKN33hsBogQbG0vXougPUnnQ1NWw7q+TtnLeKzOvMSGXfUsv7Cj7V5DYQf+eEps2ruUuy1HJhEr56pP7mYZC+Mo="]
        #以下隱藏資訊的value不用輸入，直接帶入即可
        payload_loginPage["__VIEWSTATE"] = soup.select_one("#__VIEWSTATE")["value"]
        payload_loginPage["__VIEWSTATEGENERATOR"] = soup.select_one("#__VIEWSTATEGENERATOR")["value"]
        payload_loginPage["__EVENTVALIDATION"] = soup.select_one("#__EVENTVALIDATION")["value"]
        page2 = s.post('https://norway.twsthr.info/StockHolders.aspx', data=payload_loginPage, headers=headers)#, proxies=proxies)
        soup2 = BeautifulSoup(page2.content, 'lxml')
        
    time.sleep(random.randint(3,6))
    table = soup2.select('#Details')  #  真正表格數據 id = Details 


    dfs0 = pd.read_html(str(table))
    table2 = dfs0[0]   #0為正確表格
    #xx = table2[0]  #2為資料月份 8平均價 9週轉率
    #test = table2.iloc[0]  #0為標題
    #test2 = table2.iloc[1]  #1為最新週
    #test3 = table2.iloc[1].iloc[2]  
    #2為最新週日期
    #3為集保總張數
    #4為總股東人數
    #5為平均張數/人
    #6為>400張大股東持有張數
    #7為>400張大股東持有百分比
    #8為>400張大股東人數
    #12為>1000張人數
    #13為>1000張大股東持有百分比
    #14為 收盤價
    w01title = str(table2.iloc[1].iloc[2])
    w01over400p = str(table2.iloc[1].iloc[7])
    w01close = str(table2.iloc[1].iloc[14])
    #不知為何，每一週跳一個空格？iloc[1,3,5,7]...
    w02title = str(table2.iloc[3].iloc[2])
    w02over400p = str(table2.iloc[3].iloc[7])
    w02close = str(table2.iloc[3].iloc[14])

    w03title = str(table2.iloc[5].iloc[2])
    w03over400p = str(table2.iloc[5].iloc[7])     
    w03close = str(table2.iloc[5].iloc[14])


    w04title = str(table2.iloc[7].iloc[2])
    w04over400p = str(table2.iloc[7].iloc[7])
    w04close = str(table2.iloc[7].iloc[14])


    w05title = str(table2.iloc[9].iloc[2])
    w05over400p = str(table2.iloc[9].iloc[7])
    w05close = str(table2.iloc[9].iloc[14])


    w06title = str(table2.iloc[11].iloc[2])
    w06over400p = str(table2.iloc[11].iloc[7])
    w06close = str(table2.iloc[11].iloc[14])


    w07title = str(table2.iloc[13].iloc[2])
    w07over400p = str(table2.iloc[13].iloc[7])
    w07close = str(table2.iloc[13].iloc[14])

    
    w08title = str(table2.iloc[15].iloc[2])
    w08over400p = str(table2.iloc[15].iloc[7])
    w08close = str(table2.iloc[15].iloc[14])

    
    w09title = str(table2.iloc[17].iloc[2])
    w09over400p = str(table2.iloc[17].iloc[7])
    w09close = str(table2.iloc[17].iloc[14])

    
    w10title = str(table2.iloc[19].iloc[2])
    w10over400p = str(table2.iloc[19].iloc[7])
    w10close = str(table2.iloc[19].iloc[14])


    w11title = str(table2.iloc[21].iloc[2])
    w11over400p = str(table2.iloc[21].iloc[7])
    w11close = str(table2.iloc[21].iloc[14])

    w12title = str(table2.iloc[23].iloc[2])
    w12over400p = str(table2.iloc[23].iloc[7])
    w12close = str(table2.iloc[23].iloc[14])

    w13title = str(table2.iloc[25].iloc[2])
    w13over400p = str(table2.iloc[25].iloc[7])
    w13close = str(table2.iloc[25].iloc[14])

    w14title = str(table2.iloc[27].iloc[2])
    w14over400p = str(table2.iloc[27].iloc[7])
    w14close = str(table2.iloc[27].iloc[14])

    w15title = str(table2.iloc[29].iloc[2])
    w15over400p = str(table2.iloc[29].iloc[7])
    w15close = str(table2.iloc[29].iloc[14])

    w16title = str(table2.iloc[31].iloc[2])
    w16over400p = str(table2.iloc[31].iloc[7])
    w16close = str(table2.iloc[31].iloc[14])

    w17title = str(table2.iloc[33].iloc[2])
    w17over400p = str(table2.iloc[33].iloc[7])
    w17close = str(table2.iloc[33].iloc[14])

    w18title = str(table2.iloc[35].iloc[2])
    w18over400p = str(table2.iloc[35].iloc[7])
    w18close = str(table2.iloc[35].iloc[14])

    w19title = str(table2.iloc[37].iloc[2])
    w19over400p = str(table2.iloc[37].iloc[7])
    w19close = str(table2.iloc[37].iloc[14])

    w20title = str(table2.iloc[39].iloc[2])
    w20over400p = str(table2.iloc[39].iloc[7])    
    w20close = str(table2.iloc[39].iloc[14])
    
    stock_message = '☆集保庫存-大於400張大股東持有百分比快速查詢（太頻繁查詢會被擋而發生錯誤，請隔3-4分鐘以上）☆\n\n☆股票代號：' + stock_id + '，' + '股票名稱：' + stock_name + '☆\n\n' + \
    ' 日期 ' + '  :  ' + '持股比率' + ' : ' + '收盤價' + '\n' + \
    w01title + ' : ' + w01over400p + '%' + ' : ' + w01close + '\n' + \
    w02title + ' : ' + w02over400p + '%' + ' : ' + w02close + '\n' + \
    w03title + ' : ' + w03over400p + '%' + ' : ' + w03close + '\n' + \
    w04title + ' : ' + w04over400p + '%' + ' : ' + w04close + '\n' + \
    w05title + ' : ' + w05over400p + '%' + ' : ' + w05close + '\n' + \
    w06title + ' : ' + w06over400p + '%' + ' : ' + w06close + '\n' + \
    w07title + ' : ' + w07over400p + '%' + ' : ' + w07close + '\n' + \
    w08title + ' : ' + w08over400p + '%' + ' : ' + w08close + '\n' + \
    w09title + ' : ' + w09over400p + '%' + ' : ' + w09close + '\n' + \
    w10title + ' : ' + w10over400p + '%' + ' : ' + w10close + '\n' + \
    w11title + ' : ' + w11over400p + '%' + ' : ' + w11close + '\n' + \
    w12title + ' : ' + w12over400p + '%' + ' : ' + w12close + '\n' + \
    w13title + ' : ' + w13over400p + '%' + ' : ' + w13close + '\n' + \
    w14title + ' : ' + w14over400p + '%' + ' : ' + w14close + '\n' + \
    w15title + ' : ' + w15over400p + '%' + ' : ' + w15close + '\n' + \
    w16title + ' : ' + w16over400p + '%' + ' : ' + w16close + '\n' + \
    w17title + ' : ' + w17over400p + '%' + ' : ' + w17close + '\n' + \
    w18title + ' : ' + w18over400p + '%' + ' : ' + w18close + '\n' + \
    w19title + ' : ' + w19over400p + '%' + ' : ' + w19close + '\n' + \
    w20title + ' : ' + w20over400p + '%' + ' : ' + w20close + '\n\n' + '☆六大指標智慧系統☆有更多功能可測試，包括EPS達成率、股本變動率、本益比區間穩定率等功能和眾多資料庫☆ https://twstock168.herokuapp.com'
    
    
    
    return stock_message