# -*- coding: utf-8 -*-
"""
myapp/views/__init__.py
"""

# ========================================================
# 第一區：核心功能 (強制匯入，不使用 try-except)
# 這裡包含 UsersListAll, index, adminmain 等重要 View
# 如果這裡報錯，代表 views_others.py 裡面有問題 (例如缺套件或縮排錯)
# ========================================================
from .views_others import * # ========================================================
# 第二區：其他功能 (使用 try-except 避免缺檔導致崩潰)
# ========================================================
try:
    from .views_stock6 import *
    from .views_stock6DB import *
    from .views_stockPERseg import *
    from .views_monthlyAlterStuff import *
    from .views_otherDBlistall import *
    
    # 以下檔案若您沒上傳，可能會報錯，所以放在 try 裡面
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
    # 這裡會印出哪個檔案缺漏，但不會讓網站掛掉
    print(f"Warning: 部分 View 檔案匯入失敗 (非核心功能): {e}")
