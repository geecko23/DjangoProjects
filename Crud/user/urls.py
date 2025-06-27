from django.contrib import admin
from django.urls import path,include
from . import views
from django.shortcuts import redirect


def redirect_to_login(request):
    return redirect('login')

urlpatterns= [

    path('register/', views.register, name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout, name='logout'),

]