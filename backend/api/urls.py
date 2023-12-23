# backend/api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('get', views.get_message, name='get_message'),
    path('post_time', views.post_time, name='post_time'),
    path('get_time', views.get_time, name='get_time'),
]
