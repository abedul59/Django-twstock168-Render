# -*- coding: utf-8 -*-
"""
Modified Yieldupdate.py for Django View Trigger
"""

from bs4 import BeautifulSoup
import requests 
import time
import pandas as pd
import os
import datetime

# 引入您的模組 (請確保 module 資料夾與 manage.py 同層級或在 Python 路徑中)
from module import func_usbond
from module import func_crb

# 引入 Django Models
# 注意：因為是被 views.py 呼叫，此時 Django App 已經載入，可以直接 import
from myapp import models
from myapp.models import MacroWaveA

# ==========================================
# 主要對外呼叫的函式
# ==========================================
def run_yield_update_task():
    print(">>> [Yieldupdate] 開始執行 MacroWaveA (債券與CRB) 更新...")
    try:
        # 嘗試執行主要邏輯
        viewsGetMacroWaveAdmin()
        print(">>> [Yieldupdate] 執行成功！")
    except Exception as e:
        # 簡單的錯誤重試邏輯 (仿照您原本的寫法)
        print(f">>> [Yieldupdate] 第一次執行失敗: {e}，嘗試重試...")
        try:
            time.sleep(2)
            viewsGetMacroWaveAdmin()
            print(">>> [Yieldupdate] 重試成功！")
        except Exception as e2:
            print(f">>> [Yieldupdate] 更新失敗 (放棄): {e2}")

# ==========================================
# 核心邏輯函式 (原本的邏輯)
# ==========================================
def viewsGetMacroWaveAdmin():  
    
    # 1. 取得時間
    wholetime = str(datetime.datetime.now()) 
    realdate = wholetime[:10] # 年月日 (例如: 2026-02-04)
    
    print(f"更新日期: {realdate}")

    # 2. 爬取數據 (呼叫外部 module)
    # 取得各天期美債殖利率
    USBond3mYieldClose, USBond6mYieldClose, USBond2yYieldClose, USBond3yYieldClose, USBond5yYieldClose, USBond7yYieldClose, USBond10yYieldClose, USBond30yYieldClose = func_usbond.getUSBondYieldALL()

    # 取得 CRB 指數
    CRBindex, CRBhalfyear, CRBoneyear = func_crb.getCRB()    

    # 3. 寫入資料庫
    try:  
        # --- 情境 A: 資料庫已有該日資料 (執行更新) ---
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
        
        # 計算 10年 - 3個月 利差
        bond.cIYC10yminus3m = str(round(float(USBond10yYieldClose) - float(USBond3mYieldClose), 4))
        
        bond.cCRBindex = CRBindex
        bond.cCRBhalfyear = CRBhalfyear
        bond.cCRBoneyear = CRBoneyear

        bond.save()
        print(f"已更新資料庫: {realdate}")

    except models.MacroWaveA.DoesNotExist:  
        # --- 情境 B: 資料庫無該日資料 (執行創建) ---
        print(f"新增資料庫紀錄: {realdate}")
        
        bond = models.MacroWaveA.objects.create(
            cDate=realdate, 
            cInvertedYieldCurve10y = USBond10yYieldClose, 
            cInvertedYieldCurve3m = USBond3mYieldClose, 
            cIYC10yminus3m = str(round(float(USBond10yYieldClose) - float(USBond3mYieldClose), 4)), 
            cInvertedYieldCurve6m = USBond6mYieldClose,
            cInvertedYieldCurve2y = USBond2yYieldClose,
            cInvertedYieldCurve3y = USBond3yYieldClose,
            cInvertedYieldCurve5y = USBond5yYieldClose,
            cInvertedYieldCurve7y = USBond7yYieldClose,
            cInvertedYieldCurve30y = USBond30yYieldClose, 
            cCRBindex = CRBindex, 
            cCRBhalfyear = CRBhalfyear, 
            cCRBoneyear = CRBoneyear
        )
        bond.save()
