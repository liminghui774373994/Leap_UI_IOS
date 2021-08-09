from django.conf.urls import re_path
from autoTest import views




urlpatterns = [
    re_path(r'^index/', views.index,name = 'index'),
    re_path(r'^post_request/', views.post_request,name = 'post_request'),
    re_path(r'^get_request/', views.get_request,name = 'get_request'),

]




