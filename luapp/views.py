from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'luapp/home.html', context={'name':'LUIZA SOEIRO'})

def contato(request):
    return HttpResponse('CONTATO')

def sobre(request):
    return HttpResponse('SOBRE')