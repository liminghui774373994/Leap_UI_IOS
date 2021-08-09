from django.conf.urls import re_path
from app import views




urlpatterns = [
    re_path(r'^index/', views.index),
    re_path(r'^checkfile/', views.checkfile,name = 'checkfile'),
]




