
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.manage,name='home'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('add/',views.addstudent,name='add'),
    path('search/',views.searchstudent,name='search')
]

