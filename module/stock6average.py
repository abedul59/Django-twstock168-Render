# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 20:44:15 2020

@author: YanHua
"""

'''    
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
            average6stock = str(round(int(total)/6,1))
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
            average6stock = str(round(int(total)/5,1)) 
'''
'''
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
    average6stock = str(round(int(total)/6,1))
'''