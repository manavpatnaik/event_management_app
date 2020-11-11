from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.users, name='participants'),
    path('organisers/', views.organisers, name='organisers'),
    path('events/', views.events, name='events'),
    path('shippers/', views.shippers, name='shippers'),
    path('store/', views.store, name='store'),

    path('create_event/', views.createEvent, name='create_event')
]