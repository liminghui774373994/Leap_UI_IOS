from django.conf.urls import re_path
from monitor import views




urlpatterns = [
    re_path(r'^index/', views.index,name = 'index'),
    re_path(r'^content_center_monitor/', views.content_center_monitor,name = 'content_center_monitor'),
    re_path(r'^activity_monitor/', views.activity_monitor,name = 'activity_monitor'),
    re_path(r'^get_log_data/', views.get_log_data,name = 'get_log_data'),

]