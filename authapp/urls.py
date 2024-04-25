from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('authapp/signup/', views.signup, name='signup'), 
    path('authapp/login/', views.login_view, name='login'), 
    path('authapp/logout/',views.logout_view,name='logout')
]