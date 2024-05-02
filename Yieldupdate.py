# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 07:24:15 2021

@author: pcuser
"""

#Radar_Echo.py
from bs4 import BeautifulSoup
import requests 




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





#https://docs.djangoproject.com/en/3.2/topics/settings/
#import os
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstproject.settings')
#2021/9/13 修改
import os

try:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
except:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')



#from myapp import views, models
from module import func_usbond
from module import func_crb


if __name__ == '__main__':

    import django    
    django.setup()

    from django.contrib.auth.decorators import permission_required
    from django.views.decorators.csrf import csrf_exempt
    from django.shortcuts import render

    def viewsGetMacroWaveAdmin():  #
        #收集資料創建時間
    #from django.utils import timezone
    #wholetime = str(timezone.now()) 
    #realtime = wholetime[:16]  #取得獲取資料時間


        from myapp import models

    



        from myapp.models import MacroWaveA





        import datetime
        wholetime = str(datetime.datetime.now()) 
        #realtime = wholetime[:16]  #取得獲取資料時間
        realdate = wholetime[:10] #年月日
        
        #USBond3mYieldClose, USBond10yYieldClose = func_usbond.getUSBondYield()
        USBond3mYieldClose, USBond6mYieldClose, USBond2yYieldClose, USBond3yYieldClose, USBond5yYieldClose, USBond7yYieldClose, USBond10yYieldClose, USBond30yYieldClose = func_usbond.getUSBondYieldALL()

        CRBindex, CRBhalfyear, CRBoneyear= func_crb.getCRB()    
        #以下寫入資料庫
        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理

            #不存在，發生錯誤，跳到except            
            bond = models.MacroWaveA.objects.get(cDate=realdate)


            bond.cDate = realdate
            bond.cInvertedYieldCurve10y = USBond10yYieldClose
            bond.cInvertedYieldCurve3m = USBond3mYieldClose
            
            
            bond.cInvertedYieldCurve6m = USBond6mYieldClose        
            bond.cInvertedYieldCurve2y = USBond2yYieldClose         
            bond.cInvertedYieldCurve3y = USBond3yYieldClose
            bond.cInvertedYieldCurve5y = USBond5yYieldClose
            bond.cInvertedYieldCurve7y = USBond7yYieldClose
            bond.cInvertedYieldCurve30y = USBond30yYieldClose            
            
            
            bond.cIYC10yminus3m = str(round(float(USBond10yYieldClose) - float(USBond3mYieldClose),4))
            bond.cCRBindex = CRBindex
            bond.cCRBhalfyear = CRBhalfyear
            bond.cCRBoneyear = CRBoneyear

            bond.save()
            
            ###################


        except:  #針對沒有的股票，抓取資料存入資料庫
            #先創建7月資料，儲存
            #bond = models.MacroWaveA.objects.create(cDate=realdate, cInvertedYieldCurve10y = USBond10yYieldClose, cInvertedYieldCurve3m = USBond3mYieldClose, cIYC10yminus3m = str(round(float(USBond10yYieldClose) - float(USBond3mYieldClose),4)), cCRBindex = CRBindex, cCRBhalfyear = CRBhalfyear, cCRBoneyear = CRBoneyear)
            bond = models.MacroWaveA.objects.create(cDate=realdate, cInvertedYieldCurve10y = USBond10yYieldClose, cInvertedYieldCurve3m = USBond3mYieldClose, cIYC10yminus3m = str(round(float(USBond10yYieldClose) - float(USBond3mYieldClose),4)), cInvertedYieldCurve6m = USBond6mYieldClose,cInvertedYieldCurve2y = USBond2yYieldClose,cInvertedYieldCurve3y = USBond3yYieldClose,cInvertedYieldCurve5y = USBond5yYieldClose,cInvertedYieldCurve7y = USBond7yYieldClose,cInvertedYieldCurve30y = USBond30yYieldClose, cCRBindex = CRBindex, cCRBhalfyear = CRBhalfyear, cCRBoneyear = CRBoneyear)

            bond.save()     

    #return render(request, "viewsGetMacroWave.html", locals())
        
        
    ######################主程式
    try:
        viewsGetMacroWaveAdmin()
    except:
        try:
            viewsGetMacroWaveAdmin()
        except:
            viewsGetMacroWaveAdmin()

