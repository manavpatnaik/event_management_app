from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.home, name='home'),
    path('users/', views.users, name='participants'),
    path('organisers/', views.organisers, name='organisers'),
    path('events/', views.events, name='events'),
    path('shippers/', views.shippers, name='shippers'),
    path('store/', views.store, name='store'),

    path('create_event/', views.createEvent, name='create_event'),
    path('add_item/', views.createItem, name='add_item'),
    path('add_organiser/', views.createOrganiser, name='add_organiser'),

    path('view_event/<str:pk>', views.view_event, name='view_event'),
]