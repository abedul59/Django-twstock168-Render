# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 14:19:28 2022

@author: PCUSER
"""
import math

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.conf import settings
#from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
#########################iii##################
from myapp.models import StockPERsegStable2021Q2
from myapp.models import EpsProfit2021Q2
from myapp.models import StockCapVar2021Q2
from myapp.models import EPSachieve2021Q2

from myapp.models import StockPERsegStable2021Q3
from myapp.models import EpsProfit2021Q3
from myapp.models import StockCapVar2021Q3
from myapp.models import EPSachieve2021Q3

from myapp.models import StockPERsegStable2021Q4
from myapp.models import EpsProfit2021Q4
from myapp.models import StockCapVar2021Q4
from myapp.models import EPSachieve2021Q3



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







from myapp.models import Stock6Sign202203
from myapp.models import Stock6Sign202202
from myapp.models import Stock6Sign202201
from myapp import models

from myapp.models import StockFavs_test168
from myapp.models import StockFavDB

from myapp.models import PriEPSPER_DB


from module import func0
from module import func
from module import func2
from module import func2x
from module import func2t
from module import func3
from module import func3x
from module import func4
from module import func4x
from module import func5
from module import func5x2
from module import func6
from module import func7
from module import func8
##################函式位置改寫，一個函式一個檔案，棄用func
from module_PERseg import Price5yDB, Price5y, PERseg, PERsegPEG, PERsegPEGxDB, PERsegStable, PERsegx, PERsegxDB, NetCapDB, PERseg3
from module_Kn import KnQuery, Kn8yPrice

from myapp import views
from .views_monthlyAlterStuff import DBfunc 
DBv = DBfunc()

#DBv = DBfunc()

#################每個月換資料庫
DB1 = Stock6Sign202209
DB2 = Stock6Sign202208
DB3 = Stock6Sign202207
#############################################

#DBv = NowTimeDBs()  #從views_monthlyAlterStuff.py取得每月需要的資料庫變數

DBv.getRightDB()  #Stock6Sgin
DBv.getRightPERDB() #StockPERseg

DBv.getRightEPSADB() #EPSachieve
DBv.getRightEPSNDB() #EPSProfit
DBv.getRightCAPDB() #StockCAP
DBv.getRightSTABDB() #StockPERsegStable
########


DBEPSAy = DBv.EPSAy
DBEPSAz = DBv.EPSAz

DBEPSNy = DBv.EPSNy
DBEPSNz = DBv.EPSNz
        
DBCAPy = DBv.CAPy
DBCAPz = DBv.CAPz

DBSTABy = DBv.STABy
DBSTABz = DBv.STABz



DBz = DBv.z  #每個月的主要資料庫  #y= 上個月 x = 上上個月
DBy = DBv.y
DBx = DBv.x

#print(DBz, DBy, DBx)
DBPERz = DBv.PERz  #每個月的主要資料庫  #y= 上個月 x = 上上個月
DBPERy = DBv.PERy
DBPERx = DBv.PERx
##################################

def usersmain_app(request, pageindex=None):  #app試用功能首頁
	global page1u
	pagesize = 20  #8
	newsall = models.NewsUnit.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1u = 1
		newsunits0 = models.NewsUnit.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1u-2)*pagesize
		if start >= 0:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u -= 1
	elif pageindex=='2':
		start = page1u*pagesize
		if start < datasize:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u += 1
	elif pageindex=='3':
		start = (page1u-1)*pagesize
		newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1u

######################################################
	global page1
	pagesize = 20  #8
	newsall = models.StockFavs_test168.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1 = 1
		newsunits = models.StockFavs_test168.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1-2)*pagesize
		if start >= 0:
			newsunits = models.StockFavs_test168.objects.order_by('-id')[start:(start+pagesize)]
			page1 -= 1
	elif pageindex=='2':
		start = page1*pagesize
		if start < datasize:
			newsunits = models.StockFavs_test168.objects.order_by('-id')[start:(start+pagesize)]
			page1 += 1
	elif pageindex=='3':
		start = (page1-1)*pagesize
		newsunits = models.StockFavs_test168.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1
	return render(request, "usersmain_app.html", locals())



@permission_required('myapp.Can_enter_usersmain_test168', login_url='/login2/')
def usersmain_test168(request, pageindex=None):  #使用者功能首頁
	global page1u
	pagesize = 20  #8
	newsall = models.NewsUnit.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1u = 1
		newsunits0 = models.NewsUnit.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1u-2)*pagesize
		if start >= 0:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u -= 1
	elif pageindex=='2':
		start = page1u*pagesize
		if start < datasize:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u += 1
	elif pageindex=='3':
		start = (page1u-1)*pagesize
		newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1u

######################################################
	global page1
	pagesize = 20  #8
	newsall = models.StockFavs_test168.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1 = 1
		newsunits = models.StockFavs_test168.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1-2)*pagesize
		if start >= 0:
			newsunits = models.StockFavs_test168.objects.order_by('-id')[start:(start+pagesize)]
			page1 -= 1
	elif pageindex=='2':
		start = page1*pagesize
		if start < datasize:
			newsunits = models.StockFavs_test168.objects.order_by('-id')[start:(start+pagesize)]
			page1 += 1
	elif pageindex=='3':
		start = (page1-1)*pagesize
		newsunits = models.StockFavs_test168.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1
	return render(request, "usersmain_test168.html", locals())




#@permission_required('myapp.Can_enter_AdminOnly', login_url='/login/')
def newsdelete_test168(request, newsid=None, deletetype=None):  #刪除資料
	unit = models.StockFavs_test168.objects.get(id=newsid)  #讀取指定資料
	if deletetype == None:  #進入刪除頁面,顯示原有資料
		type = str(unit.cStockID.strip())
		#subject = unit.title
		#editor = unit.nickname
		#content = unit.message
		#date = unit.pubtime
	elif deletetype == '1':  #按刪除鈕
		unit.delete()
		return redirect('/usersmain_test168/')
	return render(request, "newsdelete_test168.html", locals())


def test168_StoFavlistall(request):
    segs = StockFavs_test168.objects.all().order_by('-cStockID')
    return render(request, "common_StoFavlistall.html", locals())




def test168_enterStockFav(request):  

        
    if request.method == "POST":  #假如是以POST方式才處理
        mess = request.POST['stockid']  #取得表單輸入內容
        mess2 = request.POST['monthid']
        
        stock_name = func2.GetStockName(mess)

        H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, New_up_profit, New_down_loss, risk_reward, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average, pNet1, pNet2, pNet3, pNet4, pNet4Average, H0, thisYear_Sum, theRest_Predict, H6, L6, Predict_EPS0, eps1N =PERsegx.PERsegx(mess, mess2)

        #Product_name, url, itemState, ItemNumber2, buttonType, quantity_atmost = func1.pchome_checkF(mess)
        
    else:
        mess = "股票代號尚未送出！"

    return render(request, "test168_enterStockFav.html", locals())


def test168_enterStockFavAdmin(request):  

        
    if request.method == "POST":  #假如是以POST方式才處理
        mess = request.POST['stockid']  #取得表單輸入內容
        mess2 = request.POST['monthid']
        
        stock_name = func2.GetStockName(mess)

        #H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, New_up_profit, New_down_loss, risk_reward, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average, pNet1, pNet2, pNet3, pNet4, pNet4Average, H0, thisYear_Sum, theRest_Predict, H6, L6, Predict_EPS0, eps1N =PERsegx.PERsegx(mess, mess2)


        #####2022/11/10 增加down30%數據
        H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, New_up_profit, New_down_loss, risk_reward, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average, pNet1, pNet2, pNet3, pNet4, pNet4Average, H0, thisYear_Sum, theRest_Predict, H6, L6, Predict_EPS0, eps1N =PERsegx.PERsegx(mess, mess2)
        #H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, New_up_profit, New_down_loss, risk_reward, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average, pNet1, pNet2, pNet3, pNet4, pNet4Average, H0, thisYear_Sum, theRest_Predict, H6, L6, Predict_EPS0, eps1N =PERsegx.PERsegx(mess, mess2)

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

        ###############################
        xUrl = "/ListallStockFavDB/" + str(mess) + "/"        

        try:
            c1 = DBz.objects.get(cStockID = mess) #本月
            print(DBz)
            ScoreAve1 = c1.cAverageScore
            print(ScoreAve1)
        except:
            ScoreAve1 = "N/A"
            #c1 = DB1.objects.get(cStockID = mess)
            #ScoreAve1 = c1.cAverageScore
        
        try:
            c2 = DBy.objects.get(cStockID = mess)  #上個月
            print(DBy)
            ScoreAve2 = c2.cAverageScore
        except:
            ScoreAve2 = "N/A"
            #c2 = DB2.objects.get(cStockID = mess)
            #ScoreAve2 = c2.cAverageScore
        
        try:
            c3 = DBx.objects.get(cStockID = mess)  #上上個月
            print(DBx)
            ScoreAve3 = c3.cAverageScore      
        except:
            ScoreAve3 = "N/A"
            #c3 = DB3.objects.get(cStockID = mess)
            #ScoreAve3 = c3.cAverageScore               
        #收集資料創建時間
        import datetime
        wholetime = str(datetime.datetime.now()) 
        realtime = wholetime[:16]  #取得獲取資料時間
        
        yeardateOnly = wholetime[:10]

#########################公有最愛股票資料庫########################################



        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
            cOld2 = StockFavDB.objects.get(cStockID = mess, cYearDate = yeardateOnly)#(cYearDate = yeardateOnly)
            
            #if str(cOld2.cYearDate) != str(yeardateOnly):
                
            #cDB = StockFavDB.objects.create(cStockID = mess,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            #cDB.save()
                
            #else:
                
            cOld2.cStockID = mess
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
            
            cOld2 = StockFavDB.objects.create(cStockID = mess,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            cOld2.save()


###################################################################



        #以下寫入資料庫
        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
            cOld = StockFavs_test168.objects.get(cStockID = mess)

        #cOld.cItemName = Product_name
            cOld.cStockID = mess
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

            cOld.cPredict_high_price_down30 = Predict_high_price_30percentDown              
            cOld.cPredict_low_price_down30 = Predict_low_price_30percentDown
            cOld.cNew_up_profit_down30 = New_up_profit2          
            cOld.cNew_down_loss_down30 = New_down_loss2    
            cOld.cRisk_reward_down30 = New_risk_reward


            ##################################################
            try:
                #epsach = EPSachieve2021Q3.objects.get(cStockID = mess)
                epsach = DBEPSAz.objects.get(cStockID = mess)            
                #cOld.cEPSach = str(epsach.cEPSAchieveRate)

                if len(str(epsach.cEPSAchieveRate)) > 4:
                    cOld.cEPSach = str(epsach.cEPSAchieveRate)[:5] + "%"
                else:
                    cOld.cEPSach = str(epsach.cEPSAchieveRate)
                    
            
            except:
                cOld.cEPSach = "No"
            ########################################
            try:
                #stacap = StockCapVar2021Q4.objects.get(cStockID = mess)
                stacap = DBCAPz.objects.get(cStockID = mess)
            
                cOld.cStCap = str(stacap.cLatestMoM)
            
            except:
                cOld.cStCap = "No"
            ###########################################                
            try:
                #epsprf = EpsProfit2021Q4.objects.get(cStockID = mess)
                epsprf = DBEPSNz.objects.get(cStockID = mess)
            
                cOld.cEPSnPrf = "Yes"
            
            except:
                cOld.cEPSnPrf = "No"                
                
            
            try:
                #stab = StockPERsegStable2021Q4.objects.get(cStockID = mess)
                stab = DBSTABz.objects.get(cStockID = mess)
            
                cOld.cPERstab = "Yes"
            except:
                cOld.cPERstab = "No"                
            
            
            
            
            
            cOld.pubtime =realtime      
                 
            cOld.save()
            
            ###################
        except:  #針對沒有的，抓取資料存入資料庫

            cOld2 = StockFavs_test168.objects.create(cStockID = mess,cStockName = stock_name,cDBURL = xUrl,cScore1st = ScoreAve1,cScore2nd = ScoreAve2,cScore3rd = ScoreAve3,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            cOld2.save()

            cOld = StockFavs_test168.objects.get(cStockID = mess)

            try:
                epsach = EPSachieve2021Q3.objects.get(cStockID = mess)
            
                #cOld.cEPSach = str(epsach.cEPSAchieveRate)

                if len(str(epsach.cEPSAchieveRate)) > 4:
                    cOld.cEPSach = str(epsach.cEPSAchieveRate)[:5] + "%"
                else:
                    cOld.cEPSach = str(epsach.cEPSAchieveRate)
                    
            
            except:
                cOld.cEPSach = "No"

            try:
                stacap = StockCapVar2021Q3.objects.get(cStockID = mess)
            
                cOld.cStCap = str(stacap.cLatestMoM)
            
            except:
                cOld.cStCap = "No"
                
            try:
                epsprf = EpsProfit2021Q3.objects.get(cStockID = mess)
            
                cOld.cEPSnPrf = "Yes"
            
            except:
                cOld.cEPSnPrf = "No"                
                
            
            try:
                stab = StockPERsegStable2021Q3.objects.get(cStockID = mess)
            
                cOld.cPERstab = "Yes"
            except:
                cOld.cPERstab = "No"                
            
            
            
            
            
            cOld.pubtime =realtime      
                 
            cOld.save()
   
    else:
        mess = "股票代號尚未送出！"


    return render(request, "test168_enterStockFavAdmin.html", locals())



def ListallStockFavDB(request, mess=None):


    if mess == None:
        segs = StockFavDB.objects.all().order_by('-id')
    else:
        segs = StockFavDB.objects.filter(cStockID = mess).order_by('-cYearDate')        
    return render(request, "ListallStockFavDB.html", locals())



##################################

#@permission_required('myapp.Can_enter_usersmain_test168', login_url='/login2/')
def usersmain_bobmax(request, pageindex=None):  #使用者功能首頁
	global page1u
	pagesize = 20  #8
	newsall = models.NewsUnit.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1u = 1
		newsunits0 = models.NewsUnit.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1u-2)*pagesize
		if start >= 0:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u -= 1
	elif pageindex=='2':
		start = page1u*pagesize
		if start < datasize:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u += 1
	elif pageindex=='3':
		start = (page1u-1)*pagesize
		newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1u

######################################################
	global page1
	pagesize = 20  #8
	newsall = models.StockFavs_bobmax.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1 = 1
		newsunits = models.StockFavs_bobmax.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1-2)*pagesize
		if start >= 0:
			newsunits = models.StockFavs_bobmax.objects.order_by('-id')[start:(start+pagesize)]
			page1 -= 1
	elif pageindex=='2':
		start = page1*pagesize
		if start < datasize:
			newsunits = models.StockFavs_bobmax.objects.order_by('-id')[start:(start+pagesize)]
			page1 += 1
	elif pageindex=='3':
		start = (page1-1)*pagesize
		newsunits = models.StockFavs_bobmax.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1
	return render(request, "usersmain_bobmax.html", locals())




#@permission_required('myapp.Can_enter_AdminOnly', login_url='/login/')
def newsdelete_bobmax(request, newsid=None, deletetype=None):  #刪除資料
	unit = models.StockFavs_bobmax.objects.get(id=newsid)  #讀取指定資料
	if deletetype == None:  #進入刪除頁面,顯示原有資料
		type = str(unit.cStockID.strip())
		#subject = unit.title
		#editor = unit.nickname
		#content = unit.message
		#date = unit.pubtime
	elif deletetype == '1':  #按刪除鈕
		unit.delete()
		return redirect('/usersmain_bobmax/')
	return render(request, "newsdelete_bobmax.html", locals())


def bobmax_StoFavlistall(request):
    segs = models.StockFavs_bobmax.objects.all().order_by('-cStockID')
    return render(request, "common_StoFavlistall.html", locals())


def bobmax_enterStockFavAdmin(request):  

        
    if request.method == "POST":  #假如是以POST方式才處理
        mess = request.POST['stockid']  #取得表單輸入內容
        mess2 = request.POST['monthid']
        
        stock_name = func2.GetStockName(mess)

        H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, New_up_profit, New_down_loss, risk_reward, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average, pNet1, pNet2, pNet3, pNet4, pNet4Average, H0, thisYear_Sum, theRest_Predict, H6, L6, Predict_EPS0, eps1N =PERsegx.PERsegx(mess, mess2)

        xUrl = "/ListallStockFavDB/" + str(mess) + "/"        

        try:
            c1 = DBz.objects.get(cStockID = mess)
            print(DBz)
            ScoreAve1 = c1.cAverageScore
            print(ScoreAve1)
        except:
            ScoreAve1 = "N/A"
            #c1 = DB1.objects.get(cStockID = mess)
            #ScoreAve1 = c1.cAverageScore
        
        try:
            c2 = DBy.objects.get(cStockID = mess)
            print(DBy)
            ScoreAve2 = c2.cAverageScore
        except:
            ScoreAve2 = "N/A"
            #c2 = DB2.objects.get(cStockID = mess)
            #ScoreAve2 = c2.cAverageScore
        
        try:
            c3 = DBx.objects.get(cStockID = mess)
            print(DBx)
            ScoreAve3 = c3.cAverageScore      
        except:
            ScoreAve3 = "N/A"
            #c3 = DB3.objects.get(cStockID = mess)
            #ScoreAve3 = c3.cAverageScore            
        #收集資料創建時間
        import datetime
        wholetime = str(datetime.datetime.now()) 
        realtime = wholetime[:16]  #取得獲取資料時間
        
        yeardateOnly = wholetime[:10]

        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
            cOld2 = StockFavDB.objects.get(cStockID = mess, cYearDate = yeardateOnly)#(cYearDate = yeardateOnly)
            
            #if str(cOld2.cYearDate) != str(yeardateOnly):
                
            #cDB = StockFavDB.objects.create(cStockID = mess,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            #cDB.save()
                
            #else:
                
            cOld2.cStockID = mess
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
            
            cOld2 = StockFavDB.objects.create(cStockID = mess,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            cOld2.save()


        #以下寫入資料庫
        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
            cOld = models.StockFavs_bobmax.objects.get(cStockID = mess)

        #cOld.cItemName = Product_name
            cOld.cStockID = mess
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

            
            cOld.pubtime =realtime      
                 
            cOld.save()
            
            ###################
        except:  #針對沒有的，抓取資料存入資料庫

            cOld = models.StockFavs_bobmax.objects.create(cStockID = mess,cStockName = stock_name,cDBURL = xUrl,cScore1st = ScoreAve1,cScore2nd = ScoreAve2,cScore3rd = ScoreAve3,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            cOld.save()


   
    else:
        mess = "股票代號尚未送出！"


    return render(request, "common_enterStockFavAdmin.html", locals())

#############################################################################
##################################

#@permission_required('myapp.Can_enter_usersmain_test168', login_url='/login2/')
def usersmain_deno36(request, pageindex=None):  #使用者功能首頁
	global page1u
	pagesize = 20  #8
	newsall = models.NewsUnit.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1u = 1
		newsunits0 = models.NewsUnit.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1u-2)*pagesize
		if start >= 0:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u -= 1
	elif pageindex=='2':
		start = page1u*pagesize
		if start < datasize:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u += 1
	elif pageindex=='3':
		start = (page1u-1)*pagesize
		newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1u

######################################################
	global page1
	pagesize = 20  #8
	newsall = models.StockFavs_deno36.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1 = 1
		newsunits = models.StockFavs_deno36.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1-2)*pagesize
		if start >= 0:
			newsunits = models.StockFavs_deno36.objects.order_by('-id')[start:(start+pagesize)]
			page1 -= 1
	elif pageindex=='2':
		start = page1*pagesize
		if start < datasize:
			newsunits = models.StockFavs_deno36.objects.order_by('-id')[start:(start+pagesize)]
			page1 += 1
	elif pageindex=='3':
		start = (page1-1)*pagesize
		newsunits = models.StockFavs_deno36.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1
	return render(request, "usersmain_deno36.html", locals())




#@permission_required('myapp.Can_enter_AdminOnly', login_url='/login/')
def newsdelete_deno36(request, newsid=None, deletetype=None):  #刪除資料
	unit = models.StockFavs_deno36.objects.get(id=newsid)  #讀取指定資料
	if deletetype == None:  #進入刪除頁面,顯示原有資料
		type = str(unit.cStockID.strip())
		#subject = unit.title
		#editor = unit.nickname
		#content = unit.message
		#date = unit.pubtime
	elif deletetype == '1':  #按刪除鈕
		unit.delete()
		return redirect('/usersmain_deno36/')
	return render(request, "newsdelete_deno36.html", locals())


def deno36_StoFavlistall(request):
    segs = models.StockFavs_deno36.objects.all().order_by('-cStockID')
    return render(request, "common_StoFavlistall.html", locals())


def deno36_enterStockFavAdmin(request):  

        
    if request.method == "POST":  #假如是以POST方式才處理
        mess = request.POST['stockid']  #取得表單輸入內容
        mess2 = request.POST['monthid']
        
        stock_name = func2.GetStockName(mess)

        H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, New_up_profit, New_down_loss, risk_reward, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average, pNet1, pNet2, pNet3, pNet4, pNet4Average, H0, thisYear_Sum, theRest_Predict, H6, L6, Predict_EPS0, eps1N =PERsegx.PERsegx(mess, mess2)

        xUrl = "/ListallStockFavDB/" + str(mess) + "/"        

        try:
            c1 = DBz.objects.get(cStockID = mess)
            print(DBz)
            ScoreAve1 = c1.cAverageScore
            print(ScoreAve1)
        except:
            ScoreAve1 = "N/A"
            #c1 = DB1.objects.get(cStockID = mess)
            #ScoreAve1 = c1.cAverageScore
        
        try:
            c2 = DBy.objects.get(cStockID = mess)
            print(DBy)
            ScoreAve2 = c2.cAverageScore
        except:
            ScoreAve2 = "N/A"
            #c2 = DB2.objects.get(cStockID = mess)
            #ScoreAve2 = c2.cAverageScore
        
        try:
            c3 = DBx.objects.get(cStockID = mess)
            print(DBx)
            ScoreAve3 = c3.cAverageScore      
        except:
            ScoreAve3 = "N/A"
            #c3 = DB3.objects.get(cStockID = mess)
            #ScoreAve3 = c3.cAverageScore           
        #收集資料創建時間
        import datetime
        wholetime = str(datetime.datetime.now()) 
        realtime = wholetime[:16]  #取得獲取資料時間
        
        yeardateOnly = wholetime[:10]

        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
            cOld2 = StockFavDB.objects.get(cStockID = mess, cYearDate = yeardateOnly)#(cYearDate = yeardateOnly)
            
            #if str(cOld2.cYearDate) != str(yeardateOnly):
                
            #cDB = StockFavDB.objects.create(cStockID = mess,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            #cDB.save()
                
            #else:
                
            cOld2.cStockID = mess
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
            
            cOld2 = StockFavDB.objects.create(cStockID = mess,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            cOld2.save()


        #以下寫入資料庫
        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
            cOld = models.StockFavs_deno36.objects.get(cStockID = mess)

        #cOld.cItemName = Product_name
            cOld.cStockID = mess
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

            
            cOld.pubtime =realtime      
                 
            cOld.save()
            
            ###################
        except:  #針對沒有的，抓取資料存入資料庫

            cOld = models.StockFavs_deno36.objects.create(cStockID = mess,cStockName = stock_name,cDBURL = xUrl,cScore1st = ScoreAve1,cScore2nd = ScoreAve2,cScore3rd = ScoreAve3,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            cOld.save()


   
    else:
        mess = "股票代號尚未送出！"


    return render(request, "common_enterStockFavAdmin.html", locals())

#############################################################################
##################################

#@permission_required('myapp.Can_enter_usersmain_test168', login_url='/login2/')
def usersmain_donhonlin(request, pageindex=None):  #使用者功能首頁
	global page1u
	pagesize = 20  #8
	newsall = models.NewsUnit.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1u = 1
		newsunits0 = models.NewsUnit.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1u-2)*pagesize
		if start >= 0:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u -= 1
	elif pageindex=='2':
		start = page1u*pagesize
		if start < datasize:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u += 1
	elif pageindex=='3':
		start = (page1u-1)*pagesize
		newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1u

######################################################
	global page1
	pagesize = 20  #8
	newsall = models.StockFavs_donhonlin.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1 = 1
		newsunits = models.StockFavs_donhonlin.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1-2)*pagesize
		if start >= 0:
			newsunits = models.StockFavs_donhonlin.objects.order_by('-id')[start:(start+pagesize)]
			page1 -= 1
	elif pageindex=='2':
		start = page1*pagesize
		if start < datasize:
			newsunits = models.StockFavs_donhonlin.objects.order_by('-id')[start:(start+pagesize)]
			page1 += 1
	elif pageindex=='3':
		start = (page1-1)*pagesize
		newsunits = models.StockFavs_donhonlin.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1
	return render(request, "usersmain_donhonlin.html", locals())




#@permission_required('myapp.Can_enter_AdminOnly', login_url='/login/')
def newsdelete_donhonlin(request, newsid=None, deletetype=None):  #刪除資料
	unit = models.StockFavs_donhonlin.objects.get(id=newsid)  #讀取指定資料
	if deletetype == None:  #進入刪除頁面,顯示原有資料
		type = str(unit.cStockID.strip())
		#subject = unit.title
		#editor = unit.nickname
		#content = unit.message
		#date = unit.pubtime
	elif deletetype == '1':  #按刪除鈕
		unit.delete()
		return redirect('/usersmain_donhonlin/')
	return render(request, "newsdelete_donhonlin.html", locals())


def donhonlin_StoFavlistall(request):
    segs = models.StockFavs_donhonlin.objects.all().order_by('-cStockID')
    return render(request, "common_StoFavlistall.html", locals())


def donhonlin_enterStockFavAdmin(request):  

        
    if request.method == "POST":  #假如是以POST方式才處理
        mess = request.POST['stockid']  #取得表單輸入內容
        mess2 = request.POST['monthid']
        
        stock_name = func2.GetStockName(mess)

        H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, New_up_profit, New_down_loss, risk_reward, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average, pNet1, pNet2, pNet3, pNet4, pNet4Average, H0, thisYear_Sum, theRest_Predict, H6, L6, Predict_EPS0, eps1N =PERsegx.PERsegx(mess, mess2)

        xUrl = "/ListallStockFavDB/" + str(mess) + "/"        

        try:
            c1 = DBz.objects.get(cStockID = mess)
            print(DBz)
            ScoreAve1 = c1.cAverageScore
            print(ScoreAve1)
        except:
            ScoreAve1 = "N/A"
            #c1 = DB1.objects.get(cStockID = mess)
            #ScoreAve1 = c1.cAverageScore
        
        try:
            c2 = DBy.objects.get(cStockID = mess)
            print(DBy)
            ScoreAve2 = c2.cAverageScore
        except:
            ScoreAve2 = "N/A"
            #c2 = DB2.objects.get(cStockID = mess)
            #ScoreAve2 = c2.cAverageScore
        
        try:
            c3 = DBx.objects.get(cStockID = mess)
            print(DBx)
            ScoreAve3 = c3.cAverageScore      
        except:
            ScoreAve3 = "N/A"
            #c3 = DB3.objects.get(cStockID = mess)
            #ScoreAve3 = c3.cAverageScore           
        #收集資料創建時間
        import datetime
        wholetime = str(datetime.datetime.now()) 
        realtime = wholetime[:16]  #取得獲取資料時間
        
        yeardateOnly = wholetime[:10]

        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
            cOld2 = StockFavDB.objects.get(cStockID = mess, cYearDate = yeardateOnly)#(cYearDate = yeardateOnly)
            
            #if str(cOld2.cYearDate) != str(yeardateOnly):
                
            #cDB = StockFavDB.objects.create(cStockID = mess,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            #cDB.save()
                
            #else:
                
            cOld2.cStockID = mess
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
            
            cOld2 = StockFavDB.objects.create(cStockID = mess,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            cOld2.save()


        #以下寫入資料庫
        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
            cOld = models.StockFavs_donhonlin.objects.get(cStockID = mess)

        #cOld.cItemName = Product_name
            cOld.cStockID = mess
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

            
            cOld.pubtime =realtime      
                 
            cOld.save()
            
            ###################
        except:  #針對沒有的，抓取資料存入資料庫

            cOld = models.StockFavs_donhonlin.objects.create(cStockID = mess,cStockName = stock_name,cDBURL = xUrl,cScore1st = ScoreAve1,cScore2nd = ScoreAve2,cScore3rd = ScoreAve3,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            cOld.save()


   
    else:
        mess = "股票代號尚未送出！"


    return render(request, "common_enterStockFavAdmin.html", locals())

#############################################################################
##################################

#@permission_required('myapp.Can_enter_usersmain_test168', login_url='/login2/')
def usersmain_goldsilver(request, pageindex=None):  #使用者功能首頁
	global page1u
	pagesize = 20  #8
	newsall = models.NewsUnit.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1u = 1
		newsunits0 = models.NewsUnit.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1u-2)*pagesize
		if start >= 0:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u -= 1
	elif pageindex=='2':
		start = page1u*pagesize
		if start < datasize:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u += 1
	elif pageindex=='3':
		start = (page1u-1)*pagesize
		newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1u

######################################################
	global page1
	pagesize = 20  #8
	newsall = models.StockFavs_goldsilver.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1 = 1
		newsunits = models.StockFavs_goldsilver.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1-2)*pagesize
		if start >= 0:
			newsunits = models.StockFavs_goldsilver.objects.order_by('-id')[start:(start+pagesize)]
			page1 -= 1
	elif pageindex=='2':
		start = page1*pagesize
		if start < datasize:
			newsunits = models.StockFavs_goldsilver.objects.order_by('-id')[start:(start+pagesize)]
			page1 += 1
	elif pageindex=='3':
		start = (page1-1)*pagesize
		newsunits = models.StockFavs_goldsilver.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1
	return render(request, "usersmain_goldsilver.html", locals())




#@permission_required('myapp.Can_enter_AdminOnly', login_url='/login/')
def newsdelete_goldsilver(request, newsid=None, deletetype=None):  #刪除資料
	unit = models.StockFavs_goldsilver.objects.get(id=newsid)  #讀取指定資料
	if deletetype == None:  #進入刪除頁面,顯示原有資料
		type = str(unit.cStockID.strip())
		#subject = unit.title
		#editor = unit.nickname
		#content = unit.message
		#date = unit.pubtime
	elif deletetype == '1':  #按刪除鈕
		unit.delete()
		return redirect('/usersmain_goldsilver/')
	return render(request, "newsdelete_goldsilver.html", locals())


def goldsilver_StoFavlistall(request):
    segs = models.StockFavs_goldsilver.objects.all().order_by('-cStockID')
    return render(request, "common_StoFavlistall.html", locals())


def goldsilver_enterStockFavAdmin(request):  

        
    if request.method == "POST":  #假如是以POST方式才處理
        mess = request.POST['stockid']  #取得表單輸入內容
        mess2 = request.POST['monthid']
        
        stock_name = func2.GetStockName(mess)

        H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, New_up_profit, New_down_loss, risk_reward, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average, pNet1, pNet2, pNet3, pNet4, pNet4Average, H0, thisYear_Sum, theRest_Predict, H6, L6, Predict_EPS0, eps1N =PERsegx.PERsegx(mess, mess2)

        xUrl = "/ListallStockFavDB/" + str(mess) + "/"        

        try:
            c1 = DBz.objects.get(cStockID = mess)
            print(DBz)
            ScoreAve1 = c1.cAverageScore
            print(ScoreAve1)
        except:
            ScoreAve1 = "N/A"
            #c1 = DB1.objects.get(cStockID = mess)
            #ScoreAve1 = c1.cAverageScore
        
        try:
            c2 = DBy.objects.get(cStockID = mess)
            print(DBy)
            ScoreAve2 = c2.cAverageScore
        except:
            ScoreAve2 = "N/A"
            #c2 = DB2.objects.get(cStockID = mess)
            #ScoreAve2 = c2.cAverageScore
        
        try:
            c3 = DBx.objects.get(cStockID = mess)
            print(DBx)
            ScoreAve3 = c3.cAverageScore      
        except:
            ScoreAve3 = "N/A"
            #c3 = DB3.objects.get(cStockID = mess)
            #ScoreAve3 = c3.cAverageScore            
        #收集資料創建時間
        import datetime
        wholetime = str(datetime.datetime.now()) 
        realtime = wholetime[:16]  #取得獲取資料時間
        
        yeardateOnly = wholetime[:10]

        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
            cOld2 = StockFavDB.objects.get(cStockID = mess, cYearDate = yeardateOnly)#(cYearDate = yeardateOnly)
            
            #if str(cOld2.cYearDate) != str(yeardateOnly):
                
            #cDB = StockFavDB.objects.create(cStockID = mess,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            #cDB.save()
                
            #else:
                
            cOld2.cStockID = mess
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
            
            cOld2 = StockFavDB.objects.create(cStockID = mess,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            cOld2.save()


        #以下寫入資料庫
        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
            cOld = models.StockFavs_goldsilver.objects.get(cStockID = mess)

        #cOld.cItemName = Product_name
            cOld.cStockID = mess
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

            
            cOld.pubtime =realtime      
                 
            cOld.save()
            
            ###################
        except:  #針對沒有的，抓取資料存入資料庫

            cOld = models.StockFavs_goldsilver.objects.create(cStockID = mess,cStockName = stock_name,cDBURL = xUrl,cScore1st = ScoreAve1,cScore2nd = ScoreAve2,cScore3rd = ScoreAve3,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            cOld.save()


   
    else:
        mess = "股票代號尚未送出！"


    return render(request, "common_enterStockFavAdmin.html", locals())

#############################################################################
##################################

#@permission_required('myapp.Can_enter_usersmain_test168', login_url='/login2/')
def usersmain_hyeth(request, pageindex=None):  #使用者功能首頁
	global page1u
	pagesize = 20  #8
	newsall = models.NewsUnit.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1u = 1
		newsunits0 = models.NewsUnit.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1u-2)*pagesize
		if start >= 0:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u -= 1
	elif pageindex=='2':
		start = page1u*pagesize
		if start < datasize:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u += 1
	elif pageindex=='3':
		start = (page1u-1)*pagesize
		newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1u

######################################################
	global page1
	pagesize = 20  #8
	newsall = models.StockFavs_hyeth.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1 = 1
		newsunits = models.StockFavs_hyeth.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1-2)*pagesize
		if start >= 0:
			newsunits = models.StockFavs_hyeth.objects.order_by('-id')[start:(start+pagesize)]
			page1 -= 1
	elif pageindex=='2':
		start = page1*pagesize
		if start < datasize:
			newsunits = models.StockFavs_hyeth.objects.order_by('-id')[start:(start+pagesize)]
			page1 += 1
	elif pageindex=='3':
		start = (page1-1)*pagesize
		newsunits = models.StockFavs_hyeth.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1
	return render(request, "usersmain_hyeth.html", locals())




#@permission_required('myapp.Can_enter_AdminOnly', login_url='/login/')
def newsdelete_hyeth(request, newsid=None, deletetype=None):  #刪除資料
	unit = models.StockFavs_hyeth.objects.get(id=newsid)  #讀取指定資料
	if deletetype == None:  #進入刪除頁面,顯示原有資料
		type = str(unit.cStockID.strip())
		#subject = unit.title
		#editor = unit.nickname
		#content = unit.message
		#date = unit.pubtime
	elif deletetype == '1':  #按刪除鈕
		unit.delete()
		return redirect('/usersmain_hyeth/')
	return render(request, "newsdelete_hyeth.html", locals())


def hyeth_StoFavlistall(request):
    segs = models.StockFavs_hyeth.objects.all().order_by('-cStockID')
    return render(request, "common_StoFavlistall.html", locals())


def hyeth_enterStockFavAdmin(request):  

        
    if request.method == "POST":  #假如是以POST方式才處理
        mess = request.POST['stockid']  #取得表單輸入內容
        mess2 = request.POST['monthid']
        
        stock_name = func2.GetStockName(mess)

        H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, New_up_profit, New_down_loss, risk_reward, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average, pNet1, pNet2, pNet3, pNet4, pNet4Average, H0, thisYear_Sum, theRest_Predict, H6, L6, Predict_EPS0, eps1N =PERsegx.PERsegx(mess, mess2)

        xUrl = "/ListallStockFavDB/" + str(mess) + "/"        

        try:
            c1 = DBz.objects.get(cStockID = mess)
            print(DBz)
            ScoreAve1 = c1.cAverageScore
            print(ScoreAve1)
        except:
            ScoreAve1 = "N/A"
            #c1 = DB1.objects.get(cStockID = mess)
            #ScoreAve1 = c1.cAverageScore
        
        try:
            c2 = DBy.objects.get(cStockID = mess)
            print(DBy)
            ScoreAve2 = c2.cAverageScore
        except:
            ScoreAve2 = "N/A"
            #c2 = DB2.objects.get(cStockID = mess)
            #ScoreAve2 = c2.cAverageScore
        
        try:
            c3 = DBx.objects.get(cStockID = mess)
            print(DBx)
            ScoreAve3 = c3.cAverageScore      
        except:
            ScoreAve3 = "N/A"
            #c3 = DB3.objects.get(cStockID = mess)
            #ScoreAve3 = c3.cAverageScore           
        #收集資料創建時間
        import datetime
        wholetime = str(datetime.datetime.now()) 
        realtime = wholetime[:16]  #取得獲取資料時間
        
        yeardateOnly = wholetime[:10]

        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
            cOld2 = StockFavDB.objects.get(cStockID = mess, cYearDate = yeardateOnly)#(cYearDate = yeardateOnly)
            
            #if str(cOld2.cYearDate) != str(yeardateOnly):
                
            #cDB = StockFavDB.objects.create(cStockID = mess,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            #cDB.save()
                
            #else:
                
            cOld2.cStockID = mess
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
            
            cOld2 = StockFavDB.objects.create(cStockID = mess,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            cOld2.save()


        #以下寫入資料庫
        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
            cOld = models.StockFavs_hyeth.objects.get(cStockID = mess)

        #cOld.cItemName = Product_name
            cOld.cStockID = mess
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

            
            cOld.pubtime =realtime      
                 
            cOld.save()
            
            ###################
        except:  #針對沒有的，抓取資料存入資料庫

            cOld = models.StockFavs_hyeth.objects.create(cStockID = mess,cStockName = stock_name,cDBURL = xUrl,cScore1st = ScoreAve1,cScore2nd = ScoreAve2,cScore3rd = ScoreAve3,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            cOld.save()


   
    else:
        mess = "股票代號尚未送出！"


    return render(request, "common_enterStockFavAdmin.html", locals())

#############################################################################
##################################

#@permission_required('myapp.Can_enter_usersmain_test168', login_url='/login2/')
def usersmain_jonyi(request, pageindex=None):  #使用者功能首頁
	global page1u
	pagesize = 20  #8
	newsall = models.NewsUnit.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1u = 1
		newsunits0 = models.NewsUnit.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1u-2)*pagesize
		if start >= 0:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u -= 1
	elif pageindex=='2':
		start = page1u*pagesize
		if start < datasize:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u += 1
	elif pageindex=='3':
		start = (page1u-1)*pagesize
		newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1u

######################################################
	global page1
	pagesize = 20  #8
	newsall = models.StockFavs_jonyi.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1 = 1
		newsunits = models.StockFavs_jonyi.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1-2)*pagesize
		if start >= 0:
			newsunits = models.StockFavs_jonyi.objects.order_by('-id')[start:(start+pagesize)]
			page1 -= 1
	elif pageindex=='2':
		start = page1*pagesize
		if start < datasize:
			newsunits = models.StockFavs_jonyi.objects.order_by('-id')[start:(start+pagesize)]
			page1 += 1
	elif pageindex=='3':
		start = (page1-1)*pagesize
		newsunits = models.StockFavs_jonyi.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1
	return render(request, "usersmain_jonyi.html", locals())




#@permission_required('myapp.Can_enter_AdminOnly', login_url='/login/')
def newsdelete_jonyi(request, newsid=None, deletetype=None):  #刪除資料
	unit = models.StockFavs_jonyi.objects.get(id=newsid)  #讀取指定資料
	if deletetype == None:  #進入刪除頁面,顯示原有資料
		type = str(unit.cStockID.strip())
		#subject = unit.title
		#editor = unit.nickname
		#content = unit.message
		#date = unit.pubtime
	elif deletetype == '1':  #按刪除鈕
		unit.delete()
		return redirect('/usersmain_jonyi/')
	return render(request, "newsdelete_jonyi.html", locals())


def jonyi_StoFavlistall(request):
    segs = models.StockFavs_jonyi.objects.all().order_by('-cStockID')
    return render(request, "common_StoFavlistall.html", locals())


def jonyi_enterStockFavAdmin(request):  

        
    if request.method == "POST":  #假如是以POST方式才處理
        mess = request.POST['stockid']  #取得表單輸入內容
        mess2 = request.POST['monthid']
        
        stock_name = func2.GetStockName(mess)

        H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, New_up_profit, New_down_loss, risk_reward, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average, pNet1, pNet2, pNet3, pNet4, pNet4Average, H0, thisYear_Sum, theRest_Predict, H6, L6, Predict_EPS0, eps1N =PERsegx.PERsegx(mess, mess2)

        xUrl = "/ListallStockFavDB/" + str(mess) + "/"        

        try:
            c1 = DBz.objects.get(cStockID = mess)
            print(DBz)
            ScoreAve1 = c1.cAverageScore
            print(ScoreAve1)
        except:
            ScoreAve1 = "N/A"
            #c1 = DB1.objects.get(cStockID = mess)
            #ScoreAve1 = c1.cAverageScore
        
        try:
            c2 = DBy.objects.get(cStockID = mess)
            print(DBy)
            ScoreAve2 = c2.cAverageScore
        except:
            ScoreAve2 = "N/A"
            #c2 = DB2.objects.get(cStockID = mess)
            #ScoreAve2 = c2.cAverageScore
        
        try:
            c3 = DBx.objects.get(cStockID = mess)
            print(DBx)
            ScoreAve3 = c3.cAverageScore      
        except:
            ScoreAve3 = "N/A"
            #c3 = DB3.objects.get(cStockID = mess)
            #ScoreAve3 = c3.cAverageScore           
        #收集資料創建時間
        import datetime
        wholetime = str(datetime.datetime.now()) 
        realtime = wholetime[:16]  #取得獲取資料時間
        
        yeardateOnly = wholetime[:10]

        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
            cOld2 = StockFavDB.objects.get(cStockID = mess, cYearDate = yeardateOnly)#(cYearDate = yeardateOnly)
            
            #if str(cOld2.cYearDate) != str(yeardateOnly):
                
            #cDB = StockFavDB.objects.create(cStockID = mess,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            #cDB.save()
                
            #else:
                
            cOld2.cStockID = mess
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
            
            cOld2 = StockFavDB.objects.create(cStockID = mess,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            cOld2.save()


        #以下寫入資料庫
        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
            cOld = models.StockFavs_jonyi.objects.get(cStockID = mess)

        #cOld.cItemName = Product_name
            cOld.cStockID = mess
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

            
            cOld.pubtime =realtime      
                 
            cOld.save()
            
            ###################
        except:  #針對沒有的，抓取資料存入資料庫

            cOld = models.StockFavs_jonyi.objects.create(cStockID = mess,cStockName = stock_name,cDBURL = xUrl,cScore1st = ScoreAve1,cScore2nd = ScoreAve2,cScore3rd = ScoreAve3,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            cOld.save()


   
    else:
        mess = "股票代號尚未送出！"


    return render(request, "common_enterStockFavAdmin.html", locals())

#############################################################################
##################################

#@permission_required('myapp.Can_enter_usersmain_test168', login_url='/login2/')
def usersmain_hakkai(request, pageindex=None):  #使用者功能首頁
	global page1u
	pagesize = 20  #8
	newsall = models.NewsUnit.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1u = 1
		newsunits0 = models.NewsUnit.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1u-2)*pagesize
		if start >= 0:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u -= 1
	elif pageindex=='2':
		start = page1u*pagesize
		if start < datasize:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u += 1
	elif pageindex=='3':
		start = (page1u-1)*pagesize
		newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1u

######################################################
	global page1
	pagesize = 20  #8
	newsall = models.StockFavs_hakkai.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1 = 1
		newsunits = models.StockFavs_hakkai.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1-2)*pagesize
		if start >= 0:
			newsunits = models.StockFavs_hakkai.objects.order_by('-id')[start:(start+pagesize)]
			page1 -= 1
	elif pageindex=='2':
		start = page1*pagesize
		if start < datasize:
			newsunits = models.StockFavs_hakkai.objects.order_by('-id')[start:(start+pagesize)]
			page1 += 1
	elif pageindex=='3':
		start = (page1-1)*pagesize
		newsunits = models.StockFavs_hakkai.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1
	return render(request, "usersmain_hakkai.html", locals())




#@permission_required('myapp.Can_enter_AdminOnly', login_url='/login/')
def newsdelete_hakkai(request, newsid=None, deletetype=None):  #刪除資料
	unit = models.StockFavs_hakkai.objects.get(id=newsid)  #讀取指定資料
	if deletetype == None:  #進入刪除頁面,顯示原有資料
		type = str(unit.cStockID.strip())
		#subject = unit.title
		#editor = unit.nickname
		#content = unit.message
		#date = unit.pubtime
	elif deletetype == '1':  #按刪除鈕
		unit.delete()
		return redirect('/usersmain_hakkai/')
	return render(request, "newsdelete_hakkai.html", locals())


def hakkai_StoFavlistall(request):
    segs = models.StockFavs_hakkai.objects.all().order_by('-cStockID')
    return render(request, "common_StoFavlistall.html", locals())


def hakkai_enterStockFavAdmin(request):  

        
    if request.method == "POST":  #假如是以POST方式才處理
        mess = request.POST['stockid']  #取得表單輸入內容
        mess2 = request.POST['monthid']
        
        stock_name = func2.GetStockName(mess)

        H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, New_up_profit, New_down_loss, risk_reward, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average, pNet1, pNet2, pNet3, pNet4, pNet4Average, H0, thisYear_Sum, theRest_Predict, H6, L6, Predict_EPS0, eps1N =PERsegx.PERsegx(mess, mess2)

        xUrl = "/ListallStockFavDB/" + str(mess) + "/"        

        try:
            c1 = DBz.objects.get(cStockID = mess)
            print(DBz)
            ScoreAve1 = c1.cAverageScore
            print(ScoreAve1)
        except:
            ScoreAve1 = "N/A"
            #c1 = DB1.objects.get(cStockID = mess)
            #ScoreAve1 = c1.cAverageScore
        
        try:
            c2 = DBy.objects.get(cStockID = mess)
            print(DBy)
            ScoreAve2 = c2.cAverageScore
        except:
            ScoreAve2 = "N/A"
            #c2 = DB2.objects.get(cStockID = mess)
            #ScoreAve2 = c2.cAverageScore
        
        try:
            c3 = DBx.objects.get(cStockID = mess)
            print(DBx)
            ScoreAve3 = c3.cAverageScore      
        except:
            ScoreAve3 = "N/A"
            #c3 = DB3.objects.get(cStockID = mess)
            #ScoreAve3 = c3.cAverageScore           
        #收集資料創建時間
        import datetime
        wholetime = str(datetime.datetime.now()) 
        realtime = wholetime[:16]  #取得獲取資料時間
        
        yeardateOnly = wholetime[:10]

        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
            cOld2 = StockFavDB.objects.get(cStockID = mess, cYearDate = yeardateOnly)#(cYearDate = yeardateOnly)
            
            #if str(cOld2.cYearDate) != str(yeardateOnly):
                
            #cDB = StockFavDB.objects.create(cStockID = mess,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            #cDB.save()
                
            #else:
                
            cOld2.cStockID = mess
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
            
            cOld2 = StockFavDB.objects.create(cStockID = mess,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            cOld2.save()


        #以下寫入資料庫
        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
            cOld = models.StockFavs_hakkai.objects.get(cStockID = mess)

        #cOld.cItemName = Product_name
            cOld.cStockID = mess
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

            
            cOld.pubtime =realtime      
                 
            cOld.save()
            
            ###################
        except:  #針對沒有的，抓取資料存入資料庫

            cOld = models.StockFavs_hakkai.objects.create(cStockID = mess,cStockName = stock_name,cDBURL = xUrl,cScore1st = ScoreAve1,cScore2nd = ScoreAve2,cScore3rd = ScoreAve3,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            cOld.save()


   
    else:
        mess = "股票代號尚未送出！"


    return render(request, "common_enterStockFavAdmin.html", locals())

#############################################################################
##################################

#@permission_required('myapp.Can_enter_usersmain_test168', login_url='/login2/')
def usersmain_bakylews(request, pageindex=None):  #使用者功能首頁
	global page1u
	pagesize = 20  #8
	newsall = models.NewsUnit.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1u = 1
		newsunits0 = models.NewsUnit.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1u-2)*pagesize
		if start >= 0:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u -= 1
	elif pageindex=='2':
		start = page1u*pagesize
		if start < datasize:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u += 1
	elif pageindex=='3':
		start = (page1u-1)*pagesize
		newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1u

######################################################
	global page1
	pagesize = 20  #8
	newsall = models.StockFavs_bakylews.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1 = 1
		newsunits = models.StockFavs_bakylews.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1-2)*pagesize
		if start >= 0:
			newsunits = models.StockFavs_bakylews.objects.order_by('-id')[start:(start+pagesize)]
			page1 -= 1
	elif pageindex=='2':
		start = page1*pagesize
		if start < datasize:
			newsunits = models.StockFavs_bakylews.objects.order_by('-id')[start:(start+pagesize)]
			page1 += 1
	elif pageindex=='3':
		start = (page1-1)*pagesize
		newsunits = models.StockFavs_bakylews.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1
	return render(request, "usersmain_bakylews.html", locals())




#@permission_required('myapp.Can_enter_AdminOnly', login_url='/login/')
def newsdelete_bakylews(request, newsid=None, deletetype=None):  #刪除資料
	unit = models.StockFavs_bakylews.objects.get(id=newsid)  #讀取指定資料
	if deletetype == None:  #進入刪除頁面,顯示原有資料
		type = str(unit.cStockID.strip())
		#subject = unit.title
		#editor = unit.nickname
		#content = unit.message
		#date = unit.pubtime
	elif deletetype == '1':  #按刪除鈕
		unit.delete()
		return redirect('/usersmain_bakylews/')
	return render(request, "newsdelete_bakylews.html", locals())


def bakylews_StoFavlistall(request):
    segs = models.StockFavs_bakylews.objects.all().order_by('-cStockID')
    return render(request, "common_StoFavlistall.html", locals())


def bakylews_enterStockFavAdmin(request):  

        
    if request.method == "POST":  #假如是以POST方式才處理
        mess = request.POST['stockid']  #取得表單輸入內容
        mess2 = request.POST['monthid']
        
        stock_name = func2.GetStockName(mess)

        H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, New_up_profit, New_down_loss, risk_reward, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average, pNet1, pNet2, pNet3, pNet4, pNet4Average, H0, thisYear_Sum, theRest_Predict, H6, L6, Predict_EPS0, eps1N =PERsegx.PERsegx(mess, mess2)

        xUrl = "/ListallStockFavDB/" + str(mess) + "/"        

        try:
            c1 = DBz.objects.get(cStockID = mess)
            print(DBz)
            ScoreAve1 = c1.cAverageScore
            print(ScoreAve1)
        except:
            ScoreAve1 = "N/A"
            #c1 = DB1.objects.get(cStockID = mess)
            #ScoreAve1 = c1.cAverageScore
        
        try:
            c2 = DBy.objects.get(cStockID = mess)
            print(DBy)
            ScoreAve2 = c2.cAverageScore
        except:
            ScoreAve2 = "N/A"
            #c2 = DB2.objects.get(cStockID = mess)
            #ScoreAve2 = c2.cAverageScore
        
        try:
            c3 = DBx.objects.get(cStockID = mess)
            print(DBx)
            ScoreAve3 = c3.cAverageScore      
        except:
            ScoreAve3 = "N/A"
            #c3 = DB3.objects.get(cStockID = mess)
            #ScoreAve3 = c3.cAverageScore            
        #收集資料創建時間
        import datetime
        wholetime = str(datetime.datetime.now()) 
        realtime = wholetime[:16]  #取得獲取資料時間
        
        yeardateOnly = wholetime[:10]

        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
            cOld2 = StockFavDB.objects.get(cStockID = mess, cYearDate = yeardateOnly)#(cYearDate = yeardateOnly)
            
            #if str(cOld2.cYearDate) != str(yeardateOnly):
                
            #cDB = StockFavDB.objects.create(cStockID = mess,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            #cDB.save()
                
            #else:
                
            cOld2.cStockID = mess
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
            
            cOld2 = StockFavDB.objects.create(cStockID = mess,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            cOld2.save()


        #以下寫入資料庫
        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
            cOld = models.StockFavs_bakylews.objects.get(cStockID = mess)

        #cOld.cItemName = Product_name
            cOld.cStockID = mess
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

            
            cOld.pubtime =realtime      
                 
            cOld.save()
            
            ###################
        except:  #針對沒有的，抓取資料存入資料庫

            cOld = models.StockFavs_bakylews.objects.create(cStockID = mess,cStockName = stock_name,cDBURL = xUrl,cScore1st = ScoreAve1,cScore2nd = ScoreAve2,cScore3rd = ScoreAve3,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            cOld.save()


   
    else:
        mess = "股票代號尚未送出！"


    return render(request, "common_enterStockFavAdmin.html", locals())

#############################################################################
def usersmain_chenchi(request, pageindex=None):  #使用者功能首頁
	global page1u
	pagesize = 20  #8
	newsall = models.NewsUnit.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1u = 1
		newsunits0 = models.NewsUnit.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1u-2)*pagesize
		if start >= 0:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u -= 1
	elif pageindex=='2':
		start = page1u*pagesize
		if start < datasize:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u += 1
	elif pageindex=='3':
		start = (page1u-1)*pagesize
		newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1u

######################################################
	global page1
	pagesize = 20  #8
	newsall = models.StockFavs_chenchi.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1 = 1
		newsunits = models.StockFavs_chenchi.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1-2)*pagesize
		if start >= 0:
			newsunits = models.StockFavs_chenchi.objects.order_by('-id')[start:(start+pagesize)]
			page1 -= 1
	elif pageindex=='2':
		start = page1*pagesize
		if start < datasize:
			newsunits = models.StockFavs_chenchi.objects.order_by('-id')[start:(start+pagesize)]
			page1 += 1
	elif pageindex=='3':
		start = (page1-1)*pagesize
		newsunits = models.StockFavs_chenchi.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1
	return render(request, "usersmain_chenchi.html", locals())




#@permission_required('myapp.Can_enter_AdminOnly', login_url='/login/')
def newsdelete_chenchi(request, newsid=None, deletetype=None):  #刪除資料
	unit = models.StockFavs_chenchi.objects.get(id=newsid)  #讀取指定資料
	if deletetype == None:  #進入刪除頁面,顯示原有資料
		type = str(unit.cStockID.strip())
		#subject = unit.title
		#editor = unit.nickname
		#content = unit.message
		#date = unit.pubtime
	elif deletetype == '1':  #按刪除鈕
		unit.delete()
		return redirect('/usersmain_chenchi/')
	return render(request, "newsdelete_chenchi.html", locals())


def chenchi_StoFavlistall(request):
    segs = models.StockFavs_chenchi.objects.all().order_by('-cStockID')
    return render(request, "common_StoFavlistall.html", locals())


def chenchi_enterStockFavAdmin(request):  

        
    if request.method == "POST":  #假如是以POST方式才處理
        mess = request.POST['stockid']  #取得表單輸入內容
        mess2 = request.POST['monthid']
        
        stock_name = func2.GetStockName(mess)

        H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, New_up_profit, New_down_loss, risk_reward, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average, pNet1, pNet2, pNet3, pNet4, pNet4Average, H0, thisYear_Sum, theRest_Predict, H6, L6, Predict_EPS0, eps1N =PERsegx.PERsegx(mess, mess2)

        xUrl = "/ListallStockFavDB/" + str(mess) + "/"        

        try:
            c1 = DBz.objects.get(cStockID = mess)
            print(DBz)
            ScoreAve1 = c1.cAverageScore
            print(ScoreAve1)
        except:
            ScoreAve1 = "N/A"
            #c1 = DB1.objects.get(cStockID = mess)
            #ScoreAve1 = c1.cAverageScore
        
        try:
            c2 = DBy.objects.get(cStockID = mess)
            print(DBy)
            ScoreAve2 = c2.cAverageScore
        except:
            ScoreAve2 = "N/A"
            #c2 = DB2.objects.get(cStockID = mess)
            #ScoreAve2 = c2.cAverageScore
        
        try:
            c3 = DBx.objects.get(cStockID = mess)
            print(DBx)
            ScoreAve3 = c3.cAverageScore      
        except:
            ScoreAve3 = "N/A"
            #c3 = DB3.objects.get(cStockID = mess)
            #ScoreAve3 = c3.cAverageScore           
        #收集資料創建時間
        import datetime
        wholetime = str(datetime.datetime.now()) 
        realtime = wholetime[:16]  #取得獲取資料時間
        
        yeardateOnly = wholetime[:10]

        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
            cOld2 = StockFavDB.objects.get(cStockID = mess, cYearDate = yeardateOnly)#(cYearDate = yeardateOnly)
            
            #if str(cOld2.cYearDate) != str(yeardateOnly):
                
            #cDB = StockFavDB.objects.create(cStockID = mess,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            #cDB.save()
                
            #else:
                
            cOld2.cStockID = mess
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
            
            cOld2 = StockFavDB.objects.create(cStockID = mess,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            cOld2.save()


        #以下寫入資料庫
        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
            cOld = models.StockFavs_chenchi.objects.get(cStockID = mess)

        #cOld.cItemName = Product_name
            cOld.cStockID = mess
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

            
            cOld.pubtime =realtime      
                 
            cOld.save()
            
            ###################
        except:  #針對沒有的，抓取資料存入資料庫

            cOld = models.StockFavs_chenchi.objects.create(cStockID = mess,cStockName = stock_name,cDBURL = xUrl,cScore1st = ScoreAve1,cScore2nd = ScoreAve2,cScore3rd = ScoreAve3,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            cOld.save()


   
    else:
        mess = "股票代號尚未送出！"


    return render(request, "common_enterStockFavAdmin.html", locals())



#############################################################################
#############################################################################

def usersmain_liusnow(request, pageindex=None):  #使用者功能首頁
	global page1u
	pagesize = 20  #8
	newsall = models.NewsUnit.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1u = 1
		newsunits0 = models.NewsUnit.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1u-2)*pagesize
		if start >= 0:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u -= 1
	elif pageindex=='2':
		start = page1u*pagesize
		if start < datasize:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u += 1
	elif pageindex=='3':
		start = (page1u-1)*pagesize
		newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1u

######################################################
	global page1
	pagesize = 20  #8
	newsall = models.StockFavs_liusnow.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1 = 1
		newsunits = models.StockFavs_liusnow.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1-2)*pagesize
		if start >= 0:
			newsunits = models.StockFavs_liusnow.objects.order_by('-id')[start:(start+pagesize)]
			page1 -= 1
	elif pageindex=='2':
		start = page1*pagesize
		if start < datasize:
			newsunits = models.StockFavs_liusnow.objects.order_by('-id')[start:(start+pagesize)]
			page1 += 1
	elif pageindex=='3':
		start = (page1-1)*pagesize
		newsunits = models.StockFavs_liusnow.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1
	return render(request, "usersmain_liusnow.html", locals())




#@permission_required('myapp.Can_enter_AdminOnly', login_url='/login/')
def newsdelete_liusnow(request, newsid=None, deletetype=None):  #刪除資料
	unit = models.StockFavs_liusnow.objects.get(id=newsid)  #讀取指定資料
	if deletetype == None:  #進入刪除頁面,顯示原有資料
		type = str(unit.cStockID.strip())
		#subject = unit.title
		#editor = unit.nickname
		#content = unit.message
		#date = unit.pubtime
	elif deletetype == '1':  #按刪除鈕
		unit.delete()
		return redirect('/usersmain_liusnow/')
	return render(request, "newsdelete_liusnow.html", locals())


def liusnow_StoFavlistall(request):
    segs = models.StockFavs_liusnow.objects.all().order_by('-cStockID')
    return render(request, "common_StoFavlistall.html", locals())


def liusnow_enterStockFavAdmin(request):  

        
    if request.method == "POST":  #假如是以POST方式才處理
        mess = request.POST['stockid']  #取得表單輸入內容
        mess2 = request.POST['monthid']
        
        stock_name = func2.GetStockName(mess)

        H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, New_up_profit, New_down_loss, risk_reward, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average, pNet1, pNet2, pNet3, pNet4, pNet4Average, H0, thisYear_Sum, theRest_Predict, H6, L6, Predict_EPS0, eps1N =PERsegx.PERsegx(mess, mess2)

        xUrl = "/ListallStockFavDB/" + str(mess) + "/"        

        try:
            c1 = DBz.objects.get(cStockID = mess)
            print(DBz)
            ScoreAve1 = c1.cAverageScore
            print(ScoreAve1)
        except:
            ScoreAve1 = "N/A"
            #c1 = DB1.objects.get(cStockID = mess)
            #ScoreAve1 = c1.cAverageScore
        
        try:
            c2 = DBy.objects.get(cStockID = mess)
            print(DBy)
            ScoreAve2 = c2.cAverageScore
        except:
            ScoreAve2 = "N/A"
            #c2 = DB2.objects.get(cStockID = mess)
            #ScoreAve2 = c2.cAverageScore
        
        try:
            c3 = DBx.objects.get(cStockID = mess)
            print(DBx)
            ScoreAve3 = c3.cAverageScore      
        except:
            ScoreAve3 = "N/A"
            #c3 = DB3.objects.get(cStockID = mess)
            #ScoreAve3 = c3.cAverageScore            
        #收集資料創建時間
        import datetime
        wholetime = str(datetime.datetime.now()) 
        realtime = wholetime[:16]  #取得獲取資料時間
        
        yeardateOnly = wholetime[:10]

        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
            cOld2 = StockFavDB.objects.get(cStockID = mess, cYearDate = yeardateOnly)#(cYearDate = yeardateOnly)
            
            #if str(cOld2.cYearDate) != str(yeardateOnly):
                
            #cDB = StockFavDB.objects.create(cStockID = mess,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            #cDB.save()
                
            #else:
                
            cOld2.cStockID = mess
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
            
            cOld2 = StockFavDB.objects.create(cStockID = mess,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            cOld2.save()


        #以下寫入資料庫
        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
            cOld = models.StockFavs_liusnow.objects.get(cStockID = mess)

        #cOld.cItemName = Product_name
            cOld.cStockID = mess
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

            
            cOld.pubtime =realtime      
                 
            cOld.save()
            
            ###################
        except:  #針對沒有的，抓取資料存入資料庫

            cOld = models.StockFavs_liusnow.objects.create(cStockID = mess,cStockName = stock_name,cDBURL = xUrl,cScore1st = ScoreAve1,cScore2nd = ScoreAve2,cScore3rd = ScoreAve3,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            cOld.save()


   
    else:
        mess = "股票代號尚未送出！"


    return render(request, "common_enterStockFavAdmin.html", locals())

#############################################################################
#############################################################################


#############################################################################
#############################################################################

def usersmain_magicjohn(request, pageindex=None):  #使用者功能首頁
	global page1u
	pagesize = 20  #8
	newsall = models.NewsUnit.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1u = 1
		newsunits0 = models.NewsUnit.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1u-2)*pagesize
		if start >= 0:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u -= 1
	elif pageindex=='2':
		start = page1u*pagesize
		if start < datasize:
			newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1u += 1
	elif pageindex=='3':
		start = (page1u-1)*pagesize
		newsunits0 = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1u

######################################################
	global page1
	pagesize = 20  #8
	newsall = models.StockFavs_magicjohn.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1 = 1
		newsunits = models.StockFavs_magicjohn.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1-2)*pagesize
		if start >= 0:
			newsunits = models.StockFavs_magicjohn.objects.order_by('-id')[start:(start+pagesize)]
			page1 -= 1
	elif pageindex=='2':
		start = page1*pagesize
		if start < datasize:
			newsunits = models.StockFavs_magicjohn.objects.order_by('-id')[start:(start+pagesize)]
			page1 += 1
	elif pageindex=='3':
		start = (page1-1)*pagesize
		newsunits = models.StockFavs_magicjohn.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1
	return render(request, "usersmain_magicjohn.html", locals())




#@permission_required('myapp.Can_enter_AdminOnly', login_url='/login/')
def newsdelete_magicjohn(request, newsid=None, deletetype=None):  #刪除資料
	unit = models.StockFavs_magicjohn.objects.get(id=newsid)  #讀取指定資料
	if deletetype == None:  #進入刪除頁面,顯示原有資料
		type = str(unit.cStockID.strip())
		#subject = unit.title
		#editor = unit.nickname
		#content = unit.message
		#date = unit.pubtime
	elif deletetype == '1':  #按刪除鈕
		unit.delete()
		return redirect('/usersmain_magicjohn/')
	return render(request, "newsdelete_magicjohn.html", locals())


def magicjohn_StoFavlistall(request):
    segs = models.StockFavs_magicjohn.objects.all().order_by('-cStockID')
    return render(request, "common_StoFavlistall.html", locals())


def magicjohn_enterStockFavAdmin(request):  

        
    if request.method == "POST":  #假如是以POST方式才處理
        mess = request.POST['stockid']  #取得表單輸入內容
        mess2 = request.POST['monthid']
        
        stock_name = func2.GetStockName(mess)

        H1, H2, H3, H4, H5, L1, L2, L3, L4, L5, eps1, eps2, eps3, eps4, eps5, PER_H1, PER_H2, PER_H3, PER_H4, PER_H5, PER_L1, PER_L2, PER_L3, PER_L4, PER_L5, PER_H_average, PER_L_average, PER_H, PER_L, rYoY1N, rYoY2N, rYoY3N, rYoY4N, rYoY5N, rYoY6N, rYoY1, rYoY2, rYoY3, rYoY4, rYoY5, rYoY6, RevYoY, rYoY6Average, r1N, r2N, r3N, r4N, r5N, r6N, r7N, r8N, r9N, r10N, r11N, r12N, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, Rev_Predict, Net1N, Net2N, Net3N, Net4N, Net1, Net2, Net3, Net4, Net4Average, Net_Predict, capital_stock, Predict_EPS, Predict_high_price, Predict_low_price, yahoo_latest_tradePrice, New_up_profit, New_down_loss, risk_reward, pYoY1, pYoY2, pYoY3, pYoY4, pYoY5, pYoY6, pRevYoY, pYoY6Average, pNet1, pNet2, pNet3, pNet4, pNet4Average, H0, thisYear_Sum, theRest_Predict, H6, L6, Predict_EPS0, eps1N =PERsegx.PERsegx(mess, mess2)

        xUrl = "/ListallStockFavDB/" + str(mess) + "/"        

        try:
            c1 = DBz.objects.get(cStockID = mess)
            print(DBz)
            ScoreAve1 = c1.cAverageScore
            print(ScoreAve1)
        except:
            ScoreAve1 = "N/A"
            #c1 = DB1.objects.get(cStockID = mess)
            #ScoreAve1 = c1.cAverageScore
        
        try:
            c2 = DBy.objects.get(cStockID = mess)
            print(DBy)
            ScoreAve2 = c2.cAverageScore
        except:
            ScoreAve2 = "N/A"
            #c2 = DB2.objects.get(cStockID = mess)
            #ScoreAve2 = c2.cAverageScore
        
        try:
            c3 = DBx.objects.get(cStockID = mess)
            print(DBx)
            ScoreAve3 = c3.cAverageScore      
        except:
            ScoreAve3 = "N/A"
            #c3 = DB3.objects.get(cStockID = mess)
            #ScoreAve3 = c3.cAverageScore           
        #收集資料創建時間
        import datetime
        wholetime = str(datetime.datetime.now()) 
        realtime = wholetime[:16]  #取得獲取資料時間
        
        yeardateOnly = wholetime[:10]

        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
            cOld2 = StockFavDB.objects.get(cStockID = mess, cYearDate = yeardateOnly)#(cYearDate = yeardateOnly)
            
            #if str(cOld2.cYearDate) != str(yeardateOnly):
                
            #cDB = StockFavDB.objects.create(cStockID = mess,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            #cDB.save()
                
            #else:
                
            cOld2.cStockID = mess
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
            
            cOld2 = StockFavDB.objects.create(cStockID = mess,cStockName = stock_name,cYearDate = yeardateOnly,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            cOld2.save()


        #以下寫入資料庫
        try:  #先試著看料庫有沒有這個股票，若沒有 跳到except處理
            #不存在，發生錯誤，跳到except            
            cOld = models.StockFavs_magicjohn.objects.get(cStockID = mess)

        #cOld.cItemName = Product_name
            cOld.cStockID = mess
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

            
            cOld.pubtime =realtime      
                 
            cOld.save()
            
            ###################
        except:  #針對沒有的，抓取資料存入資料庫

            cOld = models.StockFavs_magicjohn.objects.create(cStockID = mess,cStockName = stock_name,cDBURL = xUrl,cScore1st = ScoreAve1,cScore2nd = ScoreAve2,cScore3rd = ScoreAve3,cPredict_EPS = Predict_EPS,cPredict_high_price = Predict_high_price,cPredict_low_price = Predict_low_price,cNew_up_profit = New_up_profit,cNew_down_loss = New_down_loss,cRisk_reward = risk_reward,cTodayClose = float(yahoo_latest_tradePrice),pubtime =realtime)              

            cOld.save()


   
    else:
        mess = "股票代號尚未送出！"


    return render(request, "common_enterStockFavAdmin.html", locals())