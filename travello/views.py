from django.shortcuts import render
from .models import Destination 
# Create your views here.

def index(request):
    dest1=Destination()
    dest1.name='Mumbai'
    dest1.desc='The City That never Sleep'
    dest1.price='800'

   
    dest2=Destination()
    dest2.name='Kerala'
    dest2.desc='The Gods own Country!'
    dest2.price='1000'
    return render(request,"index.html",{'dest1':dest1,'dest2':dest2})
