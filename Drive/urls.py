from django.shortcuts import render
from django.urls import path, include
from Drive import views



urlpatterns = [
    path('', views.home_drive, name='home-drive'),
]
