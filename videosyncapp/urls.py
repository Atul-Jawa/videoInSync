from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('creategrp/', views.creategrp, name='creategrp'),
    path('joingrp/', views.joingrp, name='joingrp'),
    re_path(r'watchtogether/(?P<pk>\d+)/$', views.watchtogether, name='watchtogether')
]