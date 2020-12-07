from django.urls import path, re_path
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView, name='login'),
    path('signup/', views.CustomSignUpView, name='signup'),
    path('logout/', views.signout, name='logout'),
]
