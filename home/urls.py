from django.contrib import admin
from django.urls import path, include 
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('view_login', views.view_login, name='login'),
    path('work', views.work, name='work'),
    path('view_logout', views.view_logout, name='logout'),
    path('detailC/<new_slug>', views.detailC, name='detailC'),
    path('c_codes/<new_slug>', views.c_codes, name = 'Ccode')


]