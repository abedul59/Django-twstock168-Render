"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from myapp import views
from django.conf.urls import url



from myapp.views import UsersListAll

from myapp.views import stock6
from myapp.views import stock6x
from myapp.views import stock6getOne
from myapp.views import stock6getOneAdmin


from myapp.views import stock6TSE
from myapp.views import stock6OTC

from myapp.views import stock6Admin
from myapp.views import stock6xAdmin
from myapp.views import stock6AdminGL

#from myapp.views import stock6AdminTB


from myapp.views import stock6AdminTB1M
from myapp.views import stock6AdminTB1S
from myapp.views import stock6AdminTB1S1M

from myapp.views import stock6AdminTB2M
from myapp.views import stock6AdminTB1S2M



from myapp.views import stockprice

from myapp.views import stockPrice5y
#from myapp.views import stockPERseg
from myapp.views import stockPERsegx
from myapp.views import stockPERseg2
from myapp.views import stockPERseg2b
from myapp.views import stockPERseg3
from myapp.views import stockPERseg3b

from myapp.views import stockPERsegAdmin
from myapp.views import stockPERsegPEG

from myapp.views import stockPERsegStable
from myapp.views import stockPERsegStableAdmin

from myapp.views import index2
from myapp.views import login2
from myapp.views import logout2
from myapp.views import adduser
from myapp.views import signup

##############
from myapp.views import index
from myapp.views import login
from myapp.views import logout
from myapp.views import detail
from myapp.views import adminmain
from myapp.views import newsadd
from myapp.views import newsedit
from myapp.views import newsdelete
from myapp.views import detail

#from myapp.views import listone
#from myapp.views import listall
from myapp.views import usersmain



from myapp.views import listallscore
from myapp.views import listallseg
from myapp.views import listallsegscore

from myapp.views import Epsachiever
from myapp.views import EpsachieverAdmin

from myapp.views import listallEPS
from myapp.views import EPSachieve2020Q2listall

from myapp.views import StockCapGetter
from myapp.views import StockCapGetterAdmin
from myapp.views import listallCAP
from myapp.views import StockCapVar2020Q2listall

from myapp.views import stock6listall202005
from myapp.views import stock6listall202005score

from myapp.views import stock6listall202006
from myapp.views import stock6listall202006score

from myapp.views import stock6listall2020Q2
from myapp.views import stock6listall2020Q2score

from myapp.views import stock6listall202008
from myapp.views import stock6listall202008score

from myapp.views import stock6listall202009
from myapp.views import stock6listall202009score

from myapp.views import stock6listall2020Q3
from myapp.views import stock6listall2020Q3score


from myapp.views import stock6listall202009test
#from myapp.views import stock6listall202009tse
#from myapp.views import stock6listall202009otc

#from myapp.views import stock6listall2020Q3tse
#from myapp.views import stock6listall2020Q3otc

from myapp.views import stockPERseglistall202005
from myapp.views import stockPERseglistall202005score

from myapp.views import stockPERseglistall202006
from myapp.views import stockPERseglistall202006score


from myapp.views import stockPERseglistall2020Q2
from myapp.views import stockPERseglistall2020Q2score

from myapp.views import stockPERseglistall202009
from myapp.views import stockPERseglistall202009score

from myapp.views import stockPERseglistall2020Q3
from myapp.views import stockPERseglistall2020Q3score


from myapp.views import EPSnProfitGetter
from myapp.views import EPSnProfitGetterAdmin

from myapp.views import EPSnProfitlistall2020Q1
from myapp.views import EPSnProfit2020Q2listall

from myapp.views import stockPERsegStablelistall2020
from myapp.views import stockPERsegStablelistall2020Q2

from myapp.views import AREAdownloads

from myapp.views import stock6downloads
from myapp.views import stockPERsegdownloads
from myapp.views import stockEnterAlldownloads

from myapp.views import BigMoney


from myapp.views import stockPERsegDiv




urlpatterns = [
    
 	path('home/', views.home, name='home'),
	path('population-chart/', views.population_chart, name='population-chart'),
	path('pie-chart/', views.pie_chart, name='pie-chart'),

	path('stock6x_chart/', views.stock6x_chart, name='stock6x_chart'),
    
    path('admin/', admin.site.urls),
    #path('home/', home),
    path('', index),





    path('UsersListAll/', UsersListAll),


    path('viewsISQuery/', views.viewsISQuery),
    path('viewsBSQuery/', views.viewsBSQuery),


    path('stock6/', views.stock6),
    path('stock6x/', views.stock6x),
    path('stock6xDB/', views.stock6xDB),
    path('stockKn/', views.stockKn),

    path('stock6xapp/', views.stock6xapp),


    
    path('stock6getOne/', stock6getOne),
    path('stock6getOneAdmin/', views.stock6getOneAdmin),
    path('stock6getOneH2VAdmin/', views.stock6getOneH2VAdmin),
    path('stock6getOneH2V2Admin/', views.stock6getOneH2V2Admin),

    path('stock6Admin/', stock6Admin),
    path('stock6xAdmin/', stock6xAdmin),     
    path('stock6AdminGL/', stock6AdminGL),



    path('stock6AdminTB1S/', stock6AdminTB1S),        
    path('stock6AdminTB1M/', stock6AdminTB1M),
    path('stock6AdminTB1S1M/', stock6AdminTB1S1M),


    path('stock6AdminTB2M/', stock6AdminTB2M),       
    path('stock6AdminTB1S2M/', stock6AdminTB1S2M),

    path('stock6TSE/', stock6TSE),
    path('stock6OTC/', stock6OTC),
    path('stock6SubCats/', views.stock6SubCats),
    path('stock6SubCatsAdmin/', views.stock6SubCatsAdmin),
    path('stock6Concepts/', views.stock6Concepts),
    

    
    path('stockprice/', stockprice),


    path('stockPrice5y/', stockPrice5y),
    path('stockPrice5yAdmin/', views.stockPrice5yAdmin),
    path('stockNetCapAdmin/', views.stockNetCapAdmin),    
 
    #path('stockPERseg/', views.stockPERseg),
    path('stockPERsegx/', views.stockPERsegx),
    path('stockPERsegxapp/', views.stockPERsegxapp),
    path('stockPERsegxMain/', views.stockPERsegxMain),   
    
    path('stockPERsegxDB/', views.stockPERsegxDB),

    path('stockPERseg2/', stockPERseg2),
    path('stockPERseg2xDB/', views.stockPERseg2xDB),    
    
    path('stockPERseg2b/', stockPERseg2b),
    path('stockPERseg2bxDB/', views.stockPERseg2bxDB),

    path('stockPERseg3/', stockPERseg3),
    path('stockPERseg3xDB/', views.stockPERseg3xDB),   
    
    
    path('stockPERseg3b/', stockPERseg3b),
    path('stockPERsegAdmin/', stockPERsegAdmin), 
    path('stockPERsegPEG/', views.stockPERsegPEG),
    path('stockPERsegPEGMain/', views.stockPERsegPEGMain),
    path('stockPERsegPEGxDB/', views.stockPERsegPEGxDB),    
    
    
    path('stockPERsegStable/', stockPERsegStable),
    path('stockPERsegStableAdmin/', stockPERsegStableAdmin),
    
    path('index2/', index2),
    path('login2/', login2),
    path('logout2/', logout2),
    path('adduser/', adduser),
    path('signup/', signup),

    path('login3/', views.login3),    
    path('logout3/', views.logout3),


    path('listallscore/', listallscore),    
    path('listallseg/', listallseg), 
    path('listallsegscore/', listallsegscore), 
   
    
    path('index/', index),
    path('login/', login),
    path('logout/', logout),
  
    
    re_path(r'^detail/(\d+)/$', views.detail),
    re_path(r'^adminmain/$', views.adminmain),
	re_path(r'^adminmain/(\d+)/$', views.adminmain),
 	re_path(r'^newsadd/$', views.newsadd),
	re_path(r'^newsedit/(\d+)/$', views.newsedit),
	re_path(r'^newsedit/(\d+)/(\d+)/$', views.newsedit),
	re_path(r'^newsdelete/(\d+)/$', views.newsdelete),
	re_path(r'^newsdelete/(\d+)/(\d+)/$', views.newsdelete),

    
    re_path(r'^usersmain/$', views.usersmain),
	re_path(r'^usersmain/(\d+)/$', views.usersmain),

##############################
    path('usersmain_common/', views.usersmain_common),  
    path('usersmain_common/<str:username>/', views.usersmain_common), 
    path('usersmain_common/<str:username>/<int:pageindex>/', views.usersmain_common),

	path('newsdelete_common/<str:username>/', views.newsdelete_common),
	path('newsdelete_common/<str:username>/<int:newsid>/', views.newsdelete_common),    
	path('newsdelete_common/<str:username>/<int:newsid>/<int:deletetype>/', views.newsdelete_common),    
	#path('newsdelete_common/(\d+)/(\d+)/$', views.newsdelete_common),        

    path('common_enterStockFavAdmin/', views.common_enterStockFavAdmin),  
    path('common_enterStockFavAdmin/<str:username>/', views.common_enterStockFavAdmin),      
    
    
    path('common_StoFavlistall/', views.common_StoFavlistall),
    path('common_StoFavlistall/<str:username>/', views.common_StoFavlistall),
####################################



    #re_path(r'^usersmain_common/$', views.usersmain_common),
	#re_path(r'^usersmain_common/(\d+)/$', views.usersmain_common),


    re_path(r'^usersmain_app/$', views.usersmain_app),
	re_path(r'^usersmain_app/(\d+)/$', views.usersmain_app),


    re_path(r'^usersmain_test168/$', views.usersmain_test168),
	re_path(r'^usersmain_test168/(\d+)/$', views.usersmain_test168),
	re_path(r'^newsdelete_test168/(\d+)/$', views.newsdelete_test168),
	re_path(r'^newsdelete_test168/(\d+)/(\d+)/$', views.newsdelete_test168),        
    #path('test168_enterStockFav/', views.test168_enterStockFav),    
    path('test168_enterStockFavAdmin/', views.test168_enterStockFavAdmin),  
    path('test168_StoFavlistall/', views.test168_StoFavlistall),

    path('ListallStockFavDB/<str:mess>/', views.ListallStockFavDB),
    path('ListallStockFavDB/', views.ListallStockFavDB),
    #bobmax首頁
    re_path(r'^usersmain_bobmax/$', views.usersmain_bobmax),
	re_path(r'^usersmain_bobmax/(\d+)/$', views.usersmain_bobmax),
	re_path(r'^newsdelete_bobmax/(\d+)/$', views.newsdelete_bobmax),
	re_path(r'^newsdelete_bobmax/(\d+)/(\d+)/$', views.newsdelete_bobmax),        
    path('bobmax_enterStockFavAdmin/', views.bobmax_enterStockFavAdmin),  
    path('bobmax_StoFavlistall/', views.bobmax_StoFavlistall),

    #deno36首頁
    re_path(r'^usersmain_deno36/$', views.usersmain_deno36),
	re_path(r'^usersmain_deno36/(\d+)/$', views.usersmain_deno36),
	re_path(r'^newsdelete_deno36/(\d+)/$', views.newsdelete_deno36),
	re_path(r'^newsdelete_deno36/(\d+)/(\d+)/$', views.newsdelete_deno36),        
    path('deno36_enterStockFavAdmin/', views.deno36_enterStockFavAdmin),  
    path('deno36_StoFavlistall/', views.deno36_StoFavlistall),

    #donhonlin首頁
    re_path(r'^usersmain_donhonlin/$', views.usersmain_donhonlin),
	re_path(r'^usersmain_donhonlin/(\d+)/$', views.usersmain_donhonlin),
	re_path(r'^newsdelete_donhonlin/(\d+)/$', views.newsdelete_donhonlin),
	re_path(r'^newsdelete_donhonlin/(\d+)/(\d+)/$', views.newsdelete_donhonlin),        
    path('donhonlin_enterStockFavAdmin/', views.donhonlin_enterStockFavAdmin),  
    path('donhonlin_StoFavlistall/', views.donhonlin_StoFavlistall),


    #goldsilver首頁
    re_path(r'^usersmain_goldsilver/$', views.usersmain_goldsilver),
	re_path(r'^usersmain_goldsilver/(\d+)/$', views.usersmain_goldsilver),
	re_path(r'^newsdelete_goldsilver/(\d+)/$', views.newsdelete_goldsilver),
	re_path(r'^newsdelete_goldsilver/(\d+)/(\d+)/$', views.newsdelete_goldsilver),        
    path('goldsilver_enterStockFavAdmin/', views.goldsilver_enterStockFavAdmin),  
    path('goldsilver_StoFavlistall/', views.goldsilver_StoFavlistall),

    #hyeth首頁
    re_path(r'^usersmain_hyeth/$', views.usersmain_hyeth),
	re_path(r'^usersmain_hyeth/(\d+)/$', views.usersmain_hyeth),
	re_path(r'^newsdelete_hyeth/(\d+)/$', views.newsdelete_hyeth),
	re_path(r'^newsdelete_hyeth/(\d+)/(\d+)/$', views.newsdelete_hyeth),        
    path('hyeth_enterStockFavAdmin/', views.hyeth_enterStockFavAdmin),  
    path('hyeth_StoFavlistall/', views.hyeth_StoFavlistall),

    #jonyi首頁
    re_path(r'^usersmain_jonyi/$', views.usersmain_jonyi),
	re_path(r'^usersmain_jonyi/(\d+)/$', views.usersmain_jonyi),
	re_path(r'^newsdelete_jonyi/(\d+)/$', views.newsdelete_jonyi),
	re_path(r'^newsdelete_jonyi/(\d+)/(\d+)/$', views.newsdelete_jonyi),        
    path('jonyi_enterStockFavAdmin/', views.jonyi_enterStockFavAdmin),  
    path('jonyi_StoFavlistall/', views.jonyi_StoFavlistall),

    #hakkai首頁
    re_path(r'^usersmain_hakkai/$', views.usersmain_hakkai),
	re_path(r'^usersmain_hakkai/(\d+)/$', views.usersmain_hakkai),
	re_path(r'^newsdelete_hakkai/(\d+)/$', views.newsdelete_hakkai),
	re_path(r'^newsdelete_hakkai/(\d+)/(\d+)/$', views.newsdelete_hakkai),        
    path('hakkai_enterStockFavAdmin/', views.hakkai_enterStockFavAdmin),  
    path('hakkai_StoFavlistall/', views.hakkai_StoFavlistall),


    #bakylews首頁
    re_path(r'^usersmain_bakylews/$', views.usersmain_bakylews),
	re_path(r'^usersmain_bakylews/(\d+)/$', views.usersmain_bakylews),
	re_path(r'^newsdelete_bakylews/(\d+)/$', views.newsdelete_bakylews),
	re_path(r'^newsdelete_bakylews/(\d+)/(\d+)/$', views.newsdelete_bakylews),        
    path('bakylews_enterStockFavAdmin/', views.bakylews_enterStockFavAdmin),  
    path('bakylews_StoFavlistall/', views.bakylews_StoFavlistall),


    #chenchi首頁
    re_path(r'^usersmain_chenchi/$', views.usersmain_chenchi),
	re_path(r'^usersmain_chenchi/(\d+)/$', views.usersmain_chenchi),
	re_path(r'^newsdelete_chenchi/(\d+)/$', views.newsdelete_chenchi),
	re_path(r'^newsdelete_chenchi/(\d+)/(\d+)/$', views.newsdelete_chenchi),        
    path('chenchi_enterStockFavAdmin/', views.chenchi_enterStockFavAdmin),  
    path('chenchi_StoFavlistall/', views.chenchi_StoFavlistall),



    #magicjohn首頁
    re_path(r'^usersmain_magicjohn/$', views.usersmain_magicjohn),
	re_path(r'^usersmain_magicjohn/(\d+)/$', views.usersmain_magicjohn),
	re_path(r'^newsdelete_magicjohn/(\d+)/$', views.newsdelete_magicjohn),
	re_path(r'^newsdelete_magicjohn/(\d+)/(\d+)/$', views.newsdelete_magicjohn),        
    path('magicjohn_enterStockFavAdmin/', views.magicjohn_enterStockFavAdmin),  
    path('magicjohn_StoFavlistall/', views.magicjohn_StoFavlistall),



    
    path('Epsachiever/', Epsachiever),
    path('EpsachieverAdmin/', EpsachieverAdmin),
    path('listallEPS/', listallEPS), 
    
    path('StockCapGetter/', StockCapGetter),
    path('StockCapGetterAdmin/', StockCapGetterAdmin),
    path('listallCAP/', listallCAP), 
    
    
    
    path('EPSnProfitGetter/', EPSnProfitGetter),
    path('EPSnProfitGetterAdmin/', EPSnProfitGetterAdmin),

    ####六大指標    
    path('stock6listall202005/', stock6listall202005),
    path('stock6listall202006/', stock6listall202006),    
    path('stock6listall2020Q2/', stock6listall2020Q2),      
    
    path('stock6listall202005score/', stock6listall202005score),    
    path('stock6listall202006score/', stock6listall202006score),    
    path('stock6listall2020Q2score/', stock6listall2020Q2score), 
    
    path('stock6listall202008/', stock6listall202008),
    path('stock6listall202008score/', stock6listall202008score),  
    
    path('stock6listall202009/', stock6listall202009),
    path('stock6listall202009score/', stock6listall202009score),  
    
    
    path('stock6listall2020Q3/', stock6listall2020Q3),
    path('stock6listall2020Q3score/', stock6listall2020Q3score),  
    
    path('stock6listall202011/', views.stock6listall202011),
    path('stock6listall202011score/', views.stock6listall202011score),

    path('stock6listall2020Q4/', views.stock6listall2020Q4),
    path('stock6listall2020Q4score/', views.stock6listall2020Q4score),

    path('stock6listall202101/', views.stock6listall202101),
    path('stock6listall202101score/', views.stock6listall202101score),

    path('stock6listall202102/', views.stock6listall202102),
    path('stock6listall202102score/', views.stock6listall202102score),

    path('stock6listall202103/', views.stock6listall202103),
    path('stock6listall202103score/', views.stock6listall202103score),
    
    path('stock6listall202104/', views.stock6listall202104),
    path('stock6listall202104score/', views.stock6listall202104score),    
 
    path('stock6listall202105/', views.stock6listall202105),
    path('stock6listall202105score/', views.stock6listall202105score), 
    #path('stock6sta2021/', views.stock6sta2021), #統計總表

    #path('stock6sta202105/', views.stock6sta202105),
    #path('stock6sta202106/', views.stock6sta202106),
    
    
    path('stock6listall202105/', views.stock6listall202105),
    path('stock6listall202105score/', views.stock6listall202105score),    

    path('stock6listall202106/', views.stock6listall202106),
    path('stock6listall202106score/', views.stock6listall202106score),    

    path('stock6listall202107/', views.stock6listall202107),
    path('stock6listall202107score/', views.stock6listall202107score),  

    path('stock6listall202108/', views.stock6listall202108),
    path('stock6listall202108score/', views.stock6listall202108score), 

    path('stock6listall202109/', views.stock6listall202109),
    path('stock6listall202109score/', views.stock6listall202109score), 
    
    path('stock6listall202110/', views.stock6listall202110),
    path('stock6listall202110score/', views.stock6listall202110score), 
    
    path('stock6listall202111/', views.stock6listall202111),
    path('stock6listall202111score/', views.stock6listall202111score), 
    
    path('stock6listall202112/', views.stock6listall202112),
    path('stock6listall202112score/', views.stock6listall202112score),
    
    path('stock6listall202201/', views.stock6listall202201),
    path('stock6listall202201score/', views.stock6listall202201score),    
    path('stock6listall202202/', views.stock6listall202202),
    path('stock6listall202202score/', views.stock6listall202202score),    
    path('stock6listall202203/', views.stock6listall202203),
    path('stock6listall202203score/', views.stock6listall202203score),        
    path('stock6listall202204/', views.stock6listall202204),
    path('stock6listall202204score/', views.stock6listall202204score),
    path('stock6listall202205/', views.stock6listall202205),
    path('stock6listall202205score/', views.stock6listall202205score),
    path('stock6listall202206/', views.stock6listall202206),
    path('stock6listall202206score/', views.stock6listall202206score),
    path('stock6listall202207/', views.stock6listall202207),
    path('stock6listall202207score/', views.stock6listall202207score),    
    path('stock6listall202208/', views.stock6listall202208),
    path('stock6listall202208score/', views.stock6listall202208score), 
    path('stock6listall202209/', views.stock6listall202209),
    path('stock6listall202209score/', views.stock6listall202209score),
    path('stock6listall202210/', views.stock6listall202210),
    path('stock6listall202210score/', views.stock6listall202210score),



    path('stock6listall202208v/', views.stock6listall202208v),
    
    path('DCstock6listall202011/', views.DCstock6listall202011),
    path('DCstock6listall2020Q4/', views.DCstock6listall2020Q4),
    path('DCstock6listall202101/', views.DCstock6listall202101),
    path('DCstock6listall202102/', views.DCstock6listall202102),
    path('DCstock6listall202103/', views.DCstock6listall202103),
    path('DCstock6listall202104/', views.DCstock6listall202104),
    path('DCstock6listall202105/', views.DCstock6listall202105),
    path('DCstock6listall202106/', views.DCstock6listall202106),
    path('DCstock6listall202107/', views.DCstock6listall202107),
    path('DCstock6listall202108/', views.DCstock6listall202108),
    path('DCstock6listall202109/', views.DCstock6listall202109),
    path('DCstock6listall202110/', views.DCstock6listall202110),
    path('DCstock6listall202111/', views.DCstock6listall202111),
    path('DCstock6listall202112/', views.DCstock6listall202112),
###########################################################################################
    
    
    
    path('stock6listall202009test/', stock6listall202009test),
  
    
    #path('stock6listall202102tse/<str:mess>/', views.stock6listall202102tse),
    path('stock6listalltse/<str:mess>/', views.stock6listalltse),


    #path('stock6listall202102otc/<str:mess>/', views.stock6listall202102otc),     
    path('stock6listallotc/<str:mess>/', views.stock6listallotc),     

    #path('stock6listall202102Concepts/<str:mess>/', views.stock6listall202102Concepts)
    path('stock6listallConcepts/<str:mess>/', views.stock6listallConcepts),
    #path('stock6listall202102SubCats/<str:mess>/', views.stock6listall202102SubCats),     
    path('stock6listallSubCats/<str:mess>/', views.stock6listallSubCats),     


    #path('stock6listall202102SubCatsAdmin/<str:mess>/', views.stock6listall202102SubCatsAdmin),
    path('stock6listallSubCatsAdmin/<str:mess>/<str:mess_db1>/<str:mess_db2>/', views.stock6listallSubCatsAdmin),
 
###############################################################################################    
    
    
    ####本益比區間
    path('stockPERseglistall202005/', stockPERseglistall202005),
    path('stockPERseglistall202005score/', stockPERseglistall202005score),

    path('stockPERseglistall202006/', stockPERseglistall202006),
    path('stockPERseglistall202006score/', stockPERseglistall202006score),    

    path('stockPERseglistall2020Q2/', stockPERseglistall2020Q2),
    path('stockPERseglistall2020Q2score/', stockPERseglistall2020Q2score), 

    path('stockPERseglistall202008/', views.stockPERseglistall202008),
    path('stockPERseglistall202008score/', views.stockPERseglistall202008score),  

    path('stockPERseglistall202009/', stockPERseglistall202009),
    path('stockPERseglistall202009score/', stockPERseglistall202009score),  

    path('stockPERseglistall2020Q3/', stockPERseglistall2020Q3),
    path('stockPERseglistall2020Q3score/', stockPERseglistall2020Q3score),
    
    path('stockPERseglistall202011/', views.stockPERseglistall202011),
    path('stockPERseglistall202011score/', views.stockPERseglistall202011score),    

    path('stockPERseglistall2020Q4/', views.stockPERseglistall2020Q4),
    path('stockPERseglistall2020Q4score/', views.stockPERseglistall2020Q4score), 
    
    path('stockPERseglistall202101/', views.stockPERseglistall202101),
    path('stockPERseglistall202101score/', views.stockPERseglistall202101score), 

    path('stockPERseglistall202102/', views.stockPERseglistall202102),
    path('stockPERseglistall202102score/', views.stockPERseglistall202102score), 

    path('stockPERseglistall202103/', views.stockPERseglistall202103),
    path('stockPERseglistall202103score/', views.stockPERseglistall202103score), 

    path('stockPERseglistall202104/', views.stockPERseglistall202104),
    path('stockPERseglistall202104score/', views.stockPERseglistall202104score), 

    path('stockPERseglistall202105/', views.stockPERseglistall202105),
    path('stockPERseglistall202105score/', views.stockPERseglistall202105score), 

    path('stockPERseglistall202106/', views.stockPERseglistall202106),
    path('stockPERseglistall202106score/', views.stockPERseglistall202106score), 

    path('stockPERseglistall202107/', views.stockPERseglistall202107),
    path('stockPERseglistall202107score/', views.stockPERseglistall202107score), 
    
    path('stockPERseglistall202108/', views.stockPERseglistall202108),
    path('stockPERseglistall202108score/', views.stockPERseglistall202108score), 
    
    path('stockPERseglistall202109/', views.stockPERseglistall202109),
    path('stockPERseglistall202109score/', views.stockPERseglistall202109score), 

    path('stockPERseglistall202110/', views.stockPERseglistall202110),
    path('stockPERseglistall202110score/', views.stockPERseglistall202110score), 

    path('stockPERseglistall202111/', views.stockPERseglistall202111),
    path('stockPERseglistall202111score/', views.stockPERseglistall202111score), 
    
    path('stockPERseglistall202112/', views.stockPERseglistall202112),
    path('stockPERseglistall202112score/', views.stockPERseglistall202112score), 

    path('stockPERseglistall202201/', views.stockPERseglistall202201),
    path('stockPERseglistall202201score/', views.stockPERseglistall202201score),
    
    path('stockPERseglistall202202/', views.stockPERseglistall202202),
    path('stockPERseglistall202202score/', views.stockPERseglistall202202score),
    
    path('stockPERseglistall202203/', views.stockPERseglistall202203),
    path('stockPERseglistall202203score/', views.stockPERseglistall202203score),

    path('stockPERseglistall202204/', views.stockPERseglistall202204),
    path('stockPERseglistall202204score/', views.stockPERseglistall202204score),
    
    
    path('stockPERseglistall202205/', views.stockPERseglistall202205),
    path('stockPERseglistall202205score/', views.stockPERseglistall202205score),
    
    path('stockPERseglistall202206/', views.stockPERseglistall202206),
    path('stockPERseglistall202206score/', views.stockPERseglistall202206score), 
    
    path('stockPERseglistall202207/', views.stockPERseglistall202207),
    path('stockPERseglistall202207score/', views.stockPERseglistall202207score), 
    
    path('stockPERseglistall202208/', views.stockPERseglistall202208),
    path('stockPERseglistall202208score/', views.stockPERseglistall202208score), 
    
    
    path('stockPERseglistall202209/', views.stockPERseglistall202209),
    path('stockPERseglistall202209score/', views.stockPERseglistall202209score),

    path('stockPERseglistall202210/', views.stockPERseglistall202210),
    path('stockPERseglistall202210score/', views.stockPERseglistall202210score),

###############################################
        
    path('EPSnProfitlistall2020Q1/', EPSnProfitlistall2020Q1),
    path('EPSnProfit2020Q2listall/', EPSnProfit2020Q2listall),    
    path('EPSnProfit2020Q3listall/', views.EPSnProfit2020Q3listall),  
    path('EPSnProfit2020Q4listall/', views.EPSnProfit2020Q4listall), 
    path('EPSnProfit2021Q1listall/', views.EPSnProfit2021Q1listall), 
    path('EPSnProfit2021Q2listall/', views.EPSnProfit2021Q2listall), 
    path('EPSnProfit2021Q3listall/', views.EPSnProfit2021Q3listall), 
    path('EPSnProfit2021Q4listall/', views.EPSnProfit2021Q4listall),
    path('EPSnProfit2022Q1listall/', views.EPSnProfit2022Q1listall),

    path('stockPERsegStablelistall2020/', stockPERsegStablelistall2020), 
    path('stockPERsegStablelistall2020Q2/', stockPERsegStablelistall2020Q2), 
    path('stockPERsegStablelistall2020Q3/', views.stockPERsegStablelistall2020Q3), 
    path('stockPERsegStablelistall2020Q4/', views.stockPERsegStablelistall2020Q4), 
    path('stockPERsegStablelistall2021Q1/', views.stockPERsegStablelistall2021Q1), 
    path('stockPERsegStablelistall2021Q2/', views.stockPERsegStablelistall2021Q2), 
    path('stockPERsegStablelistall2021Q3/', views.stockPERsegStablelistall2021Q3), 
    path('stockPERsegStablelistall2021Q4/', views.stockPERsegStablelistall2021Q4),
    path('stockPERsegStablelistall2022Q1/', views.stockPERsegStablelistall2022Q1),


    path('StockCapVar2020Q2listall/', StockCapVar2020Q2listall),
    path('StockCapVar2020Q3listall/', views.StockCapVar2020Q3listall),
    path('StockCapVar2020Q4listall/', views.StockCapVar2020Q4listall),
    path('StockCapVar2021Q1listall/', views.StockCapVar2021Q1listall),
    path('StockCapVar2021Q2listall/', views.StockCapVar2021Q2listall),
    path('StockCapVar2021Q3listall/', views.StockCapVar2021Q3listall),
    path('StockCapVar2021Q4listall/', views.StockCapVar2021Q4listall),
    path('StockCapVar2022Q1listall/', views.StockCapVar2021Q1listall),
            
    path('EPSachieve2020Q2listall/', EPSachieve2020Q2listall),    
    path('EPSachieve2020Q3listall/', views.EPSachieve2020Q3listall),     
    path('EPSachieve2021Q1listall/', views.EPSachieve2021Q1listall),     
    path('EPSachieve2021Q2listall/', views.EPSachieve2021Q2listall),  
    path('EPSachieve2021Q3listall/', views.EPSachieve2021Q3listall),
    path('EPSachieve2022Q1listall/', views.EPSachieve2022Q1listall),     


    path('SubCatslistall202102/', views.SubCatslistall202102), 
    path('SubCatslistall202103/', views.SubCatslistall202103), 
    path('SubCatslistall202104/', views.SubCatslistall202104), 
    path('SubCatslistall202105/', views.SubCatslistall202105), 
    path('SubCatslistall202106/', views.SubCatslistall202106), 
    path('SubCatslistall202107/', views.SubCatslistall202107), 
    path('SubCatslistall202108/', views.SubCatslistall202108), 
    path('SubCatslistall202109/', views.SubCatslistall202109), 
    path('SubCatslistall202110/', views.SubCatslistall202110), 
    path('SubCatslistall202111/', views.SubCatslistall202111), 
    path('SubCatslistall202112/', views.SubCatslistall202112), 

    path('DC_Prof/', views.DC_Prof),
    path('DC_Rev/', views.DC_Rev),
    path('DC_NetInc/', views.DC_NetInc),    
    path('DC_EPS/', views.DC_EPS),
    path('DC_InvTO/', views.DC_InvTO),
    path('DC_Cashflow/', views.DC_Cashflow),
    path('DC_Stock6Admin/', views.DC_Stock6Admin),
    
    path('AREAdownloads/', AREAdownloads), 

    path('stock6downloads/', stock6downloads), 
    path('stockPERsegdownloads/', stockPERsegdownloads), 
    path('stockEnterAlldownloads/', stockEnterAlldownloads),     

    path('BigMoney/', BigMoney),
    path('stockPERsegDiv/', stockPERsegDiv),
    
    
    path('DB_stock6sign/', views.DB_stock6sign),
    path('DB_stockPERseg/', views.DB_stockPERseg),

    path('DB_DCstock6sign/', views.DB_DCstock6sign),
    path('DB_stockPERsegStable/', views.DB_stockPERsegStable),    

    path('DB_EPSachiever/', views.DB_EPSachiever),

    path('DB_StockCapGetter/', views.DB_StockCapGetter),
    
    path('DB_EPSnProfitGetter/', views.DB_EPSnProfitGetter),
]