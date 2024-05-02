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











    def StoFav_AutoRenew(stock_id, month_id, db_id):
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
            
            cOld2 = StockFavDB.objects.create(cStockID = stock_id,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            cOld2.save()

        

        FavDBid = db_id  #選擇寫入哪一個使用者的最愛資料庫
        #以下寫入資料庫
        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
            cOld = FavDBid.objects.get(cStockID = stock_id)

        #cOld.cItemName = Product_name
            cOld.cStockID = stock_id
            cOld.cStockName = stock_name
            cOld.cDBURL = xUrl

            cOld.cScore1st = ScoreAve1
            cOld.cScore2nd = ScoreAve2            
            cOld.cScore3rd = ScoreAve3            
            
            cOld.cPredict_EPS = Predict_EPS  
            cOld.cPredict_high_price = Predict_high_price              
            cOld.cPredict_low_price = Predict_low_price
            cOld.cNew_up_profit = New_up_profit          
            cOld.cNew_down_loss = New_down_loss    
            cOld.cRisk_reward = risk_reward 
            cOld.cTodayClose = float(yahoo_latest_tradePrice)
            #####
            cOld.cPredict_high_price_down30 = Predict_high_price_30percentDown              
            cOld.cPredict_low_price_down30 = Predict_low_price_30percentDown
            cOld.cNew_up_profit_down30 = New_up_profit2          
            cOld.cNew_down_loss_down30 = New_down_loss2    
            cOld.cRisk_reward_down30 = New_risk_reward
            #####            
            cOld.pubtime =realtime      


            try:
                #epsach = EPSachieve2021Q3.objects.get(cStockID = mess)
                print("test1")
                epsach = DBEPSAz.objects.get(cStockID = stock_id)
                print("test2")
                #cOld.cEPSach = str(epsach.cEPSAchieveRate)

                if len(str(epsach.cEPSAchieveRate)) > 4:
                    cOld.cEPSach = str(epsach.cEPSAchieveRate)[:5] + "%"
                else:
                    cOld.cEPSach = str(epsach.cEPSAchieveRate)
                    
            
            except:
                cOld.cEPSach = "No"
                
            print("EPS達成率：")
            print(str(cOld.cEPSach))
            ########################################
            try:
                #stacap = StockCapVar2021Q4.objects.get(cStockID = mess)
                stacap = DBCAPz.objects.get(cStockID = stock_id)
            
                cOld.cStCap = str(stacap.cLatestMoM)
            
            except:
                cOld.cStCap = "No"
                
            print("股本變動率：")
            print(str(cOld.cStCap))

            ###########################################                
            try:
                #epsprf = EpsProfit2021Q4.objects.get(cStockID = mess)
                epsprf = DBEPSNz.objects.get(cStockID = stock_id)
            
                cOld.cEPSnPrf = "Yes"
            
            except:
                cOld.cEPSnPrf = "No"                
                
            print("EPS或營益率創八季新高：")
            print(str(cOld.cEPSnPrf))
            
            try:
                #stab = StockPERsegStable2021Q4.objects.get(cStockID = mess)
                stab = DBSTABz.objects.get(cStockID = stock_id)
            
                cOld.cPERstab = "Yes"
            except:
                cOld.cPERstab = "No"

            print("本益比區間變動率在30%內：")
            print(str(cOld.cPERstab))
                 
            cOld.save()
            
            ###################
        except:  #針對沒有的，抓取資料存入資料庫

            #cOld = FavDBid.objects.create(cStockID = stock_id,cStockName = stock_name,cDBURL = xUrl,cScore1st = ScoreAve1,cScore2nd = ScoreAve2,cScore3rd = ScoreAve3,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              
            cOld = FavDBid.objects.create(cStockID = stock_id,cStockName = stock_name,cDBURL = xUrl,cScore1st = ScoreAve1,cScore2nd = ScoreAve2,cScore3rd = ScoreAve3,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice), cPredict_high_price_down30 = Predict_high_price_30percentDown, cPredict_low_price_down30 = Predict_low_price_30percentDown, cNew_up_profit_down30 = New_up_profit2, cNew_down_loss_down30 = New_down_loss2, cRisk_reward_down30 = New_risk_reward, pubtime =realtime)              




            cOld.save()
            
            try:
                #epsach = EPSachieve2021Q3.objects.get(cStockID = mess)
                epsach = DBEPSAz.objects.get(cStockID = stock_id)            
                #cOld.cEPSach = str(epsach.cEPSAchieveRate)

                if len(str(epsach.cEPSAchieveRate)) > 4:
                    cOld.cEPSach = str(epsach.cEPSAchieveRate)[:5] + "%"
                else:
                    cOld.cEPSach = str(epsach.cEPSAchieveRate)
                    
            
            except:
                cOld.cEPSach = "No"
                
            print("EPS達成率：")
            print(str(cOld.cEPSach))
            ########################################
            try:
                #stacap = StockCapVar2021Q4.objects.get(cStockID = mess)
                stacap = DBCAPz.objects.get(cStockID = stock_id)
            
                cOld.cStCap = str(stacap.cLatestMoM)
            
            except:
                cOld.cStCap = "No"
            ###########################################                
            try:
                #epsprf = EpsProfit2021Q4.objects.get(cStockID = mess)
                epsprf = DBEPSNz.objects.get(cStockID = stock_id)
            
                cOld.cEPSnPrf = "Yes"
            
            except:
                cOld.cEPSnPrf = "No"                
                
            
            try:
                #stab = StockPERsegStable2021Q4.objects.get(cStockID = mess)
                stab = DBSTABz.objects.get(cStockID = stock_id)
            
                cOld.cPERstab = "Yes"
            except:
                cOld.cPERstab = "No"
            
            cOld.save()
###############################################################################




    
    def PERseg_check(stock_id):

        django.setup()   #擺在os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'costcobot168.settings')之後，才不會有問題。
        import datetime

        from myapp.models import StockPERseg202107
        from myapp.models import Stock6Sign202107
        from myapp.models import StockPERseg202108
        from myapp.models import Stock6Sign202108
        from myapp.models import StockPERseg202110
        from myapp.models import Stock6Sign202110
        from myapp.models import StockPERseg202111
        from myapp.models import Stock6Sign202111
        from myapp.models import StockPERseg202112
        from myapp.models import Stock6Sign202112
        from myapp.models import StockPERseg202201
        from myapp.models import Stock6Sign202201
        from myapp.models import StockPERseg202202
        from myapp.models import Stock6Sign202202
        from myapp.models import StockPERseg202203
        from myapp.models import Stock6Sign202203
        from myapp.models import StockPERseg202204
        from myapp.models import Stock6Sign202204
        from myapp.models import StockFavDB






        bank_url2 = 'https://goodinfo.tw/StockInfo/DayTrading.asp?STOCK_ID=' 
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
        url = bank_url2 + stock_id
        r = requests.post(url, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        table = soup.find_all('table');
        dfs = pd.read_html(str(table))        

#    yahoo_tradePrice = dfs[0][3] #yahoo成交價
#    yahoo_time= dfs[0][0] #yahoo成交時間
        yahoo_latest_tradePrice = float(dfs[-2].iloc[0].iloc[1]) #goodinfo最新成交價
        #float(dfs[0][3][6]) #yahoo最新成交價

#    yahoo_latest_time = dfs[0][0][6] #yahoo最新成交時間    
        #print("結束getYahooPrice函式！")
        #return yahoo_latest_tradePrice

        #return Product_name, url, itemState, ItemNumber2, buttonType, quantity_atmost
###

            ########################以下資料庫舊時間####################

        #try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
        #cOld = StockPERseg202203.objects.get(cStockID=stock_id)
        
        cOld = DBPERz.objects.get(cStockID=stock_id)
        
        cOld2 = DBz.objects.get(cStockID=stock_id)  

        oldAveScore = float(cOld2.cAverageScore)          
            
        str1 = str(cOld.pubtime)  #"2021年7月20日 11:02"

        hour = str1[-5:-3]
        minute = str1[-2:]

        day = str1[-9:-7]
            #print(day)

        newTime = int(hour + minute)

            #print(int(newTime)) 
           ######################################以下新時間      
        #收集資料創建時間
        import datetime
        wholetime = str(datetime.datetime.now()) 
        realtime = wholetime[:16]  #取得獲取資料時間

        str2 = realtime  #"2021年7月20日 11:02"

        hour2 = str2[-5:-3]
        minute2 = str2[-2:]

        day2 = str2[-9:-7]
            #print(day)

        newTime2 = int(hour2 + minute2)

            #print(int(newTime))

        try:
            oldPrice = str(cOld.cLatest_price)

            oldPredict_high_price = float(cOld.cPredict_high_price)
            oldPredict_low_price = float(cOld.cPredict_low_price)  
        #oldUp_profit = float(cOld.cNew_up_profit)
        #oldDown_loss = float(cOld.cNew_down_loss)

            oldRisk_reward = str(cOld.cRisk_reward)
        #########################################        
            newPrice = float(yahoo_latest_tradePrice)
        
            newUp_profit = abs(round((oldPredict_high_price - newPrice)/newPrice,4))      
            newDown_loss = abs(round((newPrice - oldPredict_low_price)/newPrice,4))       
            
            newRisk_reward = str(round(newUp_profit/newDown_loss,2)) #新風險報酬倍數


            priceGapUP = float(newPrice) - float(oldPrice) #漲價價差
            priceGapDOWN = float(oldPrice) - float(newPrice) #降價價差        


    
            stock_name = str(cOld.cStockName)
        except:
            pass
        
        if newTime2 > newTime:
            if float(newRisk_reward) >= 2.66:
                riskRewardOver266[stock_name] = {"股票代碼":str(stock_id), "目前價格":newPrice, "資料庫價格":oldPrice, "舊風險報酬倍數":oldRisk_reward, "新風險報酬倍數":newRisk_reward}

            if 1 <= float(newRisk_reward) < 2.66:
                riskReward1to266[stock_name] = {"股票代碼":str(stock_id), "目前價格":newPrice, "資料庫價格":oldPrice, "舊風險報酬倍數":oldRisk_reward, "新風險報酬倍數":newRisk_reward}
             
            elif float(newPrice) - float(oldPrice) > 0:
                print("股票價格走高了唷！以下股票：")
                print("股票代碼：" + str(stock_id) + "；" + "股票名稱：" + str(stock_name))

                priceGapUPDict[stock_name] = {"股票代碼":str(stock_id), "目前價格":newPrice, "正價差":priceGapUP, "舊風險報酬倍數":oldRisk_reward, "新風險報酬倍數":newRisk_reward}

                print("股票價格漲了" + str(priceGapUP) + "元！")

            elif float(oldPrice) - float(newPrice) > 0:
                print("股票價格調降了唷！以下股票：")
                print("股票代碼：" + str(stock_id) + "；" + "股票名稱：" + str(stock_name))

                priceGapDOWNDict[stock_name] = {"股票代碼":str(stock_id), "目前價格":newPrice, "負價差":priceGapDOWN, "舊風險報酬倍數":oldRisk_reward, "新風險報酬倍數":newRisk_reward}

                print("股票價格降了" + str(priceGapDOWN) + "元！")                
                
            else:
                print("股票價格不變。以下股票：")
                print("股票代碼：" + str(stock_id) + "；" + "股票名稱：" + str(stock_name))

                SameList2.append(stock_name)

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
    import random
    #每個人的最愛股票代號
    StoFavIDlist = []
    
    #每個人的最愛資料庫群組######################################
    FavDBgroup = [StockFavs_test168, StockFavs_bobmax, StockFavs_deno36, StockFavs_donhonlin, StockFavs_goldsilver, StockFavs_hyeth, StockFavs_magicjohn, StockFavs_jonyi, StockFavs_hakkai, StockFavs_bakylews, StockFavs_chenchi, StockFavs_yuhuahsiao, StockFavs_liusnow, StockFavs_kevinlee]

    for i in FavDBgroup:
        favs = i.objects.all().order_by('-cStockID')  

        for fav in favs:  #我的最愛股票資料庫
            id_z = str(fav.cStockID)
            StoFavIDlist.append(id_z)  #建立最愛股票清單      


        
        #import random
        for c in StoFavIDlist:
            if len(StoFavIDlist) == 0:  #若名單內沒有代號，跳過
                pass
            else:
                
                #StoFav_AutoRenew(c, "1", i)  #i為寫入資料庫名稱                
                StoFav_AutoRenew(c, DBgetMonthid, i)  #i為寫入資料庫名稱
                time.sleep(random.choice([10, 11, 12, 13]))
        
        StoFavIDlist.clear() #最後，清空每個人所有最愛名單，避免重複


'''
########################################################################
    ###第二個主程式開始#####################################
    stockIDlist0 = []    #segs     
    stockIDlist = []  #cOlds


    from myapp.models import StockPERseg202108
    from myapp.models import Stock6Sign202108
    from myapp.models import StockPERseg202110
    from myapp.models import Stock6Sign202110
    from myapp.models import StockPERseg202111
    from myapp.models import Stock6Sign202111
    from myapp.models import StockPERseg202112
    from myapp.models import Stock6Sign202112 

    from myapp.models import StockPERseg202201
    from myapp.models import Stock6Sign202201     
    from myapp.models import StockPERseg202202
    from myapp.models import Stock6Sign202202
    from myapp.models import StockPERseg202202
    from myapp.models import Stock6Sign202202



    #from myapp import views
    #from .views_monthlyAlterStuff import NowTimeDBs 


    DBv = NowTimeDBs()  #從views_monthlyAlterStuff.py取得每月需要的資料庫變數

    DBv.getRightDB()  #Stock6Sgin
    DBv.getRightPERDB() #StockPERseg


    DBz = DBv.z  #每個月的主要資料庫  #y= 上個月 x = 上上個月
    DBy = DBv.y
    DBx = DBv.x


    DBPERz = DBv.PERz  #每個月的主要資料庫  #y= 上個月 x = 上上個月
    DBPERy = DBv.PERy
    DBPERx = DBv.PERx
    
    

    #segs = StockPERseg202203.objects.all().order_by('-cStockID') 
    segs = DBPERz.objects.all().order_by('-cStockID')  
    
    cOlds = DBz.objects.all().order_by('-cAverageScore')






    for seg in segs:  #segs的所有代號
        id_z = str(seg.cStockID)
        stockIDlist0.append(id_z)
        


    
    for cOld in cOlds:  #cOlds所有代號
        id_s = str(cOld.cStockID)
        if id_s not in stockIDlist0:
            continue
        
        elif float(cOld.cAverageScore) >= 3:
            stockIDlist.append(id_s)
            print(id_s)
        
    import random
    for c in stockIDlist:
        PERseg_check(c)
        time.sleep(random.choice([3, 4, 5, 6]))
        

        

        
    print("完成。最後價格調漲股票總名單：")
    print(str(priceGapUPDict))

    if len(priceGapUPDict) == 0:
        priceGapUPDict = "無"


    print("完成。最後價格調降股票總名單：")
    print(str(priceGapDOWNDict))


    if len(priceGapDOWNDict) == 0:
        priceGapDOWNDict = "無"

    print("完成。最後價格不變股票總名單：")
    print(str(SameList2))

    if len(SameList2) == 0:
        SameList2 = "無"


    import datetime
    wholetime = str(datetime.datetime.now()) 
    realtime = wholetime[:16]  #取得獲取資料時間

    MailContent = "調查時間：" + realtime + "。" + "新風險報酬倍數超過2.66的股票清單：" + str(riskRewardOver266) + "。"+ "新風險報酬倍數位於1至2.66之間的股票清單：" + str(riskReward1to266) + "。" 
    #+ "價格走高股票名單：" + str(priceGapUPDict) + "。"  + "價格降低股票名單（股票名稱:降低價差）：" + str(priceGapDOWNDict)+ "。"   + "價格不變股票名單：" + str(SameList2)+ "。"              
                   
    fromEmail = 'pyfbsdk59@gmail.com'
    toEmailList = ['twstock168.service@gmail.com']

    email = EmailMessage(
            '訂閱者新通知功能測試中！ 2022/10 六大指標3分以上股票 即時價格和風險報酬倍數 變動情況' + realtime,
            MailContent,
            fromEmail,
            toEmailList,
            )
            
    email.send()
    
    ############################
'''
