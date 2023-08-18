from django.urls import path
from luapp.views import home, contato,sobre


urlpatterns = [
    path('',home),#HOME
    path('sobre/',sobre),#/sobre
    path('contato/',contato),#/contato
] 