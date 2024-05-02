# -*- coding: utf-8 -*-

'''
import csv

with open('PERseg.csv', 'w', newline='') as csvfile:
    
    writer = csv.writer(csvfile)
    
    writer.writerow(['股票代號','H1','L1'])
    writer.writerow(['2002','22','7'])    
    writer.writerow(['2330','234','176'])    
'''

import csv

with open('../static/csv/PERseg.csv', newline='') as csvfile:
    
    rows = csv.reader(csvfile)
    for row in rows:
        H1 = row

        #print(K1)


    list(H1)
    H2 = H1[1]
    print(H2)


'''
import pandas as pd # 引用套件並縮寫為 pd  
df = pd.read_csv('PERseg.csv')  
#print(df) 

H1 = df.iloc[1][1]
H2 = df.iloc[1][2]
print(H1)
print(H2)
'''

