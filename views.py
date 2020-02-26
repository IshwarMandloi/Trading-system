from django.shortcuts import render,HttpResponseRedirect
from .models import *
from django.http import *
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from tradeapp.models import Trade
from account.forms import User
from datetime import date
import pdb
import math 

def trade(request):
	if request.method=='POST':
		form = trade_form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(request,'/welcome/')
	else:
		form = trade_form()
		return render(request,'trade.html',{'form':form})


class TradeList(ListView):
        model=Trade
        success_url = reverse_lazy('TradeList')

    
def search(request):
    if request.method=='POST':
        srch = request.POST['search_text']
        if srch:
            match = Trade.objects.filter(name__icontains=srch)
            if match:
                #pdb.set_trace()
                return render(request,'tradeapp/ajax_search.html',{'sr':match})
        else:
            return redirect('/search/')
    return render(request,'tradeapp/ajax_search.html')
    
def dashboard(request):
    return render(request, 'tradeapp/dashboard.html')
    


def modal(request):
    if request.method=='POST':
        button = request.POST.get('button')
        name = request.POST.get('company')
        choice1 = request.POST.get('choice1')
        price = request.POST.get('price')
        tprice =request.POST.get('tprice')
        qty = request.POST.get('qty')
        user = User.objects.get(username = request.user)
        if button =='buy':    
            choice2 = request.POST.get('choice2')
            if 'market'==choice2:
                Tradder.objects.create(choice1=choice1,choice2 = choice2,price=price,name=name,button=button,qty=qty,user=user)
                return render(request, 'tradeapp/dashboard.html')
            if 'limit'==choice2:
                Tradder.objects.create(choice1=choice1,choice2 = choice2,price=price,name=name,button=button,qty=qty,user=user)
                return render(request, 'tradeapp/dashboard.html')
            if 'sl'==choice2:
                if tprice>=price:
                    Tradder.objects.create(choice1=choice1,choice2 = choice2,price=price,name=name,button=button,qty=qty,trigger= tprice,user=user)
                    return render(request, 'tradeapp/dashboard.html') 
                else:
                    messages.error(request,'Trigger price for stoploss buy orders should be higher than the last traded price  '+(price)+' . Try limit order to buy at a lower price.')
                    return render(request, 'tradeapp/dashboard.html')        
            if 'slm'==choice2:
                if tprice>=price:
                    Tradder.objects.create(choice1=choice1,choice2 = choice2,price=price,name=name,button=button,qty=qty,user=user)
                    return render(request, 'tradeapp/dashboard.html')
                else:
                    messages.error(request,'Trigger price for stoploss buy orders should be higher than the last traded price '+(price)+' . Try limit order to buy at a lower price.')
                    return render(request, 'tradeapp/dashboard.html')
    if button =='sell':    
            choice2 = request.POST.get('choice2')
            if 'market'==choice2:
                Tradder.objects.create(choice1=choice1,choice2 = choice2,price=price,name=name,button=button,qty=qty,user=user)
                return render(request, 'tradeapp/dashboard.html')
            elif 'limit'==choice2:
                Tradder.objects.create(choice1=choice1,choice2 = choice2,price=price,name=name,button=button,qty=qty,user=user)
                return render(request, 'tradeapp/dashboard.html')
            elif 'sl'==choice2:
                if tprice == price:
                    Tradder.objects.create(choice1=choice1,choice2 = choice2,price=price,name=name,button=button,qty=qty,trigger= tprice,user=user)
                    return render(request, 'tradeapp/dashboard.html') 
                else:
                    messages.error(request,'Trigger price for stoploss sell orders should be lower than the last traded price '+(price)+' . Try limit order to sell at a higher price.')
                    return render(request, 'tradeapp/dashboard.html')        
            elif 'slm'==choice2:
                if tprice<=price:
                    Tradder.objects.create(choice1=choice1,choice2 = choice2,price=price,name=name,button=button,qty=qty,user=user)
                    return render(request, 'tradeapp/dashboard.html')
                else:
                    messages.error(request,'Trigger price for stoploss sell orders should be lower than the last traded price '+(price)+' . Try limit order to sell at a higher price.')
                    return render(request, 'tradeapp/dashboard.html')
                                        
def order(request):
    user = User.objects.get(username = request.user)
    #pdb.set_trace()
    orders = Tradder.objects.filter(user__pk=user.id)
    return render(request,'tradeapp/order.html',{'orders':orders})

def position(request):
    return render(request,'tradeapp/position.html')

def funds(request):
    return render(request,'tradeapp/funds.html')

def holding(request):
    return render(request,'tradeapp/holding.html')

def delete(request, id):  
    order = Order.objects.get(id=id)  
    order.delete()  
    return redirect("/dashboard")  


       

