from django.conf.urls import re_path
from activity import views




urlpatterns = [
    re_path(r'^index/', views.index,name = 'index'),
    re_path(r'^returncoupon/', views.returncoupon,name = 'returncoupon'),
    #re_path(r'^returncoupon$', views.returncoupon, name = 'returncoupon'),
]




