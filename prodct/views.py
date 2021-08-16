from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def prodct(request):
    return HttpResponse("Product details")

# url nood fav enna view mao cheythu ini in=vade ath impliment cheyyanam ok?

def fav(request):
    return HttpResponse("my favourite product details  product details")
    # http respoinse single line ne pageleek render cheyyan ullathaan 

# ini oru oage poole okke akanamenkil
def mypage(request):
    return HttpResponse('<html><body><h1>Hi First Line</h1><br><h1>Second Line</h1></body></html>')

# okke vannu  ini entheelm change varuthumboo
#ivade ennitt ndh ms nik 