# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 10:00:35 2023

@author: PCUSER
"""


from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.conf import settings
#from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
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
from module import func8, func_usbond
##################函式位置改寫，一個函式一個檔案，棄用func
from module_PERseg import Price5yDB, Price5y, PERseg, PERsegPEG, PERsegPEGxDB, PERsegStable, PERsegx, PERsegxDB, NetCapDB, PERseg3
from module_Kn import KnQuery, Kn8yPrice

#################
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User

from myapp.models import Stock6Sign
from myapp.models import StockPERseg

from myapp.models import DCStock6Sign202011
from myapp.models import DCStock6Sign2020Q4
from myapp.models import DCStock6Sign202101
from myapp.models import DCStock6Sign202102
from myapp.models import DCStock6Sign202103
from myapp.models import DCStock6Sign202104
from myapp.models import DCStock6Sign202105
from myapp.models import DCStock6Sign202106
from myapp.models import DCStock6Sign202107
from myapp.models import DCStock6Sign202108
from myapp.models import DCStock6Sign202109
from myapp.models import DCStock6Sign202110
from myapp.models import DCStock6Sign202111
from myapp.models import DCStock6Sign202112


from myapp.models import Stock6Sign202005
from myapp.models import Stock6Sign202006

from myapp.models import Stock6Sign2020Q2
from myapp.models import Stock6Sign202008
from myapp.models import Stock6Sign202009
from myapp.models import Stock6Sign2020Q3
from myapp.models import Stock6Sign202011
from myapp.models import Stock6Sign2020Q4
from myapp.models import Stock6Sign202101
from myapp.models import Stock6Sign202102
from myapp.models import Stock6Sign202103
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

from myapp.models import Stock6Sign202401
from myapp.models import Stock6Sign202402
from myapp.models import Stock6Sign202403
from myapp.models import Stock6Sign202404
from myapp.models import Stock6Sign202405
from myapp.models import Stock6Sign202406
#from myapp.models import Stock6sta2021
#from myapp.models import Stock6Sign202109
#from myapp.models import Stock6Sign202110
#from myapp.models import Stock6Sign202111
#from myapp.models import Stock6Sign202112



from myapp.models import StockPERseg202005
from myapp.models import StockPERseg202006
from myapp.models import StockPERseg2020Q2
from myapp.models import StockPERseg202008
from myapp.models import StockPERseg202009
from myapp.models import StockPERseg2020Q3
from myapp.models import StockPERseg202011
from myapp.models import StockPERseg2020Q4
from myapp.models import StockPERseg202101
from myapp.models import StockPERseg202102
from myapp.models import StockPERseg202103
from myapp.models import StockPERseg202104
from myapp.models import StockPERseg202105
from myapp.models import StockPERseg202106
from myapp.models import StockPERseg202107
from myapp.models import StockPERseg202108
from myapp.models import StockPERseg202109
from myapp.models import StockPERseg202110
from myapp.models import StockPERseg202111
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

from myapp.models import StockPERseg202401
from myapp.models import StockPERseg202402
from myapp.models import StockPERseg202403
from myapp.models import StockPERseg202404
from myapp.models import StockPERseg202405
from myapp.models import StockPERseg202406

from myapp.models import EpsProfit2020Q1
from myapp.models import EpsProfit2020Q2
from myapp.models import EpsProfit2020Q3
from myapp.models import EpsProfit2020Q4
from myapp.models import EpsProfit2021Q1
from myapp.models import EpsProfit2021Q2
from myapp.models import EpsProfit2021Q3
from myapp.models import EpsProfit2021Q4
from myapp.models import EpsProfit2022Q1
from myapp.models import EpsProfit2022Q3

from myapp.models import StockPERsegStable2020
from myapp.models import StockPERsegStable2020Q2
from myapp.models import StockPERsegStable2020Q3
from myapp.models import StockPERsegStable2020Q3x
from myapp.models import StockPERsegStable2020Q4
from myapp.models import StockPERsegStable2021Q1
from myapp.models import StockPERsegStable2021Q2
from myapp.models import StockPERsegStable2021Q3
from myapp.models import StockPERsegStable2021Q4
from myapp.models import StockPERsegStable2022Q1
from myapp.models import StockPERsegStable2022Q3



from myapp.models import EPSachieve
from myapp.models import EPSachieve2020Q2
from myapp.models import EPSachieve2020Q3
from myapp.models import EPSachieve2021Q1
from myapp.models import EPSachieve2021Q2
from myapp.models import EPSachieve2021Q3
from myapp.models import EPSachieve2022Q1
from myapp.models import EPSachieve2022Q3

from myapp.models import StockCapVar
from myapp.models import StockCapVar2020Q2
from myapp.models import StockCapVar2020Q3
from myapp.models import StockCapVar2020Q4
from myapp.models import StockCapVar2021Q1
from myapp.models import StockCapVar2021Q2
from myapp.models import StockCapVar2021Q3
from myapp.models import StockCapVar2021Q4
from myapp.models import StockCapVar2022Q1
from myapp.models import StockCapVar2022Q3

from myapp.models import SubCats202011
from myapp.models import SubCats202102
from myapp.models import SubCats202103
from myapp.models import SubCats202104
from myapp.models import SubCats202105
from myapp.models import SubCats202106
from myapp.models import SubCats202107
from myapp.models import SubCats202108
from myapp.models import SubCats202109
from myapp.models import SubCats202110
from myapp.models import SubCats202111
from myapp.models import SubCats202112

from myapp.models import StockFavs_test168
from myapp.models import StockFavDB

from myapp.models import PriEPSPER_DB

#from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse

from myapp.models import City


################################################本益比區間##################################################



@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202005(request):
    segs = StockPERseg202005.objects.all().order_by('id')
    return render(request, "stockPERseglistall202005.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202006(request):
    segs = StockPERseg202006.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202006.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall2020Q2(request):
    segs = StockPERseg2020Q2.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall2020Q2.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202008(request):
    segs = StockPERseg202008.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202008.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202009(request):
    segs = StockPERseg202009.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202009.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall2020Q3(request):
    segs = StockPERseg2020Q3.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall2020Q3.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202011(request):
    segs = StockPERseg202011.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202011.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall2020Q4(request):
    segs = StockPERseg2020Q4.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall2020Q4.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202101(request):
    segs = StockPERseg202101.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202101.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202102(request):
    segs = StockPERseg202102.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202102.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202103(request):
    segs = StockPERseg202103.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202103.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202104(request):
    segs = StockPERseg202104.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202104.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202105(request):
    segs = StockPERseg202105.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202105.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202106(request):
    segs = StockPERseg202106.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202106.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202107(request):
    segs = StockPERseg202107.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202107.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202108(request):
    segs = StockPERseg202108.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202108.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202109(request):
    segs = StockPERseg202109.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202109.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202110(request):
    segs = StockPERseg202110.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202110.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202111(request):
    segs = StockPERseg202111.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202111.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202112(request):
    segs = StockPERseg202112.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202112.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202201(request):
    segs = StockPERseg202201.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202201.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202202(request):
    segs = StockPERseg202202.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202202.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202203(request):
    segs = StockPERseg202203.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202203.html", locals())
@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202204(request):
    segs = StockPERseg202204.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202204.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202205(request):
    segs = StockPERseg202205.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202205.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202206(request):
    segs = StockPERseg202206.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202206.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202207(request):
    segs = StockPERseg202207.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202207.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202208(request):
    segs = StockPERseg202208.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202208.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202209(request):
    segs = StockPERseg202209.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202209.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202210(request):
    segs = StockPERseg202210.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202210.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202211(request):
    segs = StockPERseg202211.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202211.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202212(request):
    segs = StockPERseg202212.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202212.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202301(request):
    segs = StockPERseg202301.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202301.html", locals())
@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202302(request):
    segs = StockPERseg202302.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202302.html", locals())
@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202303(request):
    segs = StockPERseg202303.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202303.html", locals())
@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202304(request):
    segs = StockPERseg202304.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202304.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202305(request):
    segs = StockPERseg202305.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202305.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202306(request):
    segs = StockPERseg202306.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202306.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202307(request):
    segs = StockPERseg202307.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202307.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202308(request):
    segs = StockPERseg202308.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202308.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202309(request):
    segs = StockPERseg202309.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202309.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202310(request):
    segs = StockPERseg202310.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202310.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202311(request):
    segs = StockPERseg202311.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202311.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202312(request):
    segs = StockPERseg202312.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202312.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202401(request):
    segs = StockPERseg202401.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202401.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202402(request):
    segs = StockPERseg202402.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202402.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202403(request):
    segs = StockPERseg202403.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202403.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202404(request):
    segs = StockPERseg202404.objects.all().order_by('cStockID')
    return render(request, "stockPERseglistall202404.html", locals())
#######################################################################
##########################################################################







@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202005score(request):
    segs = StockPERseg202005.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202005score.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202006score(request):
    segs = StockPERseg202006.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202006score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall2020Q2score(request):
    segs = StockPERseg2020Q2.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall2020Q2score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202008score(request):
    segs = StockPERseg202008.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202008score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202009score(request):
    segs = StockPERseg202009.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202009score.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall2020Q3score(request):
    segs = StockPERseg2020Q3.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall2020Q3score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202011score(request):
    segs = StockPERseg202011.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202011score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall2020Q4score(request):
    segs = StockPERseg2020Q4.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall2020Q4score.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202101score(request):
    segs = StockPERseg202101.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202101score.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202102score(request):
    segs = StockPERseg202102.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202102score.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202103score(request):
    segs = StockPERseg202103.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202103score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202104score(request):
    segs = StockPERseg202104.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202104score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202105score(request):
    segs = StockPERseg202105.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202105score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202106score(request):
    segs = StockPERseg202106.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202106score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202107score(request):
    segs = StockPERseg202107.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202107score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202108score(request):
    segs = StockPERseg202108.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202108score.html", locals())




@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202109score(request):
    segs = StockPERseg202109.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202109score.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202110score(request):
    segs = StockPERseg202110.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202110score.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202111score(request):
    segs = StockPERseg202111.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202111score.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202112score(request):
    segs = StockPERseg202112.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202112score.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202201score(request):
    segs = StockPERseg202201.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202201score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202202score(request):
    segs = StockPERseg202202.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202202score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202203score(request):
    segs = StockPERseg202203.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202203score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202204score(request):
    segs = StockPERseg202204.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202204score.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202205score(request):
    segs = StockPERseg202205.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202205score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202206score(request):
    segs = StockPERseg202206.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202206score.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202207score(request):
    segs = StockPERseg202207.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202207score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202208score(request):
    segs = StockPERseg202208.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202208score.html", locals())



@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202209score(request):
    segs = StockPERseg202209.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202209score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202210score(request):
    segs = StockPERseg202210.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202210score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202211score(request):
    segs = StockPERseg202211.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202211score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202212score(request):
    segs = StockPERseg202212.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202212score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202301score(request):
    segs = StockPERseg202301.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202301score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202302score(request):
    segs = StockPERseg202302.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202302score.html", locals())
@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202303score(request):
    segs = StockPERseg202303.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202303score.html", locals())
@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202304score(request):
    segs = StockPERseg202304.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202304score.html", locals())
@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202305score(request):
    segs = StockPERseg202305.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202305score.html", locals())
@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202306score(request):
    segs = StockPERseg202306.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202306score.html", locals())
@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202307score(request):
    segs = StockPERseg202307.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202307score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202308score(request):
    segs = StockPERseg202308.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202308score.html", locals())


@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202309score(request):
    segs = StockPERseg202309.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202309score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202310score(request):
    segs = StockPERseg202310.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202310score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202311score(request):
    segs = StockPERseg202311.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202311score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202312score(request):
    segs = StockPERseg202312.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202312score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202401score(request):
    segs = StockPERseg202401.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202401score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202402score(request):
    segs = StockPERseg202402.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202402score.html", locals())



@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202403score(request):
    segs = StockPERseg202403.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202403score.html", locals())

@permission_required('myapp.Can_enter_stockPERseg DB', login_url='/login2/')
def stockPERseglistall202404score(request):
    segs = StockPERseg202404.objects.all().order_by('-cRisk_reward')
    return render(request, "stockPERseglistall202404score.html", locals())
###################

