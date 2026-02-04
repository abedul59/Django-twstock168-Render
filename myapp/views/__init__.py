# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 09:00:06 2022

@author: green
"""
#from myapp.models import Stock6Sign202201
#from myapp.models import Stock6Sign202202
#from myapp.models import Stock6Sign202203
#每月更新的上市 上櫃 概念股 子產業資料庫
#DB = Stock6Sign202203

# ========================================================
# 【修正重點】將 views_others 移到最上方
# 因為 UsersListAll, index, login 等重要功能都在這裡
# 這樣就算後面的檔案有缺，網站也能至少跑起來
# ========================================================
from .views_others import * # ========================================================
# 其他 Views (若 Render 上缺少對應檔案，建議先註解掉以免報錯)
# ========================================================

# 嘗試匯入其他檔案，如果檔案不存在則略過 (避免整站崩潰)
try:
    from .views_stock6 import *
    from .views_stock6DB import *
    from .views_stockPERseg import *
    from .views_monthlyAlterStuff import *
    from .views_otherDBlistall import *
    
    # 以下檔案若您沒上傳，可能會報錯，建議依實際情況保留或註解
    from .views_stock6Concepts import *
    from .views_stock6SubCats import *
    from .views_DCstock6 import *
    from .views_stock6TB import *
    from .views_stockPrice5y import *
    from .views_stock6TSE import *
    from .views_stock6OTC import *
    from .views_stockPERseg2 import *
    from .views_stockPERseg3 import *
    from .views_stockPERsegStable import *
    from .views_stockPERsegPEG import *
    from .views_StockCapGetter import *
    from .views_Epsachiever import *
    from .views_EPSnProfitGetter import *
    from .views_UsersInterface import *
    from .views_stock6listall import *
    from .views_stockPERseglistall import *
    
except ImportError as e:
    print(f"Warning: 部分 View 檔案匯入失敗，可能是檔案未上傳: {e}")
    pass
