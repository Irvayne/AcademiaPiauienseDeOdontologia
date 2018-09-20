from django.contrib import admin
from front import views
from django.urls import path, include


urlpatterns = [
    path('/', views.index, name='index'),
    path('estatuto/', views.estatuto, name='front_estatuto'),
]