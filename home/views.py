
from django.shortcuts import render

from home.model import *

# Create your views here.

def home(request):
    return render(request,'home.html')

def result(request):
    searchQueury =request.GET['search']
    uri = graph(searchQueury)
    uri2 = graph2(searchQueury)
    dic ={'result':searchQueury ,'data':uri, 'data2':uri2}
    return render(request,'result.html',dic)