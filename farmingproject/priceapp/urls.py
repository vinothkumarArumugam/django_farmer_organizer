"""
URL configuration for farmingproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from priceapp.views.flower import FlowerView,flower_price_view
from priceapp.views.sugarcane import SugarcaneView,sugarcane_price_view
from priceapp.views.turmeric import TurmericView,turmeric_price_view
from priceapp.views.signup import signup
from priceapp.views.login import login_view,logout_view
from priceapp.views.formredirect import form_redirect_view



urlpatterns = [
    
    path('form/',form_redirect_view,name='form'),
    path('sugarcane/',SugarcaneView,name='sugarcane_form'),
    path('turmeric/',TurmericView,name='turmeric_form'),
    path('flower/',FlowerView,name='flower_form'),
    path('',signup,name='signup'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('sugarcaneprice/',sugarcane_price_view,name='sugarcaneprice'),
    path('turmericprice/',turmeric_price_view,name='turmericprice'),
    path('flowerprice/',flower_price_view,name='flowerprice'),

]
