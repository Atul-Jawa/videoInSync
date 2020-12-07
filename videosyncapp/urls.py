from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contactus/', views.contact, name='contactus'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('watchtogether/', views.watchtogether, name='watchtogether'),
]