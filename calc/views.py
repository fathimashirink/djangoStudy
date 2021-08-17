from django.http.response import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def calc(request):
    return render(request,"Home.html",{'name':'shirin'})
def add(request):
    val1= request.GET['n1']
    val2= request.GET['n2']
    res= val1 + val2

    return render(request,"result.html",{'result':res})