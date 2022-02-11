"""T3000 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
app_name = 'mtinwentura'
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.mtinw_sc, name='mtinw_sc'),
    url(r'^mtinw_pc/$', views.mtinw_pc, name='mtinw_pc'),
    url(r'^mtinw_pc2/$', views.mtinw_pc2, name='mtinw_pc2'),
    url(r'^export_xlsx/$', views.export_xlsx, name='export_xlsx'),
    url(r'^rap_xlsx/$', views.rap_xlsx, name='rap_xlsx'),
    url(r'^export_xlsx_bazowe/$', views.export_xlsx_bazowe, name='export_xlsx_bazowe'),
    url(r'^rap_xlsx_bazowe/$', views.rap_xlsx_bazowe, name='rap_xlsx_bazowe'),
    url(r'^przeslij_zlicz/$',views.przeslij_zlicz, name='przeslij_zlicz'),
    url(r'^przeslij_inw/$',views.przeslij_inw, name='przeslij_inw'),
    url(r'^kopiuj_bazowe/$', views.kopiuj_bazowe, name ='kopiuj_bazowe'),
    url(r'^zerowanie_indeks/$', views.zerowanie_indeks, name ='zerowanie_indeks'),
    url(r'^zerowanie_indeks_bazowy/$', views.zerowanie_indeks_bazowy, name ='zerowanie_indeks_bazowy'),
]
