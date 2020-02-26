from django.db import models
from account.forms import User
import time

class Trade(models.Model):
    name = models.CharField(max_length=30)
    current_price = models.FloatField()
    open_price = models.FloatField()
    previous_close = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()

    def __str__(self):
    	return self.name

class Tradder(models.Model): 
    name = models.CharField(max_length=90,)
    choice1 = models.CharField(max_length=90,default="")
    choice2 = models.CharField(max_length=90,default="")
    regular = models.CharField(max_length=90,default="")
    price = models.FloatField(default=True)
    trigger= models.FloatField(default=True)
    qty = models.IntegerField(default=True)
    disclose = models.FloatField(default=True)
    button = models.CharField(max_length=40)
    time = models.TimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name



  
