from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):
    dest1=Destination()
    dest1.name='Mumbai'
    dest1.img='destination_1.jpg'
    dest1.desc='The City That never Sleep'
    dest1.price='800'
    dest1.offer=True

   
    dest2=Destination()
    dest2.name='Hyderabad'
    dest2.img='destination_2.jpg'
    dest2.desc='First Biriyany,Then Shervani'
    dest2.price='1000'
    dest2.offer=False

        
    dest3=Destination()
    dest3.name='Bangluru'
    dest3.img='destination_3.jpg'

    dest3.desc='The Beautiful City'
    dest3.price='750'
    dest3.offer=True
    dests=[dest1,dest2,dest3]

    return render(request,"index.html",{'dests':dests})
