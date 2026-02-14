# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 17:31:29 2021
@author: pcuser
"""

import random
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from decimal import Decimal, ROUND_HALF_UP

#from func3_eps import EPS_quarterlyGetter

a = 'https://www.google.com.tw'
b = 'https://tw.yahoo.com'
c = 'https://www.pchome.com.tw/'
d = 'https://djinfo.cathaysec.com.tw/'

my_Referer = random.choice([a,b,c,d])

my_UserAgent = 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'

# 完整股票清單 (請勿刪除，確保變數存在)
TSEAll = ['1101','1102','1103','1104','1108','1109','1110','1201','1203','1210','1213','1215','1216','1217','1218','1219','1220','1225','1227','1229','1231','1232','1233','1234','1235','1236','1256','1301','1303','1304','1305','1307','1308','1309','1310','1312','1313','1314','1315','1316','1319','1321','1323','1324','1325','1326','1337','1338','1339','1340','1341','1402','1409','1410','1413','1414','1416','1417','1418','1419','1423','1432','1434','1435','1436','1437','1438','1439','1440','1441','1442','1443','1444','1445','1446','1447','1449','1451','1452','1453','1454','1455','1456','1457','1459','1460','1463','1464','1465','1466','1467','1468','1470','1471','1472','1473','1474','1475','1476','1477','1503','1504','1506','1507','1512','1513','1514','1515','1516','1517','1519','1521','1522','1524','1525','1526','1527','1528','1529','1530','1531','1532','1533','1535','1536','1537','1538','1539','1540','1541','1558','1560','1568','1582','1583','1587','1589','1590','1592','1598','1603','1604','1605','1608','1609','1611','1612','1614','1615','1616','1617','1618','1626','1701','1702','1707','1708','1709','1710','1711','1712','1713','1714','1717','1718','1720','1721','1722','1723','1724','1725','1726','1727','1730','1731','1732','1733','1734','1735','1736','1737','1760','1762','1773','1776','1783','1786','1789','1795','1802','1805','1806','1808','1809','1810','1817','1903','1904','1905','1906','1907','1909','2002','2006','2007','2008','2009','2010','2012','2013','2014','2015','2017','2020','2022','2023','2024','2025','2027','2028','2029','2030','2031','2032','2033','2034','2038','2049','2059','2062','2069','2101','2102','2103','2104','2105','2106','2107','2108','2109','2114','2115','2201','2204','2206','2207','2208','2227','2228','2231','2233','2236','2239','2241','2243','2247','2301','2302','2303','2305','2308','2312','2313','2314','2316','2317','2321','2323','2324','2327','2328','2329','2330','2331','2332','2337','2338','2340','2342','2344','2345','2347','2348','2349','2351','2352','2353','2354','2355','2356','2357','2358','2359','2360','2362','2363','2364','2365','2367','2368','2369','2371','2373','2374','2375','2376','2377','2379','2380','2382','2383','2385','2387','2388','2390','2392','2393','2395','2397','2399','2401','2402','2404','2405','2406','2408','2409','2412','2413','2414','2415','2417','2419','2420','2421','2423','2424','2425','2426','2427','2428','2429','2430','2431','2433','2434','2436','2438','2439','2440','2441','2442','2443','2444','2448','2449','2450','2451','2453','2454','2455','2456','2457','2458','2459','2460','2461','2462','2464','2465','2466','2467','2468','2471','2472','2474','2476','2477','2478','2480','2481','2482','2483','2484','2485','2486','2488','2489','2491','2492','2493','2495','2496','2497','2498','2499','2501','2504','2505','2506','2509','2511','2514','2515','2516','2520','2524','2527','2528','2530','2534','2535','2536','2537','2538','2539','2540','2542','2543','2545','2546','2547','2548','2597','2601','2603','2605','2606','2607','2608','2609','2610','2611','2612','2613','2614','2615','2616','2617','2618','2630','2633','2634','2636','2637','2642','2701','2702','2704','2705','2706','2707','2712','2722','2723','2727','2731','2739','2748','2801','2809','2812','2816','2820','2823','2832','2834','2836','2838','2841','2845','2849','2850','2851','2852','2855','2867','2880','2881','2882','2883','2884','2885','2886','2887','2888','2889','2890','2891','2892','2897','2901','2903','2904','2905','2906','2908','2910','2911','2912','2913','2915','2923','2929','2936','2939','3002','3003','3004','3005','3006','3008','3010','3011','3013','3014','3015','3016','3017','3018','3019','3021','3022','3023','3024','3025','3026','3027','3028','3029','3030','3031','3032','3033','3034','3035','3036','3037','3038','3040','3041','3042','3043','3044','3045','3046','3047','3048','3049','3050','3051','3052','3054','3055','3056','3057','3058','3059','3060','3062','3090','3094','3130','3149','3164','3167','3189','3209','3229','3231','3257','3266','3296','3305','3308','3311','3312','3321','3338','3346','3356','3376','3380','3383','3406','3413','3416','3419','3432','3437','3443','3450','3454','3481','3494','3501','3504','3515','3518','3528','3530','3532','3533','3535','3536','3543','3545','3550','3557','3563','3576','3583','3588','3591','3593','3596','3605','3607','3617','3622','3645','3653','3661','3665','3669','3673','3679','3682','3686','3694','3698','3701','3702','3703','3704','3705','3706','3708','3711','3712','4104','4106','4108','4119','4133','4137','4141','4142','4148','4155','4164','4190','4306','4414','4426','4438','4439','4526','4532','4536','4540','4545','4551','4552','4555','4557','4560','4562','4564','4566','4571','4572','4576','4581','4720','4722','4725','4737','4739','4746','4755','4763','4764','4766','4807','4904','4906','4912','4915','4916','4919','4927','4930','4934','4935','4938','4942','4943','4952','4956','4958','4960','4961','4967','4968','4976','4977','4989','4994','4999','5007','5203','5215','5225','5234','5243','5258','5264','5269','5283','5284','5285','5288','5305','5388','5434','5469','5471','5484','5515','5519','5521','5522','5525','5531','5533','5534','5538','5546','5607','5608','5706','5871','5876','5880','5906','5907','6005','6024','6108','6112','6115','6116','6117','6120','6128','6131','6133','6136','6139','6141','6142','6152','6153','6155','6164','6165','6166','6168','6172','6176','6177','6183','6184','6189','6191','6192','6196','6197','6201','6202','6205','6206','6209','6213','6214','6215','6216','6224','6225','6226','6230','6235','6239','6243','6251','6257','6269','6271','6277','6278','6281','6282','6283','6285','6288','6289','6405','6409','6412','6414','6415','6416','6431','6442','6443','6449','6451','6456','6464','6477','6491','6504','6505','6525','6531','6533','6541','6552','6558','6573','6579','6581','6582','6591','6592','6598','6605','6625','6641','6655','6666','6668','6669','6670','6671','6672','6674','6698','6706','6715','6754','8011','8016','8021','8028','8033','8039','8046','8070','8072','8081','8101','8103','8104','8105','8110','8112','8114','8131','8150','8163','8201','8210','8213','8215','8222','8249','8261','8271','8341','8367','8374','8404','8411','8422','8427','8429','8442','8443','8454','8462','8463','8464','8466','8467','8473','8478','8480','8481','8482','8488','8499','8926','8940','8996','9105','912000','912398','9802','9902','9904','9905','9906','9907','9908','9910','9911','9912','9914','9917','9918','9919','9921','9924','9925','9926','9927','9928','9929','9930','9931','9933','9934','9935','9937','9938','9939','9940','9941','9942','9943','9944','9945','9946','9955','9958']
OTCAll = ['1240','1258','1259','1264','1268','1333','1336','1565','1569','1570','1580','1584','1586','1591','1593','1595','1597','1599','1742','1752','1777','1781','1784','1785','1788','1796','1799','1813','1815','2035','2061','2063','2064','2065','2066','2067','2070','2221','2230','2235','2596','2640','2641','2643','2718','2719','2724','2726','2729','2732','2734','2736','2740','2743','2745','2752','2754','2916','2924','2926','2928','2937','3064','3066','3067','3071','3073','3078','3081','3083','3085','3086','3088','3089','3092','3093','3095','3105','3114','3115','3118','3122','3128','3131','3141','3144','3147','3152','3162','3163','3169','3171','3176','3178','3188','3191','3202','3205','3206','3207','3211','3213','3217','3218','3219','3221','3224','3226','3227','3228','3230','3232','3234','3236','3252','3259','3260','3264','3265','3268','3272','3276','3284','3285','3287','3288','3289','3290','3293','3294','3297','3303','3306','3310','3313','3317','3322','3323','3324','3325','3332','3339','3354','3360','3362','3363','3372','3373','3374','3379','3388','3390','3402','3426','3434','3438','3441','3444','3455','3465','3466','3479','3483','3484','3489','3490','3491','3492','3498','3499','3508','3511','3512','3516','3520','3521','3522','3523','3526','3527','3529','3531','3537','3540','3541','3546','3548','3551','3552','3555','3556','3558','3564','3567','3570','3577','3580','3581','3587','3594','3597','3609','3611','3615','3623','3624','3625','3628','3629','3630','3631','3632','3642','3646','3652','3663','3664','3666','3672','3675','3680','3684','3685','3687','3689','3691','3693','3707','3709','3710','3713','4102','4105','4107','4109','4111','4113','4114','4116','4120','4121','4123','4126','4127','4128','4129','4130','4131','4138','4139','4147','4152','4153','4154','4157','4160','4161','4162','4163','4167','4168','4171','4173','4174','4175','4183','4188','4192','4198','4205','4207','4303','4304','4305','4401','4402','4406','4413','4416','4417','4419','4420','4429','4430','4432','4433','4502','4503','4506','4510','4513','4523','4527','4528','4529','4530','4533','4534','4535','4538','4541','4542','4543','4549','4550','4554','4556','4561','4563','4568','4580','4609','4702','4706','4707','4711','4712','4714','4716','4721','4726','4728','4729','4735','4736','4741','4743','4744','4745','4747','4754','4760','4767','4803','4804','4806','4903','4905','4907','4908','4909','4911','4924','4931','4933','4939','4944','4946','4950','4953','4966','4971','4972','4973','4974','4979','4987','4991','4995','5009','5011','5013','5014','5015','5016','5102','5201','5202','5205','5206','5209','5210','5211','5212','5213','5220','5223','5227','5230','5245','5251','5263','5272','5274','5276','5278','5281','5287','5289','5291','5299','5301','5302','5304','5306','5309','5310','5312','5314','5315','5321','5324','5328','5340','5344','5345','5347','5348','5351','5353','5355','5356','5364','5371','5381','5383','5386','5392','5398','5403','5410','5425','5426','5432','5438','5439','5443','5450','5452','5455','5457','5460','5464','5465','5468','5474','5475','5478','5481','5483','5487','5488','5489','5490','5493','5498','5508','5511','5512','5514','5516','5520','5523','5529','5530','5536','5543','5601','5603','5604','5609','5701','5703','5704','5820','5864','5878','5902','5903','5904','5905','6015','6016','6020','6021','6023','6026','6101','6103','6104','6109','6111','6113','6114','6118','6121','6122','6123','6124','6125','6126','6127','6129','6130','6134','6138','6140','6143','6144','6146','6147','6148','6150','6151','6154','6156','6158','6160','6161','6163','6167','6169','6170','6171','6173','6174','6175','6179','6180','6182','6185','6186','6187','6188','6190','6194','6195','6198','6199','6203','6204','6207','6208','6210','6212','6217','6218','6219','6220','6221','6222','6223','6227','6228','6229','6231','6233','6234','6236','6237','6240','6241','6242','6244','6245','6246','6247','6248','6259','6261','6263','6264','6265','6266','6270','6274','6275','6276','6279','6284','6287','6290','6291','6292','6294','6404','6411','6417','6418','6419','6425','6426','6432','6435','6438','6441','6446','6457','6461','6462','6465','6469','6470','6472','6482','6485','6486','6488','6492','6494','6496','6499','6506','6508','6509','6510','6512','6514','6516','6523','6527','6530','6532','6535','6538','6542','6547','6548','6556','6560','6561','6568','6569','6570','6574','6576','6577','6578','6588','6589','6590','6593','6594','6596','6603','6609','6612','6613','6615','6616','6624','6629','6640','6642','6643','6649','6654','6662','6664','6667','6679','6680','6683','6690','6697','6703','6716','6732','6803','7402','7556','8024','8027','8032','8034','8038','8040','8042','8043','8044','8047','8048','8049','8050','8054','8059','8064','8066','8067','8068','8069','8071','8074','8076','8077','8080','8083','8084','8085','8086','8087','8088','8089','8091','8092','8093','8096','8097','8099','8107','8109','8111','8121','8147','8155','8171','8176','8182','8183','8234','8240','8255','8277','8279','8284','8289','8291','8299','8342','8349','8354','8358','8383','8390','8401','8403','8406','8409','8410','8415','8416','8418','8420','8421','8423','8424','8426','8431','8432','8433','8435','8436','8437','8440','8444','8446','8450','8455','8472','8476','8477','8489','8905','8906','8908','8916','8917','8921','8923','8924','8927','8928','8929','8930','8931','8932','8933','8934','8935','8936','8937','8938','8941','8942','9949','9950','9951','9960','9962']
Allcompany = TSEAll + OTCAll # 合併列表

#PERsegx
#############################################################以下為本益比區間程式
def PERsegx(stock_id, month_id):
    headers = {'Referer': my_Referer ,'user-agent': my_UserAgent}
    ######以下為判斷上市或上櫃，取得年度股價程式
    import pandas as pd 
    import requests
    from bs4 import BeautifulSoup    

    # 【重要】初始化所有變數，避免 UnboundLocalError
    H0=H1=H2=H3=H4=H5=H6 = 0.0
    L0=L1=L2=L3=L4=L5=L6 = 0.0
    ls0=ls1=ls2=ls3=ls4=ls5=ls6 = None
    eps1N = ""
    eps1=eps2=eps3=eps4=eps5=eps6 = 0.0 # 初始化 EPS 變數

    if stock_id in TSEAll:  #查詢上市年股價
    #try:  #查詢上市年股價 （先上市，有些股票會上櫃轉上市，但上櫃還會留下資料，會抓錯。）
        twse_url = 'http://www.twse.com.tw/exchangeReport/FMNPTK?response=html&stockNo=' #國泰世華
        url = twse_url + stock_id 
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        table = soup.find_all('table')[0];
        dfs = pd.read_html(str(table))


        #2021/12/31 欄位已改變 12/30最後交易日 2024/1/9修改
        ls1  = dfs[0].iloc[-1] #2023/112年
        ls2  = dfs[0].iloc[-2] #2022/111年
        ls3  = dfs[0].iloc[-3] #110年
        ls4  = dfs[0].iloc[-4] #109年
        ls5  = dfs[0].iloc[-5] #108年
        ls6  = dfs[0].iloc[-6] #107年        

        H1 = ls1[4] #112年最高價
        L1 = ls1[6] #112年最低價

        H2 = ls2[4] #2021/111年最高價
        L2 = ls2[6] #111年最低價

        H3 = ls3[4] #110年最高價
        L3 = ls3[6] #110年最低價

        H4 = ls4[4] #109年最高價
        L4 = ls4[6] #109年最低價

        H5 = ls5[4] #108年最高價
        L5 = ls5[6] #108年最低價

        H6 = ls6[4] #107年最高價
        L6 = ls6[6] #107年最低價


        print(H1)
        #print(L5)
              
        ##抓取上市今年最高價 一個月一個月抓，再算最大值
        twse_url2 = 'http://www.twse.com.tw/exchangeReport/FMSRFK?response=html&stockNo=' 
        url = twse_url2 + stock_id 
        r2 = requests.get(url, headers=headers)
        soup2 = BeautifulSoup(r2.content, 'lxml')
        table2 = soup2.find_all('table')[0];
        dfs2 = pd.read_html(str(table2))

        monthlen = len(dfs2[0]) #計算有幾個欄位（幾個月份）
        
        print(monthlen)
    #dfs[0].iloc[m-1] #109年1月
        priceGroup = []

        if monthlen == 1 :   ##不分流會發生錯誤#20210201
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)
            print(lm1)
        elif monthlen == 2 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)
            #print(lm1)        
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)
            #print(lm2)        
        elif monthlen == 3 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)        
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)           
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3)        
        elif monthlen == 4 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)        
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)           
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
        elif monthlen == 5 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)        
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)           
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
            lm5  = dfs2[0].iloc[int(monthlen)-5][2] #110年最新的5個月最高價
            priceGroup.append(lm5)
        elif monthlen == 6 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)        
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)           
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
            lm5  = dfs2[0].iloc[int(monthlen)-5][2] #110年最新的5個月最高價
            priceGroup.append(lm5)
            lm6  = dfs2[0].iloc[int(monthlen)-6][2] #110年最新的6個月最高價
            priceGroup.append(lm6)
        elif monthlen == 7 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)        
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)           
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
            lm5  = dfs2[0].iloc[int(monthlen)-5][2] #110年最新的5個月最高價
            priceGroup.append(lm5)
            lm6  = dfs2[0].iloc[int(monthlen)-6][2] #110年最新的6個月最高價
            priceGroup.append(lm6)
            lm7  = dfs2[0].iloc[int(monthlen)-7][2] #110年最新的7個月最高價
            priceGroup.append(lm7)
        elif monthlen == 8 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)        
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)           
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
            lm5  = dfs2[0].iloc[int(monthlen)-5][2] #110年最新的5個月最高價
            priceGroup.append(lm5)
            lm6  = dfs2[0].iloc[int(monthlen)-6][2] #110年最新的6個月最高價
            priceGroup.append(lm6)
            lm7  = dfs2[0].iloc[int(monthlen)-7][2] #110年最新的7個月最高價
            priceGroup.append(lm7)
            lm8  = dfs2[0].iloc[int(monthlen)-8][2] #110年最新的8個月最高價
            priceGroup.append(lm8)

        elif monthlen == 9 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)        
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)           
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
            lm5  = dfs2[0].iloc[int(monthlen)-5][2] #110年最新的5個月最高價
            priceGroup.append(lm5)
            lm6  = dfs2[0].iloc[int(monthlen)-6][2] #110年最新的6個月最高價
            priceGroup.append(lm6)
            lm7  = dfs2[0].iloc[int(monthlen)-7][2] #110年最新的7個月最高價
            priceGroup.append(lm7)
            lm8  = dfs2[0].iloc[int(monthlen)-8][2] #110年最新的8個月最高價
            priceGroup.append(lm8)
            lm9  = dfs2[0].iloc[int(monthlen)-9][2] #110年最新的9個月最高價
            priceGroup.append(lm9)

        elif monthlen == 10 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)        
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)           
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
            lm5  = dfs2[0].iloc[int(monthlen)-5][2] #110年最新的5個月最高價
            priceGroup.append(lm5)
            lm6  = dfs2[0].iloc[int(monthlen)-6][2] #110年最新的6個月最高價
            priceGroup.append(lm6)
            lm7  = dfs2[0].iloc[int(monthlen)-7][2] #110年最新的7個月最高價
            priceGroup.append(lm7)
            lm8  = dfs2[0].iloc[int(monthlen)-8][2] #110年最新的8個月最高價
            priceGroup.append(lm8)
            lm9  = dfs2[0].iloc[int(monthlen)-9][2] #110年最新的9個月最高價
            priceGroup.append(lm9)
            lm10  = dfs2[0].iloc[int(monthlen)-10][2] #110年最新的10個月最高價
            priceGroup.append(lm10)
        elif monthlen == 11 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)        
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)           
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
            lm5  = dfs2[0].iloc[int(monthlen)-5][2] #110年最新的5個月最高價
            priceGroup.append(lm5)
            lm6  = dfs2[0].iloc[int(monthlen)-6][2] #110年最新的6個月最高價
            priceGroup.append(lm6)
            lm7  = dfs2[0].iloc[int(monthlen)-7][2] #110年最新的7個月最高價
            priceGroup.append(lm7)
            lm8  = dfs2[0].iloc[int(monthlen)-8][2] #110年最新的8個月最高價
            priceGroup.append(lm8)
            lm9  = dfs2[0].iloc[int(monthlen)-9][2] #110年最新的9個月最高價
            priceGroup.append(lm9)
            lm10  = dfs2[0].iloc[int(monthlen)-10][2] #110年最新的10個月最高價
            priceGroup.append(lm10)
            lm11  = dfs2[0].iloc[int(monthlen)-11][2] #110年最新的11個月最高價
            priceGroup.append(lm11)
        elif monthlen == 12 :
            lm1  = dfs2[0].iloc[int(monthlen)-1][2] #110年最新的1個月最高價
            priceGroup.append(lm1)        
            lm2  = dfs2[0].iloc[int(monthlen)-2][2] #110年最新的2個月最高價
            priceGroup.append(lm2)           
            lm3  = dfs2[0].iloc[int(monthlen)-3][2] #110年最新的3個月最高價
            priceGroup.append(lm3) 
            lm4  = dfs2[0].iloc[int(monthlen)-4][2] #110年最新的4個月最高價
            priceGroup.append(lm4)
            lm5  = dfs2[0].iloc[int(monthlen)-5][2] #110年最新的5個月最高價
            priceGroup.append(lm5)
            lm6  = dfs2[0].iloc[int(monthlen)-6][2] #110年最新的6個月最高價
            priceGroup.append(lm6)
            lm7  = dfs2[0].iloc[int(monthlen)-7][2] #110年最新的7個月最高價
            priceGroup.append(lm7)
            lm8  = dfs2[0].iloc[int(monthlen)-8][2] #110年最新的8個月最高價
            priceGroup.append(lm8)
            lm9  = dfs2[0].iloc[int(monthlen)-9][2] #110年最新的9個月最高價
            priceGroup.append(lm9)
            lm10  = dfs2[0].iloc[int(monthlen)-10][2] #110年最新的10個月最高價
            priceGroup.append(lm10)
            lm11  = dfs2[0].iloc[int(monthlen)-11][2] #110年最新的11個月最高價
            priceGroup.append(lm11)
            lm12  = dfs2[0].iloc[int(monthlen)-12][2] #110年最新的12個月最高價
            priceGroup.append(lm12)     
    
        thisYearMax = max(priceGroup)
        H0 = str(thisYearMax)  #111年目前已出現過的最高價
        #print(priceGroup)
        #print(thisYearMax)

####################################################################################################
#  查詢上櫃股票 (OTC) 年股價 - 修改後的部分 (使用新版 API)
####################################################################################################

    else:    # 查詢上櫃年股價
        try:
            # 取得國泰世華 EPS 資料 (為了確定年份)
            bank_url0 = 'https://djinfo.cathaysec.com.tw/z/zc/zcq/zcq0.djhtm?b=Y&a='
            url_cathay = bank_url0 + stock_id
            r = requests.get(url_cathay, headers=headers)
            soup = BeautifulSoup(r.content, 'html.parser')
            
            table2 = soup.find_all(class_='table-row')
            
            # 初始化 EPS 列表，避免下面引用報錯
            xEPSList = []

            if len(table2) > 0:
                xYearSeasonTitle = table2[0].text
                xYearSeasonTitleList = [x for x in xYearSeasonTitle.split("\n") if x.strip()]
                xEPS = table2[-1].text
                xEPSList = [x for x in xEPS.split("\n") if x.strip()]

                if len(xYearSeasonTitleList) > 2:
                    eps1N = xYearSeasonTitleList[1] # 國泰最新1年的名稱 (可能是 2024 或 2023)
                    print("xYearSeasonTitleList[0]=")
                    print(xYearSeasonTitleList[0])
                    print("xYearSeasonTitleList[]=")
                    print(xYearSeasonTitleList[1])

                    
                    print(f"DEBUG: 抓到的最新 EPS 年份為 {eps1N}")
                else:
                    eps1N = "Unknown"
            else:
                eps1N = "Unknown"


            # ---------------------------------------------------------------------
            # 改用新版 API 抓取櫃買中心年成交資訊
            # ---------------------------------------------------------------------
            
            # 新版 API 網址
            tpex_url = "https://www.tpex.org.tw/www/zh-tw/statistics/yearlyStock"
            
            # 設定 Payload (表單資料)
            payload = {
                'code': stock_id,
                'id': '',
                'response': 'json'
            }
            
            # 新版 API 需要正確的 User-Agent 和 Referer
            api_headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Origin': 'https://www.tpex.org.tw',
                'Referer': 'https://www.tpex.org.tw/zh-tw/mainboard/trading/info/stock-year.html'
            }

            # 發送 POST 請求
            r_tpex = requests.post(tpex_url, data=payload, headers=api_headers)
            
            # 模擬 pd.read_html 的回傳格式 (List of DataFrames)
            dfs = []
            
            if r_tpex.status_code == 200:
                try:
                    data = r_tpex.json()
                    
                    # 解析 JSON 結構: data['tables'][0]['data']
                    if 'tables' in data and len(data['tables']) > 0 and 'data' in data['tables'][0]:
                        raw_data = data['tables'][0]['data']
                        df = pd.DataFrame(raw_data)
                        
                        # 手動設定欄位名稱 (對應 Index)
                        # 0:年度, 1:成交張數, 2:金額, 3:筆數, 4:加權平均價, 5:盤中最高價, 6:日期, 7:盤中最低價, 8:日期, 9:收盤平均價
                        headers_ui = [
                            "年度", "成交張數", "成交金額", "成交筆數", 
                            "加權平均價", "盤中最高價", "最高價日期", 
                            "盤中最低價", "最低價日期", "收盤平均價"
                        ]
                        
                        if df.shape[1] >= len(headers_ui):
                            df = df.iloc[:, :len(headers_ui)]
                            df.columns = headers_ui
                            
                            # 重要：資料清洗 (去除千分位逗號，否則 float() 會報錯)
                            # 原本網頁爬蟲可能回傳的是字串，這裡轉回字串格式並清理
                            cols_to_fix = ['盤中最高價', '盤中最低價']
                            for col in cols_to_fix:
                                df[col] = df[col].astype(str).str.replace(',', '').str.replace('--', '0')
                            
                            dfs.append(df) # 將 DataFrame 放入 list，模擬 read_html 結果
                        else:
                            print(f"{stock_id} 欄位數量不符")
                    else:
                        print(f"{stock_id} API 回傳無資料")
                except Exception as e:
                    print(f"API 解析錯誤: {e}")
            else:
                print(f"{stock_id} 連線失敗: {r_tpex.status_code}")

            
            # ---------------------------------------------------------------------
            # 接續您原本的資料處理邏輯
            # ---------------------------------------------------------------------
            
            if len(dfs) > 0:
                tablelen = len(dfs[0])
                #print(tablelen) 

                # 防呆：確保 list index 不會出錯
                if tablelen > 0: ls0 = dfs[0].iloc[0]; H0 = float(ls0[5])
                if tablelen > 1: ls1 = dfs[0].iloc[1]; H1 = float(ls1[5]); L1 = float(ls1[7])
                if tablelen > 2: ls2 = dfs[0].iloc[2]; H2 = float(ls2[5]); L2 = float(ls2[7])
                if tablelen > 3: ls3 = dfs[0].iloc[3]; H3 = float(ls3[5]); L3 = float(ls3[7])
                if tablelen > 4: ls4 = dfs[0].iloc[4]; H4 = float(ls4[5]); L4 = float(ls4[7])
                if tablelen > 5: ls5 = dfs[0].iloc[5]; H5 = float(ls5[5]); L5 = float(ls5[7])
                if tablelen > 6: ls6 = dfs[0].iloc[6]; H6 = float(ls6[5]); L6 = float(ls6[7])

        except Exception as e:
             print(f"查詢上櫃股票 {stock_id} 發生錯誤: {e}")
             # 發生錯誤時給予預設值，避免後面程式當掉
             H0=H1=H2=H3=H4=H5=H6=0
             L0=L1=L2=L3=L4=L5=L6=0


################################################接著取得上市股票EPS (或上櫃共用)
#stock_id = "3034"
    if stock_id in TSEAll: #如果是上市股票，上面已經跑過一次國泰世華，這邊可能重複跑，但為了維持原架構不動
        bank_url0 = 'https://djinfo.cathaysec.com.tw/z/zc/zcq/zcq0.djhtm?b=Y&a=' #國泰世華
        #sheet_type = 'z/zc/zcq/zcq_' #ISQ 合併損益表 季表

        url = bank_url0 + stock_id
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        #table = soup.find_all('table')[0];
        table2 = soup.find_all(class_ = 'table-row') 


        xYearSeasonTitle = table2[0].text
        xYearSeasonTitleList = xYearSeasonTitle.split("\n")

        xEPS = table2[-1].text
        xEPSList = xEPS.split("\n")
        #dfs[2] 真正表格
        #dfs[2][1] 由左至右 第一欄 最新季
        print(xYearSeasonTitle)
        eps1N = xYearSeasonTitleList[1] #dfs[2][1][0] #最新1年的名稱 2020
        print("xYearSeasonTitleList[1]=")
        print(xYearSeasonTitleList[1])
        print("xYearSeasonTitleList[2]=")
        print(xYearSeasonTitleList[2])        
        print(stock_id)
        print("eps1N=")
        print(eps1N)

    print(xEPSList)
    ######2021/03/13 Q4財報出來大修改  20211224 MoneyDJ大改版
    
    # 初始化 PER 相關變數
    PER_H1=PER_L1=PER_H2=PER_L2=PER_H3=PER_L3=PER_H4=PER_L4=PER_H5=PER_L5=0
    PER_H_average=PER_L_average=PER_H=PER_L=0
    
    # 初始化 EPS 相關變數，解決 UnboundLocalError
    eps1=eps2=eps3=eps4=eps5=eps6=0.0

    # 【重要】修正年份判斷，增加 2025/2024/2023 以符合現在 (2026年) 的各種情況
    if eps1N == '2025':  #在3/31前，Q4財報先出來的情況  年度轉換時還不適用
        
        eps1 = xEPSList[2] #dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2021
        eps2 = xEPSList[3] #dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2020
        eps3 = xEPSList[4] #dfs[2][3][98] #最新3年的合併總損益 每股盈餘 2019
        eps4 = xEPSList[5] #dfs[2][4][98] #最新4年的合併總損益 每股盈餘 2018
        eps5 = xEPSList[6] #dfs[2][5][98] #最新5年的合併總損益 每股盈餘 2017
        eps6 = xEPSList[7] #dfs[2][6][98] #最新5年的合併總損益 每股盈餘 2016
        
        print(f"DEBUG: EPS1 (2025) = {eps1}")
        
    ####2020/07/02 加入本益比成長率    
    #2021/1/6更改
        PER_H1 = round(float(H1)/float(eps1),2)  #110/2021本益比 高
        PER_L1 = round(float(L1)/float(eps1),2)  #110本益比 低 

        PER_H2 = round(float(H2)/float(eps2),2)  #109本益比 高
        PER_L2 = round(float(L2)/float(eps2),2)  #109本益比 低 

        PER_H3 = round(float(H3)/float(eps3),2)  #108本益比 高
        PER_L3 = round(float(L3)/float(eps3),2)  #108本益比 低 
        
        PER_H4 = round(float(H4)/float(eps4),2)  #107本益比 高
        PER_L4 = round(float(L4)/float(eps4),2)  #107本益比 低 
    
        PER_H5 = round(float(H5)/float(eps5),2)  #106本益比 高
        PER_L5 = round(float(L5)/float(eps5),2)  #106本益比 低 

        PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3 + PER_H4 + PER_H5)/5),2)
        PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3 + PER_L4 + PER_L5)/5),2)
#print(PER_H1)

        PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
        PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低  

    # 【重要】修正年份判斷 2024
    elif eps1N == '2024':  #3/31前，Q4財報還沒出來的情況 沒有2021的全年EPS
    ####2020/07/02 加入本益比成長率
        #2021EPS還沒出來的情況   #2021/12/31修改 欄位已改變 12/30最後交易日
        eps1 = xEPSList[2] #dfs[2][1][98] #最新1年的合併總損益 每股盈餘 2020
        eps2 = xEPSList[3] #dfs[2][2][98] #最新2年的合併總損益 每股盈餘 2019
        eps3 = xEPSList[4] #dfs[2][3][98] #最新3年的合併總損益 每股盈餘 2018
        eps4 = xEPSList[5] #dfs[2][4][98] #最新4年的合併總損益 每股盈餘 2017
        eps5 = xEPSList[6] #dfs[2][5][98] #最新5年的合併總損益 每股盈餘 2016
        eps6 = xEPSList[7] #dfs[2][6][98] #最新5年的合併總損益 每股盈餘 2015
        
        print(f"DEBUG: EPS1 (2024) = {eps1}")

    #2021/1/6更改  H1為2020高點
        PER_H1 = round(float(H2)/float(eps1),2)  #109/2020本益比 高
        PER_L1 = round(float(L2)/float(eps1),2)  #109本益比 低 

        PER_H2 = round(float(H3)/float(eps2),2)  #108本益比 高
        PER_L2 = round(float(L3)/float(eps2),2)  #108本益比 低 

        PER_H3 = round(float(H4)/float(eps3),2)  #107本益比 高
        PER_L3 = round(float(L4)/float(eps3),2)  #107本益比 低 

        PER_H4 = round(float(H5)/float(eps4),2)  #106本益比 高
        PER_L4 = round(float(L5)/float(eps4),2)  #106本益比 低 
    
        PER_H5 = round(float(H6)/float(eps5),2)  #105本益比 高
        PER_L5 = round(float(L6)/float(eps5),2)  #105本益比 低 

        PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3 + PER_H4 + PER_H5)/5),2)
        PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3 + PER_L4 + PER_L5)/5),2)

#print(PER_H1)
        PER_H = min(PER_H_average,PER_H1)  #本益比高點與最新孰低
        PER_L = min(PER_L_average,PER_L1)  #本益比低點與最新孰低

    # 【新增】年份判斷 2023 (如果資料庫尚未更新 2024 年報)
    elif eps1N == '2023':  
        eps1 = xEPSList[2] # 2023
        eps2 = xEPSList[3] # 2022
        eps3 = xEPSList[4] # 2021
        eps4 = xEPSList[5] # 2020
        eps5 = xEPSList[6] # 2019
        eps6 = xEPSList[7] # 2018
        
        print(f"DEBUG: EPS1 (2023) = {eps1}")

        # 使用 H3 (2023股價) 對應 eps1 (2023 EPS)
        PER_H1 = round(float(H3)/float(eps1),2)  
        PER_L1 = round(float(L3)/float(eps1),2)  

        PER_H2 = round(float(H4)/float(eps2),2)  
        PER_L2 = round(float(L4)/float(eps2),2)  

        PER_H3 = round(float(H5)/float(eps3),2)  
        PER_L3 = round(float(L5)/float(eps3),2)  

        PER_H4 = round(float(H6)/float(eps4),2)  
        PER_L4 = round(float(L6)/float(eps4),2)  
    
        # H7, L7 我們沒有抓，所以這裡可能要用 None 或簡化
        PER_H5 = 0
        PER_L5 = 0

        # 平均只算前 4 年有資料的
        PER_H_average = round(float((PER_H1 + PER_H2 + PER_H3 + PER_H4)/4),2)
        PER_L_average = round(float((PER_L1 + PER_L2 + PER_L3 + PER_L4)/4),2)

        PER_H = min(PER_H_average,PER_H1)  
        PER_L = min(PER_L_average,PER_L1) 


    #只有三月時年報公佈前後需要  2021轉2022時就需要 可能更早就要
########################2021/2/28新增單季EPS計算 取代整年營收估EPS計算
    bank_url = 'https://djinfo.cathaysec.com.tw/z/zc/zcq/zcq.djhtm?b=Y&a=' #國泰世華
    headers = {'Referer':my_Referer,'user-agent': my_UserAgent}
    #sheet_type = 'z/zc/zcr/zcr_' #FRQ 財務比率 季表
    url = bank_url + stock_id
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
        #table = soup.find_all('table')[0];
    table2 = soup.find_all(class_ = 'table-row') 


    xYearSeasonTitle = table2[0].text
    xYearSeasonTitleList = xYearSeasonTitle.split("\n")

    xqEPS = table2[-9].text
    xqEPSList = xqEPS.split("\n")
#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
    print(xYearSeasonTitle) 
    
    #newest_Fin_Q = str(dfs5[2][1][1]) #最新1季的財報季份

    epsq1N = xYearSeasonTitleList[2] #最新1季的名稱
    #epsq2N = dfs5[2][2][1] #最新2季的名稱
    #epsq3N = dfs5[2][3][1] #最新3季的名稱
    #epsq4N = dfs5[2][4][1] #最新4季的名稱
    #epsq5N = dfs5[2][5][1] #最新5季的名稱
    #epsq6N = dfs5[2][6][1] #最新6季的名稱
    #epsq7N = dfs5[2][7][1] #最新7季的名稱
    #epsq8N = dfs5[2][8][1] #最新8季的名稱
    

    epsq1 = float(xqEPSList[2]) #最新1季的EPS
    epsq2 = float(xqEPSList[3]) #最新2季的EPS
    epsq3 = float(xqEPSList[4]) #最新3季的EPS
    epsq4 = float(xqEPSList[5]) #最新4季的EPS
    #epsq5 = float((dfs5[2][5][25])) #最新5季的EPS
    #epsq6 = float((dfs5[2][6][25])) #最新6季的EPS
    #epsq7 = float((dfs5[2][7][25])) #最新7季的EPS
    #epsq8 = float((dfs5[2][8][25])) #最新8季的EPS
    
##############################################取得營收######################################
############################
    sheet_type = 'z/zc/zch/zch_' #Rev 營收
    #stock_id = "3034"
    bank_url = 'https://djinfo.cathaysec.com.tw/' #國泰世華
    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser') #原本lxml 2022/5/1修改
    table = soup.find_all('table')[0];
    dfs = pd.read_html(str(table))

    rYoY1N = dfs[2][0][6] #最新一個月名稱
    rYoY2N = dfs[2][0][7]
    rYoY3N = dfs[2][0][8]
    rYoY4N = dfs[2][0][9]
    rYoY5N = dfs[2][0][10]
    rYoY6N = dfs[2][0][11]

#目前2020/5/12
    rYoY1 = round(float(dfs[2][4][6][:-1])/100,4) #最新一個月年增率
    rYoY2 = round(float(dfs[2][4][7][:-1])/100,4)
    rYoY3 = round(float(dfs[2][4][8][:-1])/100,4)
    rYoY4 = round(float(dfs[2][4][9][:-1])/100,4)
    rYoY5 = round(float(dfs[2][4][10][:-1])/100,4)
    rYoY6 = round(float(dfs[2][4][11][:-1])/100,4)
    
    pYoY1 = str(round(rYoY1*100,2))+'%'
    pYoY2 = str(round(rYoY2*100,2))+'%'
    pYoY3 = str(round(rYoY3*100,2))+'%'
    pYoY4 = str(round(rYoY4*100,2))+'%'
    pYoY5 = str(round(rYoY5*100,2))+'%'
    pYoY6 = str(round(rYoY6*100,2))+'%'
    
    

    rYoY6Average  = (rYoY1+rYoY2+rYoY3+rYoY4+rYoY5+rYoY6)/6 #最新六個月營收平均
#print(rYoY6Average)
    pYoY6Average = str(round(rYoY6Average*100,2))+'%'

    RevYoY = round(min(rYoY6Average,rYoY1),4) #兩者擇一較低
    
    pRevYoY = str(round(RevYoY*100,2))+'%'

##############################以下開始預估未來一整年的營收###########################################

#print(RevYoY)


    if (month_id == '1'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 110/1

    
        thisYear_Sum = r1 #今年已公布營收 1月營收
        
        r2 = int(dfs[2][1][7])/100000  #109/12
        r3 = int(dfs[2][1][8])/100000  #109/11
        r4 = int(dfs[2][1][9])/100000  #109/10
        r5 = int(dfs[2][1][10])/100000  #109/9
        r6 = int(dfs[2][1][11])/100000  #109/8
        r7 = int(dfs[2][1][12])/100000  #109/7
        r8 = int(dfs[2][1][13])/100000  #109/6
        r9 = int(dfs[2][1][14])/100000  #109/5
        r10 = int(dfs[2][1][15])/100000  #109/4
        r11 = int(dfs[2][1][16])/100000  #109/3
        r12 = int(dfs[2][1][17])/100000  #109/2


        theRest_Predict = (r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12)*(1+RevYoY) #預估今年10-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #預估今年全年營收

        ###2021/2/28新增單季eps
        #估計2020Q4 EPS 因為尚未公佈
        Q4_Rev_Predict = r2+r3+r4 #2021/10,11,12月營收

    elif (month_id == '2'):  #3月整個月都會在公佈前一年Q4營收，會同時有Q3和Q4財報並存現象
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
    
        thisYear_Sum = r1+r2 #今年已公布營收 1-2月營收
        
        
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000  
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000
        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000


        theRest_Predict = (r3+r4+r5+r6+r7+r8+r9+r10+r11+r12)*(1+RevYoY) #預估今年10-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #預估今年全年營收

        if epsq1N == '2020.4Q' :
            Q4_Rev_Predict = None
        else:            
            Q4_Rev_Predict = r3+r4+r5 #2020/10,11,12月營收

    elif (month_id == '3'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        
        thisYear_Sum = r1+r2+r3 #今年已公布營收 1-3月營收
        
        

        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000  
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000
        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000


        theRest_Predict = (r4+r5+r6+r7+r8+r9+r10+r11+r12)*(1+RevYoY) #預估今年4-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #預估今年全年營收

    elif (month_id == '4'): 
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  #最新一個月營收的名稱 109/4
        r2N = dfs[2][0][7]  #109/3
        r3N = dfs[2][0][8]  #109/2
        r4N = dfs[2][0][9]  #109/1
        r5N = dfs[2][0][10]  #108/12
        r6N = dfs[2][0][11]  #108/11
        r7N = dfs[2][0][12]  #108/10
        r8N = dfs[2][0][13]  #108/9
        r9N = dfs[2][0][14]  #108/8
        r10N = dfs[2][0][15]  #108/7
        r11N = dfs[2][0][16]  #108/6
        r12N = dfs[2][0][17]  #108/5
        ##########################各月份營收############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 109/4
        r2 = int(dfs[2][1][7])/100000  #109/3
        r3 = int(dfs[2][1][8])/100000  #109/2
        r4 = int(dfs[2][1][9])/100000  #109/1
    
    #r1_9Sum = Jan_Sep_Sum = r1+r2+r3+r4+r5+r6+r7+r8+r9 #今年1-9月營收
        thisYear_Sum = r1+r2+r3+r4 #今年1-4月營收

        r5 = int(dfs[2][1][10])/100000  #108/12
        r6 = int(dfs[2][1][11])/100000  #108/11
        r7 = int(dfs[2][1][12])/100000  #108/10
        r8 = int(dfs[2][1][13])/100000  #108/9
        r9 = int(dfs[2][1][14])/100000  #108/8
        r10 = int(dfs[2][1][15])/100000  #108/7
        r11 = int(dfs[2][1][16])/100000  #108/6
        r12 = int(dfs[2][1][17])/100000  #108/5

    #r10_12Sum_Predict = (r10+r11+r12)*(1+RevYoY) #預估今年10-12月營收
        theRest_Predict = (r5+r6+r7+r8+r9+r10+r11+r12)*(1+RevYoY) #預估今年10-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #預估今年全年營收

        Q4_Rev_Predict = None


    elif (month_id == '5'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        
        thisYear_Sum = r1+r2+r3+r4+r5 #今年已公布營收 1-5月營收
        
        


        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000  
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000
        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000


        theRest_Predict = (r6+r7+r8+r9+r10+r11+r12)*(1+RevYoY) #預估今年6-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #預估今年全年營收

        Q4_Rev_Predict = None

    elif (month_id == '6'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        
        thisYear_Sum = r1+r2+r3+r4+r5+r6 #今年已公布營收 1-6月營收
        
        
        r7 = int(dfs[2][1][12])/100000  
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000
        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000


        theRest_Predict = (r7+r8+r9+r10+r11+r12)*(1+RevYoY) #預估今年7-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #預估今年全年營收

    elif (month_id == '7'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000 
        
        thisYear_Sum = r1+r2+r3+r4+r5+r6+r7 #今年已公布營收 1-7月營收
        
         
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000
        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000


        theRest_Predict = (r8+r9+r10+r11+r12)*(1+RevYoY) #預估今年8-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #預估今年全年營收

    elif (month_id == '8'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000 
        r8 = int(dfs[2][1][13])/100000
        
        thisYear_Sum = r1+r2+r3+r4+r5+r6+r7+r8 #今年已公布營收 1-7月營收
        
        
        r9 = int(dfs[2][1][14])/100000
        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000


        theRest_Predict = (r9+r10+r11+r12)*(1+RevYoY) #預估今年9-12月營收

        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #預估今年全年營收



########################################暑假過後，只能估算明年的數字######################################
    elif (month_id == '9'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000 
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000 
       
        thisYear_Sum = r1+r2+r3+r4+r5+r6+r7+r8+r9 #今年已公布營收 1-9月營收
        
        

        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000


        theRest_Predict = (r10+r11+r12)*(1+RevYoY) #預估今年10-12月營收

        #Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #預估明年全年營收
        #十月以後採用下面
        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4)*(1+RevYoY) #用今年2021營收 預估明年2022全年營收 20211004修改


    elif (month_id == '10'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000 
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000 
        r10 = int(dfs[2][1][15])/100000
        
        thisYear_Sum = r1+r2+r3+r4+r5+r6+r7+r8+r9+r10 #今年已公布營收 1-10月營收
        
        
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000


        theRest_Predict = (r11+r12)*(1+RevYoY) #預估今年11-12月營收

        #Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #預估明年全年營收
        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4)*(1+RevYoY) #用今年2021營收 預估明年2022全年營收 20211004修改


    elif (month_id == '11'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000 
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000 
        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000
        
        thisYear_Sum = r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11 #今年已公布營收 1-11月營收
        
        

        r12 = int(dfs[2][1][17])/100000


        theRest_Predict = (r12)*(1+RevYoY) #預估今年12月營收

        #Rev_Predict = round(thisYear_Sum + theRest_Predict, 4) #預估明年全年營收
        Rev_Predict = round(thisYear_Sum + theRest_Predict, 4)*(1+RevYoY) #用今年2021營收 預估明年2022全年營收 20211004修改

        Q4_Rev_Predict = r1+r2+ r12*(1+RevYoY) #2021/10,11,12月營收  12月必須估算
        
    elif (month_id == '12'):
        ##########################月份名稱############
        r1N = dfs[2][0][6] #千元 改 億  最新月份名稱
        r2N = dfs[2][0][7]  
        r3N = dfs[2][0][8]
        r4N = dfs[2][0][9]  
        r5N = dfs[2][0][10]  
        r6N = dfs[2][0][11]  
        r7N = dfs[2][0][12]  
        r8N = dfs[2][0][13]  
        r9N = dfs[2][0][14]  
        r10N = dfs[2][0][15]  
        r11N = dfs[2][0][16]  
        r12N = dfs[2][0][17]  
        
        ##########################各月份營收金額############

        r1 = int(dfs[2][1][6])/100000 #千元 改 億  #最新一個月營收 
        r2 = int(dfs[2][1][7])/100000  
        r3 = int(dfs[2][1][8])/100000  
        r4 = int(dfs[2][1][9])/100000
        r5 = int(dfs[2][1][10])/100000
        r6 = int(dfs[2][1][11])/100000
        r7 = int(dfs[2][1][12])/100000 
        r8 = int(dfs[2][1][13])/100000
        r9 = int(dfs[2][1][14])/100000 
        r10 = int(dfs[2][1][15])/100000
        r11 = int(dfs[2][1][16])/100000
        r12 = int(dfs[2][1][17])/100000
        
        thisYear_Sum = r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12 #去年已公布營收 1-12月營收
        #其實是lastYear_Sum 因為名字要一致 才不出錯
        

        


        theRest_Predict = thisYear_Sum*(1+RevYoY) #預估今年全年營收


        Rev_Predict = round(theRest_Predict, 4) #預估今年全年營收

        Q4_Rev_Predict = r1+r2+r3 #2021/10,11,12月營收

##################################取得稅後淨利率

    bank_url = 'https://djinfo.cathaysec.com.tw/' #國泰世華
    sheet_type = 'z/zc/zcr/zcr_' #FRQ 財務比率 季表

    url = bank_url + sheet_type + stock_id + '.djhtm'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser') #原本lxml 2022/5/1修改
        #table = soup.find_all('table')[0];
    table2 = soup.find_all(class_ = 'table-row') 
    #print(table2)
   
    xYearSeasonTitle = table2[0].text
    xYearSeasonTitleList = xYearSeasonTitle.split("\n")

    xNet = table2[11].text
    xNetList = xNet.split("\n")
#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
    #print(xYearSeasonTitle)
    epsq1N = xYearSeasonTitleList[2] #dfs[2][1][0] #最新1年的名稱 2020
    print("epsq1N=")
    print(epsq1N)
    print(xNetList)

#dfs[2] 真正表格
#dfs[2][1] 由左至右 第一欄 最新季
#dfs[2][1][13] 最新一季稅後淨利率
    Net1N = xYearSeasonTitleList[2] #dfs[2][1][1] #最新1季的稅後淨利率名稱
    Net2N = xYearSeasonTitleList[3] #dfs[2][2][1] #最新1季的稅後淨利率名稱
    Net3N = xYearSeasonTitleList[4] #dfs[2][3][1] #最新1季的稅後淨利率名稱
    Net4N = xYearSeasonTitleList[5] #dfs[2][4][1] #最新1季的稅後淨利率名稱


    Net1 = round(float((xNetList[2]))/100,4) #最新1季的稅後淨利率
    Net2 = round(float((xNetList[3]))/100,4) #最新1季的稅後淨利率
    Net3 = round(float((xNetList[4]))/100,4) #最新1季的稅後淨利率
    Net4 = round(float((xNetList[5]))/100,4) #最新1季的稅後淨利率
    
    pNet1 = str(round(Net1*100,2))+'%'
    pNet2 = str(round(Net2*100,2))+'%'
    pNet3 = str(round(Net3*100,2))+'%'
    pNet4 = str(round(Net4*100,2))+'%'

    Net4Average = (Net1+Net2+Net3+Net4)/4
    
    pNet4Average = str(round(Net4Average*100,2))+'%'

#print(Net4Average)

###############預估 淨利 EPS
    Net_Predict = round(Rev_Predict*Net4Average,6)
    #2021/2/28新增
    if eps1N == '2025' :
        
        Q4_Net_Predict = None
        
    else:
        Q4_Net_Predict = round(Q4_Rev_Predict*Net4Average,6)

#print(Net_Predict)

####################################################取得股本


    bank_url0 = 'https://djinfo.cathaysec.com.tw/' #國泰世華
    sheet_type = 'z/zc/zcp/zcpa_' #資產負債表
    ###MoneyDJ
    url = bank_url0 + sheet_type + stock_id +'.djhtm'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
        #table = soup.find_all('table')[0];
    table2 = soup.find_all(class_ = 'table-row') 
    #print(table2)
   
    xCap = table2[-14].text
    xCapList = xCap.split("\n")


    print(xCapList)

    cap1 = round(float(xCapList[2].replace(",", ""))/100,2) #最新一季股本（單位：百萬） 2020/7/4 要轉換成 億
#print(table)
#stock_id_name = dfs[2][0][0][:-24] #股票代號和名稱
    #stock_name = dfs[2][0][0][0:3] #股票名稱
#latest_trade_date = dfs[2][0][0][-13:-8] #最近交易日
#open = dfs[2][1][1] #開盤價
#high = dfs[2][3][1] #最高價
#low  = dfs[2][5][1] #最低價
#close  = dfs[2][7][1] #收盤價
    capital_stock = cap1 #本來Basic表股本 單位：億
#print(capital_stock)
####################計算預估EPS
    Predict_EPS = round(Net_Predict/capital_stock*10,2) #2021
    
    # 解決 UnboundLocalError 的關鍵賦值
    Predict_EPS0 = 0.0

    #2021/2/28新增  3/12更改Q3 Q4並存情況  4/16再修改精簡
    if eps1N == '2025' :
        #pass
        Predict_EPS0 = eps1
    else:
        #pass
        if Q4_Net_Predict is not None:
            Q4_Predict_EPS = round(Q4_Net_Predict/capital_stock*10,2) #估算2021/Q4 eps
            Predict_EPS0 = epsq1 + epsq2 + epsq3 + Q4_Predict_EPS #估2021全年EPS 2022/3/31前 尚未公佈2021Q4財報
        else:
            Predict_EPS0 = epsq1 + epsq2 + epsq3 # 如果無法預估 Q4
            
#print(Predict_EPS)
    #print(PER_H)
    

    Predict_high_price = round(Predict_EPS*PER_H,2)
    Predict_low_price = round(Predict_EPS*PER_L,2)

    # 【重要】ZeroDivisionError 防呆修正
    # 如果預估價格為 0，View 做除法時會崩潰。強制設為非零值。
    if Predict_high_price == 0:
        Predict_high_price = 0.01
    
    if Predict_low_price == 0:
        Predict_low_price = 0.01

#print(Predict_high_price)  #預估股價高點
#print(Predict_low_price)  #預估股價低點
########################取得目前股價
#    url = 'https://tw.stock.yahoo.com/q/ts?s=' + stock_id
#    r = requests.get(url)
#    soup = BeautifulSoup(r.content, 'html.parser')
#    table = soup.find_all('table')[0];
#    dfs = pd.read_html(str(table))

#    yahoo_tradePriceX = float(dfs[0][3][6]) #yahoo成交價
    #print(yahoo_tradePrice)
    #########取得最新價格
    def get_headers():
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        ]
        return {'User-Agent': random.choice(user_agents), 'Referer': 'https://tw.stock.yahoo.com/'}


    
    url = f'https://stock.wearn.com/a{stock_id}.html'
    r = requests.post(url, headers=get_headers())
    soup = BeautifulSoup(r.content, 'html.parser')
    
    yahoo_latest_tradePrice = 0.0 # 初始化避免錯誤
    
    uls = soup.find_all('ul')
    for ul in uls:
        if "成交價" in str(ul):
            li = ul.find_all('li')[0]
            try:
                yahoo_latest_tradePrice = float(li.text)
            except:
                pass
            break
            
    # 如果上面沒抓到，嘗試用固定位置抓取 (這部分可能會因為網頁改版失效，加個 try-except)
    if yahoo_latest_tradePrice == 0 and len(uls) > 4:
        try:
            yahoo_latest_tradePrice = float(uls[4].find_all('li')[0].text)
        except:
            print("無法抓取最新股價")



   
################################ 
    
#######################################    

    if yahoo_latest_tradePrice != 0:
        up_profit = round((Predict_high_price - yahoo_latest_tradePrice)/yahoo_latest_tradePrice,2)
        down_loss = round((Predict_low_price - yahoo_latest_tradePrice)/yahoo_latest_tradePrice,2)
    else:
        up_profit = 0
        down_loss = 0

#print(up_profit)
#print(down_loss)
    New_up_profit = str((Decimal(up_profit).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'
    New_down_loss = str((Decimal(down_loss).quantize(Decimal('.00'), ROUND_HALF_UP))*100)  + '%'


    #New_up_profit = str(up_profit*100) + '%'
    #New_down_loss = str(down_loss*100) + '%'

#print(New_up_profit)
#print(New_down_loss)

    #risk_reward = round(abs(up_profit)/abs(down_loss),2)
    if down_loss != 0:
        risk_reward = round(abs(up_profit/down_loss),2)
    else:
        risk_reward = 0
    
    print(risk_reward)
    
    return H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, New_up_profit, New_down_loss, risk_reward, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average, pNet1, pNet2, pNet3, pNet4, pNet4Average, H0, thisYear_Sum, theRest_Predict, H6, L6, Predict_EPS0, eps1N
#, epsYoY1, epsYoY2, epsYoY3, epsYoY4, PER_H_YoY1, PER_H_YoY2, PER_H_YoY3, PER_H_YoY4, PEG_H1, PEG_H2, PEG_H3, PEG_H4, PEG_L1, PEG_L2, PEG_L3, PEG_L4 

#PERsegx("2330", "11")
