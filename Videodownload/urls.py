from django.contrib import admin
from django.urls import path;
from . import views

urlpatterns = [ 
  path('',views.home, name='home'),
  path('contact/',views.contact,name='contact'),
  path('pinterestvideo/',views.pinterestlink,name='pinterestlink'),
  
  path('Instagram-download/',views.Instagram,name='Instagram'),
  path('videodisplay/',views.videodisplay,name='videodisplay'),
  path('Instagramplay/',views.Instagramplay,name='Instagramplay'),
  path('videodisplayPin/',views.videodisplayPin,name='videodisplayPin')
]   