from django.urls import path

from . import views


urlpatterns=[
    path('', views.calc, name='home'),
    path('add', views.add, name='add')
]
