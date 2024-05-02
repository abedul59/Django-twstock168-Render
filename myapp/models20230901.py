from django.db import models
from django.contrib.auth.models import User

class Person(User):
    cName = models.CharField(max_length=20, null=False)
    cCellphone = models.CharField(max_length=10, null=False, default=False)

    class Meta:
        permissions = (
            ("Can_enter_stock6", "Can enter stock6"),
            ("Can_enter_stock6 DB", "Can enter stock6 DB"),
            ("Can_enter_stockPERseg", "Can enter stockPERseg"),
            ("Can_enter_stockPERseg DB", "Can enter stockPERseg DB"),
            ("Can_enter_All", "Can enter All"), 
            ("Can_enter_PaidUsersOnly", "Can enter PaidUsersOnly"),  
            ("Can_enter_AdminOnly", "Can enter AdminOnly"),
            ("Can_enter_VIPsOnly", "Can enter VIPsOnly"),                
            ("Can_enter_stockKn", "Can enter stockKn"),
            ("Can_enter_usersmain_test168", "Can enter usersmain_test168"),

        )
    def __str__(self):
        return self.cName

class NewsUnit(models.Model):
    catego = models.CharField(max_length=10, null=False)
    nickname = models.CharField(max_length=20, null=False)
    title = models.CharField(max_length=50, null=False)
    message = models.TextField(null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    
    

class Country(models.Model):
    name = models.CharField(max_length=30)


class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.PositiveIntegerField()

'''
class Stock6sta2021(models.Model):

    cTime = models.CharField(max_length=10, null=True, blank=True)
    cOver3p = models.IntegerField(null=True, blank=True)
    cOver2p = models.IntegerField(null=True, blank=True)
    cOver1p = models.IntegerField(null=True, blank=True)
    cOver0p = models.IntegerField(null=True, blank=True)

    cMorep = models.IntegerField(null=True, blank=True)
    cSamep = models.IntegerField(null=True, blank=True)
    cLessp = models.IntegerField(null=True, blank=True)
    

    pubtime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cTime
    '''
class MacroWaveA(models.Model):  
    cDate = models.CharField(max_length=15, default='')        
    cInvertedYieldCurve30y = models.CharField(max_length=15, default='')
    cInvertedYieldCurve10y = models.CharField(max_length=15, default='')
    cInvertedYieldCurve3m = models.CharField(max_length=15, default='')
    cInvertedYieldCurve6m = models.CharField(max_length=15, default='')
    cInvertedYieldCurve2y = models.CharField(max_length=15, default='')
    cInvertedYieldCurve3y = models.CharField(max_length=15, default='')    
    cInvertedYieldCurve5y = models.CharField(max_length=15, default='')
    cInvertedYieldCurve7y = models.CharField(max_length=15, default='')     
 
    cIYC10yminus3m = models.CharField(max_length=15, default='')

    cCRBindex  = models.CharField(max_length=15, default='')
    cCRBhalfyear  = models.CharField(max_length=15, default='')    
    cCRBoneyear  = models.CharField(max_length=15, default='')  
    pubtime = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.cDate 
    
class MacroWaveB(models.Model):  
    cDate = models.CharField(max_length=15, default='')        

    cRecesTime  = models.CharField(max_length=15, default='')
    cRecesNum  = models.CharField(max_length=15, default='')
    cM1bTime   = models.CharField(max_length=15, default='')
    cM1bNum = models.CharField(max_length=15, default='')
    cM1bYoY = models.CharField(max_length=15, default='')
    cMarketVaule = models.CharField(max_length=15, default='')
    cMVTime = models.CharField(max_length=15, default='')
    cMVvsM1b = models.CharField(max_length=15, default='')
    
    pubtime = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.cDate    
    
class MacroWaveC(models.Model):  
    cDate = models.CharField(max_length=15, default='')        

    cUSUnemploymentRateTime  = models.CharField(max_length=15, default='')
    cUSUnemploymentRate  = models.CharField(max_length=15, default='')
    cUSLeadingIndicatorTime  = models.CharField(max_length=15, default='')    
    cUSLeadingIndicator  = models.CharField(max_length=15, default='')
    cMichiganComsumerTime = models.CharField(max_length=15, default='')    
    cMichiganComsumer = models.CharField(max_length=15, default='')
    cDurableGoodsNewOrder2 = models.CharField(max_length=15, default='')
    cDurableGoodsNewOrder1 = models.CharField(max_length=15, default='')

    cChinaPMITime = models.CharField(max_length=15, default='')
    cChinaPMI = models.CharField(max_length=15, default='')
    
    pubtime = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.cDate 

    
class USBondYieldDB(models.Model):  
    cDate = models.CharField(max_length=15, default='')        
    cInvertedYieldCurve10y = models.CharField(max_length=15, default='')
    cInvertedYieldCurve3m = models.CharField(max_length=15, default='')
    cIYC10yminus3m = models.CharField(max_length=15, default='')

    

    pubtime = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.cDate  
    
    
    
class Stock6Sign(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)
    cSign1 = models.CharField(max_length=10, null=False)
    cSign2 = models.CharField(max_length=10, null=False)
    cSign3 = models.CharField(max_length=10, null=False)
    cSign4 = models.CharField(max_length=10, null=False)
    cSign5 = models.CharField(max_length=10, null=False)
    cSign6 = models.CharField(max_length=10, null=False)
    cAverageScore = models.CharField(max_length=5, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    

class Stock6Sign202005(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)
    cSign1 = models.CharField(max_length=10, null=False)
    cSign2 = models.CharField(max_length=10, null=False)
    cSign3 = models.CharField(max_length=10, null=False)
    cSign4 = models.CharField(max_length=10, null=False)
    cSign5 = models.CharField(max_length=10, null=False)
    cSign6 = models.CharField(max_length=10, null=False)
    cAverageScore = models.CharField(max_length=10, null=False)
    #cLossGain  = models.CharField(max_length=10, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID


class Stock6Sign202006(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)
    cSign1 = models.CharField(max_length=10, null=False)
    cSign2 = models.CharField(max_length=10, null=False)
    cSign3 = models.CharField(max_length=10, null=False)
    cSign4 = models.CharField(max_length=10, null=False)
    cSign5 = models.CharField(max_length=10, null=False)
    cSign6 = models.CharField(max_length=10, null=False)
    cAverageScore = models.CharField(max_length=10, null=False)
    cLossGain  = models.CharField(max_length=10, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    




class Stock6Sign2020Q2(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)
    
    
    cNewestSeason = models.CharField(max_length=15, null=False, default='')
    cNewestRev = models.CharField(max_length=15, null=False, default='')
    
    cSign1 = models.CharField(max_length=10, null=False)
    cSign2 = models.CharField(max_length=10, null=False)
    cSign3 = models.CharField(max_length=10, null=False)
    cSign4 = models.CharField(max_length=10, null=False)
    cSign5 = models.CharField(max_length=10, null=False)
    cSign6 = models.CharField(max_length=10, null=False)
    cAverageScore = models.CharField(max_length=10, null=False)
    cLossGain  = models.CharField(max_length=10, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 
    
class Stock6Sign202007(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)
    
    
    cNewestSeason = models.CharField(max_length=15, null=False, default='')
    cNewestRev = models.CharField(max_length=15, null=False, default='')
    
    cSign1 = models.CharField(max_length=10, null=False)
    cSign2 = models.CharField(max_length=10, null=False)
    cSign3 = models.CharField(max_length=10, null=False)
    cSign4 = models.CharField(max_length=10, null=False)
    cSign5 = models.CharField(max_length=10, null=False)
    cSign6 = models.CharField(max_length=10, null=False)
    cAverageScore = models.CharField(max_length=10, null=False)
    cLossGain  = models.CharField(max_length=10, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID   

class Stock6Sign202008(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)
    
    
    cNewestSeason = models.CharField(max_length=15, null=False, default='')
    cNewestRev = models.CharField(max_length=15, null=False, default='')
    
    cSign1 = models.CharField(max_length=10, null=False)
    cSign2 = models.CharField(max_length=10, null=False)
    cSign3 = models.CharField(max_length=10, null=False)
    cSign4 = models.CharField(max_length=10, null=False)
    cSign5 = models.CharField(max_length=10, null=False)
    cSign6 = models.CharField(max_length=10, null=False)
    cAverageScore = models.CharField(max_length=10, null=False)
    cLossGain  = models.CharField(max_length=10, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID  

class Stock6Sign202009(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)
    
    
    cNewestSeason = models.CharField(max_length=15, null=False, default='')
    cNewestRev = models.CharField(max_length=15, null=False, default='')
    
    cSign1 = models.CharField(max_length=10, null=False)
    cSign2 = models.CharField(max_length=10, null=False)
    cSign3 = models.CharField(max_length=10, null=False)
    cSign4 = models.CharField(max_length=10, null=False)
    cSign5 = models.CharField(max_length=10, null=False)
    cSign6 = models.CharField(max_length=10, null=False)
    cAverageScore = models.CharField(max_length=10, null=False)
    cLossGain  = models.CharField(max_length=10, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 

class Stock6Sign2020Q3(models.Model):
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=10)
    cLossGain  = models.CharField(max_length=10)
    
    sCore2009= models.CharField(max_length=10)
    sCore2008= models.CharField(max_length=10)
    sCore20Q2= models.CharField(max_length=10)
    sCore2006= models.CharField(max_length=10)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID   
    
class Stock6Sign202011(models.Model):
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore20Q3= models.CharField(max_length=10)    
    sCore2009= models.CharField(max_length=10)
    sCore2008= models.CharField(max_length=10)
    sCore20Q2= models.CharField(max_length=10)
    sCore2006= models.CharField(max_length=10)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID


class Stock6Sign2020Q4(models.Model):
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2011= models.CharField(max_length=10)
    sCore20Q3= models.CharField(max_length=10)    
    sCore2009= models.CharField(max_length=10)
    sCore2008= models.CharField(max_length=10)
    sCore20Q2= models.CharField(max_length=10)
    sCore2006= models.CharField(max_length=10)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID


class Stock6Sign202101(models.Model):
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore20Q4= models.CharField(max_length=10)
    sCore2011= models.CharField(max_length=10)
    sCore20Q3= models.CharField(max_length=10)    
    sCore2009= models.CharField(max_length=10)
    sCore2008= models.CharField(max_length=10)
    sCore20Q2= models.CharField(max_length=10)
    sCore2006= models.CharField(max_length=10)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID

class Stock6Sign202102(models.Model):
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2101= models.CharField(max_length=10)
    sCore20Q4= models.CharField(max_length=10)
    sCore2011= models.CharField(max_length=10)
    sCore20Q3= models.CharField(max_length=10)    
    sCore2009= models.CharField(max_length=10)
    sCore2008= models.CharField(max_length=10)
    sCore20Q2= models.CharField(max_length=10)
    sCore2006= models.CharField(max_length=10)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID

class Stock6Sign202103(models.Model):
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2102= models.CharField(max_length=10)
    sCore2101= models.CharField(max_length=10)
    sCore20Q4= models.CharField(max_length=10)
    sCore2011= models.CharField(max_length=10)
    sCore20Q3= models.CharField(max_length=10)    
    sCore2009= models.CharField(max_length=10)
    sCore2008= models.CharField(max_length=10)
    sCore20Q2= models.CharField(max_length=10)
    sCore2006= models.CharField(max_length=10)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    

class Stock6Sign202104(models.Model):
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2103= models.CharField(max_length=10)
    sCore2102= models.CharField(max_length=10)
    sCore2101= models.CharField(max_length=10)
    sCore20Q4= models.CharField(max_length=10)
    sCore2011= models.CharField(max_length=10)
    sCore20Q3= models.CharField(max_length=10)    
    sCore2009= models.CharField(max_length=10)
    sCore2008= models.CharField(max_length=10)
    sCore20Q2= models.CharField(max_length=10)
    sCore2006= models.CharField(max_length=10)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID    

class Stock6Sign202105(models.Model):
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2104= models.CharField(max_length=10)
    sCore2103= models.CharField(max_length=10)
    sCore2102= models.CharField(max_length=10)
    sCore2101= models.CharField(max_length=10)
    sCore20Q4= models.CharField(max_length=10)
    sCore2011= models.CharField(max_length=10)
    sCore20Q3= models.CharField(max_length=10)    
    sCore2009= models.CharField(max_length=10)
    sCore2008= models.CharField(max_length=10)
    sCore20Q2= models.CharField(max_length=10)
    sCore2006= models.CharField(max_length=10)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID


class Stock6Sign202106(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2105= models.CharField(max_length=10)
    sCore2104= models.CharField(max_length=10)
    sCore2103= models.CharField(max_length=10)
    sCore2102= models.CharField(max_length=10)
    sCore2101= models.CharField(max_length=10)

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID

class Stock6Sign202107(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2106= models.CharField(max_length=10)
    sCore2105= models.CharField(max_length=10)
    sCore2104= models.CharField(max_length=10)
    sCore2103= models.CharField(max_length=10)
    sCore2102= models.CharField(max_length=10)
    sCore2101= models.CharField(max_length=10)

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID

class Stock6Sign202108(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2107= models.CharField(max_length=10)
    sCore2106= models.CharField(max_length=10)
    sCore2105= models.CharField(max_length=10)
    sCore2104= models.CharField(max_length=10)
    sCore2103= models.CharField(max_length=10)
    sCore2102= models.CharField(max_length=10)
    sCore2101= models.CharField(max_length=10)

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    

class Stock6Sign202109(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2108= models.CharField(max_length=10)
    sCore2107= models.CharField(max_length=10)
    sCore2106= models.CharField(max_length=10)
    sCore2105= models.CharField(max_length=10)
    sCore2104= models.CharField(max_length=10)
    sCore2103= models.CharField(max_length=10)
    sCore2102= models.CharField(max_length=10)
    sCore2101= models.CharField(max_length=10)

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
class Stock6Sign202110(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2109= models.CharField(max_length=10)
    sCore2108= models.CharField(max_length=10)
    sCore2107= models.CharField(max_length=10)
    sCore2106= models.CharField(max_length=10)
    sCore2105= models.CharField(max_length=10)
    sCore2104= models.CharField(max_length=10)
    sCore2103= models.CharField(max_length=10)
    sCore2102= models.CharField(max_length=10)
    sCore2101= models.CharField(max_length=10)

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID

class Stock6Sign202111(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2110= models.CharField(max_length=10)
    sCore2109= models.CharField(max_length=10)
    sCore2108= models.CharField(max_length=10)
    sCore2107= models.CharField(max_length=10)
    sCore2106= models.CharField(max_length=10)
    sCore2105= models.CharField(max_length=10)
    sCore2104= models.CharField(max_length=10)
    sCore2103= models.CharField(max_length=10)
    sCore2102= models.CharField(max_length=10)
    sCore2101= models.CharField(max_length=10)

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
class Stock6Sign202112(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2111= models.CharField(max_length=10)
    sCore2110= models.CharField(max_length=10)
    sCore2109= models.CharField(max_length=10)
    sCore2108= models.CharField(max_length=10)
    sCore2107= models.CharField(max_length=10)
    sCore2106= models.CharField(max_length=10)
    sCore2105= models.CharField(max_length=10)
    sCore2104= models.CharField(max_length=10)
    sCore2103= models.CharField(max_length=10)
    sCore2102= models.CharField(max_length=10)
    sCore2101= models.CharField(max_length=10)

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID

class Stock6Sign202201(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2112= models.CharField(max_length=10)
    sCore2111= models.CharField(max_length=10)
    sCore2110= models.CharField(max_length=10)
    sCore2109= models.CharField(max_length=10)
    sCore2108= models.CharField(max_length=10)
    sCore2107= models.CharField(max_length=10)
    sCore2106= models.CharField(max_length=10)
    sCore2105= models.CharField(max_length=10)
    sCore2104= models.CharField(max_length=10)
    sCore2103= models.CharField(max_length=10)
    sCore2102= models.CharField(max_length=10)
    sCore2101= models.CharField(max_length=10)

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID    
    
class Stock6Sign202202(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2201= models.CharField(max_length=10)
    sCore2112= models.CharField(max_length=10)
    sCore2111= models.CharField(max_length=10)
    sCore2110= models.CharField(max_length=10)
    sCore2109= models.CharField(max_length=10)
    sCore2108= models.CharField(max_length=10)
    sCore2107= models.CharField(max_length=10)
    sCore2106= models.CharField(max_length=10)
    sCore2105= models.CharField(max_length=10)
    sCore2104= models.CharField(max_length=10)
    sCore2103= models.CharField(max_length=10)
    sCore2102= models.CharField(max_length=10)
    sCore2101= models.CharField(max_length=10)

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID    
    
class Stock6Sign202203(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2202= models.CharField(max_length=10)
    sCore2201= models.CharField(max_length=10)
    sCore2112= models.CharField(max_length=10)
    sCore2111= models.CharField(max_length=10)
    sCore2110= models.CharField(max_length=10)
    sCore2109= models.CharField(max_length=10)
    sCore2108= models.CharField(max_length=10)
    sCore2107= models.CharField(max_length=10)
    sCore2106= models.CharField(max_length=10)
    sCore2105= models.CharField(max_length=10)
    sCore2104= models.CharField(max_length=10)
    sCore2103= models.CharField(max_length=10)
    sCore2102= models.CharField(max_length=10)
    sCore2101= models.CharField(max_length=10)

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID      
    
class Stock6Sign202204(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2203= models.CharField(max_length=10)
    sCore2202= models.CharField(max_length=10)
    sCore2201= models.CharField(max_length=10)
    sCore2112= models.CharField(max_length=10)
    sCore2111= models.CharField(max_length=10)
    sCore2110= models.CharField(max_length=10)
    sCore2109= models.CharField(max_length=10)
    sCore2108= models.CharField(max_length=10)
    sCore2107= models.CharField(max_length=10)
    sCore2106= models.CharField(max_length=10)
    sCore2105= models.CharField(max_length=10)
    sCore2104= models.CharField(max_length=10)

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID  
    
class Stock6Sign202205(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2204= models.CharField(max_length=10)
    sCore2203= models.CharField(max_length=10)
    sCore2202= models.CharField(max_length=10)
    sCore2201= models.CharField(max_length=10)
    sCore2112= models.CharField(max_length=10)
    sCore2111= models.CharField(max_length=10)
    sCore2110= models.CharField(max_length=10)
    sCore2109= models.CharField(max_length=10)
    sCore2108= models.CharField(max_length=10)
    sCore2107= models.CharField(max_length=10)
    sCore2106= models.CharField(max_length=10)
    sCore2105= models.CharField(max_length=10)


    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 

class Stock6Sign202206(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤


    sCore2205= models.CharField(max_length=10)
    sCore2204= models.CharField(max_length=10)
    sCore2203= models.CharField(max_length=10)
    sCore2202= models.CharField(max_length=10)
    sCore2201= models.CharField(max_length=10)
    sCore2112= models.CharField(max_length=10)
    sCore2111= models.CharField(max_length=10)
    sCore2110= models.CharField(max_length=10)
    sCore2109= models.CharField(max_length=10)
    sCore2108= models.CharField(max_length=10)
    sCore2107= models.CharField(max_length=10)
    sCore2106= models.CharField(max_length=10)

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 
    

class Stock6Sign202207(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤


    sCore2206= models.CharField(max_length=10)
    sCore2205= models.CharField(max_length=10)
    sCore2204= models.CharField(max_length=10)
    sCore2203= models.CharField(max_length=10)
    sCore2202= models.CharField(max_length=10)
    sCore2201= models.CharField(max_length=10)
    sCore2112= models.CharField(max_length=10)
    sCore2111= models.CharField(max_length=10)
    sCore2110= models.CharField(max_length=10)
    sCore2109= models.CharField(max_length=10)
    sCore2108= models.CharField(max_length=10)
    sCore2107= models.CharField(max_length=10)


    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 
    
class Stock6Sign202208(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2207= models.CharField(max_length=10)
    sCore2206= models.CharField(max_length=10)
    sCore2205= models.CharField(max_length=10)
    sCore2204= models.CharField(max_length=10)
    sCore2203= models.CharField(max_length=10)
    sCore2202= models.CharField(max_length=10)
    sCore2201= models.CharField(max_length=10)
    sCore2112= models.CharField(max_length=10)
    sCore2111= models.CharField(max_length=10)
    sCore2110= models.CharField(max_length=10)
    sCore2109= models.CharField(max_length=10)
    sCore2108= models.CharField(max_length=10)



    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 
    

class Stock6Sign202209(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2208= models.CharField(max_length=10)
    sCore2207= models.CharField(max_length=10)
    sCore2206= models.CharField(max_length=10)
    sCore2205= models.CharField(max_length=10)
    sCore2204= models.CharField(max_length=10)
    sCore2203= models.CharField(max_length=10)
    sCore2202= models.CharField(max_length=10)
    sCore2201= models.CharField(max_length=10)
    sCore2112= models.CharField(max_length=10)
    sCore2111= models.CharField(max_length=10)
    sCore2110= models.CharField(max_length=10)
    sCore2109= models.CharField(max_length=10)




    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 
    
class Stock6Sign202210(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2209= models.CharField(max_length=10)
    sCore2208= models.CharField(max_length=10)
    sCore2207= models.CharField(max_length=10)
    sCore2206= models.CharField(max_length=10)
    sCore2205= models.CharField(max_length=10)
    sCore2204= models.CharField(max_length=10)
    sCore2203= models.CharField(max_length=10)
    sCore2202= models.CharField(max_length=10)
    sCore2201= models.CharField(max_length=10)
    sCore2112= models.CharField(max_length=10)
    sCore2111= models.CharField(max_length=10)
    sCore2110= models.CharField(max_length=10)

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 
    
class Stock6Sign202211(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2210= models.CharField(max_length=10)
    sCore2209= models.CharField(max_length=10)
    sCore2208= models.CharField(max_length=10)
    sCore2207= models.CharField(max_length=10)
    sCore2206= models.CharField(max_length=10)
    sCore2205= models.CharField(max_length=10)
    sCore2204= models.CharField(max_length=10)
    sCore2203= models.CharField(max_length=10)
    sCore2202= models.CharField(max_length=10)
    sCore2201= models.CharField(max_length=10)
    sCore2112= models.CharField(max_length=10)
    sCore2111= models.CharField(max_length=10)


    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
class Stock6Sign202212(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2211= models.CharField(max_length=10)
    sCore2210= models.CharField(max_length=10)
    sCore2209= models.CharField(max_length=10)
    sCore2208= models.CharField(max_length=10)
    sCore2207= models.CharField(max_length=10)
    sCore2206= models.CharField(max_length=10)
    sCore2205= models.CharField(max_length=10)
    sCore2204= models.CharField(max_length=10)
    sCore2203= models.CharField(max_length=10)
    sCore2202= models.CharField(max_length=10)
    sCore2201= models.CharField(max_length=10)
    sCore2112= models.CharField(max_length=10)



    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
#############2023##
class Stock6Sign202301(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2212= models.CharField(max_length=10)
    sCore2211= models.CharField(max_length=10)
    sCore2210= models.CharField(max_length=10)
    sCore2209= models.CharField(max_length=10)
    sCore2208= models.CharField(max_length=10)
    sCore2207= models.CharField(max_length=10)
    sCore2206= models.CharField(max_length=10)
    sCore2205= models.CharField(max_length=10)
    sCore2204= models.CharField(max_length=10)
    sCore2203= models.CharField(max_length=10)
    sCore2202= models.CharField(max_length=10)
    sCore2201= models.CharField(max_length=10)

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID    
    
class Stock6Sign202302(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2301= models.CharField(max_length=10)
    sCore2212= models.CharField(max_length=10)
    sCore2211= models.CharField(max_length=10)
    sCore2210= models.CharField(max_length=10)
    sCore2209= models.CharField(max_length=10)
    sCore2208= models.CharField(max_length=10)
    sCore2207= models.CharField(max_length=10)
    sCore2206= models.CharField(max_length=10)
    sCore2205= models.CharField(max_length=10)
    sCore2204= models.CharField(max_length=10)
    sCore2203= models.CharField(max_length=10)
    sCore2202= models.CharField(max_length=10)


    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID    
    
class Stock6Sign202303(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2302= models.CharField(max_length=10)
    sCore2301= models.CharField(max_length=10)
    sCore2212= models.CharField(max_length=10)
    sCore2211= models.CharField(max_length=10)
    sCore2210= models.CharField(max_length=10)
    sCore2209= models.CharField(max_length=10)
    sCore2208= models.CharField(max_length=10)
    sCore2207= models.CharField(max_length=10)
    sCore2206= models.CharField(max_length=10)
    sCore2205= models.CharField(max_length=10)
    sCore2204= models.CharField(max_length=10)
    sCore2103= models.CharField(max_length=10)

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID      
    
class Stock6Sign202304(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2303= models.CharField(max_length=10)
    sCore2302= models.CharField(max_length=10)
    sCore2301= models.CharField(max_length=10)
    sCore2212= models.CharField(max_length=10)
    sCore2211= models.CharField(max_length=10)
    sCore2210= models.CharField(max_length=10)
    sCore2209= models.CharField(max_length=10)
    sCore2208= models.CharField(max_length=10)
    sCore2207= models.CharField(max_length=10)
    sCore2206= models.CharField(max_length=10)
    sCore2205= models.CharField(max_length=10)
    sCore2204= models.CharField(max_length=10)

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID  
    
class Stock6Sign202305(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2304= models.CharField(max_length=10)
    sCore2303= models.CharField(max_length=10)
    sCore2302= models.CharField(max_length=10)
    sCore2301= models.CharField(max_length=10)
    sCore2212= models.CharField(max_length=10)
    sCore2211= models.CharField(max_length=10)
    sCore2210= models.CharField(max_length=10)
    sCore2209= models.CharField(max_length=10)
    sCore2208= models.CharField(max_length=10)
    sCore2207= models.CharField(max_length=10)
    sCore2206= models.CharField(max_length=10)
    sCore2205= models.CharField(max_length=10)


    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 

class Stock6Sign202306(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤


    sCore2305= models.CharField(max_length=10)
    sCore2304= models.CharField(max_length=10)
    sCore2303= models.CharField(max_length=10)
    sCore2302= models.CharField(max_length=10)
    sCore2301= models.CharField(max_length=10)
    sCore2212= models.CharField(max_length=10)
    sCore2211= models.CharField(max_length=10)
    sCore2210= models.CharField(max_length=10)
    sCore2209= models.CharField(max_length=10)
    sCore2208= models.CharField(max_length=10)
    sCore2207= models.CharField(max_length=10)
    sCore2206= models.CharField(max_length=10)

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 
    

class Stock6Sign202307(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤


    sCore2306= models.CharField(max_length=10)
    sCore2305= models.CharField(max_length=10)
    sCore2304= models.CharField(max_length=10)
    sCore2303= models.CharField(max_length=10)
    sCore2302= models.CharField(max_length=10)
    sCore2301= models.CharField(max_length=10)
    sCore2212= models.CharField(max_length=10)
    sCore2211= models.CharField(max_length=10)
    sCore2210= models.CharField(max_length=10)
    sCore2209= models.CharField(max_length=10)
    sCore2208= models.CharField(max_length=10)
    sCore2207= models.CharField(max_length=10)


    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 
    
class Stock6Sign202308(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2307= models.CharField(max_length=10)
    sCore2306= models.CharField(max_length=10)
    sCore2305= models.CharField(max_length=10)
    sCore2304= models.CharField(max_length=10)
    sCore2303= models.CharField(max_length=10)
    sCore2302= models.CharField(max_length=10)
    sCore2301= models.CharField(max_length=10)
    sCore2212= models.CharField(max_length=10)
    sCore2211= models.CharField(max_length=10)
    sCore2210= models.CharField(max_length=10)
    sCore2209= models.CharField(max_length=10)
    sCore2208= models.CharField(max_length=10)



    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 
    

class Stock6Sign202309(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2308= models.CharField(max_length=10)
    sCore2307= models.CharField(max_length=10)
    sCore2306= models.CharField(max_length=10)
    sCore2305= models.CharField(max_length=10)
    sCore2304= models.CharField(max_length=10)
    sCore2303= models.CharField(max_length=10)
    sCore2302= models.CharField(max_length=10)
    sCore2301= models.CharField(max_length=10)
    sCore2212= models.CharField(max_length=10)
    sCore2211= models.CharField(max_length=10)
    sCore2210= models.CharField(max_length=10)
    sCore2209= models.CharField(max_length=10)




    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 
    
class Stock6Sign202310(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2309= models.CharField(max_length=10)
    sCore2308= models.CharField(max_length=10)
    sCore2307= models.CharField(max_length=10)
    sCore2306= models.CharField(max_length=10)
    sCore2305= models.CharField(max_length=10)
    sCore2304= models.CharField(max_length=10)
    sCore2303= models.CharField(max_length=10)
    sCore2302= models.CharField(max_length=10)
    sCore2301= models.CharField(max_length=10)
    sCore2212= models.CharField(max_length=10)
    sCore2211= models.CharField(max_length=10)
    sCore2210= models.CharField(max_length=10)

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 
    
class Stock6Sign202311(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2310= models.CharField(max_length=10)
    sCore2309= models.CharField(max_length=10)
    sCore2308= models.CharField(max_length=10)
    sCore2307= models.CharField(max_length=10)
    sCore2306= models.CharField(max_length=10)
    sCore2305= models.CharField(max_length=10)
    sCore2304= models.CharField(max_length=10)
    sCore2303= models.CharField(max_length=10)
    sCore2302= models.CharField(max_length=10)
    sCore2301= models.CharField(max_length=10)
    sCore2212= models.CharField(max_length=10)
    sCore2211= models.CharField(max_length=10)


    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
class Stock6Sign202312(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    
    cSign1 = models.CharField(max_length=10)
    cSign2 = models.CharField(max_length=10)
    cSign3 = models.CharField(max_length=10)
    cSign4 = models.CharField(max_length=10)
    cSign5 = models.CharField(max_length=10)
    cSign6 = models.CharField(max_length=10)
    cAverageScore = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤
    cLossGain  = models.CharField(max_length=15)  #不能改成FloatField，會發生錯誤

    sCore2311= models.CharField(max_length=10)
    sCore2310= models.CharField(max_length=10)
    sCore2309= models.CharField(max_length=10)
    sCore2308= models.CharField(max_length=10)
    sCore2307= models.CharField(max_length=10)
    sCore2306= models.CharField(max_length=10)
    sCore2305= models.CharField(max_length=10)
    sCore2304= models.CharField(max_length=10)
    sCore2303= models.CharField(max_length=10)
    sCore2302= models.CharField(max_length=10)
    sCore2301= models.CharField(max_length=10)
    sCore2212= models.CharField(max_length=10)



    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
####################################################################################
####################################################################################

class DCStock6Sign202011(models.Model):
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    


    #營收
    cS1AA1 = models.CharField(max_length=15, default='')
    cS1A1 = models.CharField(max_length=15, default='')
    cS1A2 = models.CharField(max_length=15, default='')
    cS1BB1 = models.CharField(max_length=15, default='')
    cS1BB3 = models.CharField(max_length=15, default='')
    cS1B1 = models.CharField(max_length=15, default='')
    cS1C1 = models.CharField(max_length=15, default='')
    cS1C2 = models.CharField(max_length=15, default='')    


    #營益率
    cS2AA1 = models.CharField(max_length=15, default='')
    cS2AA2 = models.CharField(max_length=15, default='')
    cS2A1 = models.CharField(max_length=15, default='')
    cS2A2 = models.CharField(max_length=15, default='')
    cS2BB1 = models.CharField(max_length=15, default='')
    cS2BB2 = models.CharField(max_length=15, default='')
    cS2BB3 = models.CharField(max_length=15, default='')
    cS2B1 = models.CharField(max_length=15, default='')
    cS2B2 = models.CharField(max_length=15, default='')
    cS2C1 = models.CharField(max_length=15, default='')
    cS2C2 = models.CharField(max_length=15, default='')

    #稅後淨利YoY
    cS3AA1 = models.CharField(max_length=15, default='')
    cS3AA2 = models.CharField(max_length=15, default='')
    cS3A1 = models.CharField(max_length=15, default='')
    cS3BB1 = models.CharField(max_length=15, default='')
    cS3BB2 = models.CharField(max_length=15, default='')
    cS3BB3 = models.CharField(max_length=15, default='')
    cS3B1 = models.CharField(max_length=15, default='')
    cS3B2 = models.CharField(max_length=15, default='')
    cS3B3 = models.CharField(max_length=15, default='')
    cS3C1 = models.CharField(max_length=15, default='')    
    
    
    #EPS
    cS4AA1 = models.CharField(max_length=15, default='')
    cS4A1 = models.CharField(max_length=15, default='')
    cS4BB1 = models.CharField(max_length=15, default='')
    cS4B1 = models.CharField(max_length=15, default='')
    cS4B2 = models.CharField(max_length=15, default='')
    cS4C1 = models.CharField(max_length=15, default='')
   
    #存貨週轉率
    cS5AA1 = models.CharField(max_length=15, default='')
    cS5A1 = models.CharField(max_length=15, default='')
    cS5BB1 = models.CharField(max_length=15, default='')
    cS5BB2 = models.CharField(max_length=15, default='')
    cS5B1 = models.CharField(max_length=15, default='')
    cS5C1 = models.CharField(max_length=15, default='')
    cS5No1 = models.CharField(max_length=15, default='')     

    #現金流量
    cS6AA1 = models.CharField(max_length=15, default='')
    cS6A1 = models.CharField(max_length=15, default='')
    cS6BB1 = models.CharField(max_length=15, default='')
    cS6B1 = models.CharField(max_length=15, default='')
    cS6C1 = models.CharField(max_length=15, default='')

    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    
    def __str__(self):
        return self.cStockID 
    
    

class DCStock6Sign2020Q4(models.Model):
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    


    #營收
    cS1AA1 = models.CharField(max_length=15, default='')
    cS1A1 = models.CharField(max_length=15, default='')
    cS1A2 = models.CharField(max_length=15, default='')
    cS1BB1 = models.CharField(max_length=15, default='')
    cS1BB3 = models.CharField(max_length=15, default='')
    cS1B1 = models.CharField(max_length=15, default='')
    cS1C1 = models.CharField(max_length=15, default='')
    cS1C2 = models.CharField(max_length=15, default='')    


    #營益率
    cS2AA1 = models.CharField(max_length=15, default='')
    cS2AA2 = models.CharField(max_length=15, default='')
    cS2A1 = models.CharField(max_length=15, default='')
    cS2A2 = models.CharField(max_length=15, default='')
    cS2BB1 = models.CharField(max_length=15, default='')
    cS2BB2 = models.CharField(max_length=15, default='')
    cS2BB3 = models.CharField(max_length=15, default='')
    cS2B1 = models.CharField(max_length=15, default='')
    cS2B2 = models.CharField(max_length=15, default='')
    cS2C1 = models.CharField(max_length=15, default='')
    cS2C2 = models.CharField(max_length=15, default='')

    #稅後淨利YoY
    cS3AA1 = models.CharField(max_length=15, default='')
    cS3AA2 = models.CharField(max_length=15, default='')
    cS3A1 = models.CharField(max_length=15, default='')
    cS3BB1 = models.CharField(max_length=15, default='')
    cS3BB2 = models.CharField(max_length=15, default='')
    cS3BB3 = models.CharField(max_length=15, default='')
    cS3B1 = models.CharField(max_length=15, default='')
    cS3B2 = models.CharField(max_length=15, default='')
    cS3B3 = models.CharField(max_length=15, default='')
    cS3C1 = models.CharField(max_length=15, default='')    
    
    
    #EPS
    cS4AA1 = models.CharField(max_length=15, default='')
    cS4A1 = models.CharField(max_length=15, default='')
    cS4BB1 = models.CharField(max_length=15, default='')
    cS4B1 = models.CharField(max_length=15, default='')
    cS4B2 = models.CharField(max_length=15, default='')
    cS4C1 = models.CharField(max_length=15, default='')
   
    #存貨週轉率
    cS5AA1 = models.CharField(max_length=15, default='')
    cS5A1 = models.CharField(max_length=15, default='')
    cS5BB1 = models.CharField(max_length=15, default='')
    cS5BB2 = models.CharField(max_length=15, default='')
    cS5B1 = models.CharField(max_length=15, default='')
    cS5C1 = models.CharField(max_length=15, default='')
    cS5No1 = models.CharField(max_length=15, default='')     

    #現金流量
    cS6AA1 = models.CharField(max_length=15, default='')
    cS6A1 = models.CharField(max_length=15, default='')
    cS6BB1 = models.CharField(max_length=15, default='')
    cS6B1 = models.CharField(max_length=15, default='')
    cS6C1 = models.CharField(max_length=15, default='')

    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    
    def __str__(self):
        return self.cStockID 

class DCStock6Sign202101(models.Model):
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    


    #營收
    cS1AA1 = models.CharField(max_length=15, default='')
    cS1A1 = models.CharField(max_length=15, default='')
    cS1A2 = models.CharField(max_length=15, default='')
    cS1BB1 = models.CharField(max_length=15, default='')
    cS1BB3 = models.CharField(max_length=15, default='')
    cS1B1 = models.CharField(max_length=15, default='')
    cS1C1 = models.CharField(max_length=15, default='')
    cS1C2 = models.CharField(max_length=15, default='')    


    #營益率
    cS2AA1 = models.CharField(max_length=15, default='')
    cS2AA2 = models.CharField(max_length=15, default='')
    cS2A1 = models.CharField(max_length=15, default='')
    cS2A2 = models.CharField(max_length=15, default='')
    cS2BB1 = models.CharField(max_length=15, default='')
    cS2BB2 = models.CharField(max_length=15, default='')
    cS2BB3 = models.CharField(max_length=15, default='')
    cS2B1 = models.CharField(max_length=15, default='')
    cS2B2 = models.CharField(max_length=15, default='')
    cS2C1 = models.CharField(max_length=15, default='')
    cS2C2 = models.CharField(max_length=15, default='')

    #稅後淨利YoY
    cS3AA1 = models.CharField(max_length=15, default='')
    cS3AA2 = models.CharField(max_length=15, default='')
    cS3A1 = models.CharField(max_length=15, default='')
    cS3BB1 = models.CharField(max_length=15, default='')
    cS3BB2 = models.CharField(max_length=15, default='')
    cS3BB3 = models.CharField(max_length=15, default='')
    cS3B1 = models.CharField(max_length=15, default='')
    cS3B2 = models.CharField(max_length=15, default='')
    cS3B3 = models.CharField(max_length=15, default='')
    cS3C1 = models.CharField(max_length=15, default='')    
    
    
    #EPS
    cS4AA1 = models.CharField(max_length=15, default='')
    cS4A1 = models.CharField(max_length=15, default='')
    cS4BB1 = models.CharField(max_length=15, default='')
    cS4B1 = models.CharField(max_length=15, default='')
    cS4B2 = models.CharField(max_length=15, default='')
    cS4C1 = models.CharField(max_length=15, default='')
   
    #存貨週轉率
    cS5AA1 = models.CharField(max_length=15, default='')
    cS5A1 = models.CharField(max_length=15, default='')
    cS5BB1 = models.CharField(max_length=15, default='')
    cS5BB2 = models.CharField(max_length=15, default='')
    cS5B1 = models.CharField(max_length=15, default='')
    cS5C1 = models.CharField(max_length=15, default='')
    cS5No1 = models.CharField(max_length=15, default='')     

    #現金流量
    cS6AA1 = models.CharField(max_length=15, default='')
    cS6A1 = models.CharField(max_length=15, default='')
    cS6BB1 = models.CharField(max_length=15, default='')
    cS6B1 = models.CharField(max_length=15, default='')
    cS6C1 = models.CharField(max_length=15, default='')

    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    
    def __str__(self):
        return self.cStockID     
    
    
class DCStock6Sign202102(models.Model):
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    


    #營收
    cS1AA1 = models.CharField(max_length=15, default='')
    cS1A1 = models.CharField(max_length=15, default='')
    cS1A2 = models.CharField(max_length=15, default='')
    cS1BB1 = models.CharField(max_length=15, default='')
    cS1BB3 = models.CharField(max_length=15, default='')
    cS1B1 = models.CharField(max_length=15, default='')
    cS1C1 = models.CharField(max_length=15, default='')
    cS1C2 = models.CharField(max_length=15, default='')    


    #營益率
    cS2AA1 = models.CharField(max_length=15, default='')
    cS2AA2 = models.CharField(max_length=15, default='')
    cS2A1 = models.CharField(max_length=15, default='')
    cS2A2 = models.CharField(max_length=15, default='')
    cS2BB1 = models.CharField(max_length=15, default='')
    cS2BB2 = models.CharField(max_length=15, default='')
    cS2BB3 = models.CharField(max_length=15, default='')
    cS2B1 = models.CharField(max_length=15, default='')
    cS2B2 = models.CharField(max_length=15, default='')
    cS2C1 = models.CharField(max_length=15, default='')
    cS2C2 = models.CharField(max_length=15, default='')

    #稅後淨利YoY
    cS3AA1 = models.CharField(max_length=15, default='')
    cS3AA2 = models.CharField(max_length=15, default='')
    cS3A1 = models.CharField(max_length=15, default='')
    cS3BB1 = models.CharField(max_length=15, default='')
    cS3BB2 = models.CharField(max_length=15, default='')
    cS3BB3 = models.CharField(max_length=15, default='')
    cS3B1 = models.CharField(max_length=15, default='')
    cS3B2 = models.CharField(max_length=15, default='')
    cS3B3 = models.CharField(max_length=15, default='')
    cS3C1 = models.CharField(max_length=15, default='')    
    
    
    #EPS
    cS4AA1 = models.CharField(max_length=15, default='')
    cS4A1 = models.CharField(max_length=15, default='')
    cS4BB1 = models.CharField(max_length=15, default='')
    cS4B1 = models.CharField(max_length=15, default='')
    cS4B2 = models.CharField(max_length=15, default='')
    cS4C1 = models.CharField(max_length=15, default='')
   
    #存貨週轉率
    cS5AA1 = models.CharField(max_length=15, default='')
    cS5A1 = models.CharField(max_length=15, default='')
    cS5BB1 = models.CharField(max_length=15, default='')
    cS5BB2 = models.CharField(max_length=15, default='')
    cS5B1 = models.CharField(max_length=15, default='')
    cS5C1 = models.CharField(max_length=15, default='')
    cS5No1 = models.CharField(max_length=15, default='')     

    #現金流量
    cS6AA1 = models.CharField(max_length=15, default='')
    cS6A1 = models.CharField(max_length=15, default='')
    cS6BB1 = models.CharField(max_length=15, default='')
    cS6B1 = models.CharField(max_length=15, default='')
    cS6C1 = models.CharField(max_length=15, default='')

    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    
    def __str__(self):
        return self.cStockID    


class DCStock6Sign202103(models.Model):
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    


    #營收
    cS1AA1 = models.CharField(max_length=15, default='')
    cS1A1 = models.CharField(max_length=15, default='')
    cS1A2 = models.CharField(max_length=15, default='')
    cS1BB1 = models.CharField(max_length=15, default='')
    cS1BB3 = models.CharField(max_length=15, default='')
    cS1B1 = models.CharField(max_length=15, default='')
    cS1C1 = models.CharField(max_length=15, default='')
    cS1C2 = models.CharField(max_length=15, default='')    


    #營益率
    cS2AA1 = models.CharField(max_length=15, default='')
    cS2AA2 = models.CharField(max_length=15, default='')
    cS2A1 = models.CharField(max_length=15, default='')
    cS2A2 = models.CharField(max_length=15, default='')
    cS2BB1 = models.CharField(max_length=15, default='')
    cS2BB2 = models.CharField(max_length=15, default='')
    cS2BB3 = models.CharField(max_length=15, default='')
    cS2B1 = models.CharField(max_length=15, default='')
    cS2B2 = models.CharField(max_length=15, default='')
    cS2C1 = models.CharField(max_length=15, default='')
    cS2C2 = models.CharField(max_length=15, default='')

    #稅後淨利YoY
    cS3AA1 = models.CharField(max_length=15, default='')
    cS3AA2 = models.CharField(max_length=15, default='')
    cS3A1 = models.CharField(max_length=15, default='')
    cS3BB1 = models.CharField(max_length=15, default='')
    cS3BB2 = models.CharField(max_length=15, default='')
    cS3BB3 = models.CharField(max_length=15, default='')
    cS3B1 = models.CharField(max_length=15, default='')
    cS3B2 = models.CharField(max_length=15, default='')
    cS3B3 = models.CharField(max_length=15, default='')
    cS3C1 = models.CharField(max_length=15, default='')    
    
    
    #EPS
    cS4AA1 = models.CharField(max_length=15, default='')
    cS4A1 = models.CharField(max_length=15, default='')
    cS4BB1 = models.CharField(max_length=15, default='')
    cS4B1 = models.CharField(max_length=15, default='')
    cS4B2 = models.CharField(max_length=15, default='')
    cS4C1 = models.CharField(max_length=15, default='')
   
    #存貨週轉率
    cS5AA1 = models.CharField(max_length=15, default='')
    cS5A1 = models.CharField(max_length=15, default='')
    cS5BB1 = models.CharField(max_length=15, default='')
    cS5BB2 = models.CharField(max_length=15, default='')
    cS5B1 = models.CharField(max_length=15, default='')
    cS5C1 = models.CharField(max_length=15, default='')
    cS5No1 = models.CharField(max_length=15, default='')     

    #現金流量
    cS6AA1 = models.CharField(max_length=15, default='')
    cS6A1 = models.CharField(max_length=15, default='')
    cS6BB1 = models.CharField(max_length=15, default='')
    cS6B1 = models.CharField(max_length=15, default='')
    cS6C1 = models.CharField(max_length=15, default='')

    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    
    def __str__(self):
        return self.cStockID  

        

class DCStock6Sign202104(models.Model):
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    


    #營收
    cS1AA1 = models.CharField(max_length=15, default='')
    cS1A1 = models.CharField(max_length=15, default='')
    cS1A2 = models.CharField(max_length=15, default='')
    cS1BB1 = models.CharField(max_length=15, default='')
    cS1BB3 = models.CharField(max_length=15, default='')
    cS1B1 = models.CharField(max_length=15, default='')
    cS1C1 = models.CharField(max_length=15, default='')
    cS1C2 = models.CharField(max_length=15, default='')    


    #營益率
    cS2AA1 = models.CharField(max_length=15, default='')
    cS2AA2 = models.CharField(max_length=15, default='')
    cS2A1 = models.CharField(max_length=15, default='')
    cS2A2 = models.CharField(max_length=15, default='')
    cS2BB1 = models.CharField(max_length=15, default='')
    cS2BB2 = models.CharField(max_length=15, default='')
    cS2BB3 = models.CharField(max_length=15, default='')
    cS2B1 = models.CharField(max_length=15, default='')
    cS2B2 = models.CharField(max_length=15, default='')
    cS2C1 = models.CharField(max_length=15, default='')
    cS2C2 = models.CharField(max_length=15, default='')

    #稅後淨利YoY
    cS3AA1 = models.CharField(max_length=15, default='')
    cS3AA2 = models.CharField(max_length=15, default='')
    cS3A1 = models.CharField(max_length=15, default='')
    cS3BB1 = models.CharField(max_length=15, default='')
    cS3BB2 = models.CharField(max_length=15, default='')
    cS3BB3 = models.CharField(max_length=15, default='')
    cS3B1 = models.CharField(max_length=15, default='')
    cS3B2 = models.CharField(max_length=15, default='')
    cS3B3 = models.CharField(max_length=15, default='')
    cS3C1 = models.CharField(max_length=15, default='')    
    
    
    #EPS
    cS4AA1 = models.CharField(max_length=15, default='')
    cS4A1 = models.CharField(max_length=15, default='')
    cS4BB1 = models.CharField(max_length=15, default='')
    cS4B1 = models.CharField(max_length=15, default='')
    cS4B2 = models.CharField(max_length=15, default='')
    cS4C1 = models.CharField(max_length=15, default='')
   
    #存貨週轉率
    cS5AA1 = models.CharField(max_length=15, default='')
    cS5A1 = models.CharField(max_length=15, default='')
    cS5BB1 = models.CharField(max_length=15, default='')
    cS5BB2 = models.CharField(max_length=15, default='')
    cS5B1 = models.CharField(max_length=15, default='')
    cS5C1 = models.CharField(max_length=15, default='')
    cS5No1 = models.CharField(max_length=15, default='')     

    #現金流量
    cS6AA1 = models.CharField(max_length=15, default='')
    cS6A1 = models.CharField(max_length=15, default='')
    cS6BB1 = models.CharField(max_length=15, default='')
    cS6B1 = models.CharField(max_length=15, default='')
    cS6C1 = models.CharField(max_length=15, default='')

    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    
    def __str__(self):
        return self.cStockID  
    
class DCStock6Sign202105(models.Model):
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    


    #營收
    cS1AA1 = models.CharField(max_length=15, default='')
    cS1A1 = models.CharField(max_length=15, default='')
    cS1A2 = models.CharField(max_length=15, default='')
    cS1BB1 = models.CharField(max_length=15, default='')
    cS1BB3 = models.CharField(max_length=15, default='')
    cS1B1 = models.CharField(max_length=15, default='')
    cS1C1 = models.CharField(max_length=15, default='')
    cS1C2 = models.CharField(max_length=15, default='')    


    #營益率
    cS2AA1 = models.CharField(max_length=15, default='')
    cS2AA2 = models.CharField(max_length=15, default='')
    cS2A1 = models.CharField(max_length=15, default='')
    cS2A2 = models.CharField(max_length=15, default='')
    cS2BB1 = models.CharField(max_length=15, default='')
    cS2BB2 = models.CharField(max_length=15, default='')
    cS2BB3 = models.CharField(max_length=15, default='')
    cS2B1 = models.CharField(max_length=15, default='')
    cS2B2 = models.CharField(max_length=15, default='')
    cS2C1 = models.CharField(max_length=15, default='')
    cS2C2 = models.CharField(max_length=15, default='')

    #稅後淨利YoY
    cS3AA1 = models.CharField(max_length=15, default='')
    cS3AA2 = models.CharField(max_length=15, default='')
    cS3A1 = models.CharField(max_length=15, default='')
    cS3BB1 = models.CharField(max_length=15, default='')
    cS3BB2 = models.CharField(max_length=15, default='')
    cS3BB3 = models.CharField(max_length=15, default='')
    cS3B1 = models.CharField(max_length=15, default='')
    cS3B2 = models.CharField(max_length=15, default='')
    cS3B3 = models.CharField(max_length=15, default='')
    cS3C1 = models.CharField(max_length=15, default='')    
    
    
    #EPS
    cS4AA1 = models.CharField(max_length=15, default='')
    cS4A1 = models.CharField(max_length=15, default='')
    cS4BB1 = models.CharField(max_length=15, default='')
    cS4B1 = models.CharField(max_length=15, default='')
    cS4B2 = models.CharField(max_length=15, default='')
    cS4C1 = models.CharField(max_length=15, default='')
   
    #存貨週轉率
    cS5AA1 = models.CharField(max_length=15, default='')
    cS5A1 = models.CharField(max_length=15, default='')
    cS5BB1 = models.CharField(max_length=15, default='')
    cS5BB2 = models.CharField(max_length=15, default='')
    cS5B1 = models.CharField(max_length=15, default='')
    cS5C1 = models.CharField(max_length=15, default='')
    cS5No1 = models.CharField(max_length=15, default='')     

    #現金流量
    cS6AA1 = models.CharField(max_length=15, default='')
    cS6A1 = models.CharField(max_length=15, default='')
    cS6BB1 = models.CharField(max_length=15, default='')
    cS6B1 = models.CharField(max_length=15, default='')
    cS6C1 = models.CharField(max_length=15, default='')

    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    
    def __str__(self):
        return self.cStockID  


class DCStock6Sign202106(models.Model):
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    


    #營收
    cS1AA1 = models.CharField(max_length=15, default='')
    cS1A1 = models.CharField(max_length=15, default='')
    cS1A2 = models.CharField(max_length=15, default='')
    cS1BB1 = models.CharField(max_length=15, default='')
    cS1BB3 = models.CharField(max_length=15, default='')
    cS1B1 = models.CharField(max_length=15, default='')
    cS1C1 = models.CharField(max_length=15, default='')
    cS1C2 = models.CharField(max_length=15, default='')    


    #營益率
    cS2AA1 = models.CharField(max_length=15, default='')
    cS2AA2 = models.CharField(max_length=15, default='')
    cS2A1 = models.CharField(max_length=15, default='')
    cS2A2 = models.CharField(max_length=15, default='')
    cS2BB1 = models.CharField(max_length=15, default='')
    cS2BB2 = models.CharField(max_length=15, default='')
    cS2BB3 = models.CharField(max_length=15, default='')
    cS2B1 = models.CharField(max_length=15, default='')
    cS2B2 = models.CharField(max_length=15, default='')
    cS2C1 = models.CharField(max_length=15, default='')
    cS2C2 = models.CharField(max_length=15, default='')

    #稅後淨利YoY
    cS3AA1 = models.CharField(max_length=15, default='')
    cS3AA2 = models.CharField(max_length=15, default='')
    cS3A1 = models.CharField(max_length=15, default='')
    cS3BB1 = models.CharField(max_length=15, default='')
    cS3BB2 = models.CharField(max_length=15, default='')
    cS3BB3 = models.CharField(max_length=15, default='')
    cS3B1 = models.CharField(max_length=15, default='')
    cS3B2 = models.CharField(max_length=15, default='')
    cS3B3 = models.CharField(max_length=15, default='')
    cS3C1 = models.CharField(max_length=15, default='')    
    
    
    #EPS
    cS4AA1 = models.CharField(max_length=15, default='')
    cS4A1 = models.CharField(max_length=15, default='')
    cS4BB1 = models.CharField(max_length=15, default='')
    cS4B1 = models.CharField(max_length=15, default='')
    cS4B2 = models.CharField(max_length=15, default='')
    cS4C1 = models.CharField(max_length=15, default='')
   
    #存貨週轉率
    cS5AA1 = models.CharField(max_length=15, default='')
    cS5A1 = models.CharField(max_length=15, default='')
    cS5BB1 = models.CharField(max_length=15, default='')
    cS5BB2 = models.CharField(max_length=15, default='')
    cS5B1 = models.CharField(max_length=15, default='')
    cS5C1 = models.CharField(max_length=15, default='')
    cS5No1 = models.CharField(max_length=15, default='')     

    #現金流量
    cS6AA1 = models.CharField(max_length=15, default='')
    cS6A1 = models.CharField(max_length=15, default='')
    cS6BB1 = models.CharField(max_length=15, default='')
    cS6B1 = models.CharField(max_length=15, default='')
    cS6C1 = models.CharField(max_length=15, default='')

    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    
    def __str__(self):
        return self.cStockID 


class DCStock6Sign202107(models.Model):
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    


    #營收
    cS1AA1 = models.CharField(max_length=15, default='')
    cS1A1 = models.CharField(max_length=15, default='')
    cS1A2 = models.CharField(max_length=15, default='')
    cS1BB1 = models.CharField(max_length=15, default='')
    cS1BB3 = models.CharField(max_length=15, default='')
    cS1B1 = models.CharField(max_length=15, default='')
    cS1C1 = models.CharField(max_length=15, default='')
    cS1C2 = models.CharField(max_length=15, default='')    


    #營益率
    cS2AA1 = models.CharField(max_length=15, default='')
    cS2AA2 = models.CharField(max_length=15, default='')
    cS2A1 = models.CharField(max_length=15, default='')
    cS2A2 = models.CharField(max_length=15, default='')
    cS2BB1 = models.CharField(max_length=15, default='')
    cS2BB2 = models.CharField(max_length=15, default='')
    cS2BB3 = models.CharField(max_length=15, default='')
    cS2B1 = models.CharField(max_length=15, default='')
    cS2B2 = models.CharField(max_length=15, default='')
    cS2C1 = models.CharField(max_length=15, default='')
    cS2C2 = models.CharField(max_length=15, default='')

    #稅後淨利YoY
    cS3AA1 = models.CharField(max_length=15, default='')
    cS3AA2 = models.CharField(max_length=15, default='')
    cS3A1 = models.CharField(max_length=15, default='')
    cS3BB1 = models.CharField(max_length=15, default='')
    cS3BB2 = models.CharField(max_length=15, default='')
    cS3BB3 = models.CharField(max_length=15, default='')
    cS3B1 = models.CharField(max_length=15, default='')
    cS3B2 = models.CharField(max_length=15, default='')
    cS3B3 = models.CharField(max_length=15, default='')
    cS3C1 = models.CharField(max_length=15, default='')    
    
    
    #EPS
    cS4AA1 = models.CharField(max_length=15, default='')
    cS4A1 = models.CharField(max_length=15, default='')
    cS4BB1 = models.CharField(max_length=15, default='')
    cS4B1 = models.CharField(max_length=15, default='')
    cS4B2 = models.CharField(max_length=15, default='')
    cS4C1 = models.CharField(max_length=15, default='')
   
    #存貨週轉率
    cS5AA1 = models.CharField(max_length=15, default='')
    cS5A1 = models.CharField(max_length=15, default='')
    cS5BB1 = models.CharField(max_length=15, default='')
    cS5BB2 = models.CharField(max_length=15, default='')
    cS5B1 = models.CharField(max_length=15, default='')
    cS5C1 = models.CharField(max_length=15, default='')
    cS5No1 = models.CharField(max_length=15, default='')     

    #現金流量
    cS6AA1 = models.CharField(max_length=15, default='')
    cS6A1 = models.CharField(max_length=15, default='')
    cS6BB1 = models.CharField(max_length=15, default='')
    cS6B1 = models.CharField(max_length=15, default='')
    cS6C1 = models.CharField(max_length=15, default='')

    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    
    def __str__(self):
        return self.cStockID 
    
class DCStock6Sign202108(models.Model):
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    


    #營收
    cS1AA1 = models.CharField(max_length=15, default='')
    cS1A1 = models.CharField(max_length=15, default='')
    cS1A2 = models.CharField(max_length=15, default='')
    cS1BB1 = models.CharField(max_length=15, default='')
    cS1BB3 = models.CharField(max_length=15, default='')
    cS1B1 = models.CharField(max_length=15, default='')
    cS1C1 = models.CharField(max_length=15, default='')
    cS1C2 = models.CharField(max_length=15, default='')    


    #營益率
    cS2AA1 = models.CharField(max_length=15, default='')
    cS2AA2 = models.CharField(max_length=15, default='')
    cS2A1 = models.CharField(max_length=15, default='')
    cS2A2 = models.CharField(max_length=15, default='')
    cS2BB1 = models.CharField(max_length=15, default='')
    cS2BB2 = models.CharField(max_length=15, default='')
    cS2BB3 = models.CharField(max_length=15, default='')
    cS2B1 = models.CharField(max_length=15, default='')
    cS2B2 = models.CharField(max_length=15, default='')
    cS2C1 = models.CharField(max_length=15, default='')
    cS2C2 = models.CharField(max_length=15, default='')

    #稅後淨利YoY
    cS3AA1 = models.CharField(max_length=15, default='')
    cS3AA2 = models.CharField(max_length=15, default='')
    cS3A1 = models.CharField(max_length=15, default='')
    cS3BB1 = models.CharField(max_length=15, default='')
    cS3BB2 = models.CharField(max_length=15, default='')
    cS3BB3 = models.CharField(max_length=15, default='')
    cS3B1 = models.CharField(max_length=15, default='')
    cS3B2 = models.CharField(max_length=15, default='')
    cS3B3 = models.CharField(max_length=15, default='')
    cS3C1 = models.CharField(max_length=15, default='')    
    
    
    #EPS
    cS4AA1 = models.CharField(max_length=15, default='')
    cS4A1 = models.CharField(max_length=15, default='')
    cS4BB1 = models.CharField(max_length=15, default='')
    cS4B1 = models.CharField(max_length=15, default='')
    cS4B2 = models.CharField(max_length=15, default='')
    cS4C1 = models.CharField(max_length=15, default='')
   
    #存貨週轉率
    cS5AA1 = models.CharField(max_length=15, default='')
    cS5A1 = models.CharField(max_length=15, default='')
    cS5BB1 = models.CharField(max_length=15, default='')
    cS5BB2 = models.CharField(max_length=15, default='')
    cS5B1 = models.CharField(max_length=15, default='')
    cS5C1 = models.CharField(max_length=15, default='')
    cS5No1 = models.CharField(max_length=15, default='')     

    #現金流量
    cS6AA1 = models.CharField(max_length=15, default='')
    cS6A1 = models.CharField(max_length=15, default='')
    cS6BB1 = models.CharField(max_length=15, default='')
    cS6B1 = models.CharField(max_length=15, default='')
    cS6C1 = models.CharField(max_length=15, default='')

    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    
    def __str__(self):
        return self.cStockID  
    
    
class DCStock6Sign202109(models.Model):
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    


    #營收
    cS1AA1 = models.CharField(max_length=15, default='')
    cS1A1 = models.CharField(max_length=15, default='')
    cS1A2 = models.CharField(max_length=15, default='')
    cS1BB1 = models.CharField(max_length=15, default='')
    cS1BB3 = models.CharField(max_length=15, default='')
    cS1B1 = models.CharField(max_length=15, default='')
    cS1C1 = models.CharField(max_length=15, default='')
    cS1C2 = models.CharField(max_length=15, default='')    


    #營益率
    cS2AA1 = models.CharField(max_length=15, default='')
    cS2AA2 = models.CharField(max_length=15, default='')
    cS2A1 = models.CharField(max_length=15, default='')
    cS2A2 = models.CharField(max_length=15, default='')
    cS2BB1 = models.CharField(max_length=15, default='')
    cS2BB2 = models.CharField(max_length=15, default='')
    cS2BB3 = models.CharField(max_length=15, default='')
    cS2B1 = models.CharField(max_length=15, default='')
    cS2B2 = models.CharField(max_length=15, default='')
    cS2C1 = models.CharField(max_length=15, default='')
    cS2C2 = models.CharField(max_length=15, default='')

    #稅後淨利YoY
    cS3AA1 = models.CharField(max_length=15, default='')
    cS3AA2 = models.CharField(max_length=15, default='')
    cS3A1 = models.CharField(max_length=15, default='')
    cS3BB1 = models.CharField(max_length=15, default='')
    cS3BB2 = models.CharField(max_length=15, default='')
    cS3BB3 = models.CharField(max_length=15, default='')
    cS3B1 = models.CharField(max_length=15, default='')
    cS3B2 = models.CharField(max_length=15, default='')
    cS3B3 = models.CharField(max_length=15, default='')
    cS3C1 = models.CharField(max_length=15, default='')    
    
    
    #EPS
    cS4AA1 = models.CharField(max_length=15, default='')
    cS4A1 = models.CharField(max_length=15, default='')
    cS4BB1 = models.CharField(max_length=15, default='')
    cS4B1 = models.CharField(max_length=15, default='')
    cS4B2 = models.CharField(max_length=15, default='')
    cS4C1 = models.CharField(max_length=15, default='')
   
    #存貨週轉率
    cS5AA1 = models.CharField(max_length=15, default='')
    cS5A1 = models.CharField(max_length=15, default='')
    cS5BB1 = models.CharField(max_length=15, default='')
    cS5BB2 = models.CharField(max_length=15, default='')
    cS5B1 = models.CharField(max_length=15, default='')
    cS5C1 = models.CharField(max_length=15, default='')
    cS5No1 = models.CharField(max_length=15, default='')     

    #現金流量
    cS6AA1 = models.CharField(max_length=15, default='')
    cS6A1 = models.CharField(max_length=15, default='')
    cS6BB1 = models.CharField(max_length=15, default='')
    cS6B1 = models.CharField(max_length=15, default='')
    cS6C1 = models.CharField(max_length=15, default='')

    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    
    def __str__(self):
        return self.cStockID
    
class DCStock6Sign202110(models.Model):
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    


    #營收
    cS1AA1 = models.CharField(max_length=15, default='')
    cS1A1 = models.CharField(max_length=15, default='')
    cS1A2 = models.CharField(max_length=15, default='')
    cS1BB1 = models.CharField(max_length=15, default='')
    cS1BB3 = models.CharField(max_length=15, default='')
    cS1B1 = models.CharField(max_length=15, default='')
    cS1C1 = models.CharField(max_length=15, default='')
    cS1C2 = models.CharField(max_length=15, default='')    


    #營益率
    cS2AA1 = models.CharField(max_length=15, default='')
    cS2AA2 = models.CharField(max_length=15, default='')
    cS2A1 = models.CharField(max_length=15, default='')
    cS2A2 = models.CharField(max_length=15, default='')
    cS2BB1 = models.CharField(max_length=15, default='')
    cS2BB2 = models.CharField(max_length=15, default='')
    cS2BB3 = models.CharField(max_length=15, default='')
    cS2B1 = models.CharField(max_length=15, default='')
    cS2B2 = models.CharField(max_length=15, default='')
    cS2C1 = models.CharField(max_length=15, default='')
    cS2C2 = models.CharField(max_length=15, default='')

    #稅後淨利YoY
    cS3AA1 = models.CharField(max_length=15, default='')
    cS3AA2 = models.CharField(max_length=15, default='')
    cS3A1 = models.CharField(max_length=15, default='')
    cS3BB1 = models.CharField(max_length=15, default='')
    cS3BB2 = models.CharField(max_length=15, default='')
    cS3BB3 = models.CharField(max_length=15, default='')
    cS3B1 = models.CharField(max_length=15, default='')
    cS3B2 = models.CharField(max_length=15, default='')
    cS3B3 = models.CharField(max_length=15, default='')
    cS3C1 = models.CharField(max_length=15, default='')    
    
    
    #EPS
    cS4AA1 = models.CharField(max_length=15, default='')
    cS4A1 = models.CharField(max_length=15, default='')
    cS4BB1 = models.CharField(max_length=15, default='')
    cS4B1 = models.CharField(max_length=15, default='')
    cS4B2 = models.CharField(max_length=15, default='')
    cS4C1 = models.CharField(max_length=15, default='')
   
    #存貨週轉率
    cS5AA1 = models.CharField(max_length=15, default='')
    cS5A1 = models.CharField(max_length=15, default='')
    cS5BB1 = models.CharField(max_length=15, default='')
    cS5BB2 = models.CharField(max_length=15, default='')
    cS5B1 = models.CharField(max_length=15, default='')
    cS5C1 = models.CharField(max_length=15, default='')
    cS5No1 = models.CharField(max_length=15, default='')     

    #現金流量
    cS6AA1 = models.CharField(max_length=15, default='')
    cS6A1 = models.CharField(max_length=15, default='')
    cS6BB1 = models.CharField(max_length=15, default='')
    cS6B1 = models.CharField(max_length=15, default='')
    cS6C1 = models.CharField(max_length=15, default='')

    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    
    def __str__(self):
        return self.cStockID
    
class DCStock6Sign202111(models.Model):
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    


    #營收
    cS1AA1 = models.CharField(max_length=15, default='')
    cS1A1 = models.CharField(max_length=15, default='')
    cS1A2 = models.CharField(max_length=15, default='')
    cS1BB1 = models.CharField(max_length=15, default='')
    cS1BB3 = models.CharField(max_length=15, default='')
    cS1B1 = models.CharField(max_length=15, default='')
    cS1C1 = models.CharField(max_length=15, default='')
    cS1C2 = models.CharField(max_length=15, default='')    


    #營益率
    cS2AA1 = models.CharField(max_length=15, default='')
    cS2AA2 = models.CharField(max_length=15, default='')
    cS2A1 = models.CharField(max_length=15, default='')
    cS2A2 = models.CharField(max_length=15, default='')
    cS2BB1 = models.CharField(max_length=15, default='')
    cS2BB2 = models.CharField(max_length=15, default='')
    cS2BB3 = models.CharField(max_length=15, default='')
    cS2B1 = models.CharField(max_length=15, default='')
    cS2B2 = models.CharField(max_length=15, default='')
    cS2C1 = models.CharField(max_length=15, default='')
    cS2C2 = models.CharField(max_length=15, default='')

    #稅後淨利YoY
    cS3AA1 = models.CharField(max_length=15, default='')
    cS3AA2 = models.CharField(max_length=15, default='')
    cS3A1 = models.CharField(max_length=15, default='')
    cS3BB1 = models.CharField(max_length=15, default='')
    cS3BB2 = models.CharField(max_length=15, default='')
    cS3BB3 = models.CharField(max_length=15, default='')
    cS3B1 = models.CharField(max_length=15, default='')
    cS3B2 = models.CharField(max_length=15, default='')
    cS3B3 = models.CharField(max_length=15, default='')
    cS3C1 = models.CharField(max_length=15, default='')    
    
    
    #EPS
    cS4AA1 = models.CharField(max_length=15, default='')
    cS4A1 = models.CharField(max_length=15, default='')
    cS4BB1 = models.CharField(max_length=15, default='')
    cS4B1 = models.CharField(max_length=15, default='')
    cS4B2 = models.CharField(max_length=15, default='')
    cS4C1 = models.CharField(max_length=15, default='')
   
    #存貨週轉率
    cS5AA1 = models.CharField(max_length=15, default='')
    cS5A1 = models.CharField(max_length=15, default='')
    cS5BB1 = models.CharField(max_length=15, default='')
    cS5BB2 = models.CharField(max_length=15, default='')
    cS5B1 = models.CharField(max_length=15, default='')
    cS5C1 = models.CharField(max_length=15, default='')
    cS5No1 = models.CharField(max_length=15, default='')     

    #現金流量
    cS6AA1 = models.CharField(max_length=15, default='')
    cS6A1 = models.CharField(max_length=15, default='')
    cS6BB1 = models.CharField(max_length=15, default='')
    cS6B1 = models.CharField(max_length=15, default='')
    cS6C1 = models.CharField(max_length=15, default='')

    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    
    def __str__(self):
        return self.cStockID
    
    
class DCStock6Sign202112(models.Model):
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
    
    
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    


    #營收
    cS1AA1 = models.CharField(max_length=15, default='')
    cS1A1 = models.CharField(max_length=15, default='')
    cS1A2 = models.CharField(max_length=15, default='')
    cS1BB1 = models.CharField(max_length=15, default='')
    cS1BB3 = models.CharField(max_length=15, default='')
    cS1B1 = models.CharField(max_length=15, default='')
    cS1C1 = models.CharField(max_length=15, default='')
    cS1C2 = models.CharField(max_length=15, default='')    


    #營益率
    cS2AA1 = models.CharField(max_length=15, default='')
    cS2AA2 = models.CharField(max_length=15, default='')
    cS2A1 = models.CharField(max_length=15, default='')
    cS2A2 = models.CharField(max_length=15, default='')
    cS2BB1 = models.CharField(max_length=15, default='')
    cS2BB2 = models.CharField(max_length=15, default='')
    cS2BB3 = models.CharField(max_length=15, default='')
    cS2B1 = models.CharField(max_length=15, default='')
    cS2B2 = models.CharField(max_length=15, default='')
    cS2C1 = models.CharField(max_length=15, default='')
    cS2C2 = models.CharField(max_length=15, default='')

    #稅後淨利YoY
    cS3AA1 = models.CharField(max_length=15, default='')
    cS3AA2 = models.CharField(max_length=15, default='')
    cS3A1 = models.CharField(max_length=15, default='')
    cS3BB1 = models.CharField(max_length=15, default='')
    cS3BB2 = models.CharField(max_length=15, default='')
    cS3BB3 = models.CharField(max_length=15, default='')
    cS3B1 = models.CharField(max_length=15, default='')
    cS3B2 = models.CharField(max_length=15, default='')
    cS3B3 = models.CharField(max_length=15, default='')
    cS3C1 = models.CharField(max_length=15, default='')    
    
    
    #EPS
    cS4AA1 = models.CharField(max_length=15, default='')
    cS4A1 = models.CharField(max_length=15, default='')
    cS4BB1 = models.CharField(max_length=15, default='')
    cS4B1 = models.CharField(max_length=15, default='')
    cS4B2 = models.CharField(max_length=15, default='')
    cS4C1 = models.CharField(max_length=15, default='')
   
    #存貨週轉率
    cS5AA1 = models.CharField(max_length=15, default='')
    cS5A1 = models.CharField(max_length=15, default='')
    cS5BB1 = models.CharField(max_length=15, default='')
    cS5BB2 = models.CharField(max_length=15, default='')
    cS5B1 = models.CharField(max_length=15, default='')
    cS5C1 = models.CharField(max_length=15, default='')
    cS5No1 = models.CharField(max_length=15, default='')     

    #現金流量
    cS6AA1 = models.CharField(max_length=15, default='')
    cS6A1 = models.CharField(max_length=15, default='')
    cS6BB1 = models.CharField(max_length=15, default='')
    cS6B1 = models.CharField(max_length=15, default='')
    cS6C1 = models.CharField(max_length=15, default='')

    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    
    def __str__(self):
        return self.cStockID
#####################################################
class StockPERseg(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)
    cH1 = models.CharField(max_length=8, null=False)  #以下為最近五年最高價和最低價
    cL1 = models.CharField(max_length=8, null=False)
    cH2 = models.CharField(max_length=8, null=False)
    cL2 = models.CharField(max_length=8, null=False)
    cH3 = models.CharField(max_length=8, null=False)
    cL3 = models.CharField(max_length=8, null=False)
    cH4 = models.CharField(max_length=8, null=False)
    cL4 = models.CharField(max_length=8, null=False)
    cH5 = models.CharField(max_length=8, null=False)
    cL5 = models.CharField(max_length=8, null=False)

    cEPS1 = models.CharField(max_length=8, null=False)  #以下為最近五年EPS
    cEPS2 = models.CharField(max_length=8, null=False)
    cEPS3 = models.CharField(max_length=8, null=False)
    cEPS4 = models.CharField(max_length=8, null=False)
    cEPS5 = models.CharField(max_length=8, null=False)
    
    cPER_H1 = models.CharField(max_length=15, null=False)   #以下為最近五年最高和最低本益比區間
    cPER_L1 = models.CharField(max_length=15, null=False)
    cPER_H2 = models.CharField(max_length=15, null=False)
    cPER_L2 = models.CharField(max_length=15, null=False)
    cPER_H3 = models.CharField(max_length=15, null=False)
    cPER_L3 = models.CharField(max_length=15, null=False)
    cPER_H4 = models.CharField(max_length=15, null=False)
    cPER_L4 = models.CharField(max_length=15, null=False)
    cPER_H5 = models.CharField(max_length=15, null=False)
    cPER_L5 = models.CharField(max_length=15, null=False)
    
    cPER_H_average = models.CharField(max_length=15, null=False)  #最近五年平均
    cPER_L_average = models.CharField(max_length=15, null=False)

    cPER_H = models.CharField(max_length=15, null=False)  #本益比兩者孰低
    cPER_L = models.CharField(max_length=15, null=False)    
    
    cYoY6Average = models.CharField(max_length=15, null=False)  #營收六個月平均
    cRevYoY = models.CharField(max_length=15, null=False)  #營收兩者孰低    
    
    cNet1 = models.CharField(max_length=15, null=False)
    cNet2 = models.CharField(max_length=15, null=False)
    cNet3 = models.CharField(max_length=15, null=False)
    cNet4 = models.CharField(max_length=15, null=False)
    cNet4Average = models.CharField(max_length=15, null=False)    

    cRev_Predict = models.CharField(max_length=15, null=False) #預估未來營收
    cNet_Predict = models.CharField(max_length=15, null=False) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15, null=False) #最新股本
    cPredict_EPS = models.CharField(max_length=15, null=False) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15, null=False) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15, null=False) #預估未來最低價    
    cLatest_price = models.CharField(max_length=15, null=False) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=15, null=False) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=15, null=False) #預估未來往下空間    
    
    cRisk_reward = models.CharField(max_length=10, null=False) #預估風險報酬比率
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
   

class StockPERseg202005(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)
    cH1 = models.CharField(max_length=8, null=False)  #以下為最近五年最高價和最低價
    cL1 = models.CharField(max_length=8, null=False)
    cH2 = models.CharField(max_length=8, null=False)
    cL2 = models.CharField(max_length=8, null=False)
    cH3 = models.CharField(max_length=8, null=False)
    cL3 = models.CharField(max_length=8, null=False)
    cH4 = models.CharField(max_length=8, null=False)
    cL4 = models.CharField(max_length=8, null=False)
    cH5 = models.CharField(max_length=8, null=False)
    cL5 = models.CharField(max_length=8, null=False)

    cEPS1 = models.CharField(max_length=8, null=False)  #以下為最近五年EPS
    cEPS2 = models.CharField(max_length=8, null=False)
    cEPS3 = models.CharField(max_length=8, null=False)
    cEPS4 = models.CharField(max_length=8, null=False)
    cEPS5 = models.CharField(max_length=8, null=False)
    
    cPER_H1 = models.CharField(max_length=15, null=False)   #以下為最近五年最高和最低本益比區間
    cPER_L1 = models.CharField(max_length=15, null=False)
    cPER_H2 = models.CharField(max_length=15, null=False)
    cPER_L2 = models.CharField(max_length=15, null=False)
    cPER_H3 = models.CharField(max_length=15, null=False)
    cPER_L3 = models.CharField(max_length=15, null=False)
    cPER_H4 = models.CharField(max_length=15, null=False)
    cPER_L4 = models.CharField(max_length=15, null=False)
    cPER_H5 = models.CharField(max_length=15, null=False)
    cPER_L5 = models.CharField(max_length=15, null=False)
    
    cPER_H_average = models.CharField(max_length=15, null=False)  #最近五年平均
    cPER_L_average = models.CharField(max_length=15, null=False)

    cPER_H = models.CharField(max_length=15, null=False)  #本益比兩者孰低
    cPER_L = models.CharField(max_length=15, null=False)    
    
    cYoY6Average = models.CharField(max_length=15, null=False)  #營收六個月平均
    cRevYoY = models.CharField(max_length=15, null=False)  #營收兩者孰低    
    
    cNet1 = models.CharField(max_length=15, null=False)
    cNet2 = models.CharField(max_length=15, null=False)
    cNet3 = models.CharField(max_length=15, null=False)
    cNet4 = models.CharField(max_length=15, null=False)
    cNet4Average = models.CharField(max_length=15, null=False)    

    cRev_Predict = models.CharField(max_length=15, null=False) #預估未來營收
    cNet_Predict = models.CharField(max_length=15, null=False) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15, null=False) #最新股本
    cPredict_EPS = models.CharField(max_length=15, null=False) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15, null=False) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15, null=False) #預估未來最低價    
    cLatest_price = models.CharField(max_length=15, null=False) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=15, null=False) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=15, null=False) #預估未來往下空間    
    
    cRisk_reward = models.CharField(max_length=10, null=False) #預估風險報酬比率
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID


class StockPERseg202006(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)
    cH1 = models.CharField(max_length=8, null=False)  #以下為最近五年最高價和最低價
    cL1 = models.CharField(max_length=8, null=False)
    cH2 = models.CharField(max_length=8, null=False)
    cL2 = models.CharField(max_length=8, null=False)
    cH3 = models.CharField(max_length=8, null=False)
    cL3 = models.CharField(max_length=8, null=False)
    cH4 = models.CharField(max_length=8, null=False)
    cL4 = models.CharField(max_length=8, null=False)
    cH5 = models.CharField(max_length=8, null=False)
    cL5 = models.CharField(max_length=8, null=False)

    cEPS1 = models.CharField(max_length=8, null=False)  #以下為最近五年EPS
    cEPS2 = models.CharField(max_length=8, null=False)
    cEPS3 = models.CharField(max_length=8, null=False)
    cEPS4 = models.CharField(max_length=8, null=False)
    cEPS5 = models.CharField(max_length=8, null=False)
    
    cPER_H1 = models.CharField(max_length=15, null=False)   #以下為最近五年最高和最低本益比區間
    cPER_L1 = models.CharField(max_length=15, null=False)
    cPER_H2 = models.CharField(max_length=15, null=False)
    cPER_L2 = models.CharField(max_length=15, null=False)
    cPER_H3 = models.CharField(max_length=15, null=False)
    cPER_L3 = models.CharField(max_length=15, null=False)
    cPER_H4 = models.CharField(max_length=15, null=False)
    cPER_L4 = models.CharField(max_length=15, null=False)
    cPER_H5 = models.CharField(max_length=15, null=False)
    cPER_L5 = models.CharField(max_length=15, null=False)
    
    cPER_H_average = models.CharField(max_length=15, null=False)  #最近五年平均
    cPER_L_average = models.CharField(max_length=15, null=False)

    cPER_H = models.CharField(max_length=15, null=False)  #本益比兩者孰低
    cPER_L = models.CharField(max_length=15, null=False)    
    
    cYoY6Average = models.CharField(max_length=15, null=False)  #營收六個月平均
    cRevYoY = models.CharField(max_length=15, null=False)  #營收兩者孰低    
    
    cNet1 = models.CharField(max_length=15, null=False)
    cNet2 = models.CharField(max_length=15, null=False)
    cNet3 = models.CharField(max_length=15, null=False)
    cNet4 = models.CharField(max_length=15, null=False)
    cNet4Average = models.CharField(max_length=15, null=False)    

    cRev_Predict = models.CharField(max_length=15, null=False) #預估未來營收
    cNet_Predict = models.CharField(max_length=15, null=False) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15, null=False) #最新股本
    cPredict_EPS = models.CharField(max_length=15, null=False) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15, null=False) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15, null=False) #預估未來最低價    
    cLatest_price = models.CharField(max_length=15, null=False) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=15, null=False) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=15, null=False) #預估未來往下空間    
    
    cRisk_reward = models.CharField(max_length=10, null=False) #預估風險報酬比率
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID


class StockPERseg2020Q2(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15, null=False) #預估未來營收
    cNet_Predict = models.CharField(max_length=15, null=False) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15, null=False) #最新股本
    cPredict_EPS = models.CharField(max_length=15, null=False) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15, null=False) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15, null=False) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25, null=False) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25, null=False) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25, null=False) #預估未來往下空間    
    
    cRisk_reward = models.CharField(max_length=10, null=False) #預估風險報酬比率
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID



class StockPERseg202007(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15, null=False) #預估未來營收
    cNet_Predict = models.CharField(max_length=15, null=False) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15, null=False) #最新股本
    cPredict_EPS = models.CharField(max_length=15, null=False) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15, null=False) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15, null=False) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25, null=False) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25, null=False) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25, null=False) #預估未來往下空間    
    
    cRisk_reward = models.CharField(max_length=10, null=False) #預估風險報酬比率
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID

class StockPERseg202008(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15, null=False) #預估未來營收
    cNet_Predict = models.CharField(max_length=15, null=False) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15, null=False) #最新股本
    cPredict_EPS = models.CharField(max_length=15, null=False) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15, null=False) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15, null=False) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25, null=False) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25, null=False) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25, null=False) #預估未來往下空間    
    
    cRisk_reward = models.CharField(max_length=10, null=False) #預估風險報酬比率
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID

class StockPERseg202009(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15, null=False) #預估未來營收
    cNet_Predict = models.CharField(max_length=15, null=False) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15, null=False) #最新股本
    cPredict_EPS = models.CharField(max_length=15, null=False) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15, null=False) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15, null=False) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25, null=False) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25, null=False) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25, null=False) #預估未來往下空間    
    
    cRisk_reward = models.CharField(max_length=10, null=False) #預估風險報酬比率
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID

class StockPERseg2020Q3(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15, null=False) #預估未來營收
    cNet_Predict = models.CharField(max_length=15, null=False) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15, null=False) #最新股本
    cPredict_EPS = models.CharField(max_length=15, null=False) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15, null=False) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15, null=False) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25, null=False) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25, null=False) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25, null=False) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID

class StockPERseg202011(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
class StockPERseg2020Q4(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID   

class StockPERseg202101(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID  


class StockPERseg202102(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID  

class StockPERseg202103(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 

class StockPERseg202104(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID  
    
class StockPERseg202105(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID      


class StockPERseg202106(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 
    
class StockPERseg202107(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID


class StockPERseg202108(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 
    
class StockPERseg202109(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 


class StockPERseg202110(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 

class StockPERseg202111(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 

class StockPERseg202112(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 

class StockPERseg202201(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 
    
class StockPERseg202202(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 
    
class StockPERseg202203(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 
    
class StockPERseg202204(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 
    
class StockPERseg202205(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 
    
    
class StockPERseg202206(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 
    
class StockPERseg202207(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 
    
class StockPERseg202208(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 
    
class StockPERseg202209(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 
    
class StockPERseg202210(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 
    
class StockPERseg202211(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 
    
class StockPERseg202212(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 
#####

class StockPERseg202301(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float


    cPredict_high_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價      
    cNew_up_profit_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間
    cRisk_reward_down30 = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float


    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    

class StockPERseg202302(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float


    cPredict_high_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價      
    cNew_up_profit_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間
    cRisk_reward_down30 = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float


    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    

class StockPERseg202303(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float


    cPredict_high_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價      
    cNew_up_profit_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間
    cRisk_reward_down30 = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float


    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    

class StockPERseg202304(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float


    cPredict_high_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價      
    cNew_up_profit_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間
    cRisk_reward_down30 = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float


    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    

class StockPERseg202305(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float


    cPredict_high_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價      
    cNew_up_profit_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間
    cRisk_reward_down30 = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float


    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    

class StockPERseg202306(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float


    cPredict_high_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價      
    cNew_up_profit_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間
    cRisk_reward_down30 = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float


    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
    

class StockPERseg202307(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float


    cPredict_high_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價      
    cNew_up_profit_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間
    cRisk_reward_down30 = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float


    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    

class StockPERseg202308(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float


    cPredict_high_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價      
    cNew_up_profit_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間
    cRisk_reward_down30 = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float


    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    

class StockPERseg202309(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float


    cPredict_high_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價      
    cNew_up_profit_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間
    cRisk_reward_down30 = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float


    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    

class StockPERseg202310(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float


    cPredict_high_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價      
    cNew_up_profit_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間
    cRisk_reward_down30 = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float


    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    

class StockPERseg202311(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float


    cPredict_high_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價      
    cNew_up_profit_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間
    cRisk_reward_down30 = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float


    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
    

class StockPERseg202312(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)



    cRev_Predict = models.CharField(max_length=15) #預估未來營收
    cNet_Predict = models.CharField(max_length=15) #預估未來淨利
    cCapital_stock = models.CharField(max_length=15) #最新股本
    cPredict_EPS = models.CharField(max_length=15) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15) #預估未來最低價    
    cLatest_price = models.CharField(max_length=25) #目前最新成交價
    cNew_up_profit = models.CharField(max_length=25) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25) #預估未來往下空間    
    
    cRisk_reward = models.FloatField(max_length=20) #預估風險報酬比率  #20201202 可以使用Float


    cPredict_high_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價      
    cNew_up_profit_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間
    cRisk_reward_down30 = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float


    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
###############################################################################    

##########################################################################
    
class EPSachieve(models.Model):
    cStockID = models.CharField(max_length=8, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    cEPS1 = models.CharField(max_length=10, null=False)  
    cEPSQ1 = models.CharField(max_length=10, null=False)
    #cEPSQ2 = models.CharField(max_length=10)
    #cEPSQ3 = models.CharField(max_length=10)
    cEPSAchieveRate = models.CharField(max_length=10, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
class EPSachieve2020Q2(models.Model):
    cStockID = models.CharField(max_length=8, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    cEPS1 = models.CharField(max_length=20, null=False)  
    cEPSQ1 = models.CharField(max_length=20, null=False)
    cEPSQ2 = models.CharField(max_length=20, null=False)
    #cEPSQ3 = models.CharField(max_length=10)
    cEPSAchieveRate = models.CharField(max_length=20, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID


class EPSachieve2020Q3(models.Model):
    cStockID = models.CharField(max_length=8, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    cEPS1 = models.CharField(max_length=20, null=False)  
    cEPSQ1 = models.CharField(max_length=20, null=False)
    cEPSQ2 = models.CharField(max_length=20, null=False)
    cEPSQ3 = models.CharField(max_length=20)
    cEPSAchieveRate = models.CharField(max_length=20, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID

class EPSachieve2021Q1(models.Model):
    cStockID = models.CharField(max_length=8, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    cEPS1 = models.CharField(max_length=20, null=False)  
    cEPSQ1 = models.CharField(max_length=20, null=False)
    #cEPSQ2 = models.CharField(max_length=20, null=False)
    #cEPSQ3 = models.CharField(max_length=20)
    cEPSAchieveRate = models.CharField(max_length=20, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID


class EPSachieve2021Q2(models.Model):
    cStockID = models.CharField(max_length=8, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    cEPS1 = models.CharField(max_length=20, null=False)  
    cEPSQ1 = models.CharField(max_length=20, null=False)
    cEPSQ2 = models.CharField(max_length=20, null=False)
    #cEPSQ3 = models.CharField(max_length=20)
    cEPSAchieveRate = models.CharField(max_length=20, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID


class EPSachieve2021Q3(models.Model):
    cStockID = models.CharField(max_length=8, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    cEPS1 = models.CharField(max_length=20, null=False)  
    cEPSQ1 = models.CharField(max_length=20, null=False)
    cEPSQ2 = models.CharField(max_length=20, null=False)
    cEPSQ3 = models.CharField(max_length=20, null=False)
    cEPSAchieveRate = models.CharField(max_length=20, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
class EPSachieve2022Q1(models.Model):
    cStockID = models.CharField(max_length=8, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    cEPS1 = models.CharField(max_length=20, null=False)  
    cEPSQ1 = models.CharField(max_length=20, null=False)
    #cEPSQ2 = models.CharField(max_length=20, null=False)
    #cEPSQ3 = models.CharField(max_length=20)
    cEPSAchieveRate = models.CharField(max_length=20, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID


class EPSachieve2022Q2(models.Model):
    cStockID = models.CharField(max_length=8, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    cEPS1 = models.CharField(max_length=20, null=False)  
    cEPSQ1 = models.CharField(max_length=20, null=False)
    cEPSQ2 = models.CharField(max_length=20, null=False)
    #cEPSQ3 = models.CharField(max_length=20)
    cEPSAchieveRate = models.CharField(max_length=20, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID


class EPSachieve2022Q3(models.Model):
    cStockID = models.CharField(max_length=8, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    cEPS1 = models.CharField(max_length=20, null=False)  
    cEPSQ1 = models.CharField(max_length=20, null=False)
    cEPSQ2 = models.CharField(max_length=20, null=False)
    cEPSQ3 = models.CharField(max_length=20, null=False)
    cEPSAchieveRate = models.CharField(max_length=20, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
class EPSachieve2023Q1(models.Model):
    cStockID = models.CharField(max_length=8, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    cEPS1 = models.CharField(max_length=20, null=False)  
    cEPSQ1 = models.CharField(max_length=20, null=False)
    #cEPSQ2 = models.CharField(max_length=20, null=False)
    #cEPSQ3 = models.CharField(max_length=20)
    cEPSAchieveRate = models.CharField(max_length=20, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
#####################################################################
class StockCapVar(models.Model):
    cStockID = models.CharField(max_length=8, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    cCap1 = models.CharField(max_length=10, null=False)  
    cCap2 = models.CharField(max_length=10, null=False)
    cCap3 = models.CharField(max_length=10, null=False)  
    cCap4 = models.CharField(max_length=10, null=False)
    cCap5 = models.CharField(max_length=10, null=False)  
    cCap6 = models.CharField(max_length=10, null=False)
    cCap7 = models.CharField(max_length=10, null=False)  
    cCap8 = models.CharField(max_length=10, null=False)    

    cLatestYoY = models.CharField(max_length=10, null=False)
    cLatestMoM = models.CharField(max_length=10, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
    
class StockCapVar2020Q2(models.Model):
    cStockID = models.CharField(max_length=8, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    cCap1 = models.CharField(max_length=20, null=False)  
    cCap2 = models.CharField(max_length=20, null=False)
    cCap3 = models.CharField(max_length=20, null=False)  
    cCap4 = models.CharField(max_length=20, null=False)
    cCap5 = models.CharField(max_length=20, null=False)  
    cCap6 = models.CharField(max_length=20, null=False)
    cCap7 = models.CharField(max_length=20, null=False)  
    cCap8 = models.CharField(max_length=20, null=False)    

    cLatestYoY = models.CharField(max_length=20, null=False)
    cLatestMoM = models.CharField(max_length=20, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
    
class StockCapVar2020Q3(models.Model):
    cStockID = models.CharField(max_length=8, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    cCap1 = models.CharField(max_length=20, null=False)  
    cCap2 = models.CharField(max_length=20, null=False)
    cCap3 = models.CharField(max_length=20, null=False)  
    cCap4 = models.CharField(max_length=20, null=False)
    cCap5 = models.CharField(max_length=20, null=False)  
    cCap6 = models.CharField(max_length=20, null=False)
    cCap7 = models.CharField(max_length=20, null=False)  
    cCap8 = models.CharField(max_length=20, null=False)    

    cLatestYoY = models.CharField(max_length=20, null=False)
    cLatestMoM = models.CharField(max_length=20, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID    


class StockCapVar2020Q4(models.Model):
    cStockID = models.CharField(max_length=8, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    cCap1 = models.CharField(max_length=20, null=False)  
    cCap2 = models.CharField(max_length=20, null=False)
    cCap3 = models.CharField(max_length=20, null=False)  
    cCap4 = models.CharField(max_length=20, null=False)
    cCap5 = models.CharField(max_length=20, null=False)  
    cCap6 = models.CharField(max_length=20, null=False)
    cCap7 = models.CharField(max_length=20, null=False)  
    cCap8 = models.CharField(max_length=20, null=False)    

    cLatestYoY = models.CharField(max_length=20, null=False)
    cLatestMoM = models.CharField(max_length=20, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID  


class StockCapVar2021Q1(models.Model):
    cStockID = models.CharField(max_length=8, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    cCap1 = models.CharField(max_length=20, null=False)  
    cCap2 = models.CharField(max_length=20, null=False)
    cCap3 = models.CharField(max_length=20, null=False)  
    cCap4 = models.CharField(max_length=20, null=False)
    cCap5 = models.CharField(max_length=20, null=False)  
    cCap6 = models.CharField(max_length=20, null=False)
    cCap7 = models.CharField(max_length=20, null=False)  
    cCap8 = models.CharField(max_length=20, null=False)    

    cLatestYoY = models.CharField(max_length=20, null=False)
    cLatestMoM = models.CharField(max_length=20, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 

class StockCapVar2021Q2(models.Model):
    cStockID = models.CharField(max_length=8, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    cCap1 = models.CharField(max_length=20, null=False)  
    cCap2 = models.CharField(max_length=20, null=False)
    cCap3 = models.CharField(max_length=20, null=False)  
    cCap4 = models.CharField(max_length=20, null=False)
    cCap5 = models.CharField(max_length=20, null=False)  
    cCap6 = models.CharField(max_length=20, null=False)
    cCap7 = models.CharField(max_length=20, null=False)  
    cCap8 = models.CharField(max_length=20, null=False)    

    cLatestYoY = models.CharField(max_length=20, null=False)
    cLatestMoM = models.CharField(max_length=20, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID     
    
class StockCapVar2021Q3(models.Model):
    cStockID = models.CharField(max_length=8, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    cCap1 = models.CharField(max_length=20, null=False)  
    cCap2 = models.CharField(max_length=20, null=False)
    cCap3 = models.CharField(max_length=20, null=False)  
    cCap4 = models.CharField(max_length=20, null=False)
    cCap5 = models.CharField(max_length=20, null=False)  
    cCap6 = models.CharField(max_length=20, null=False)
    cCap7 = models.CharField(max_length=20, null=False)  
    cCap8 = models.CharField(max_length=20, null=False)    

    cLatestYoY = models.CharField(max_length=20, null=False)
    cLatestMoM = models.CharField(max_length=20, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID  
    
    
class StockCapVar2021Q4(models.Model):
    cStockID = models.CharField(max_length=8, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    cCap1 = models.CharField(max_length=20, null=False)  
    cCap2 = models.CharField(max_length=20, null=False)
    cCap3 = models.CharField(max_length=20, null=False)  
    cCap4 = models.CharField(max_length=20, null=False)
    cCap5 = models.CharField(max_length=20, null=False)  
    cCap6 = models.CharField(max_length=20, null=False)
    cCap7 = models.CharField(max_length=20, null=False)  
    cCap8 = models.CharField(max_length=20, null=False)    

    cLatestYoY = models.CharField(max_length=20, null=False)
    cLatestMoM = models.CharField(max_length=20, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID  
    
    

class StockCapVar2022Q1(models.Model):
    cStockID = models.CharField(max_length=8, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    cCap1 = models.CharField(max_length=20, null=False)  
    cCap2 = models.CharField(max_length=20, null=False)
    cCap3 = models.CharField(max_length=20, null=False)  
    cCap4 = models.CharField(max_length=20, null=False)
    cCap5 = models.CharField(max_length=20, null=False)  
    cCap6 = models.CharField(max_length=20, null=False)
    cCap7 = models.CharField(max_length=20, null=False)  
    cCap8 = models.CharField(max_length=20, null=False)    

    cLatestYoY = models.CharField(max_length=20, null=False)
    cLatestMoM = models.CharField(max_length=20, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID 

class StockCapVar2022Q2(models.Model):
    cStockID = models.CharField(max_length=8, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    cCap1 = models.CharField(max_length=20, null=False)  
    cCap2 = models.CharField(max_length=20, null=False)
    cCap3 = models.CharField(max_length=20, null=False)  
    cCap4 = models.CharField(max_length=20, null=False)
    cCap5 = models.CharField(max_length=20, null=False)  
    cCap6 = models.CharField(max_length=20, null=False)
    cCap7 = models.CharField(max_length=20, null=False)  
    cCap8 = models.CharField(max_length=20, null=False)    

    cLatestYoY = models.CharField(max_length=20, null=False)
    cLatestMoM = models.CharField(max_length=20, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID     
    
class StockCapVar2022Q3(models.Model):
    cStockID = models.CharField(max_length=8, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    cCap1 = models.CharField(max_length=20, null=False)  
    cCap2 = models.CharField(max_length=20, null=False)
    cCap3 = models.CharField(max_length=20, null=False)  
    cCap4 = models.CharField(max_length=20, null=False)
    cCap5 = models.CharField(max_length=20, null=False)  
    cCap6 = models.CharField(max_length=20, null=False)
    cCap7 = models.CharField(max_length=20, null=False)  
    cCap8 = models.CharField(max_length=20, null=False)    

    cLatestYoY = models.CharField(max_length=20, null=False)
    cLatestMoM = models.CharField(max_length=20, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID  
    
    
class StockCapVar2022Q4(models.Model):
    cStockID = models.CharField(max_length=8, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    cCap1 = models.CharField(max_length=20, null=False)  
    cCap2 = models.CharField(max_length=20, null=False)
    cCap3 = models.CharField(max_length=20, null=False)  
    cCap4 = models.CharField(max_length=20, null=False)
    cCap5 = models.CharField(max_length=20, null=False)  
    cCap6 = models.CharField(max_length=20, null=False)
    cCap7 = models.CharField(max_length=20, null=False)  
    cCap8 = models.CharField(max_length=20, null=False)    

    cLatestYoY = models.CharField(max_length=20, null=False)
    cLatestMoM = models.CharField(max_length=20, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID  
    
class StockCapVar2023Q1(models.Model):
    cStockID = models.CharField(max_length=8, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    cCap1 = models.CharField(max_length=20, null=False)  
    cCap2 = models.CharField(max_length=20, null=False)
    cCap3 = models.CharField(max_length=20, null=False)  
    cCap4 = models.CharField(max_length=20, null=False)
    cCap5 = models.CharField(max_length=20, null=False)  
    cCap6 = models.CharField(max_length=20, null=False)
    cCap7 = models.CharField(max_length=20, null=False)  
    cCap8 = models.CharField(max_length=20, null=False)    

    cLatestYoY = models.CharField(max_length=20, null=False)
    cLatestMoM = models.CharField(max_length=20, null=False)
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
###########################################################    

class EpsProfit2020Q1(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)

    cEPS1 = models.CharField(max_length=10, null=False)  #以下為最近8季EPS
    cEPS2 = models.CharField(max_length=10, null=False)
    cEPS3 = models.CharField(max_length=10, null=False)
    cEPS4 = models.CharField(max_length=10, null=False)
    cEPS5 = models.CharField(max_length=10, null=False)
    cEPS6 = models.CharField(max_length=10, null=False) 
    cEPS7 = models.CharField(max_length=10, null=False)
    cEPS8 = models.CharField(max_length=10, null=False)

    #cEPS8MAX = models.CharField(max_length=10, null=False)
    
    
    cProf1 = models.CharField(max_length=10, null=False)  #以下為最近8季EPS
    cProf2 = models.CharField(max_length=10, null=False)
    cProf3 = models.CharField(max_length=10, null=False)
    cProf4 = models.CharField(max_length=10, null=False)
    cProf5 = models.CharField(max_length=10, null=False)
    cProf6 = models.CharField(max_length=10, null=False) 
    cProf7 = models.CharField(max_length=10, null=False)
    cProf8 = models.CharField(max_length=10, null=False)

    #cProf8MAX = models.CharField(max_length=10, null=False)
    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
    
class EpsProfit2020Q2(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)

    cEPS1 = models.CharField(max_length=20, null=False)  #以下為最近8季EPS
    cEPS2 = models.CharField(max_length=20, null=False)
    cEPS3 = models.CharField(max_length=20, null=False)
    cEPS4 = models.CharField(max_length=20, null=False)
    cEPS5 = models.CharField(max_length=20, null=False)
    cEPS6 = models.CharField(max_length=20, null=False) 
    cEPS7 = models.CharField(max_length=20, null=False)
    cEPS8 = models.CharField(max_length=20, null=False)

    #cEPS8MAX = models.CharField(max_length=10, null=False)
    
    
    cProf1 = models.CharField(max_length=20, null=False)  #以下為最近8季EPS
    cProf2 = models.CharField(max_length=20, null=False)
    cProf3 = models.CharField(max_length=20, null=False)
    cProf4 = models.CharField(max_length=20, null=False)
    cProf5 = models.CharField(max_length=20, null=False)
    cProf6 = models.CharField(max_length=20, null=False) 
    cProf7 = models.CharField(max_length=20, null=False)
    cProf8 = models.CharField(max_length=20, null=False)

    #cProf8MAX = models.CharField(max_length=10, null=False)
    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    

class EpsProfit2020Q3(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)

    cEPS1 = models.CharField(max_length=20, null=False)  #以下為最近8季EPS
    cEPS2 = models.CharField(max_length=20, null=False)
    cEPS3 = models.CharField(max_length=20, null=False)
    cEPS4 = models.CharField(max_length=20, null=False)
    cEPS5 = models.CharField(max_length=20, null=False)
    cEPS6 = models.CharField(max_length=20, null=False) 
    cEPS7 = models.CharField(max_length=20, null=False)
    cEPS8 = models.CharField(max_length=20, null=False)

    #cEPS8MAX = models.CharField(max_length=10, null=False)
    
    
    cProf1 = models.CharField(max_length=20, null=False)  #以下為最近8季EPS
    cProf2 = models.CharField(max_length=20, null=False)
    cProf3 = models.CharField(max_length=20, null=False)
    cProf4 = models.CharField(max_length=20, null=False)
    cProf5 = models.CharField(max_length=20, null=False)
    cProf6 = models.CharField(max_length=20, null=False) 
    cProf7 = models.CharField(max_length=20, null=False)
    cProf8 = models.CharField(max_length=20, null=False)

    #cProf8MAX = models.CharField(max_length=10, null=False)
    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID


class EpsProfit2020Q4(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)

    cEPS1 = models.CharField(max_length=20, null=False)  #以下為最近8季EPS
    cEPS2 = models.CharField(max_length=20, null=False)
    cEPS3 = models.CharField(max_length=20, null=False)
    cEPS4 = models.CharField(max_length=20, null=False)
    cEPS5 = models.CharField(max_length=20, null=False)
    cEPS6 = models.CharField(max_length=20, null=False) 
    cEPS7 = models.CharField(max_length=20, null=False)
    cEPS8 = models.CharField(max_length=20, null=False)

    #cEPS8MAX = models.CharField(max_length=10, null=False)
    
    
    cProf1 = models.CharField(max_length=20, null=False)  #以下為最近8季EPS
    cProf2 = models.CharField(max_length=20, null=False)
    cProf3 = models.CharField(max_length=20, null=False)
    cProf4 = models.CharField(max_length=20, null=False)
    cProf5 = models.CharField(max_length=20, null=False)
    cProf6 = models.CharField(max_length=20, null=False) 
    cProf7 = models.CharField(max_length=20, null=False)
    cProf8 = models.CharField(max_length=20, null=False)

    #cProf8MAX = models.CharField(max_length=10, null=False)
    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID

class EpsProfit2021Q1(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)

    cEPS1 = models.CharField(max_length=20, null=False)  #以下為最近8季EPS
    cEPS2 = models.CharField(max_length=20, null=False)
    cEPS3 = models.CharField(max_length=20, null=False)
    cEPS4 = models.CharField(max_length=20, null=False)
    cEPS5 = models.CharField(max_length=20, null=False)
    cEPS6 = models.CharField(max_length=20, null=False) 
    cEPS7 = models.CharField(max_length=20, null=False)
    cEPS8 = models.CharField(max_length=20, null=False)

    #cEPS8MAX = models.CharField(max_length=10, null=False)
    
    
    cProf1 = models.CharField(max_length=20, null=False)  #以下為最近8季EPS
    cProf2 = models.CharField(max_length=20, null=False)
    cProf3 = models.CharField(max_length=20, null=False)
    cProf4 = models.CharField(max_length=20, null=False)
    cProf5 = models.CharField(max_length=20, null=False)
    cProf6 = models.CharField(max_length=20, null=False) 
    cProf7 = models.CharField(max_length=20, null=False)
    cProf8 = models.CharField(max_length=20, null=False)

    #cProf8MAX = models.CharField(max_length=10, null=False)
    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
class EpsProfit2021Q2(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)

    cEPS1 = models.CharField(max_length=20, null=False)  #以下為最近8季EPS
    cEPS2 = models.CharField(max_length=20, null=False)
    cEPS3 = models.CharField(max_length=20, null=False)
    cEPS4 = models.CharField(max_length=20, null=False)
    cEPS5 = models.CharField(max_length=20, null=False)
    cEPS6 = models.CharField(max_length=20, null=False) 
    cEPS7 = models.CharField(max_length=20, null=False)
    cEPS8 = models.CharField(max_length=20, null=False)

    #cEPS8MAX = models.CharField(max_length=10, null=False)
    
    
    cProf1 = models.CharField(max_length=20, null=False)  #以下為最近8季EPS
    cProf2 = models.CharField(max_length=20, null=False)
    cProf3 = models.CharField(max_length=20, null=False)
    cProf4 = models.CharField(max_length=20, null=False)
    cProf5 = models.CharField(max_length=20, null=False)
    cProf6 = models.CharField(max_length=20, null=False) 
    cProf7 = models.CharField(max_length=20, null=False)
    cProf8 = models.CharField(max_length=20, null=False)

    #cProf8MAX = models.CharField(max_length=10, null=False)
    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
    
class EpsProfit2021Q3(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)

    cEPS1 = models.CharField(max_length=20, null=False)  #以下為最近8季EPS
    cEPS2 = models.CharField(max_length=20, null=False)
    cEPS3 = models.CharField(max_length=20, null=False)
    cEPS4 = models.CharField(max_length=20, null=False)
    cEPS5 = models.CharField(max_length=20, null=False)
    cEPS6 = models.CharField(max_length=20, null=False) 
    cEPS7 = models.CharField(max_length=20, null=False)
    cEPS8 = models.CharField(max_length=20, null=False)

    #cEPS8MAX = models.CharField(max_length=10, null=False)
    
    
    cProf1 = models.CharField(max_length=20, null=False)  #以下為最近8季EPS
    cProf2 = models.CharField(max_length=20, null=False)
    cProf3 = models.CharField(max_length=20, null=False)
    cProf4 = models.CharField(max_length=20, null=False)
    cProf5 = models.CharField(max_length=20, null=False)
    cProf6 = models.CharField(max_length=20, null=False) 
    cProf7 = models.CharField(max_length=20, null=False)
    cProf8 = models.CharField(max_length=20, null=False)

    #cProf8MAX = models.CharField(max_length=10, null=False)
    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
class EpsProfit2021Q4(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)

    cEPS1 = models.CharField(max_length=20, null=False)  #以下為最近8季EPS
    cEPS2 = models.CharField(max_length=20, null=False)
    cEPS3 = models.CharField(max_length=20, null=False)
    cEPS4 = models.CharField(max_length=20, null=False)
    cEPS5 = models.CharField(max_length=20, null=False)
    cEPS6 = models.CharField(max_length=20, null=False) 
    cEPS7 = models.CharField(max_length=20, null=False)
    cEPS8 = models.CharField(max_length=20, null=False)

    #cEPS8MAX = models.CharField(max_length=10, null=False)
    
    
    cProf1 = models.CharField(max_length=20, null=False)  #以下為最近8季EPS
    cProf2 = models.CharField(max_length=20, null=False)
    cProf3 = models.CharField(max_length=20, null=False)
    cProf4 = models.CharField(max_length=20, null=False)
    cProf5 = models.CharField(max_length=20, null=False)
    cProf6 = models.CharField(max_length=20, null=False) 
    cProf7 = models.CharField(max_length=20, null=False)
    cProf8 = models.CharField(max_length=20, null=False)

    #cProf8MAX = models.CharField(max_length=10, null=False)
    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID

class EpsProfit2022Q1(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)

    cEPS1 = models.CharField(max_length=20, null=False)  #以下為最近8季EPS
    cEPS2 = models.CharField(max_length=20, null=False)
    cEPS3 = models.CharField(max_length=20, null=False)
    cEPS4 = models.CharField(max_length=20, null=False)
    cEPS5 = models.CharField(max_length=20, null=False)
    cEPS6 = models.CharField(max_length=20, null=False) 
    cEPS7 = models.CharField(max_length=20, null=False)
    cEPS8 = models.CharField(max_length=20, null=False)

    #cEPS8MAX = models.CharField(max_length=10, null=False)
    
    
    cProf1 = models.CharField(max_length=20, null=False)  #以下為最近8季EPS
    cProf2 = models.CharField(max_length=20, null=False)
    cProf3 = models.CharField(max_length=20, null=False)
    cProf4 = models.CharField(max_length=20, null=False)
    cProf5 = models.CharField(max_length=20, null=False)
    cProf6 = models.CharField(max_length=20, null=False) 
    cProf7 = models.CharField(max_length=20, null=False)
    cProf8 = models.CharField(max_length=20, null=False)

    #cProf8MAX = models.CharField(max_length=10, null=False)
    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
class EpsProfit2022Q2(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)

    cEPS1 = models.CharField(max_length=20, null=False)  #以下為最近8季EPS
    cEPS2 = models.CharField(max_length=20, null=False)
    cEPS3 = models.CharField(max_length=20, null=False)
    cEPS4 = models.CharField(max_length=20, null=False)
    cEPS5 = models.CharField(max_length=20, null=False)
    cEPS6 = models.CharField(max_length=20, null=False) 
    cEPS7 = models.CharField(max_length=20, null=False)
    cEPS8 = models.CharField(max_length=20, null=False)

    #cEPS8MAX = models.CharField(max_length=10, null=False)
    
    
    cProf1 = models.CharField(max_length=20, null=False)  #以下為最近8季EPS
    cProf2 = models.CharField(max_length=20, null=False)
    cProf3 = models.CharField(max_length=20, null=False)
    cProf4 = models.CharField(max_length=20, null=False)
    cProf5 = models.CharField(max_length=20, null=False)
    cProf6 = models.CharField(max_length=20, null=False) 
    cProf7 = models.CharField(max_length=20, null=False)
    cProf8 = models.CharField(max_length=20, null=False)

    #cProf8MAX = models.CharField(max_length=10, null=False)
    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
    
class EpsProfit2022Q3(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)

    cEPS1 = models.CharField(max_length=20, null=False)  #以下為最近8季EPS
    cEPS2 = models.CharField(max_length=20, null=False)
    cEPS3 = models.CharField(max_length=20, null=False)
    cEPS4 = models.CharField(max_length=20, null=False)
    cEPS5 = models.CharField(max_length=20, null=False)
    cEPS6 = models.CharField(max_length=20, null=False) 
    cEPS7 = models.CharField(max_length=20, null=False)
    cEPS8 = models.CharField(max_length=20, null=False)

    #cEPS8MAX = models.CharField(max_length=10, null=False)
    
    
    cProf1 = models.CharField(max_length=20, null=False)  #以下為最近8季EPS
    cProf2 = models.CharField(max_length=20, null=False)
    cProf3 = models.CharField(max_length=20, null=False)
    cProf4 = models.CharField(max_length=20, null=False)
    cProf5 = models.CharField(max_length=20, null=False)
    cProf6 = models.CharField(max_length=20, null=False) 
    cProf7 = models.CharField(max_length=20, null=False)
    cProf8 = models.CharField(max_length=20, null=False)

    #cProf8MAX = models.CharField(max_length=10, null=False)
    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
class EpsProfit2022Q4(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)

    cEPS1 = models.CharField(max_length=20, null=False)  #以下為最近8季EPS
    cEPS2 = models.CharField(max_length=20, null=False)
    cEPS3 = models.CharField(max_length=20, null=False)
    cEPS4 = models.CharField(max_length=20, null=False)
    cEPS5 = models.CharField(max_length=20, null=False)
    cEPS6 = models.CharField(max_length=20, null=False) 
    cEPS7 = models.CharField(max_length=20, null=False)
    cEPS8 = models.CharField(max_length=20, null=False)

    #cEPS8MAX = models.CharField(max_length=10, null=False)
    
    
    cProf1 = models.CharField(max_length=20, null=False)  #以下為最近8季EPS
    cProf2 = models.CharField(max_length=20, null=False)
    cProf3 = models.CharField(max_length=20, null=False)
    cProf4 = models.CharField(max_length=20, null=False)
    cProf5 = models.CharField(max_length=20, null=False)
    cProf6 = models.CharField(max_length=20, null=False) 
    cProf7 = models.CharField(max_length=20, null=False)
    cProf8 = models.CharField(max_length=20, null=False)

    #cProf8MAX = models.CharField(max_length=10, null=False)
    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
class EpsProfit2023Q1(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)

    cEPS1 = models.CharField(max_length=20, null=False)  #以下為最近8季EPS
    cEPS2 = models.CharField(max_length=20, null=False)
    cEPS3 = models.CharField(max_length=20, null=False)
    cEPS4 = models.CharField(max_length=20, null=False)
    cEPS5 = models.CharField(max_length=20, null=False)
    cEPS6 = models.CharField(max_length=20, null=False) 
    cEPS7 = models.CharField(max_length=20, null=False)
    cEPS8 = models.CharField(max_length=20, null=False)

    #cEPS8MAX = models.CharField(max_length=10, null=False)
    
    
    cProf1 = models.CharField(max_length=20, null=False)  #以下為最近8季EPS
    cProf2 = models.CharField(max_length=20, null=False)
    cProf3 = models.CharField(max_length=20, null=False)
    cProf4 = models.CharField(max_length=20, null=False)
    cProf5 = models.CharField(max_length=20, null=False)
    cProf6 = models.CharField(max_length=20, null=False) 
    cProf7 = models.CharField(max_length=20, null=False)
    cProf8 = models.CharField(max_length=20, null=False)

    #cProf8MAX = models.CharField(max_length=10, null=False)
    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
#########################################################################

class StockPERsegStable2020(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)
    
    cPER_H1 = models.CharField(max_length=15, null=False)   #以下為最近五年最高和最低本益比區間
    cPER_L1 = models.CharField(max_length=15, null=False)
    cPER_H2 = models.CharField(max_length=15, null=False)
    cPER_L2 = models.CharField(max_length=15, null=False)
    cPER_H3 = models.CharField(max_length=15, null=False)
    cPER_L3 = models.CharField(max_length=15, null=False)
    cPER_H4 = models.CharField(max_length=15, null=False)
    cPER_L4 = models.CharField(max_length=15, null=False)
    cPER_H5 = models.CharField(max_length=15, null=False)
    cPER_L5 = models.CharField(max_length=15, null=False)
    
    cPER_H_average = models.CharField(max_length=15, null=False)  #最近五年平均
    cPER_L_average = models.CharField(max_length=15, null=False)
    
    cP_Hw1 = models.CharField(max_length=15, null=False) 
    cP_Hw2 = models.CharField(max_length=15, null=False) 
    cP_Hw3 = models.CharField(max_length=15, null=False) 
    cP_Hw4 = models.CharField(max_length=15, null=False) 
    cP_Hw5 = models.CharField(max_length=15, null=False)
    
    cP_Lw1 = models.CharField(max_length=15, null=False) 
    cP_Lw2 = models.CharField(max_length=15, null=False) 
    cP_Lw3 = models.CharField(max_length=15, null=False) 
    cP_Lw4 = models.CharField(max_length=15, null=False) 
    cP_Lw5 = models.CharField(max_length=15, null=False)    
   
    

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
class StockPERsegStable2020Q2(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)
    
    cPER_H1 = models.CharField(max_length=15, null=False)   #以下為最近五年最高和最低本益比區間
    cPER_L1 = models.CharField(max_length=15, null=False)
    cPER_H2 = models.CharField(max_length=15, null=False)
    cPER_L2 = models.CharField(max_length=15, null=False)
    cPER_H3 = models.CharField(max_length=15, null=False)
    cPER_L3 = models.CharField(max_length=15, null=False)
    cPER_H4 = models.CharField(max_length=15, null=False)
    cPER_L4 = models.CharField(max_length=15, null=False)
    cPER_H5 = models.CharField(max_length=15, null=False)
    cPER_L5 = models.CharField(max_length=15, null=False)
    
    cPER_H_average = models.CharField(max_length=15, null=False)  #最近五年平均
    cPER_L_average = models.CharField(max_length=15, null=False)
    
    cP_Hw1 = models.CharField(max_length=15, null=False) 
    cP_Hw2 = models.CharField(max_length=15, null=False) 
    cP_Hw3 = models.CharField(max_length=15, null=False) 
    cP_Hw4 = models.CharField(max_length=15, null=False) 
    cP_Hw5 = models.CharField(max_length=15, null=False)
    
    cP_Lw1 = models.CharField(max_length=15, null=False) 
    cP_Lw2 = models.CharField(max_length=15, null=False) 
    cP_Lw3 = models.CharField(max_length=15, null=False) 
    cP_Lw4 = models.CharField(max_length=15, null=False) 
    cP_Lw5 = models.CharField(max_length=15, null=False)    
   
    

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID


class StockPERsegStable2020Q3(models.Model):
    cStockID = models.CharField(max_length=5, null=False)
    cStockName = models.CharField(max_length=5, null=False)
    
    cPER_H1 = models.CharField(max_length=20)   #以下為最近五年最高和最低本益比區間
    cPER_L1 = models.CharField(max_length=20)
    cPER_H2 = models.CharField(max_length=20)
    cPER_L2 = models.CharField(max_length=20)
    cPER_H3 = models.CharField(max_length=20)
    cPER_L3 = models.CharField(max_length=20)
    cPER_H4 = models.CharField(max_length=20)
    cPER_L4 = models.CharField(max_length=20)
    cPER_H5 = models.CharField(max_length=20)
    cPER_L5 = models.CharField(max_length=20)
    
    cPER_H_average = models.CharField(max_length=20)  #最近五年平均
    cPER_L_average = models.CharField(max_length=20)
    
    cP_Hw1 = models.CharField(max_length=20) 
    cP_Hw2 = models.CharField(max_length=20) 
    cP_Hw3 = models.CharField(max_length=20) 
    cP_Hw4 = models.CharField(max_length=20) 
    cP_Hw5 = models.CharField(max_length=20)
    
    cP_Lw1 = models.CharField(max_length=20) 
    cP_Lw2 = models.CharField(max_length=20) 
    cP_Lw3 = models.CharField(max_length=20) 
    cP_Lw4 = models.CharField(max_length=20) 
    cP_Lw5 = models.CharField(max_length=20)    
   
    

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
class StockPERsegStable2020Q3x(models.Model):
    cStockID = models.CharField(max_length=10, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    
    cPER_H1 = models.CharField(max_length=20)   #以下為最近五年最高和最低本益比區間
    cPER_L1 = models.CharField(max_length=20)
    cPER_H2 = models.CharField(max_length=20)
    cPER_L2 = models.CharField(max_length=20)
    cPER_H3 = models.CharField(max_length=20)
    cPER_L3 = models.CharField(max_length=20)
    cPER_H4 = models.CharField(max_length=20)
    cPER_L4 = models.CharField(max_length=20)
    cPER_H5 = models.CharField(max_length=20)
    cPER_L5 = models.CharField(max_length=20)
    
    cPER_H_average = models.CharField(max_length=20)  #最近五年平均
    cPER_L_average = models.CharField(max_length=20)
    

    

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID


class StockPERsegStable2020Q4(models.Model):
    cStockID = models.CharField(max_length=10, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    
    cPER_H1 = models.CharField(max_length=20)   #以下為最近五年最高和最低本益比區間
    cPER_L1 = models.CharField(max_length=20)
    cPER_H2 = models.CharField(max_length=20)
    cPER_L2 = models.CharField(max_length=20)
    cPER_H3 = models.CharField(max_length=20)
    cPER_L3 = models.CharField(max_length=20)
    cPER_H4 = models.CharField(max_length=20)
    cPER_L4 = models.CharField(max_length=20)
    cPER_H5 = models.CharField(max_length=20)
    cPER_L5 = models.CharField(max_length=20)
    
    cPER_H_average = models.CharField(max_length=20)  #最近五年平均
    cPER_L_average = models.CharField(max_length=20)
    

    

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID

class StockPERsegStable2021Q1(models.Model):
    cStockID = models.CharField(max_length=10, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    
    cPER_H1 = models.CharField(max_length=20)   #以下為最近五年最高和最低本益比區間
    cPER_L1 = models.CharField(max_length=20)
    cPER_H2 = models.CharField(max_length=20)
    cPER_L2 = models.CharField(max_length=20)
    cPER_H3 = models.CharField(max_length=20)
    cPER_L3 = models.CharField(max_length=20)
    cPER_H4 = models.CharField(max_length=20)
    cPER_L4 = models.CharField(max_length=20)
    cPER_H5 = models.CharField(max_length=20)
    cPER_L5 = models.CharField(max_length=20)
    
    cPER_H_average = models.CharField(max_length=20)  #最近五年平均
    cPER_L_average = models.CharField(max_length=20)
    

    

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
class StockPERsegStable2021Q2(models.Model):
    cStockID = models.CharField(max_length=10, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    
    cPER_H1 = models.CharField(max_length=20)   #以下為最近五年最高和最低本益比區間
    cPER_L1 = models.CharField(max_length=20)
    cPER_H2 = models.CharField(max_length=20)
    cPER_L2 = models.CharField(max_length=20)
    cPER_H3 = models.CharField(max_length=20)
    cPER_L3 = models.CharField(max_length=20)
    cPER_H4 = models.CharField(max_length=20)
    cPER_L4 = models.CharField(max_length=20)
    cPER_H5 = models.CharField(max_length=20)
    cPER_L5 = models.CharField(max_length=20)
    
    cPER_H_average = models.CharField(max_length=20)  #最近五年平均
    cPER_L_average = models.CharField(max_length=20)
    

    

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
class StockPERsegStable2021Q3(models.Model):
    cStockID = models.CharField(max_length=10, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    
    cPER_H1 = models.CharField(max_length=20)   #以下為最近五年最高和最低本益比區間
    cPER_L1 = models.CharField(max_length=20)
    cPER_H2 = models.CharField(max_length=20)
    cPER_L2 = models.CharField(max_length=20)
    cPER_H3 = models.CharField(max_length=20)
    cPER_L3 = models.CharField(max_length=20)
    cPER_H4 = models.CharField(max_length=20)
    cPER_L4 = models.CharField(max_length=20)
    cPER_H5 = models.CharField(max_length=20)
    cPER_L5 = models.CharField(max_length=20)
    
    cPER_H_average = models.CharField(max_length=20)  #最近五年平均
    cPER_L_average = models.CharField(max_length=20)
    

    

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID

class StockPERsegStable2021Q4(models.Model):
    cStockID = models.CharField(max_length=10, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    
    cPER_H1 = models.CharField(max_length=20)   #以下為最近五年最高和最低本益比區間
    cPER_L1 = models.CharField(max_length=20)
    cPER_H2 = models.CharField(max_length=20)
    cPER_L2 = models.CharField(max_length=20)
    cPER_H3 = models.CharField(max_length=20)
    cPER_L3 = models.CharField(max_length=20)
    cPER_H4 = models.CharField(max_length=20)
    cPER_L4 = models.CharField(max_length=20)
    cPER_H5 = models.CharField(max_length=20)
    cPER_L5 = models.CharField(max_length=20)
    
    cPER_H_average = models.CharField(max_length=20)  #最近五年平均
    cPER_L_average = models.CharField(max_length=20)
    

    

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
    
class StockPERsegStable2022Q1(models.Model):
    cStockID = models.CharField(max_length=10, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    
    cPER_H1 = models.CharField(max_length=20)   #以下為最近五年最高和最低本益比區間
    cPER_L1 = models.CharField(max_length=20)
    cPER_H2 = models.CharField(max_length=20)
    cPER_L2 = models.CharField(max_length=20)
    cPER_H3 = models.CharField(max_length=20)
    cPER_L3 = models.CharField(max_length=20)
    cPER_H4 = models.CharField(max_length=20)
    cPER_L4 = models.CharField(max_length=20)
    cPER_H5 = models.CharField(max_length=20)
    cPER_L5 = models.CharField(max_length=20)
    
    cPER_H_average = models.CharField(max_length=20)  #最近五年平均
    cPER_L_average = models.CharField(max_length=20)
    

    

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
class StockPERsegStable2022Q2(models.Model):
    cStockID = models.CharField(max_length=10, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    
    cPER_H1 = models.CharField(max_length=20)   #以下為最近五年最高和最低本益比區間
    cPER_L1 = models.CharField(max_length=20)
    cPER_H2 = models.CharField(max_length=20)
    cPER_L2 = models.CharField(max_length=20)
    cPER_H3 = models.CharField(max_length=20)
    cPER_L3 = models.CharField(max_length=20)
    cPER_H4 = models.CharField(max_length=20)
    cPER_L4 = models.CharField(max_length=20)
    cPER_H5 = models.CharField(max_length=20)
    cPER_L5 = models.CharField(max_length=20)
    
    cPER_H_average = models.CharField(max_length=20)  #最近五年平均
    cPER_L_average = models.CharField(max_length=20)
    

    

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
class StockPERsegStable2022Q3(models.Model):
    cStockID = models.CharField(max_length=10, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    
    cPER_H1 = models.CharField(max_length=20)   #以下為最近五年最高和最低本益比區間
    cPER_L1 = models.CharField(max_length=20)
    cPER_H2 = models.CharField(max_length=20)
    cPER_L2 = models.CharField(max_length=20)
    cPER_H3 = models.CharField(max_length=20)
    cPER_L3 = models.CharField(max_length=20)
    cPER_H4 = models.CharField(max_length=20)
    cPER_L4 = models.CharField(max_length=20)
    cPER_H5 = models.CharField(max_length=20)
    cPER_L5 = models.CharField(max_length=20)
    
    cPER_H_average = models.CharField(max_length=20)  #最近五年平均
    cPER_L_average = models.CharField(max_length=20)
    

    

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID

class StockPERsegStable2022Q4(models.Model):
    cStockID = models.CharField(max_length=10, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    
    cPER_H1 = models.CharField(max_length=20)   #以下為最近五年最高和最低本益比區間
    cPER_L1 = models.CharField(max_length=20)
    cPER_H2 = models.CharField(max_length=20)
    cPER_L2 = models.CharField(max_length=20)
    cPER_H3 = models.CharField(max_length=20)
    cPER_L3 = models.CharField(max_length=20)
    cPER_H4 = models.CharField(max_length=20)
    cPER_L4 = models.CharField(max_length=20)
    cPER_H5 = models.CharField(max_length=20)
    cPER_L5 = models.CharField(max_length=20)
    
    cPER_H_average = models.CharField(max_length=20)  #最近五年平均
    cPER_L_average = models.CharField(max_length=20)
    

    

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
    
class StockPERsegStable2023Q1(models.Model):
    cStockID = models.CharField(max_length=10, null=False)
    cStockName = models.CharField(max_length=10, null=False)
    
    cPER_H1 = models.CharField(max_length=20)   #以下為最近五年最高和最低本益比區間
    cPER_L1 = models.CharField(max_length=20)
    cPER_H2 = models.CharField(max_length=20)
    cPER_L2 = models.CharField(max_length=20)
    cPER_H3 = models.CharField(max_length=20)
    cPER_L3 = models.CharField(max_length=20)
    cPER_H4 = models.CharField(max_length=20)
    cPER_L4 = models.CharField(max_length=20)
    cPER_H5 = models.CharField(max_length=20)
    cPER_L5 = models.CharField(max_length=20)
    
    cPER_H_average = models.CharField(max_length=20)  #最近五年平均
    cPER_L_average = models.CharField(max_length=20)
    

    

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
#####################    
class SubCats202011(models.Model):
    #cStockID = models.CharField(max_length=8, null=False)
    cSubCatName = models.CharField(max_length=15, null=False)
    cScore2011 = models.FloatField(max_length=15)  
    cScore20Q3 = models.FloatField(max_length=15)  
    cScore2009 = models.FloatField(max_length=15)
    cScore2008 = models.FloatField(max_length=15)
    cScore20Q2 = models.FloatField(max_length=15)
    cScore2006 = models.FloatField(max_length=15) 

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cSubCatName  
    
class SubCats202102(models.Model):
    #cStockID = models.CharField(max_length=8, null=False)
    cSubCatName = models.CharField(max_length=15, null=False)
    cScore2102 = models.FloatField(max_length=15) 
    cScore2101 = models.FloatField(max_length=15) 
    cScore2012 = models.FloatField(max_length=15) 
    cScore2011 = models.FloatField(max_length=15)  
    cScore20Q3 = models.FloatField(max_length=15)  
    cScore2009 = models.FloatField(max_length=15)
    cScore2008 = models.FloatField(max_length=15)
    cScore20Q2 = models.FloatField(max_length=15)
    cScore2006 = models.FloatField(max_length=15) 

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cSubCatName  
    
class SubCats202103(models.Model):
    #cStockID = models.CharField(max_length=8, null=False)
    cSubCatName = models.CharField(max_length=15, null=False)
    cScore2103 = models.FloatField(max_length=15) 
    cScore2102 = models.FloatField(max_length=15) 
    cScore2101 = models.FloatField(max_length=15) 
    cScore2012 = models.FloatField(max_length=15) 
    cScore2011 = models.FloatField(max_length=15)  
    cScore20Q3 = models.FloatField(max_length=15)  
    cScore2009 = models.FloatField(max_length=15)
    cScore2008 = models.FloatField(max_length=15)
    cScore20Q2 = models.FloatField(max_length=15)
    cScore2006 = models.FloatField(max_length=15) 

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cSubCatName


class SubCats202104(models.Model):
    #cStockID = models.CharField(max_length=8, null=False)
    cSubCatName = models.CharField(max_length=15, null=False)
    cScore2104 = models.FloatField(max_length=15) 
    cScore2103 = models.FloatField(max_length=15) 
    cScore2102 = models.FloatField(max_length=15) 
    cScore2101 = models.FloatField(max_length=15) 
    cScore2012 = models.FloatField(max_length=15) 
    cScore2011 = models.FloatField(max_length=15)  
    cScore20Q3 = models.FloatField(max_length=15)  
    cScore2009 = models.FloatField(max_length=15)
    cScore2008 = models.FloatField(max_length=15)
    cScore20Q2 = models.FloatField(max_length=15)
    cScore2006 = models.FloatField(max_length=15) 

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cSubCatName
    
class SubCats202105(models.Model):  
    #cStockID = models.CharField(max_length=8, null=False)
    cSubCatName = models.CharField(max_length=15, null=False)
    #cScore2105 = models.FloatField(max_length=15) 
    cScore2104 = models.FloatField(max_length=15, blank=True, null=True)  #一定要設blank=True, null=True
    cScore2103 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2102 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2101 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2012 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2011 = models.FloatField(max_length=15, blank=True, null=True)  
    cScore20Q3 = models.FloatField(max_length=15, blank=True, null=True)  
    cScore2009 = models.FloatField(max_length=15, blank=True, null=True)
    cScore2008 = models.FloatField(max_length=15, blank=True, null=True)
    cScore20Q2 = models.FloatField(max_length=15, blank=True, null=True)
    cScore2006 = models.FloatField(max_length=15, blank=True, null=True) 

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cSubCatName

class SubCats202106(models.Model):
    #cStockID = models.CharField(max_length=8, null=False)
    cSubCatName = models.CharField(max_length=15, null=False)
    cScore2106 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2105 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2104 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2103 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2102 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2101 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2012 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2011 = models.FloatField(max_length=15, blank=True, null=True)  
    cScore20Q3 = models.FloatField(max_length=15, blank=True, null=True)  
    cScore2009 = models.FloatField(max_length=15, blank=True, null=True)
    cScore2008 = models.FloatField(max_length=15, blank=True, null=True)
    cScore20Q2 = models.FloatField(max_length=15, blank=True, null=True)
    cScore2006 = models.FloatField(max_length=15, blank=True, null=True) 

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cSubCatName
    
    
class SubCats202107(models.Model):
    #cStockID = models.CharField(max_length=8, null=False)
    cSubCatName = models.CharField(max_length=15, null=False)
    cScore2107 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2106 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2105 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2104 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2103 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2102 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2101 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2012 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2011 = models.FloatField(max_length=15, blank=True, null=True)  
    cScore20Q3 = models.FloatField(max_length=15, blank=True, null=True)  
    cScore2009 = models.FloatField(max_length=15, blank=True, null=True)
    cScore2008 = models.FloatField(max_length=15, blank=True, null=True)
    cScore20Q2 = models.FloatField(max_length=15, blank=True, null=True)
    cScore2006 = models.FloatField(max_length=15, blank=True, null=True) 

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cSubCatName
    
    
class SubCats202108(models.Model):
    #cStockID = models.CharField(max_length=8, null=False)
    cSubCatName = models.CharField(max_length=15, null=False)

    cScore2108 = models.FloatField(max_length=15, blank=True, null=True)     
    cScore2107 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2106 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2105 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2104 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2103 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2102 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2101 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2012 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2011 = models.FloatField(max_length=15, blank=True, null=True)  
    cScore20Q3 = models.FloatField(max_length=15, blank=True, null=True)  
    cScore2009 = models.FloatField(max_length=15, blank=True, null=True)
    cScore2008 = models.FloatField(max_length=15, blank=True, null=True)
    cScore20Q2 = models.FloatField(max_length=15, blank=True, null=True)
    cScore2006 = models.FloatField(max_length=15, blank=True, null=True) 

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cSubCatName
    
class SubCats202109(models.Model):
    #cStockID = models.CharField(max_length=8, null=False)
    cSubCatName = models.CharField(max_length=15, null=False)
    
    cScore2109 = models.FloatField(max_length=15, blank=True, null=True)
    cScore2108 = models.FloatField(max_length=15, blank=True, null=True)     
    cScore2107 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2106 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2105 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2104 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2103 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2102 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2101 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2012 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2011 = models.FloatField(max_length=15, blank=True, null=True)  
    cScore20Q3 = models.FloatField(max_length=15, blank=True, null=True)  
    cScore2009 = models.FloatField(max_length=15, blank=True, null=True)
    cScore2008 = models.FloatField(max_length=15, blank=True, null=True)
    cScore20Q2 = models.FloatField(max_length=15, blank=True, null=True)
    cScore2006 = models.FloatField(max_length=15, blank=True, null=True) 

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cSubCatName
    
class SubCats202110(models.Model):
    #cStockID = models.CharField(max_length=8, null=False)
    cSubCatName = models.CharField(max_length=15, null=False)
    
    cScore2110 = models.FloatField(max_length=15, blank=True, null=True)    
    cScore2109 = models.FloatField(max_length=15, blank=True, null=True)
    cScore2108 = models.FloatField(max_length=15, blank=True, null=True)     
    cScore2107 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2106 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2105 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2104 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2103 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2102 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2101 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2012 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2011 = models.FloatField(max_length=15, blank=True, null=True)  
    cScore20Q3 = models.FloatField(max_length=15, blank=True, null=True)  
    cScore2009 = models.FloatField(max_length=15, blank=True, null=True)
    cScore2008 = models.FloatField(max_length=15, blank=True, null=True)
    cScore20Q2 = models.FloatField(max_length=15, blank=True, null=True)
    cScore2006 = models.FloatField(max_length=15, blank=True, null=True) 

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cSubCatName
    
    
class SubCats202111(models.Model):
    #cStockID = models.CharField(max_length=8, null=False)
    cSubCatName = models.CharField(max_length=15, null=False)
    
    cScore2111 = models.FloatField(max_length=15, blank=True, null=True)     
    cScore2110 = models.FloatField(max_length=15, blank=True, null=True)    
    cScore2109 = models.FloatField(max_length=15, blank=True, null=True)
    cScore2108 = models.FloatField(max_length=15, blank=True, null=True)     
    cScore2107 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2106 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2105 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2104 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2103 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2102 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2101 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2012 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2011 = models.FloatField(max_length=15, blank=True, null=True)  
    cScore20Q3 = models.FloatField(max_length=15, blank=True, null=True)  
    cScore2009 = models.FloatField(max_length=15, blank=True, null=True)
    cScore2008 = models.FloatField(max_length=15, blank=True, null=True)
    cScore20Q2 = models.FloatField(max_length=15, blank=True, null=True)
    cScore2006 = models.FloatField(max_length=15, blank=True, null=True) 

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cSubCatName
    
    
class SubCats202112(models.Model):
    #cStockID = models.CharField(max_length=8, null=False)
    cSubCatName = models.CharField(max_length=15, null=False)

    cScore2112 = models.FloatField(max_length=15, blank=True, null=True)     
    cScore2111 = models.FloatField(max_length=15, blank=True, null=True)     
    cScore2110 = models.FloatField(max_length=15, blank=True, null=True)    
    cScore2109 = models.FloatField(max_length=15, blank=True, null=True)
    cScore2108 = models.FloatField(max_length=15, blank=True, null=True)     
    cScore2107 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2106 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2105 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2104 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2103 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2102 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2101 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2012 = models.FloatField(max_length=15, blank=True, null=True) 
    cScore2011 = models.FloatField(max_length=15, blank=True, null=True)  
    cScore20Q3 = models.FloatField(max_length=15, blank=True, null=True)  
    cScore2009 = models.FloatField(max_length=15, blank=True, null=True)
    cScore2008 = models.FloatField(max_length=15, blank=True, null=True)
    cScore20Q2 = models.FloatField(max_length=15, blank=True, null=True)
    cScore2006 = models.FloatField(max_length=15, blank=True, null=True) 

    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cSubCatName
#########################
'''
class Favorites_jonyi729(models.Model):  
    cStockID = models.CharField(max_length=5)
    cStockName = models.CharField(max_length=5)
        
    cNewestSeason = models.CharField(max_length=15, default='')
    cNewestRev = models.CharField(max_length=15, default='')
    

    sCoreThisM= models.CharField(max_length=10, null=True, blank=True)
    sCoreLastM= models.CharField(max_length=10, null=True, blank=True)
    sCoreLast2M= models.CharField(max_length=10, null=True, blank=True)
    sCoreLast3M= models.CharField(max_length=10, null=True, blank=True)
    sCoreLast4M= models.CharField(max_length=10, null=True, blank=True)
    sCoreLast5M= models.CharField(max_length=10, null=True, blank=True)
    sCoreLast6M= models.CharField(max_length=10, null=True, blank=True)
    
    pubtime = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.cStockID
        '''
        

    
class StockFavDB(models.Model):
    cStockID = models.CharField(max_length=5, null=True, blank=True)
    cStockName = models.CharField(max_length=5, null=True, blank=True)

    cYearDate = models.CharField(max_length=15, null=True, blank=True)

    cPredict_EPS = models.CharField(max_length=15, null=True, blank=True) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價  
    
    cNew_up_profit = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間    

    cTodayClose = models.FloatField(max_length=20, null=True, blank=True) #今日收盤價
    
    cRisk_reward = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float
    
    pubtime = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.cStockID
    
class StockFavs_test168(models.Model):
    cStockID = models.CharField(max_length=5, null=True, blank=True)
    cStockName = models.CharField(max_length=5, null=True, blank=True)

    cScore1st = models.CharField(max_length=5, null=True, blank=True) #最近一個月評分
    cScore2nd = models.CharField(max_length=5, null=True, blank=True) #
    cScore3rd = models.CharField(max_length=5, null=True, blank=True)

    cTodayClose = models.FloatField(max_length=20, null=True, blank=True) #今日收盤價
   

    cPredict_EPS = models.CharField(max_length=15, null=True, blank=True) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價  
    
    cNew_up_profit = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間    

    cPredict_high_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價  
    
    cNew_up_profit_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間


    cDBURL = models.CharField(max_length=40, null=True, blank=True) #  
    cRisk_reward = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float
    cRisk_reward_down30 = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float



    cEPSach = models.CharField(max_length=20, null=True, blank=True)
    cStCap = models.CharField(max_length=20, null=True, blank=True)
    cEPSnPrf = models.CharField(max_length=20, null=True, blank=True)
    cPERstab = models.CharField(max_length=20, null=True, blank=True)


    pubtime = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.cStockID
class StockFavs_bobmax(models.Model):
    cStockID = models.CharField(max_length=5, null=True, blank=True)
    cStockName = models.CharField(max_length=5, null=True, blank=True)

    cScore1st = models.CharField(max_length=5, null=True, blank=True) #最近一個月評分
    cScore2nd = models.CharField(max_length=5, null=True, blank=True) #
    cScore3rd = models.CharField(max_length=5, null=True, blank=True)

    cTodayClose = models.FloatField(max_length=20, null=True, blank=True) #今日收盤價
   

    cPredict_EPS = models.CharField(max_length=15, null=True, blank=True) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價  
    
    cNew_up_profit = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間    

    cDBURL = models.CharField(max_length=40, null=True, blank=True) #  
    cRisk_reward = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float

    cEPSach = models.CharField(max_length=20, null=True, blank=True)
    cStCap = models.CharField(max_length=20, null=True, blank=True)
    cEPSnPrf = models.CharField(max_length=20, null=True, blank=True)
    cPERstab = models.CharField(max_length=20, null=True, blank=True)

    pubtime = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.cStockID
    
class StockFavs_deno36(models.Model):
    cStockID = models.CharField(max_length=5, null=True, blank=True)
    cStockName = models.CharField(max_length=5, null=True, blank=True)

    cScore1st = models.CharField(max_length=5, null=True, blank=True) #最近一個月評分
    cScore2nd = models.CharField(max_length=5, null=True, blank=True) #
    cScore3rd = models.CharField(max_length=5, null=True, blank=True)

    cTodayClose = models.FloatField(max_length=20, null=True, blank=True) #今日收盤價
   

    cPredict_EPS = models.CharField(max_length=15, null=True, blank=True) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價  
    
    cNew_up_profit = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間    

    cDBURL = models.CharField(max_length=40, null=True, blank=True) #  
    cRisk_reward = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float

    cEPSach = models.CharField(max_length=20, null=True, blank=True)
    cStCap = models.CharField(max_length=20, null=True, blank=True)
    cEPSnPrf = models.CharField(max_length=20, null=True, blank=True)
    cPERstab = models.CharField(max_length=20, null=True, blank=True)

    pubtime = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.cStockID
    
class StockFavs_donhonlin(models.Model):
    cStockID = models.CharField(max_length=5, null=True, blank=True)
    cStockName = models.CharField(max_length=5, null=True, blank=True)

    cScore1st = models.CharField(max_length=5, null=True, blank=True) #最近一個月評分
    cScore2nd = models.CharField(max_length=5, null=True, blank=True) #
    cScore3rd = models.CharField(max_length=5, null=True, blank=True)

    cTodayClose = models.FloatField(max_length=20, null=True, blank=True) #今日收盤價
   

    cPredict_EPS = models.CharField(max_length=15, null=True, blank=True) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價  
    
    cNew_up_profit = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間    

    cDBURL = models.CharField(max_length=40, null=True, blank=True) #  
    cRisk_reward = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float

    cEPSach = models.CharField(max_length=20, null=True, blank=True)
    cStCap = models.CharField(max_length=20, null=True, blank=True)
    cEPSnPrf = models.CharField(max_length=20, null=True, blank=True)
    cPERstab = models.CharField(max_length=20, null=True, blank=True)

    pubtime = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.cStockID

class StockFavs_goldsilver(models.Model):
    cStockID = models.CharField(max_length=5, null=True, blank=True)
    cStockName = models.CharField(max_length=5, null=True, blank=True)

    cScore1st = models.CharField(max_length=5, null=True, blank=True) #最近一個月評分
    cScore2nd = models.CharField(max_length=5, null=True, blank=True) #
    cScore3rd = models.CharField(max_length=5, null=True, blank=True)

    cTodayClose = models.FloatField(max_length=20, null=True, blank=True) #今日收盤價
   

    cPredict_EPS = models.CharField(max_length=15, null=True, blank=True) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價  
    
    cNew_up_profit = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間    

    cDBURL = models.CharField(max_length=40, null=True, blank=True) #  
    cRisk_reward = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)

    cEPSach = models.CharField(max_length=20, null=True, blank=True)
    cStCap = models.CharField(max_length=20, null=True, blank=True)
    cEPSnPrf = models.CharField(max_length=20, null=True, blank=True)
    cPERstab = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.cStockID
    
class StockFavs_hyeth(models.Model):
    cStockID = models.CharField(max_length=5, null=True, blank=True)
    cStockName = models.CharField(max_length=5, null=True, blank=True)

    cScore1st = models.CharField(max_length=5, null=True, blank=True) #最近一個月評分
    cScore2nd = models.CharField(max_length=5, null=True, blank=True) #
    cScore3rd = models.CharField(max_length=5, null=True, blank=True)

    cTodayClose = models.FloatField(max_length=20, null=True, blank=True) #今日收盤價
   

    cPredict_EPS = models.CharField(max_length=15, null=True, blank=True) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價  
    
    cNew_up_profit = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間    

    cDBURL = models.CharField(max_length=40, null=True, blank=True) #  
    cRisk_reward = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float

    cEPSach = models.CharField(max_length=20, null=True, blank=True)
    cStCap = models.CharField(max_length=20, null=True, blank=True)
    cEPSnPrf = models.CharField(max_length=20, null=True, blank=True)
    cPERstab = models.CharField(max_length=20, null=True, blank=True)

    pubtime = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.cStockID
    
class StockFavs_magicjohn(models.Model):
    cStockID = models.CharField(max_length=5, null=True, blank=True)
    cStockName = models.CharField(max_length=5, null=True, blank=True)

    cScore1st = models.CharField(max_length=5, null=True, blank=True) #最近一個月評分
    cScore2nd = models.CharField(max_length=5, null=True, blank=True) #
    cScore3rd = models.CharField(max_length=5, null=True, blank=True)

    cTodayClose = models.FloatField(max_length=20, null=True, blank=True) #今日收盤價
   

    cPredict_EPS = models.CharField(max_length=15, null=True, blank=True) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價  
    
    cNew_up_profit = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間    

    cDBURL = models.CharField(max_length=40, null=True, blank=True) #  
    cRisk_reward = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float
    pubtime = models.DateTimeField(auto_now=True)

    cEPSach = models.CharField(max_length=20, null=True, blank=True)
    cStCap = models.CharField(max_length=20, null=True, blank=True)
    cEPSnPrf = models.CharField(max_length=20, null=True, blank=True)
    cPERstab = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.cStockID
    
class StockFavs_jonyi(models.Model):
    cStockID = models.CharField(max_length=5, null=True, blank=True)
    cStockName = models.CharField(max_length=5, null=True, blank=True)

    cScore1st = models.CharField(max_length=5, null=True, blank=True) #最近一個月評分
    cScore2nd = models.CharField(max_length=5, null=True, blank=True) #
    cScore3rd = models.CharField(max_length=5, null=True, blank=True)

    cTodayClose = models.FloatField(max_length=20, null=True, blank=True) #今日收盤價
   

    cPredict_EPS = models.CharField(max_length=15, null=True, blank=True) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價  
    
    cNew_up_profit = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間    

    cPredict_high_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價  
    
    cNew_up_profit_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間


    cDBURL = models.CharField(max_length=40, null=True, blank=True) #  
    cRisk_reward = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float
    cRisk_reward_down30 = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float

    pubtime = models.DateTimeField(auto_now=True)

    cEPSach = models.CharField(max_length=20, null=True, blank=True)
    cStCap = models.CharField(max_length=20, null=True, blank=True)
    cEPSnPrf = models.CharField(max_length=20, null=True, blank=True)
    cPERstab = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.cStockID
    
class StockFavs_hakkai(models.Model):
    cStockID = models.CharField(max_length=5, null=True, blank=True)
    cStockName = models.CharField(max_length=5, null=True, blank=True)

    cScore1st = models.CharField(max_length=5, null=True, blank=True) #最近一個月評分
    cScore2nd = models.CharField(max_length=5, null=True, blank=True) #
    cScore3rd = models.CharField(max_length=5, null=True, blank=True)

    cTodayClose = models.FloatField(max_length=20, null=True, blank=True) #今日收盤價
   

    cPredict_EPS = models.CharField(max_length=15, null=True, blank=True) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價  
    
    cNew_up_profit = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間    

    cDBURL = models.CharField(max_length=40, null=True, blank=True) #  
    cRisk_reward = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float

    cEPSach = models.CharField(max_length=20, null=True, blank=True)
    cStCap = models.CharField(max_length=20, null=True, blank=True)
    cEPSnPrf = models.CharField(max_length=20, null=True, blank=True)
    cPERstab = models.CharField(max_length=20, null=True, blank=True)

    pubtime = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.cStockID
    


class StockFavs_bakylews(models.Model):
    cStockID = models.CharField(max_length=5, null=True, blank=True)
    cStockName = models.CharField(max_length=5, null=True, blank=True)

    cScore1st = models.CharField(max_length=5, null=True, blank=True) #最近一個月評分
    cScore2nd = models.CharField(max_length=5, null=True, blank=True) #
    cScore3rd = models.CharField(max_length=5, null=True, blank=True)

    cTodayClose = models.FloatField(max_length=20, null=True, blank=True) #今日收盤價
   

    cPredict_EPS = models.CharField(max_length=15, null=True, blank=True) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價  
    
    cNew_up_profit = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間    

    cDBURL = models.CharField(max_length=40, null=True, blank=True) #  
    cRisk_reward = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float

    cEPSach = models.CharField(max_length=20, null=True, blank=True)
    cStCap = models.CharField(max_length=20, null=True, blank=True)
    cEPSnPrf = models.CharField(max_length=20, null=True, blank=True)
    cPERstab = models.CharField(max_length=20, null=True, blank=True)

    pubtime = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.cStockID
    

    


class StockFavs_chenchi(models.Model):
    cStockID = models.CharField(max_length=5, null=True, blank=True)
    cStockName = models.CharField(max_length=5, null=True, blank=True)

    cScore1st = models.CharField(max_length=5, null=True, blank=True) #最近一個月評分
    cScore2nd = models.CharField(max_length=5, null=True, blank=True) #
    cScore3rd = models.CharField(max_length=5, null=True, blank=True)

    cTodayClose = models.FloatField(max_length=20, null=True, blank=True) #今日收盤價
   

    cPredict_EPS = models.CharField(max_length=15, null=True, blank=True) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價  
    
    cNew_up_profit = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間    

    cPredict_high_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price_down30 = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價  
    
    cNew_up_profit_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss_down30 = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間


    cDBURL = models.CharField(max_length=40, null=True, blank=True) #  
    cRisk_reward = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float
    cRisk_reward_down30 = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float


    cEPSach = models.CharField(max_length=20, null=True, blank=True)
    cStCap = models.CharField(max_length=20, null=True, blank=True)
    cEPSnPrf = models.CharField(max_length=20, null=True, blank=True)
    cPERstab = models.CharField(max_length=20, null=True, blank=True)

    pubtime = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.cStockID
    
    


class StockFavs_yuhuahsiao(models.Model):
    cStockID = models.CharField(max_length=5, null=True, blank=True)
    cStockName = models.CharField(max_length=5, null=True, blank=True)

    cScore1st = models.CharField(max_length=5, null=True, blank=True) #最近一個月評分
    cScore2nd = models.CharField(max_length=5, null=True, blank=True) #
    cScore3rd = models.CharField(max_length=5, null=True, blank=True)

    cTodayClose = models.FloatField(max_length=20, null=True, blank=True) #今日收盤價
   

    cPredict_EPS = models.CharField(max_length=15, null=True, blank=True) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價  
    
    cNew_up_profit = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間    

    cDBURL = models.CharField(max_length=40, null=True, blank=True) #  
    cRisk_reward = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float

    cEPSach = models.CharField(max_length=20, null=True, blank=True)
    cStCap = models.CharField(max_length=20, null=True, blank=True)
    cEPSnPrf = models.CharField(max_length=20, null=True, blank=True)
    cPERstab = models.CharField(max_length=20, null=True, blank=True)    

    pubtime = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.cStockID
    
class StockFavs_liusnow(models.Model):
    cStockID = models.CharField(max_length=5, null=True, blank=True)
    cStockName = models.CharField(max_length=5, null=True, blank=True)

    cScore1st = models.CharField(max_length=5, null=True, blank=True) #最近一個月評分
    cScore2nd = models.CharField(max_length=5, null=True, blank=True) #
    cScore3rd = models.CharField(max_length=5, null=True, blank=True)

    cTodayClose = models.FloatField(max_length=20, null=True, blank=True) #今日收盤價
   

    cPredict_EPS = models.CharField(max_length=15, null=True, blank=True) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價  
    
    cNew_up_profit = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間    

    cDBURL = models.CharField(max_length=40, null=True, blank=True) #  
    cRisk_reward = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float

    cEPSach = models.CharField(max_length=20, null=True, blank=True)
    cStCap = models.CharField(max_length=20, null=True, blank=True)
    cEPSnPrf = models.CharField(max_length=20, null=True, blank=True)
    cPERstab = models.CharField(max_length=20, null=True, blank=True)

    pubtime = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.cStockID
    

class StockFavs_kevinlee(models.Model):
    cStockID = models.CharField(max_length=5, null=True, blank=True)
    cStockName = models.CharField(max_length=5, null=True, blank=True)

    cScore1st = models.CharField(max_length=5, null=True, blank=True) #最近一個月評分
    cScore2nd = models.CharField(max_length=5, null=True, blank=True) #
    cScore3rd = models.CharField(max_length=5, null=True, blank=True)

    cTodayClose = models.FloatField(max_length=20, null=True, blank=True) #今日收盤價
   

    cPredict_EPS = models.CharField(max_length=15, null=True, blank=True) #預估未來EPS
    cPredict_high_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最高價
    cPredict_low_price = models.CharField(max_length=15, null=True, blank=True) #預估未來最低價  
    
    cNew_up_profit = models.CharField(max_length=25, null=True, blank=True) #預估未來往上空間
    cNew_down_loss = models.CharField(max_length=25, null=True, blank=True) #預估未來往下空間    

    cDBURL = models.CharField(max_length=40, null=True, blank=True) #  
    cRisk_reward = models.FloatField(max_length=20, null=True, blank=True) #預估風險報酬比率  #20201202 可以使用Float

    cEPSach = models.CharField(max_length=20, null=True, blank=True)
    cStCap = models.CharField(max_length=20, null=True, blank=True)
    cEPSnPrf = models.CharField(max_length=20, null=True, blank=True)
    cPERstab = models.CharField(max_length=20, null=True, blank=True)

    pubtime = models.DateTimeField(auto_now=True)




    def __str__(self):
        return self.cStockID
#####################################################################################    
class PriEPSPER_DB(models.Model):
    cStockID = models.CharField(max_length=8, null=False)
    cStockName = models.CharField(max_length=8, null=False)

    cH2025 = models.FloatField(max_length=20, null=True, blank=True)
    cL2025 = models.FloatField(max_length=20, null=True, blank=True)

    cH2024 = models.FloatField(max_length=20, null=True, blank=True)
    cL2024 = models.FloatField(max_length=20, null=True, blank=True)

    cH2023 = models.FloatField(max_length=20, null=True, blank=True)
    cL2023 = models.FloatField(max_length=20, null=True, blank=True)

    cH2022 = models.FloatField(max_length=20, null=True, blank=True)
    cL2022 = models.FloatField(max_length=20, null=True, blank=True)

    cH2021 = models.FloatField(max_length=20, null=True, blank=True)
    cL2021 = models.FloatField(max_length=20, null=True, blank=True)

    cH2020 = models.FloatField(max_length=20, null=True, blank=True)  #以下為最近五年最高價和最低價
    cL2020 = models.FloatField(max_length=20, null=True, blank=True)
    cH2019 = models.FloatField(max_length=20, null=True, blank=True)
    cL2019 = models.FloatField(max_length=20, null=True, blank=True)
    cH2018 = models.FloatField(max_length=20, null=True, blank=True)
    cL2018 = models.FloatField(max_length=20, null=True, blank=True)
    cH2017 = models.FloatField(max_length=20, null=True, blank=True)
    cL2017 = models.FloatField(max_length=20, null=True, blank=True)
    cH2016 = models.FloatField(max_length=20, null=True, blank=True)
    cL2016 = models.FloatField(max_length=20, null=True, blank=True)

    cEPS2025 = models.FloatField(max_length=20, null=True, blank=True) 
    cEPS2024 = models.FloatField(max_length=20, null=True, blank=True)
    cEPS2023 = models.FloatField(max_length=20, null=True, blank=True)
    cEPS2022 = models.FloatField(max_length=20, null=True, blank=True)
    cEPS2021 = models.FloatField(max_length=20, null=True, blank=True)


    cEPS2020 = models.FloatField(max_length=20, null=True, blank=True)  #以下為最近五年EPS
    cEPS2019 = models.FloatField(max_length=20, null=True, blank=True)
    cEPS2018 = models.FloatField(max_length=20, null=True, blank=True)
    cEPS2017 = models.FloatField(max_length=20, null=True, blank=True)
    cEPS2016 = models.FloatField(max_length=20, null=True, blank=True)

    cPER_H2025 = models.FloatField(max_length=20, null=True, blank=True)   
    cPER_L2025 = models.FloatField(max_length=20, null=True, blank=True)
    cPER_H2024 = models.FloatField(max_length=20, null=True, blank=True)
    cPER_L2024 = models.FloatField(max_length=20, null=True, blank=True)
    cPER_H2023 = models.FloatField(max_length=20, null=True, blank=True)
    cPER_L2023 = models.FloatField(max_length=20, null=True, blank=True)
    cPER_H2022 = models.FloatField(max_length=20, null=True, blank=True)
    cPER_L2022 = models.FloatField(max_length=20, null=True, blank=True)
    cPER_H2021 = models.FloatField(max_length=20, null=True, blank=True)
    cPER_L2021 = models.FloatField(max_length=20, null=True, blank=True)



    
    cPER_H2020 = models.FloatField(max_length=20, null=True, blank=True)   #以下為最近五年最高和最低本益比區間
    cPER_L2020 = models.FloatField(max_length=20, null=True, blank=True)
    cPER_H2019 = models.FloatField(max_length=20, null=True, blank=True)
    cPER_L2019 = models.FloatField(max_length=20, null=True, blank=True)
    cPER_H2018 = models.FloatField(max_length=20, null=True, blank=True)
    cPER_L2018 = models.FloatField(max_length=20, null=True, blank=True)
    cPER_H2017 = models.FloatField(max_length=20, null=True, blank=True)
    cPER_L2017 = models.FloatField(max_length=20, null=True, blank=True)
    cPER_H2016 = models.FloatField(max_length=20, null=True, blank=True)
    cPER_L2016 = models.FloatField(max_length=20, null=True, blank=True)


    pubtime = models.DateTimeField(auto_now=True)    
    def __str__(self):
        return self.cStockID

class NetCap_DB(models.Model):
    cStockID = models.CharField(max_length=8, null=False)
    cStockName = models.CharField(max_length=8, null=False)

    cNet22Q2 = models.FloatField(max_length=20, null=True, blank=True)
    cNet22Q1 = models.FloatField(max_length=20, null=True, blank=True)
    cNet21Q4 = models.FloatField(max_length=20, null=True, blank=True)
    cNet21Q3 = models.FloatField(max_length=20, null=True, blank=True)

    cNet21Q2 = models.FloatField(max_length=20, null=True, blank=True)
    cNet21Q1 = models.FloatField(max_length=20, null=True, blank=True)
    cNet20Q4 = models.FloatField(max_length=20, null=True, blank=True)
    cNet20Q3 = models.FloatField(max_length=20, null=True, blank=True)

    cCap22Q2 = models.FloatField(max_length=20, null=True, blank=True)     
    cCap22Q1 = models.FloatField(max_length=20, null=True, blank=True)     
    cCap21Q4 = models.FloatField(max_length=20, null=True, blank=True) 
    cCap21Q3 = models.FloatField(max_length=20, null=True, blank=True) 

    cCap21Q2 = models.FloatField(max_length=20, null=True, blank=True)     
    cCap21Q1 = models.FloatField(max_length=20, null=True, blank=True)     
    cCap20Q4 = models.FloatField(max_length=20, null=True, blank=True) 
    cCap20Q3 = models.FloatField(max_length=20, null=True, blank=True)

    pubtime = models.DateTimeField(auto_now=True)     
    def __str__(self):
        return self.cStockID     