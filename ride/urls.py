from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('serchride/', views.serchride, name='serchride'),
    path('creatride/', views.creatride, name ='creatride'),
    path('contactus/', views.contactus, name ='contactus'),
    path('aboutus/', views.aboutus, name ='aboutus'),
    path('profilepage/', views.profilepage, name='profilepage'),
    

]