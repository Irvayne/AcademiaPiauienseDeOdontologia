from django.contrib import admin
from django.contrib import admin
from django.conf.urls import url
from front import views

urlpatterns = [
    url(r'^$', views.index),
]