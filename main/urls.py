from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('secondpage', secondpage, name='secondpage'),
    path('thirdpage', thirdpage, name='thirdpage'),
    path('forthpage', forthpage, name='forthpage'),
    path('lastpage', lastpage, name='lastpage'),
    path('last', last, name='last'),
]