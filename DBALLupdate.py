# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 07:24:15 2021

@author: pcuser
"""

#Radar_Echo.py
from bs4 import BeautifulSoup
import requests 
from django.core.mail import EmailMessage



#參考以下網址修改，成功。在heroku run bash裡python costcobot.py成功送信。

#https://ithelp.ithome.com.tw/articles/10252931
#https://stackoverflow.com/questions/28525825/django-core-exceptions-improperlyconfigured-requested-setting-logging-config-b

#Django寄信設定
#https://ithelp.ithome.com.tw/articles/10249625

import time
#import json
#import random
#import requests
import pandas as pd 
#from bs4 import BeautifulSoup   
#from pprint import pprint

#Call to django.setup() should go after setting DJANGO_SETTINGS_MODULE environment variable. Just move it into your __main__ right after os.environ.setdefault().
#


'''
django.setup() may only be called once.

Therefore, avoid putting reusable application logic in standalone scripts so that you have to import from the script elsewhere in your application. If you can’t avoid that, put the call to django.setup() inside an if block:

if __name__ == '__main__':
    import django
    django.setup()
'''

#import django
#from django.conf import settings
#from myapp import myapp_defaults

#settings.configure(default_settings=myapp_defaults, DEBUG=True)
#django.setup()

# Now this script or any imported module can use any part of Django it needs.
#from myapp import models



#https://docs.djangoproject.com/en/3.2/topics/settings/
#import os
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstproject.settings')
#2021/9/13 修改
import os

try:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
except:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')






if __name__ == '__main__':





    
    #價格
    ChangeList2up = []
    ChangeList2down = []

    SameList2 = []

    priceGapUPDict = {}
    priceGapDOWNDict = {}
    
    riskRewardOver266 = {}
    riskReward1to266 = {}    
    
    import django    
    django.setup()
    

    #from myapp.models import StockFavDB

    from django.contrib.auth.decorators import permission_required
    from django.views.decorators.csrf import csrf_exempt
    from django.shortcuts import render

    from myapp.models import Stock6Sign202104
    from myapp.models import Stock6Sign202105
    from myapp.models import Stock6Sign202106
    from myapp.models import Stock6Sign202107
    from myapp.models import Stock6Sign202108
    from myapp.models import Stock6Sign202109
    from myapp.models import Stock6Sign202110
    from myapp.models import Stock6Sign202111
    from myapp.models import Stock6Sign202112
    from myapp.models import Stock6Sign202201
    from myapp.models import Stock6Sign202202
    from myapp.models import Stock6Sign202203
    from myapp.models import Stock6Sign202204
    from myapp.models import Stock6Sign202205
    from myapp.models import Stock6Sign202206
    from myapp.models import Stock6Sign202207
    from myapp.models import Stock6Sign202208
    from myapp.models import Stock6Sign202209
    from myapp.models import Stock6Sign202210
    from myapp.models import Stock6Sign202211
    from myapp.models import Stock6Sign202212


    from myapp.models import Stock6Sign202301
    from myapp.models import Stock6Sign202302
    from myapp.models import Stock6Sign202303
    from myapp.models import Stock6Sign202304
    from myapp.models import Stock6Sign202305
    from myapp.models import Stock6Sign202306
    from myapp.models import Stock6Sign202307
    from myapp.models import Stock6Sign202308
    from myapp.models import Stock6Sign202309
    from myapp.models import Stock6Sign202310
    from myapp.models import Stock6Sign202311
    from myapp.models import Stock6Sign202312


    from myapp.models import EPSachieve2021Q3, EPSachieve2021Q2, EPSachieve2021Q1

    from myapp.models import StockPERseg202112
    from myapp.models import StockPERseg202201
    from myapp.models import StockPERseg202202
    from myapp.models import StockPERseg202203
    from myapp.models import StockPERseg202204
    from myapp.models import StockPERseg202205
    from myapp.models import StockPERseg202206
    from myapp.models import StockPERseg202207
    from myapp.models import StockPERseg202208
    from myapp.models import StockPERseg202209
    from myapp.models import StockPERseg202210
    from myapp.models import StockPERseg202211
    from myapp.models import StockPERseg202212

    from myapp.models import StockPERseg202301
    from myapp.models import StockPERseg202302
    from myapp.models import StockPERseg202303
    from myapp.models import StockPERseg202304
    from myapp.models import StockPERseg202305
    from myapp.models import StockPERseg202306
    from myapp.models import StockPERseg202307
    from myapp.models import StockPERseg202308
    from myapp.models import StockPERseg202309
    from myapp.models import StockPERseg202310
    from myapp.models import StockPERseg202311
    from myapp.models import StockPERseg202312

    from myapp.models import EpsProfit2021Q4
    from myapp.models import EpsProfit2022Q1
    from myapp.models import EpsProfit2022Q2
    from myapp.models import EpsProfit2022Q3
    from myapp.models import EpsProfit2022Q4


    from myapp.models import StockPERsegStable2021Q4
    from myapp.models import StockPERsegStable2022Q1
    from myapp.models import StockPERsegStable2022Q2
    from myapp.models import StockPERsegStable2022Q3
    from myapp.models import StockPERsegStable2022Q4


    from myapp.models import EPSachieve2021Q3
    from myapp.models import EPSachieve2022Q1
    from myapp.models import EPSachieve2022Q2
    from myapp.models import EPSachieve2022Q3

    from myapp.models import StockCapVar2021Q4
    from myapp.models import StockCapVar2022Q1
    from myapp.models import StockCapVar2022Q2
    from myapp.models import StockCapVar2022Q3
    from myapp.models import StockCapVar2022Q4


    from myapp import models

    
    from myapp.models import StockFavs_bobmax
    from myapp.models import StockFavs_deno36
    from myapp.models import StockFavs_donhonlin
    from myapp.models import StockFavs_goldsilver
    from myapp.models import StockFavs_hyeth
    from myapp.models import StockFavs_magicjohn
    from myapp.models import StockFavs_jonyi
    from myapp.models import StockFavs_hakkai
    from myapp.models import StockFavs_bakylews
    from myapp.models import StockFavs_chenchi



    #改變資料庫 取得現在時顛資料庫的類別 也存在於views_monthAlterStuff.py
    class NowTimeDBs:  

        def __init__(self): 
        #資料庫串列 共13個
            self.DBsLists = [Stock6Sign202112, Stock6Sign202201, Stock6Sign202202, Stock6Sign202203, Stock6Sign202204, Stock6Sign202205, Stock6Sign202206, Stock6Sign202207, Stock6Sign202208, Stock6Sign202209, Stock6Sign202210, Stock6Sign202211, Stock6Sign202212, Stock6Sign202301, Stock6Sign202302, Stock6Sign202303, Stock6Sign202304]
            self.PERDBsLists = [StockPERseg202112, StockPERseg202201, StockPERseg202202, StockPERseg202203, StockPERseg202204, StockPERseg202205, StockPERseg202206, StockPERseg202207, StockPERseg202208, StockPERseg202209, StockPERseg202210, StockPERseg202211, StockPERseg202212, StockPERseg202301, StockPERseg202302, StockPERseg202303, StockPERseg202304]
        
        #EPSachiverDB
            self.EPSaDBsLists = [EPSachieve2021Q3, EPSachieve2022Q1, EPSachieve2022Q2, EPSachieve2022Q3]
        #EPSProfitDB
            self.EPSnDBsLists = [EpsProfit2021Q4, EpsProfit2022Q1, EpsProfit2022Q2, EpsProfit2022Q3, EpsProfit2022Q4]
        #StockCapDB
            self.StCapDBsLists = [StockCapVar2021Q4, StockCapVar2022Q1, StockCapVar2022Q2, StockCapVar2022Q3, StockCapVar2022Q4]
        #StockPERsegStableDB
            self.PERstaDBsLists = [StockPERsegStable2021Q4, StockPERsegStable2022Q1, StockPERsegStable2022Q2, StockPERsegStable2022Q3, StockPERsegStable2022Q4]
        #收集資料創建時間
            import datetime
            self.wholetime = str(datetime.datetime.now())         
            self.monthOnly = self.wholetime[5:7]
            self.dayOnly = self.wholetime[8:10]

        
            self.w = ""
            self.x = ""
            self.y = ""
            self.z = ""

            self.PERw = ""
            self.PERx = ""
            self.PERy = ""
            self.PERz = ""
        
            self.EPSAy = None
            self.EPSAz = None

            self.EPSNy = None
            self.EPSNz = None
        
            self.CAPy = None
            self.CAPz = None

            self.STABy = None
            self.STABz = None
            
            self.xmonth_id = ""

        def printDate(self):
            print("月份：")
            print(str(self.wholetime[5:7]))

            print("日期：")
            print(str(self.wholetime[8:10]))

        def getRightEPSADB(self):
        #每月需要的資料庫變數
            if int(self.monthOnly) == 5 and int(self.dayOnly) < 18:
                   
                self.EPSAz = self.EPSaDBsLists[0] #21Q4
                print("test1")
                
            #22Q1
            elif int(self.monthOnly) == 5 and int(self.dayOnly) >= 20:
    
                self.EPSAy = self.EPSaDBsLists[0]
                self.EPSAz = self.EPSaDBsLists[1] 
                print("test2")                

            elif int(self.monthOnly) == 8 and int(self.dayOnly) < 20:
    
                self.EPSAy = self.EPSaDBsLists[0]
                self.EPSAz = self.EPSaDBsLists[1]

                print("test4")                
            #22Q2
            elif int(self.monthOnly) == 8 and int(self.dayOnly) >= 20:
    
                self.EPSAy = self.EPSaDBsLists[1]
                self.EPSAz = self.EPSaDBsLists[2]
                
                print("test5")

            elif int(self.monthOnly) == 11 and int(self.dayOnly) < 20:
    
                self.EPSAy = self.EPSaDBsLists[1]
                self.EPSAz = self.EPSaDBsLists[2]

                print("test7") 
            #22Q3
            elif int(self.monthOnly) == 11 and int(self.dayOnly) >= 20:
    
                self.EPSAy = self.EPSaDBsLists[2]
                self.EPSAz = self.EPSaDBsLists[3]

                print("test8") 

 
            elif int(self.monthOnly) == 9:
    
                self.EPSAy = self.EPSaDBsLists[1]
                self.EPSAz = self.EPSaDBsLists[2]
                
                print("test6a")  
            elif int(self.monthOnly) == 10:
    
                self.EPSAy = self.EPSaDBsLists[1]
                self.EPSAz = self.EPSaDBsLists[2]
                
                print("test6b")  

            elif int(self.monthOnly) == 12:
    
                self.EPSAy = self.EPSaDBsLists[2]
                self.EPSAz = self.EPSaDBsLists[3]

                print("test9a") 

            elif int(self.monthOnly) == 2:
    
                self.EPSAy = self.EPSaDBsLists[2]
                self.EPSAz = self.EPSaDBsLists[3]

                print("test9b")
            elif int(self.monthOnly) == 1:
    
                self.EPSAy = self.EPSaDBsLists[2]
                self.EPSAz = self.EPSaDBsLists[3]

                print("test9c")
                
                
            elif int(self.monthOnly) == 7:
    
                self.EPSAy = self.EPSaDBsLists[0]
                self.EPSAz = self.EPSaDBsLists[1]
                
                print("test3a") 
            elif int(self.monthOnly) == 6:
    
                self.EPSAy = self.EPSaDBsLists[0]
                self.EPSAz = self.EPSaDBsLists[1]
                
                print("test3b") 

 

              


              

            else:
                self.EPSAz = self.EPSaDBsLists[0]            
            
        def getRightEPSNDB(self):
        #每月需要的資料庫變數
            if int(self.monthOnly) == 4 and int(self.dayOnly) >= 5:
    
                self.EPSNy = self.EPSnDBsLists[3]
                self.EPSNz = self.EPSnDBsLists[4]                
            elif int(self.monthOnly) == 5 and int(self.dayOnly) < 20:
    
                self.EPSNy = self.EPSnDBsLists[3]
                self.EPSNz = self.EPSnDBsLists[4]
            


            elif int(self.monthOnly) == 5 and int(self.dayOnly) >= 20:
    
                self.EPSNy = self.EPSnDBsLists[0]
                self.EPSNz = self.EPSnDBsLists[1]
             
            elif int(self.monthOnly) == 8 and int(self.dayOnly) < 20:
    
                self.EPSNy = self.EPSnDBsLists[0]
                self.EPSNz = self.EPSnDBsLists[1]



            elif int(self.monthOnly) == 11 and int(self.dayOnly) < 20:
    
                self.EPSNy = self.EPSnDBsLists[1]
                self.EPSNz = self.EPSnDBsLists[2]


            elif int(self.monthOnly) == 11 and int(self.dayOnly) >= 20:
    
                self.EPSNy = self.EPSnDBsLists[2]
                self.EPSNz = self.EPSnDBsLists[3]
 
            elif int(self.monthOnly) == 6:
    
                self.EPSNy = self.EPSnDBsLists[0]
                self.EPSNz = self.EPSnDBsLists[1]   
            elif int(self.monthOnly) == 7:
    
                self.EPSNy = self.EPSnDBsLists[0]
                self.EPSNz = self.EPSnDBsLists[1] 


            elif int(self.monthOnly) == 9:
    
                self.EPSNy = self.EPSnDBsLists[1]
                self.EPSNz = self.EPSnDBsLists[2]
            elif int(self.monthOnly) == 10:
    
                self.EPSNy = self.EPSnDBsLists[1]
                self.EPSNz = self.EPSnDBsLists[2]
                
                
                
            elif int(self.monthOnly) == 1:
    
                self.EPSNy = self.EPSnDBsLists[2]
                self.EPSNz = self.EPSnDBsLists[3]
            elif int(self.monthOnly) == 2:
    
                self.EPSNy = self.EPSnDBsLists[2]
                self.EPSNz = self.EPSnDBsLists[3]
            elif int(self.monthOnly) == 12:
    
                self.EPSNy = self.EPSnDBsLists[2]
                self.EPSNz = self.EPSnDBsLists[3]


        def getRightCAPDB(self):
        #每月需要的資料庫變數
            if int(self.monthOnly) == 4 and int(self.dayOnly) >= 3:
    
                self.CAPy = self.StCapDBsLists[3]
                self.CAPz = self.StCapDBsLists[4]
            if int(self.monthOnly) == 5 and int(self.dayOnly) < 20:
    
                self.CAPy = self.StCapDBsLists[3]
                self.CAPz = self.StCapDBsLists[4]
            #以下要修改
############################

            elif int(self.monthOnly) == 5 and int(self.dayOnly) >= 20:
    
                self.CAPy = self.StCapDBsLists[0]
                self.CAPz = self.StCapDBsLists[1]
              
            elif int(self.monthOnly) == 8 and int(self.dayOnly) < 20:
    
                self.CAPy = self.StCapDBsLists[0]
                self.CAPz = self.StCapDBsLists[1]
                
            
            elif int(self.monthOnly) == 8 and int(self.dayOnly) >= 20:
    
                self.CAPy = self.StCapDBsLists[1]
                self.CAPz = self.StCapDBsLists[2]
################################

            elif int(self.monthOnly) == 11 and int(self.dayOnly) < 20:
    
                self.CAPy = self.StCapDBsLists[1]
                self.CAPz = self.StCapDBsLists[2]


            elif int(self.monthOnly) == 11 and int(self.dayOnly) >= 20:
    
                self.CAPy = self.StCapDBsLists[2]
                self.CAPz = self.StCapDBsLists[3]


            elif int(self.monthOnly) == 6:
    
                self.CAPy = self.StCapDBsLists[0]
                self.CAPz = self.StCapDBsLists[1] 
            elif int(self.monthOnly) == 7:
    
                self.CAPy = self.StCapDBsLists[0]
                self.CAPz = self.StCapDBsLists[1] 
                
                
            elif int(self.monthOnly) == 9:
    
                self.CAPy = self.StCapDBsLists[1]
                self.CAPz = self.StCapDBsLists[2]
            elif int(self.monthOnly) == 10:
    
                self.CAPy = self.StCapDBsLists[1]
                self.CAPz = self.StCapDBsLists[2]

                
            elif int(self.monthOnly) == 12:
    
                self.CAPy = self.StCapDBsLists[2]
                self.CAPz = self.StCapDBsLists[3]
            elif int(self.monthOnly) == 1:
    
                self.CAPy = self.StCapDBsLists[2]
                self.CAPz = self.StCapDBsLists[3]
            elif int(self.monthOnly) == 2:
    
                self.CAPy = self.StCapDBsLists[2]
                self.CAPz = self.StCapDBsLists[3]





        def getRightSTABDB(self):
        #每月需要的資料庫變數
            if int(self.monthOnly) == 4 and int(self.dayOnly) >= 3:
    
                self.STABy = self.PERstaDBsLists[3]
                self.STABz = self.PERstaDBsLists[4]
            elif int(self.monthOnly) == 5 and int(self.dayOnly) < 20:
    
                self.STABy = self.PERstaDBsLists[3]
                self.STABz = self.PERstaDBsLists[4]



            if int(self.monthOnly) == 5 and int(self.dayOnly) >= 18:
    
                self.STABy = self.PERstaDBsLists[0]
                self.STABz = self.PERstaDBsLists[1]
                
                



            elif int(self.monthOnly) == 8 and int(self.dayOnly) < 20:
    
                self.STABy = self.PERstaDBsLists[0]
                self.STABz = self.PERstaDBsLists[1]

                
            
            elif int(self.monthOnly) == 8 and int(self.dayOnly) >= 20:
    
                self.STABy = self.PERstaDBsLists[1]
                self.STABz = self.PERstaDBsLists[2]

################################


            elif int(self.monthOnly) == 11 and int(self.dayOnly) < 20:
    
                self.STABy = self.PERstaDBsLists[1]
                self.STABz = self.PERstaDBsLists[2]



            elif int(self.monthOnly) == 11 and int(self.dayOnly) >= 20:
    
                self.STABy = self.PERstaDBsLists[2]
                self.STABz = self.PERstaDBsLists[3]

            elif int(self.monthOnly) == 6:
    
                self.STABy = self.PERstaDBsLists[0]
                self.STABz = self.PERstaDBsLists[1]
            elif int(self.monthOnly) == 7:
    
                self.STABy = self.PERstaDBsLists[0]
                self.STABz = self.PERstaDBsLists[1]

            elif int(self.monthOnly) == 9:
    
                self.STABy = self.PERstaDBsLists[1]
                self.STABz = self.PERstaDBsLists[2]                
            elif int(self.monthOnly) == 10:
    
                self.STABy = self.PERstaDBsLists[1]
                self.STABz = self.PERstaDBsLists[2]

            elif int(self.monthOnly) == 12:
    
                self.STABy = self.PERstaDBsLists[2]
                self.STABz = self.PERstaDBsLists[3]
            elif int(self.monthOnly) == 1:
    
                self.STABy = self.PERstaDBsLists[2]
                self.STABz = self.PERstaDBsLists[3]
            elif int(self.monthOnly) == 2:
    
                self.STABy = self.PERstaDBsLists[2]
                self.STABz = self.PERstaDBsLists[3]


                
                
        
        
        def getRightDB(self):
        #每月需要的資料庫變數
            if int(self.monthOnly) == 4 and int(self.dayOnly) >= 13:
    
                self.w = self.DBsLists[0]
                self.x = self.DBsLists[1]
                self.y = self.DBsLists[2]
                self.z = self.DBsLists[3]
            elif int(self.monthOnly) == 5 and int(self.dayOnly) < 13:
    
                self.w = self.DBsLists[0]
                self.x = self.DBsLists[1]
                self.y = self.DBsLists[2]
                self.z = self.DBsLists[3]               
                
            elif int(self.monthOnly) == 5 and int(self.dayOnly) >= 13:
    
                self.w = self.DBsLists[1]
                self.x = self.DBsLists[2]
                self.y = self.DBsLists[3]
                self.z = self.DBsLists[4]
            elif int(self.monthOnly) == 6 and int(self.dayOnly) < 13:
    
                self.w = self.DBsLists[1]
                self.x = self.DBsLists[2]
                self.y = self.DBsLists[3]
                self.z = self.DBsLists[4] 

            elif int(self.monthOnly) == 6 and int(self.dayOnly) >= 13:
    
                self.w = self.DBsLists[2]
                self.x = self.DBsLists[3]
                self.y = self.DBsLists[4]
                self.z = self.DBsLists[5]
                
            elif int(self.monthOnly) == 7 and int(self.dayOnly) < 13:
    
                self.w = self.DBsLists[2]
                self.x = self.DBsLists[3]
                self.y = self.DBsLists[4]
                self.z = self.DBsLists[5]

            elif int(self.monthOnly) == 7 and int(self.dayOnly) >= 13:
    
                self.w = self.DBsLists[3]
                self.x = self.DBsLists[4]
                self.y = self.DBsLists[5]
                self.z = self.DBsLists[6]
                
            elif int(self.monthOnly) == 8 and int(self.dayOnly) < 13:
    
                self.w = self.DBsLists[3]
                self.x = self.DBsLists[4]
                self.y = self.DBsLists[5]
                self.z = self.DBsLists[6]

            elif int(self.monthOnly) == 8 and int(self.dayOnly) >= 13:
    
                self.w = self.DBsLists[4]
                self.x = self.DBsLists[5]
                self.y = self.DBsLists[6]
                self.z = self.DBsLists[7]                
                
            elif int(self.monthOnly) == 9 and int(self.dayOnly) < 13:
    
                self.w = self.DBsLists[4]
                self.x = self.DBsLists[5]
                self.y = self.DBsLists[6]
                self.z = self.DBsLists[7]

            elif int(self.monthOnly) == 9 and int(self.dayOnly) >= 13:
    
                self.w = self.DBsLists[5]
                self.x = self.DBsLists[6]
                self.y = self.DBsLists[7]
                self.z = self.DBsLists[8]                 

            elif int(self.monthOnly) == 10 and int(self.dayOnly) < 13:
    
                self.w = self.DBsLists[5]
                self.x = self.DBsLists[6]
                self.y = self.DBsLists[7]
                self.z = self.DBsLists[8]

            elif int(self.monthOnly) == 10 and int(self.dayOnly) >= 13:
    
                self.w = self.DBsLists[6]
                self.x = self.DBsLists[7]
                self.y = self.DBsLists[8]
                self.z = self.DBsLists[9] 

            elif int(self.monthOnly) == 11 and int(self.dayOnly) < 13:
    
                self.w = self.DBsLists[6]
                self.x = self.DBsLists[7]
                self.y = self.DBsLists[8]
                self.z = self.DBsLists[9]

            elif int(self.monthOnly) == 11 and int(self.dayOnly) >= 13:
    
                self.w = self.DBsLists[7]
                self.x = self.DBsLists[8]
                self.y = self.DBsLists[9]
                self.z = self.DBsLists[10]


            elif int(self.monthOnly) == 12 and int(self.dayOnly) < 13:
    
                self.w = self.DBsLists[7]
                self.x = self.DBsLists[8]
                self.y = self.DBsLists[9]
                self.z = self.DBsLists[10]

            elif int(self.monthOnly) == 12 and int(self.dayOnly) >= 13:
    
                self.w = self.DBsLists[8]
                self.x = self.DBsLists[9]
                self.y = self.DBsLists[10]
                self.z = self.DBsLists[11]
                
                ####只到2022結束
            elif int(self.monthOnly) == 1 and int(self.dayOnly) < 13:
    
                self.w = self.DBsLists[8]
                self.x = self.DBsLists[9]
                self.y = self.DBsLists[10]
                self.z = self.DBsLists[11]

            elif int(self.monthOnly) == 1 and int(self.dayOnly) >= 13:
    
                self.w = self.DBsLists[9]
                self.x = self.DBsLists[10]
                self.y = self.DBsLists[11]
                self.z = self.DBsLists[12]

            elif int(self.monthOnly) == 2 and int(self.dayOnly) < 13:
    
                self.w = self.DBsLists[9]
                self.x = self.DBsLists[10]
                self.y = self.DBsLists[11]
                self.z = self.DBsLists[12]

            elif int(self.monthOnly) == 2 and int(self.dayOnly) >= 13:
    
                self.w = self.DBsLists[10]
                self.x = self.DBsLists[11]
                self.y = self.DBsLists[12]
                self.z = self.DBsLists[13]

            elif int(self.monthOnly) == 3 and int(self.dayOnly) < 13:
    
                self.w = self.DBsLists[10]
                self.x = self.DBsLists[11]
                self.y = self.DBsLists[12]
                self.z = self.DBsLists[13]

            elif int(self.monthOnly) == 3 and int(self.dayOnly) >= 13:
    
                self.w = self.DBsLists[11]
                self.x = self.DBsLists[12]
                self.y = self.DBsLists[13]
                self.z = self.DBsLists[14]

            elif int(self.monthOnly) == 4 and int(self.dayOnly) < 13:
    
                self.w = self.DBsLists[11]
                self.x = self.DBsLists[12]
                self.y = self.DBsLists[13]
                self.z = self.DBsLists[14]
                
            else:
                print("發生月份歸類錯誤！")



        def getRightPERDB(self):
        #每月需要的資料庫變數
            if int(self.monthOnly) == 4 and int(self.dayOnly) >= 13:
    
                self.PERw = self.PERDBsLists[0]
                self.PERx = self.PERDBsLists[1]
                self.PERy = self.PERDBsLists[2]
                self.PERz = self.PERDBsLists[3]
            elif int(self.monthOnly) == 5 and int(self.dayOnly) < 13:
    
                self.PERw = self.PERDBsLists[0]
                self.PERx = self.PERDBsLists[1]
                self.PERy = self.PERDBsLists[2]
                self.PERz = self.PERDBsLists[3]

            elif int(self.monthOnly) == 5 and int(self.dayOnly) >= 13:
    
                self.PERw = self.PERDBsLists[1]
                self.PERx = self.PERDBsLists[2]
                self.PERy = self.PERDBsLists[3]
                self.PERz = self.PERDBsLists[4]
            elif int(self.monthOnly) == 6 and int(self.dayOnly) < 13:
    
                self.PERw = self.PERDBsLists[1]
                self.PERx = self.PERDBsLists[2]
                self.PERy = self.PERDBsLists[3]
                self.PERz = self.PERDBsLists[4]


            elif int(self.monthOnly) == 6 and int(self.dayOnly) >= 13:
    
                self.PERw = self.PERDBsLists[2]
                self.PERx = self.PERDBsLists[3]
                self.PERy = self.PERDBsLists[4]
                self.PERz = self.PERDBsLists[5]
            elif int(self.monthOnly) == 7 and int(self.dayOnly) < 13:
    
                self.PERw = self.PERDBsLists[2]
                self.PERx = self.PERDBsLists[3]
                self.PERy = self.PERDBsLists[4]
                self.PERz = self.PERDBsLists[5]



            elif int(self.monthOnly) == 7 and int(self.dayOnly) >= 13:
    
                self.PERw = self.PERDBsLists[3]
                self.PERx = self.PERDBsLists[4]
                self.PERy = self.PERDBsLists[5]
                self.PERz = self.PERDBsLists[6]            
            elif int(self.monthOnly) == 8 and int(self.dayOnly) < 13:
    
                self.PERw = self.PERDBsLists[3]
                self.PERx = self.PERDBsLists[4]
                self.PERy = self.PERDBsLists[5]
                self.PERz = self.PERDBsLists[6]

            elif int(self.monthOnly) == 8 and int(self.dayOnly) >= 13:
    
                self.PERw = self.PERDBsLists[4]
                self.PERx = self.PERDBsLists[5]
                self.PERy = self.PERDBsLists[6]
                self.PERz = self.PERDBsLists[7]  
            elif int(self.monthOnly) == 9 and int(self.dayOnly) < 13:
    
                self.PERw = self.PERDBsLists[4]
                self.PERx = self.PERDBsLists[5]
                self.PERy = self.PERDBsLists[6]
                self.PERz = self.PERDBsLists[7]


            elif int(self.monthOnly) == 9 and int(self.dayOnly) >= 13:
    
                self.PERw = self.PERDBsLists[5]
                self.PERx = self.PERDBsLists[6]
                self.PERy = self.PERDBsLists[7]
                self.PERz = self.PERDBsLists[8] 
            elif int(self.monthOnly) == 10 and int(self.dayOnly) < 13:
    
                self.PERw = self.PERDBsLists[5]
                self.PERx = self.PERDBsLists[6]
                self.PERy = self.PERDBsLists[7]
                self.PERz = self.PERDBsLists[8] 


            elif int(self.monthOnly) == 10 and int(self.dayOnly) >= 13:
    
                self.PERw = self.PERDBsLists[6]
                self.PERx = self.PERDBsLists[7]
                self.PERy = self.PERDBsLists[8]
                self.PERz = self.PERDBsLists[9] 
            elif int(self.monthOnly) == 11 and int(self.dayOnly) < 13:
    
                self.PERw = self.PERDBsLists[6]
                self.PERx = self.PERDBsLists[7]
                self.PERy = self.PERDBsLists[8]
                self.PERz = self.PERDBsLists[9]


            elif int(self.monthOnly) == 11 and int(self.dayOnly) >= 13:
    
                self.PERw = self.PERDBsLists[7]
                self.PERx = self.PERDBsLists[8]
                self.PERy = self.PERDBsLists[9]
                self.PERz = self.PERDBsLists[10] 
            elif int(self.monthOnly) == 12 and int(self.dayOnly) < 13:
    
                self.PERw = self.PERDBsLists[7]
                self.PERx = self.PERDBsLists[8]
                self.PERy = self.PERDBsLists[9]
                self.PERz = self.PERDBsLists[10]


            elif int(self.monthOnly) == 12 and int(self.dayOnly) >= 13:
    
                self.PERw = self.PERDBsLists[8]
                self.PERx = self.PERDBsLists[9]
                self.PERy = self.PERDBsLists[10]
                self.PERz = self.PERDBsLists[11]
            elif int(self.monthOnly) == 1 and int(self.dayOnly) < 13:
    
                self.PERw = self.PERDBsLists[8]
                self.PERx = self.PERDBsLists[9]
                self.PERy = self.PERDBsLists[10]
                self.PERz = self.PERDBsLists[11]

            elif int(self.monthOnly) == 1 and int(self.dayOnly) >= 13:
    
                self.PERw = self.PERDBsLists[9]
                self.PERx = self.PERDBsLists[10]
                self.PERy = self.PERDBsLists[11]
                self.PERz = self.PERDBsLists[12]
            elif int(self.monthOnly) == 2 and int(self.dayOnly) < 13:
    
                self.PERw = self.PERDBsLists[9]
                self.PERx = self.PERDBsLists[10]
                self.PERy = self.PERDBsLists[11]
                self.PERz = self.PERDBsLists[12]

            elif int(self.monthOnly) == 2 and int(self.dayOnly) >= 13:
    
                self.PERw = self.PERDBsLists[10]
                self.PERx = self.PERDBsLists[11]
                self.PERy = self.PERDBsLists[12]
                self.PERz = self.PERDBsLists[13]
            elif int(self.monthOnly) == 3 and int(self.dayOnly) < 13:
    
                self.PERw = self.PERDBsLists[10]
                self.PERx = self.PERDBsLists[11]
                self.PERy = self.PERDBsLists[12]
                self.PERz = self.PERDBsLists[13]

            elif int(self.monthOnly) == 3 and int(self.dayOnly) >= 13:
    
                self.PERw = self.PERDBsLists[11]
                self.PERx = self.PERDBsLists[12]
                self.PERy = self.PERDBsLists[13]
                self.PERz = self.PERDBsLists[14]
            elif int(self.monthOnly) == 4 and int(self.dayOnly) < 13:
    
                self.PERw = self.PERDBsLists[11]
                self.PERx = self.PERDBsLists[12]
                self.PERy = self.PERDBsLists[13]
                self.PERz = self.PERDBsLists[14]
            else:
                print("發生月份歸類錯誤！")



        def getRightMonidDB(self):
        #每月需要的資料庫變數
            if int(self.monthOnly) == 1 and int(self.dayOnly) < 13:
    
                self.xmonth_id = "11"

            elif int(self.monthOnly) == 1 and int(self.dayOnly) >= 13:
    
                self.xmonth_id = "12"

            elif int(self.monthOnly) == 2 and int(self.dayOnly) < 13:
    
                self.xmonth_id = "12"
            elif int(self.monthOnly) == 2 and int(self.dayOnly) >= 13:
    
                self.xmonth_id = "1"

            elif int(self.monthOnly) == 3 and int(self.dayOnly) < 13:
    
                self.xmonth_id = "1"
            elif int(self.monthOnly) == 3 and int(self.dayOnly) >= 13:
    
                self.xmonth_id = "2"


            elif int(self.monthOnly) == 4 and int(self.dayOnly) < 13:
    
                self.xmonth_id = "2"
            elif int(self.monthOnly) == 4 and int(self.dayOnly) >= 13:
    
                self.xmonth_id = "3"
                
                
                
            elif int(self.monthOnly) == 5 and int(self.dayOnly) < 13:
    
                self.xmonth_id = "3"
            elif int(self.monthOnly) == 5 and int(self.dayOnly) >= 13:
    
                self.xmonth_id = "4"
 

            elif int(self.monthOnly) == 6 and int(self.dayOnly) < 13:
    
                self.xmonth_id = "4"
            elif int(self.monthOnly) == 6 and int(self.dayOnly) >= 13:
    
                self.xmonth_id = "5"

            elif int(self.monthOnly) == 7 and int(self.dayOnly) < 13:
    
                self.xmonth_id = "5"
            elif int(self.monthOnly) == 7 and int(self.dayOnly) >= 13:
    
                self.xmonth_id = "6"

            elif int(self.monthOnly) == 8 and int(self.dayOnly) < 13:
    
                self.xmonth_id = "6"
            elif int(self.monthOnly) == 8 and int(self.dayOnly) >= 13:
    
                self.xmonth_id = "7"

            elif int(self.monthOnly) == 9 and int(self.dayOnly) < 13:
    
                self.xmonth_id = "7"
            elif int(self.monthOnly) == 9 and int(self.dayOnly) >= 13:
    
                self.xmonth_id = "8"

            elif int(self.monthOnly) == 10 and int(self.dayOnly) < 13:
    
                self.xmonth_id = "8"
            elif int(self.monthOnly) == 10 and int(self.dayOnly) >= 13:
    
                self.xmonth_id = "9"

            elif int(self.monthOnly) == 11 and int(self.dayOnly) < 13:
    
                self.xmonth_id = "9"
            elif int(self.monthOnly) == 11 and int(self.dayOnly) >= 13:
    
                self.xmonth_id = "10"

            elif int(self.monthOnly) == 12 and int(self.dayOnly) < 13:
    
                self.xmonth_id = "10"
            elif int(self.monthOnly) == 12 and int(self.dayOnly) >= 13:
    
                self.xmonth_id = "11"

            #以下要修改
 
            else:
                print("發生月份歸類錯誤！")

        def show(self):  
            print(self.w)
            print(self.x)
            print(self.y)
            print(self.z)











    def StoFav_AutoRenew(stock_id, month_id):
        from module_PERseg import PERsegx
        from module import func2
        from myapp.models import StockFavDB                
        from myapp.models import StockFavs_test168

        from myapp.models import Stock6Sign202105
        from myapp.models import Stock6Sign202106
        from myapp.models import Stock6Sign202107
        from myapp.models import Stock6Sign202107
        from myapp.models import Stock6Sign202108
        from myapp.models import Stock6Sign202109
        from myapp.models import Stock6Sign202110
        from myapp.models import Stock6Sign202111    
        from myapp.models import Stock6Sign202112
        from myapp.models import Stock6Sign202201
        from myapp.models import Stock6Sign202202
        from myapp.models import Stock6Sign202203


        from myapp.models import StockFavs_bobmax
        from myapp.models import StockFavs_deno36
        from myapp.models import StockFavs_donhonlin
        from myapp.models import StockFavs_goldsilver
        from myapp.models import StockFavs_hyeth
        from myapp.models import StockFavs_magicjohn
        from myapp.models import StockFavs_jonyi
        from myapp.models import StockFavs_hakkai
        from myapp.models import StockFavs_bakylews
        from myapp.models import StockFavs_chenchi
        from myapp.models import StockFavs_yuhuahsiao
        from myapp.models import StockFavs_liusnow
        from myapp.models import StockFavs_kevinlee

        #from myapp import views
        #from myapp.views_monthlyAlterStuff import NowTimeDBs 


        DBv = NowTimeDBs()  #從views_monthlyAlterStuff.py取得每月需要的資料庫變數

        DBv.printDate()


        DBv.getRightDB()  #Stock6Sgin
        DBv.getRightPERDB() #StockPERseg
        DBv.getRightMonidDB() #getMonth_id

        DBz = DBv.z  #每個月的主要資料庫  #y= 上個月 x = 上上個月
        DBy = DBv.y
        DBx = DBv.x
        
        
        print(DBz, DBy, DBx)


        DBPERz = DBv.PERz  #每個月的主要資料庫  #y= 上個月 x = 上上個月
        DBPERy = DBv.PERy
        DBPERx = DBv.PERx
        
        
        DBgetMonthid = DBv.xmonth_id

        #########
        DBv.getRightMonidDB()

        #print(str(DBEPSAz))
        
        
        DBv.getRightSTABDB()
        DBv.getRightCAPDB()
        DBv.getRightEPSADB()
        DBv.getRightEPSNDB()

        DBEPSAy = DBv.EPSAy
        DBEPSAz = DBv.EPSAz
        print(DBEPSAz)


        DBEPSNy = DBv.EPSNy
        DBEPSNz = DBv.EPSNz
        print(DBEPSNz)
        
        DBCAPy = DBv.CAPy
        DBCAPz = DBv.CAPz
        print(DBCAPz)


        DBSTABy = DBv.STABy
        DBSTABz = DBv.STABz
        print(DBSTABz)

        ##############

        


        
        stock_name = func2.GetStockName(stock_id)

        H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, New_up_profit, New_down_loss, risk_reward, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average, pNet1, pNet2, pNet3, pNet4, pNet4Average, H0, thisYear_Sum, theRest_Predict, H6, L6, Predict_EPS0, eps1N =PERsegx.PERsegx(stock_id, month_id)

        percent30down_PER_H = round(PER_H*0.7,2)
        percent30down_PER_L = round(PER_L*0.7,2)
        
        
        Predict_high_price_30percentDown = round(Predict_high_price*0.7,2)
        Predict_low_price_30percentDown = round(Predict_low_price*0.7,2)

        
        up_profit2 = round((Predict_high_price_30percentDown - yahoo_latest_tradePrice)/yahoo_latest_tradePrice,2)
        down_loss2 = round((Predict_low_price_30percentDown - yahoo_latest_tradePrice)/yahoo_latest_tradePrice,2)
        

        from decimal import Decimal, ROUND_HALF_UP
        New_up_profit2 = str((Decimal(up_profit2).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
        New_down_loss2 = str((Decimal(down_loss2).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'


        
        
        New_risk_reward = round(abs(up_profit2/down_loss2),2)



        xUrl = "/ListallStockFavDB/" + str(stock_id) + "/"        




        try:
            c1 = DBz.objects.get(cStockID = stock_id)
            ScoreAve1 = c1.cAverageScore
        except:
            ScoreAve1 = "N/A"
        
        try:
            c2 = DBy.objects.get(cStockID = stock_id)
            ScoreAve2 = c2.cAverageScore
        except:
            ScoreAve2 = "N/A"
        
        try:
            c3 = DBx.objects.get(cStockID = stock_id)
            ScoreAve3 = c3.cAverageScore      
        except:
            ScoreAve3 = "N/A"
        #收集資料創建時間
        import datetime
        wholetime = str(datetime.datetime.now()) 
        realtime = wholetime[:16]  #取得獲取資料時間
        
        yeardateOnly = wholetime[:10]

        #from decimal import Decimal, ROUND_HALF_UP

        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理  共通最愛資料庫
            #不存在，發生錯誤，跳到except            
            cOld2 = StockFavDB.objects.get(cStockID = stock_id, cYearDate = yeardateOnly)#(cYearDate = yeardateOnly)
            
            #if str(cOld2.cYearDate) != str(yeardateOnly):
                
            #cDB = StockFavDB.objects.create(cStockID = mess,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            #cDB.save()
                
            #else:



                
            cOld2.cStockID = stock_id
            cOld2.cStockName = stock_name
            cOld2.cYearDate = yeardateOnly

          
            cOld2.cPredict_EPS = Predict_EPS  
            cOld2.cPredict_high_price = Predict_high_price              
            cOld2.cPredict_low_price = Predict_low_price
            cOld2.cNew_up_profit = New_up_profit          
            cOld2.cNew_down_loss = New_down_loss    
            cOld2.cRisk_reward = risk_reward 
            cOld2.cTodayClose = float(yahoo_latest_tradePrice)

            
            cOld2.pubtime =realtime      
                 
            cOld2.save() 
            
        except:  #針對沒有的，抓取資料存入資料庫 有兩筆資料以上
            
            try:
                cOld2 = StockFavDB.objects.create(cStockID = stock_id,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

                cOld2.save()
            except:
                pass

        

###############################################################################





########################以下主程式####################            
    from myapp.models import StockFavDB                
    from myapp.models import StockFavs_test168

    from myapp.models import StockFavs_bobmax
    from myapp.models import StockFavs_deno36
    from myapp.models import StockFavs_donhonlin
    from myapp.models import StockFavs_goldsilver
    from myapp.models import StockFavs_hyeth
    from myapp.models import StockFavs_magicjohn
    from myapp.models import StockFavs_jonyi
    from myapp.models import StockFavs_hakkai
    from myapp.models import StockFavs_bakylews
    from myapp.models import StockFavs_chenchi
    from myapp.models import StockFavs_yuhuahsiao
    from myapp.models import StockFavs_liusnow
    from myapp.models import StockFavs_kevinlee

    DBv = NowTimeDBs()  #從views_monthlyAlterStuff.py取得每月需要的資料庫變數

    DBv.getRightDB()  #Stock6Sgin
    DBv.getRightPERDB() #StockPERseg
    DBv.getRightMonidDB() #getMonth_id

    DBz = DBv.z  #每個月的主要資料庫  #y= 上個月 x = 上上個月
    DBy = DBv.y
    DBx = DBv.x


    DBPERz = DBv.PERz  #每個月的主要資料庫  #y= 上個月 x = 上上個月
    DBPERy = DBv.PERy
    DBPERx = DBv.PERx
        
        
    DBgetMonthid = DBv.xmonth_id
    
    print("目前本益比區間計算月份：")
    print(DBgetMonthid)
####################################################
    #company = ['1101','1102','1103','1104','1108','1109','1110','1201','1203','1210','1213','1215','1216','1217','1218','1219','1220','1225','1227','1229','1231','1232','1233','1234','1235','1236','1240','1256','1258','1259','1262','1264','1268','1301','1303','1304','1305','1307','1308','1309','1310','1312','1313','1314','1315','1316','1319','1321','1323','1324','1325','1326','1333','1336','1337','1338','1339','1340','1341','1402','1409','1410','1413','1414','1416','1417','1418','1419','1423','1432','1434','1435','1436','1437','1438','1439','1440','1441','1442','1443','1444','1445','1446','1447','1449','1451','1452','1453','1454','1455','1456','1457','1459','1460','1463','1464','1465','1466','1467','1468','1470','1471','1472','1473','1474','1475','1476','1477','1503','1504','1506','1507','1512','1513','1514','1515','1516','1517','1519','1521','1522','1524','1525','1526','1527','1528','1529','1530','1531','1532','1533','1535','1536','1537','1538','1539','1540','1541','1558','1560','1565','1568','1569','1570','1580','1582','1583','1584','1586','1587','1589','1590','1591','1592','1593','1595','1597','1598','1599','1603','1604','1605','1608','1609','1611','1612','1614','1615','1616','1617','1618','1626','1701','1702','1707','1708','1709','1710','1711','1712','1713','1714','1717','1718','1720','1721','1722','1723','1724','1725','1726','1727','1730','1731','1732','1733','1734','1735','1736','1737','1742','1752','1760','1762','1773','1776','1777','1781','1783','1784','1785','1786','1787','1788','1789','1795','1796','1799','1802','1805','1806','1808','1809','1810','1813','1815','1817','1902','1903','1904','1905','1906','1907','1909','2002','2006','2007','2008','2009','2010','2012','2013','2014','2015','2017','2020','2022','2023','2024','2025','2027','2028','2029','2030','2031','2032','2033','2034','2035','2038','2049','2059','2061','2062','2063','2064','2065','2066','2067','2069','2070','2101','2102','2103','2104','2105','2106','2107','2108','2109','2114','2115','2201','2204','2206','2207','2208','2221','2227','2228','2230','2231','2233','2235','2236','2239','2243','2301','2302','2303','2305','2308','2312','2313','2314','2316','2317','2321','2323','2324','2327','2328','2329','2330','2331','2332','2337','2338','2340','2342','2344','2345','2347','2348','2349','2351','2352','2353','2354','2355','2356','2357','2358','2359','2360','2362','2363','2364','2365','2367','2368','2369','2371','2373','2374','2375','2376','2377','2379','2380','2382','2383','2385','2387','2388','2390','2392','2393','2395','2397','2399','2401','2402','2404','2405','2406','2408','2409','2412','2413','2414','2415','2417','2419','2420','2421','2423','2424','2425','2426','2427','2428','2429','2430','2431','2433','2434','2436','2438','2439','2440','2441','2442','2443','2444','2448','2449','2450','2451','2453','2454','2455','2456','2457','2458','2459','2460','2461','2462','2464','2465','2466','2467','2468','2471','2472','2474','2476','2477','2478','2480','2481','2482','2483','2484','2485','2486','2488','2489','2491','2492','2493','2495','2496','2497','2498','2499','2501','2504','2505','2506','2509','2511','2514','2515','2516','2520','2524','2527','2528','2530','2534','2535','2536','2537','2538','2539','2540','2542','2543','2545','2546','2547','2548','2596','2597','2601','2603','2605','2606','2607','2608','2609','2610','2611','2612','2613','2614','2615','2616','2617','2618','2630','2633','2634','2636','2637','2640','2641','2642','2643','2701','2702','2704','2705','2706','2707','2712','2718','2719','2722','2723','2724','2726','2727','2729','2731','2732','2734','2736','2739','2740','2745','2748','2801','2809','2812','2816','2820','2823','2832','2834','2836','2838','2841','2845','2849','2850','2851','2852','2855','2867','2880','2881','2882','2883','2884','2885','2886','2887','2888','2889','2890','2891','2892','2897','2901','2903','2904','2905','2906','2908','2910','2911','2912','2913','2915','2916','2923','2924','2926','2928','2929','2936','2937','2939','3002','3003','3004','3005','3006','3008','3010','3011','3013','3014','3015','3016','3017','3018','3019','3021','3022','3023','3024','3025','3026','3027','3028','3029','3030','3031','3032','3033','3034','3035','3036','3037','3038','3040','3041','3042','3043','3044','3045','3046','3047','3048','3049','3050','3051','3052','3054','3055','3056','3057','3058','3059','3060','3062','3064','3066','3067','3071','3073','3078','3081','3083','3085','3086','3088','3089','3090','3092','3093','3094','3095','3105','3114','3115','3118','3122','3128','3130','3131','3141','3144','3147','3149','3152','3162','3163','3164','3167','3169','3171','3176','3178','3188','3189','3191','3202','3205','3206','3207','3209','3211','3213','3217','3218','3219','3221','3224','3226','3227','3228','3229','3230','3231','3232','3234','3236','3252','3257','3259','3260','3264','3265','3266','3268','3272','3276','3284','3285','3287','3288','3289','3290','3293','3294','3296','3297','3303','3305','3306','3308','3310','3311','3312','3313','3317','3321','3322','3323','3324','3325','3332','3338','3339','3346','3354','3356','3360','3362','3363','3372','3373','3374','3376','3379','3380','3383','3388','3390','3402','3406','3413','3416','3419','3426','3432','3434','3437','3438','3441','3443','3444','3450','3452','3454','3455','3465','3466','3479','3481','3483','3484','3489','3490','3491','3492','3494','3498','3499','3501','3504','3508','3511','3512','3515','3516','3518','3520','3521','3522','3523','3526','3526','3527','3528','3529','3530','3531','3532','3533','3535','3536','3537','3540','3541','3545','3546','3548','3550','3551','3552','3555','3556','3557','3558','3562','3563','3564','3567','3570','3576','3577','3580','3581','3583','3587','3588','3591','3593','3594','3596','3605','3607','3609','3611','3615','3617','3622','3623','3624','3625','3628','3629','3630','3631','3632','3642','3645','3646','3652','3653','3661','3663','3664','3665','3666','3669','3672','3673','3675','3679','3680','3682','3684','3685','3686','3687','3689','3691','3693','3694','3698','3701','3702','3703','3704','3705','3705','3706','3707','3708','3709','3710','3711','3712','4102','4104','4105','4106','4107','4108','4109','4111','4113','4114','4116','4119','4120','4121','4123','4126','4127','4128','4129','4130','4131','4133','4137','4138','4139','4141','4142','4144','4147','4148','4152','4153','4154','4155','4157','4160','4161','4162','4163','4164','4167','4168','4171','4173','4174','4175','4183','4188','4190','4192','4198','4205','4207','4303','4304','4305','4306','4401','4402','4406','4413','4414','4415','4416','4417','4419','4420','4426','4429','4430','4432','4433','4438','4502','4503','4506','4510','4513','4523','4526','4527','4528','4529','4530','4532','4533','4534','4535','4536','4538','4540','4541','4542','4543','4545','4549','4550','4551','4552','4554','4555','4556','4557','4560','4561','4562','4563','4564','4566','4568','4572','4576','4609','4702','4706','4707','4711','4712','4714','4716','4720','4721','4722','4725','4726','4728','4729','4735','4736','4737','4739','4741','4743','4744','4745','4746','4747','4754','4755','4760','4763','4764','4766','4767','4803','4804','4806','4807','4903','4904','4905','4906','4907','4908','4909','4911','4912','4915','4916','4919','4924','4927','4930','4933','4934','4935','4938','4939','4942','4943','4944','4946','4947','4950','4952','4953','4956','4958','4960','4961','4966','4967','4968','4971','4972','4973','4974','4976','4977','4979','4987','4989','4991','4994','4995','4999','5007','5009','5011','5013','5014','5015','5016','5102','5201','5202','5203','5205','5206','5209','5210','5211','5212','5213','5215','5220','5223','5225','5227','5230','5234','5243','5245','5251','5258','5259','5263','5264','5269','5272','5274','5276','5278','5281','5283','5284','5285','5287','5288','5289','5291','5299','5301','5302','5304','5305','5306','5309','5310','5312','5314','5315','5317','5321','5324','5328','5340','5344','5345','5347','5348','5349','5351','5353','5355','5356','5364','5371','5381','5383','5386','5388','5392','5398','5403','5410','5425','5426','5432','5434','5438','5439','5443','5450','5452','5455','5457','5460','5464','5465','5468','5469','5471','5474','5475','5478','5481','5483','5484','5487','5488','5489','5490','5493','5498','5508','5511','5512','5514','5515','5516','5519','5520','5521','5522','5523','5525','5529','5530','5531','5533','5534','5536','5538','5543','5601','5603','5604','5607','5608','5609','5701','5703','5704','5706','5820','5864','5871','5876','5878','5880','5902','5903','5904','5905','5906','5907','6005','6015','6016','6020','6021','6023','6024','6026','6101','6103','6104','6108','6109','6111','6112','6113','6114','6115','6116','6117','6118','6120','6121','6122','6123','6124','6125','6126','6127','6128','6129','6130','6131','6133','6134','6136','6138','6139','6140','6141','6142','6143','6144','6146','6147','6148','6150','6151','6152','6153','6154','6155','6156','6158','6160','6161','6163','6164','6165','6166','6167','6168','6169','6170','6171','6172','6173','6174','6175','6176','6177','6179','6180','6182','6183','6184','6185','6186','6187','6188','6189','6190','6191','6192','6194','6195','6196','6197','6198','6199','6201','6202','6203','6204','6205','6206','6207','6208','6209','6210','6212','6213','6214','6215','6216','6217','6218','6219','6220','6221','6222','6223','6224','6225','6226','6227','6228','6229','6230','6231','6233','6234','6235','6236','6237','6238','6239','6240','6241','6242','6243','6244','6245','6246','6247','6248','6251','6257','6259','6261','6263','6264','6265','6266','6269','6270','6271','6274','6275','6276','6277','6278','6279','6281','6282','6283','6284','6285','6287','6288','6289','6290','6291','6292','6294','6404','6405','6409','6411','6412','6414','6415','6416','6417','6418','6419','6425','6426','6431','6432','6435','6438','6441','6442','6443','6446','6449','6451','6452','6456','6457','6461','6462','6464','6465','6469','6470','6472','6477','6482','6485','6486','6488','6492','6494','6496','6499','6504','6505','6506','6508','6509','6510','6512','6514','6516','6523','6525','6530','6531','6532','6533','6535','6538','6542','6547','6548','6552','6556','6558','6560','6561','6568','6569','6570','6573','6574','6576','6577','6578','6579','6581','6582','6589','6590','6591','6593','6594','6596','6603','6605','6609','6612','6613','6615','6616','6624','6625','6629','6640','6641','6643','6649','6654','6655','6662','6664','6666','6667','6668','6669','6670','6671','6672','6674','6679','6683','6803','7402','8011','8016','8021','8024','8027','8028','8032','8033','8034','8038','8039','8040','8042','8043','8044','8046','8047','8048','8049','8050','8054','8059','8064','8066','8067','8068','8069','8070','8071','8072','8074','8076','8077','8080','8081','8083','8084','8085','8086','8087','8088','8091','8092','8093','8096','8097','8099','8101','8103','8104','8105','8107','8109','8110','8111','8112','8114','8121','8131','8147','8150','8155','8163','8171','8176','8182','8183','8201','8210','8213','8215','8222','8234','8240','8249','8255','8261','8271','8277','8279','8287','8289','8291','8299','8341','8342','8349','8354','8358','8367','8374','8383','8390','8401','8403','8404','8406','8409','8410','8411','8415','8416','8418','8420','8421','8422','8423','8424','8426','8427','8429','8431','8432','8433','8435','8436','8437','8440','8442','8443','8444','8446','8450','8454','8455','8462','8463','8464','8466','8467','8472','8473','8476','8477','8478','8480','8481','8482','8488','8489','8497','8499','8905','8906','8908','8913','8916','8917','8921','8923','8924','8926','8927','8928','8929','8930','8931','8932','8933','8934','8935','8936','8937','8938','8940','8941','8942','8996','9103','9105','9110','9136','9802','9902','9904','9905','9906','9907','9908','9910','9910','9911','9912','9914','9917','9918','9919','9921','9924','9925','9926','9927','9928','9929','9930','9931','9933','9934','9935','9937','9938','9939','9940','9941','9942','9943','9944','9945','9946','9949','9950','9951','9955','9958','9960','9962']


    import random
    #每個人的最愛股票代號
    StoFavIDlist = ['1101','1102','1103','1104','1108','1109','1110','1201','1203','1210','1213','1215','1216','1217','1218','1219','1220','1225','1227','1229','1231','1232','1233','1234','1235','1236','1240','1256','1258','1259','1262','1264','1268','1301','1303','1304','1305','1307','1308','1309','1310','1312','1313','1314','1315','1316','1319','1321','1323','1324','1325','1326','1333','1336','1337','1338','1339','1340','1341','1402','1409','1410','1413','1414','1416','1417','1418','1419','1423','1432','1434','1435','1436','1437','1438','1439','1440','1441','1442','1443','1444','1445','1446','1447','1449','1451','1452','1453','1454','1455','1456','1457','1459','1460','1463','1464','1465','1466','1467','1468','1470','1471','1472','1473','1474','1475','1476','1477','1503','1504','1506','1507','1512','1513','1514','1515','1516','1517','1519','1521','1522','1524','1525','1526','1527','1528','1529','1530','1531','1532','1533','1535','1536','1537','1538','1539','1540','1541','1558','1560','1565','1568','1569','1570','1580','1582','1583','1584','1586','1587','1589','1590','1591','1592','1593','1595','1597','1598','1599','1603','1604','1605','1608','1609','1611','1612','1614','1615','1616','1617','1618','1626','1701','1702','1707','1708','1709','1710','1711','1712','1713','1714','1717','1718','1720','1721','1722','1723','1724','1725','1726','1727','1730','1731','1732','1733','1734','1735','1736','1737','1742','1752','1760','1762','1773','1776','1777','1781','1783','1784','1785','1786','1787','1788','1789','1795','1796','1799','1802','1805','1806','1808','1809','1810','1813','1815','1817','1902','1903','1904','1905','1906','1907','1909','2002','2006','2007','2008','2009','2010','2012','2013','2014','2015','2017','2020','2022','2023','2024','2025','2027','2028','2029','2030','2031','2032','2033','2034','2035','2038','2049','2059','2061','2062','2063','2064','2065','2066','2067','2069','2070','2101','2102','2103','2104','2105','2106','2107','2108','2109','2114','2115','2201','2204','2206','2207','2208','2221','2227','2228','2230','2231','2233','2235','2236','2239','2243','2301','2302','2303','2305','2308','2312','2313','2314','2316','2317','2321','2323','2324','2327','2328','2329','2330','2331','2332','2337','2338','2340','2342','2344','2345','2347','2348','2349','2351','2352','2353','2354','2355','2356','2357','2358','2359','2360','2362','2363','2364','2365','2367','2368','2369','2371','2373','2374','2375','2376','2377','2379','2380','2382','2383','2385','2387','2388','2390','2392','2393','2395','2397','2399','2401','2402','2404','2405','2406','2408','2409','2412','2413','2414','2415','2417','2419','2420','2421','2423','2424','2425','2426','2427','2428','2429','2430','2431','2433','2434','2436','2438','2439','2440','2441','2442','2443','2444','2448','2449','2450','2451','2453','2454','2455','2456','2457','2458','2459','2460','2461','2462','2464','2465','2466','2467','2468','2471','2472','2474','2476','2477','2478','2480','2481','2482','2483','2484','2485','2486','2488','2489','2491','2492','2493','2495','2496','2497','2498','2499','2501','2504','2505','2506','2509','2511','2514','2515','2516','2520','2524','2527','2528','2530','2534','2535','2536','2537','2538','2539','2540','2542','2543','2545','2546','2547','2548','2596','2597','2601','2603','2605','2606','2607','2608','2609','2610','2611','2612','2613','2614','2615','2616','2617','2618','2630','2633','2634','2636','2637','2640','2641','2642','2643','2701','2702','2704','2705','2706','2707','2712','2718','2719','2722','2723','2724','2726','2727','2729','2731','2732','2734','2736','2739','2740','2745','2748','2801','2809','2812','2816','2820','2823','2832','2834','2836','2838','2841','2845','2849','2850','2851','2852','2855','2867','2880','2881','2882','2883','2884','2885','2886','2887','2888','2889','2890','2891','2892','2897','2901','2903','2904','2905','2906','2908','2910','2911','2912','2913','2915','2916','2923','2924','2926','2928','2929','2936','2937','2939','3002','3003','3004','3005','3006','3008','3010','3011','3013','3014','3015','3016','3017','3018','3019','3021','3022','3023','3024','3025','3026','3027','3028','3029','3030','3031','3032','3033','3034','3035','3036','3037','3038','3040','3041','3042','3043','3044','3045','3046','3047','3048','3049','3050','3051','3052','3054','3055','3056','3057','3058','3059','3060','3062','3064','3066','3067','3071','3073','3078','3081','3083','3085','3086','3088','3089','3090','3092','3093','3094','3095','3105','3114','3115','3118','3122','3128','3130','3131','3141','3144','3147','3149','3152','3162','3163','3164','3167','3169','3171','3176','3178','3188','3189','3191','3202','3205','3206','3207','3209','3211','3213','3217','3218','3219','3221','3224','3226','3227','3228','3229','3230','3231','3232','3234','3236','3252','3257','3259','3260','3264','3265','3266','3268','3272','3276','3284','3285','3287','3288','3289','3290','3293','3294','3296','3297','3303','3305','3306','3308','3310','3311','3312','3313','3317','3321','3322','3323','3324','3325','3332','3338','3339','3346','3354','3356','3360','3362','3363','3372','3373','3374','3376','3379','3380','3383','3388','3390','3402','3406','3413','3416','3419','3426','3432','3434','3437','3438','3441','3443','3444','3450','3452','3454','3455','3465','3466','3479','3481','3483','3484','3489','3490','3491','3492','3494','3498','3499','3501','3504','3508','3511','3512','3515','3516','3518','3520','3521','3522','3523','3526','3526','3527','3528','3529','3530','3531','3532','3533','3535','3536','3537','3540','3541','3545','3546','3548','3550','3551','3552','3555','3556','3557','3558','3562','3563','3564','3567','3570','3576','3577','3580','3581','3583','3587','3588','3591','3593','3594','3596','3605','3607','3609','3611','3615','3617','3622','3623','3624','3625','3628','3629','3630','3631','3632','3642','3645','3646','3652','3653','3661','3663','3664','3665','3666','3669','3672','3673','3675','3679','3680','3682','3684','3685','3686','3687','3689','3691','3693','3694','3698','3701','3702','3703','3704','3705','3705','3706','3707','3708','3709','3710','3711','3712','4102','4104','4105','4106','4107','4108','4109','4111','4113','4114','4116','4119','4120','4121','4123','4126','4127','4128','4129','4130','4131','4133','4137','4138','4139','4141','4142','4144','4147','4148','4152','4153','4154','4155','4157','4160','4161','4162','4163','4164','4167','4168','4171','4173','4174','4175','4183','4188','4190','4192','4198','4205','4207','4303','4304','4305','4306','4401','4402','4406','4413','4414','4415','4416','4417','4419','4420','4426','4429','4430','4432','4433','4438','4502','4503','4506','4510','4513','4523','4526','4527','4528','4529','4530','4532','4533','4534','4535','4536','4538','4540','4541','4542','4543','4545','4549','4550','4551','4552','4554','4555','4556','4557','4560','4561','4562','4563','4564','4566','4568','4572','4576','4609','4702','4706','4707','4711','4712','4714','4716','4720','4721','4722','4725','4726','4728','4729','4735','4736','4737','4739','4741','4743','4744','4745','4746','4747','4754','4755','4760','4763','4764','4766','4767','4803','4804','4806','4807','4903','4904','4905','4906','4907','4908','4909','4911','4912','4915','4916','4919','4924','4927','4930','4933','4934','4935','4938','4939','4942','4943','4944','4946','4947','4950','4952','4953','4956','4958','4960','4961','4966','4967','4968','4971','4972','4973','4974','4976','4977','4979','4987','4989','4991','4994','4995','4999','5007','5009','5011','5013','5014','5015','5016','5102','5201','5202','5203','5205','5206','5209','5210','5211','5212','5213','5215','5220','5223','5225','5227','5230','5234','5243','5245','5251','5258','5259','5263','5264','5269','5272','5274','5276','5278','5281','5283','5284','5285','5287','5288','5289','5291','5299','5301','5302','5304','5305','5306','5309','5310','5312','5314','5315','5317','5321','5324','5328','5340','5344','5345','5347','5348','5349','5351','5353','5355','5356','5364','5371','5381','5383','5386','5388','5392','5398','5403','5410','5425','5426','5432','5434','5438','5439','5443','5450','5452','5455','5457','5460','5464','5465','5468','5469','5471','5474','5475','5478','5481','5483','5484','5487','5488','5489','5490','5493','5498','5508','5511','5512','5514','5515','5516','5519','5520','5521','5522','5523','5525','5529','5530','5531','5533','5534','5536','5538','5543','5601','5603','5604','5607','5608','5609','5701','5703','5704','5706','5820','5864','5871','5876','5878','5880','5902','5903','5904','5905','5906','5907','6005','6015','6016','6020','6021','6023','6024','6026','6101','6103','6104','6108','6109','6111','6112','6113','6114','6115','6116','6117','6118','6120','6121','6122','6123','6124','6125','6126','6127','6128','6129','6130','6131','6133','6134','6136','6138','6139','6140','6141','6142','6143','6144','6146','6147','6148','6150','6151','6152','6153','6154','6155','6156','6158','6160','6161','6163','6164','6165','6166','6167','6168','6169','6170','6171','6172','6173','6174','6175','6176','6177','6179','6180','6182','6183','6184','6185','6186','6187','6188','6189','6190','6191','6192','6194','6195','6196','6197','6198','6199','6201','6202','6203','6204','6205','6206','6207','6208','6209','6210','6212','6213','6214','6215','6216','6217','6218','6219','6220','6221','6222','6223','6224','6225','6226','6227','6228','6229','6230','6231','6233','6234','6235','6236','6237','6238','6239','6240','6241','6242','6243','6244','6245','6246','6247','6248','6251','6257','6259','6261','6263','6264','6265','6266','6269','6270','6271','6274','6275','6276','6277','6278','6279','6281','6282','6283','6284','6285','6287','6288','6289','6290','6291','6292','6294','6404','6405','6409','6411','6412','6414','6415','6416','6417','6418','6419','6425','6426','6431','6432','6435','6438','6441','6442','6443','6446','6449','6451','6452','6456','6457','6461','6462','6464','6465','6469','6470','6472','6477','6482','6485','6486','6488','6492','6494','6496','6499','6504','6505','6506','6508','6509','6510','6512','6514','6516','6523','6525','6530','6531','6532','6533','6535','6538','6542','6547','6548','6552','6556','6558','6560','6561','6568','6569','6570','6573','6574','6576','6577','6578','6579','6581','6582','6589','6590','6591','6593','6594','6596','6603','6605','6609','6612','6613','6615','6616','6624','6625','6629','6640','6641','6643','6649','6654','6655','6662','6664','6666','6667','6668','6669','6670','6671','6672','6674','6679','6683','6803','7402','8011','8016','8021','8024','8027','8028','8032','8033','8034','8038','8039','8040','8042','8043','8044','8046','8047','8048','8049','8050','8054','8059','8064','8066','8067','8068','8069','8070','8071','8072','8074','8076','8077','8080','8081','8083','8084','8085','8086','8087','8088','8091','8092','8093','8096','8097','8099','8101','8103','8104','8105','8107','8109','8110','8111','8112','8114','8121','8131','8147','8150','8155','8163','8171','8176','8182','8183','8201','8210','8213','8215','8222','8234','8240','8249','8255','8261','8271','8277','8279','8287','8289','8291','8299','8341','8342','8349','8354','8358','8367','8374','8383','8390','8401','8403','8404','8406','8409','8410','8411','8415','8416','8418','8420','8421','8422','8423','8424','8426','8427','8429','8431','8432','8433','8435','8436','8437','8440','8442','8443','8444','8446','8450','8454','8455','8462','8463','8464','8466','8467','8472','8473','8476','8477','8478','8480','8481','8482','8488','8489','8497','8499','8905','8906','8908','8913','8916','8917','8921','8923','8924','8926','8927','8928','8929','8930','8931','8932','8933','8934','8935','8936','8937','8938','8940','8941','8942','8996','9103','9105','9110','9136','9802','9902','9904','9905','9906','9907','9908','9910','9910','9911','9912','9914','9917','9918','9919','9921','9924','9925','9926','9927','9928','9929','9930','9931','9933','9934','9935','9937','9938','9939','9940','9941','9942','9943','9944','9945','9946','9949','9950','9951','9955','9958','9960','9962']
    
    #每個人的最愛資料庫群組######################################
    #FavDBgroup = [StockFavs_test168, StockFavs_bobmax, StockFavs_deno36, StockFavs_donhonlin, StockFavs_goldsilver, StockFavs_hyeth, StockFavs_magicjohn, StockFavs_jonyi, StockFavs_hakkai, StockFavs_bakylews, StockFavs_chenchi, StockFavs_yuhuahsiao, StockFavs_liusnow, StockFavs_kevinlee]

    #for i in FavDBgroup:
        #favs = i.objects.all().order_by('-cStockID')  

        #for fav in favs:  #我的最愛股票資料庫
            #id_z = str(fav.cStockID)
            #StoFavIDlist.append(id_z)  #建立最愛股票清單      


    try:        
        #import random
        for c in StoFavIDlist:
            if len(StoFavIDlist) == 0:  #若名單內沒有代號，跳過
                pass
            else:
                
                #StoFav_AutoRenew(c, "1", i)  #i為寫入資料庫名稱                
                try:
                    StoFav_AutoRenew(c, DBgetMonthid)  #i為寫入資料庫名稱
                    time.sleep(random.choice([10, 11, 12, 13]))

                except:
                    try:
                        StoFav_AutoRenew(c, DBgetMonthid)  #i為寫入資料庫名稱
                        time.sleep(random.choice([10, 11, 12, 13]))
                    except:
                        pass
        #StoFavIDlist.clear() #最後，清空每個人所有最愛名單，避免重複
    except:
        pass



