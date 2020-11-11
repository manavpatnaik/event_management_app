from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.users, name='participants'),
    path('organisers/', views.organisers, name='organisers'),
    path('shippers/', views.shippers, name='shippers'),
    path('store/', views.store, name='store'),
]