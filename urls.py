from django.urls import path, include,re_path
from tradeapp import views

urlpatterns = [
    path('search/',views.search,name='search'),
    #path('',views.TradeList.as_view(),name='TradeList'),
    path('trade/',views.trade,name='trade'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('order/',views.order,name='order'),
    path('modal/',views.modal,name='modal'),
    path('position/',views.position,name='position'),
    path('funds/',views.funds,name='funds'),
    path('holding/',views.holding,name='holding') ,  
    path('delete/<int:id>', views.delete),  
    ]