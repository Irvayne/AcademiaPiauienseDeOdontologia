from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url('', include('front.urls')),
    url('', include('back.urls')),
]