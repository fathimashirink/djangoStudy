from django.urls import path

from . import views


urlpatterns=[
    path('prod', views.prodct, name='prod'),
    path('favourite', views.fav, name='favourite'),
    path('htmlpagetest', views.mypage, name='mypage'),
    


]

# ivade oru url um athin oru view um undakka 
# athaan link ()url ok ?
