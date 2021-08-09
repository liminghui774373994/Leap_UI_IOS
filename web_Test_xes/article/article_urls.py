from django.conf.urls import re_path
from article import views




urlpatterns = [
    re_path(r'^index/', views.index),
    re_path(r'^create_tag$', views.create_tag, name='create_tag'),
    re_path(r'^create_article$', views.create_article, name='create_article'),
    re_path(r'^create_article_action', views.create_article_action, name='create_article_action'),
    re_path(r'^tag$', views.tag, name='tag'),
    re_path(r'^general_column$', views.general_column, name='general_column'),
    re_path(r'^create_banner$', views.create_banner, name='create_banner'),
    re_path(r'^create_banner_action$', views.create_banner_action, name='create_banner_action'),
    re_path(r'^search_special_column$', views.search_special_column, name='search_special_column'),
    re_path(r'^add_special_column_activity$', views.add_special_column_activity, name='add_special_column_activity'),
    re_path(r'^create_special_column_activity$', views.create_special_column_activity, name='create_special_column_activity'),
    #re_path(r'^create_columnactivity$', views.create_columnactivity, name='create_columnactivity'),
    re_path(r'^lecture_column$', views.lecture_column, name='lecture_column'),
    re_path(r'^search_lecture_column$', views.search_lecture_column, name='search_lecture_column'),
    re_path(r'^add_lecture_column_activity$', views.add_lecture_column_activity, name='add_lecture_column_activity'),
]