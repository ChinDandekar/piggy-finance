# backend/api/urls.py
from django.urls import path, include
from . import views

from . import auth

urlpatterns = [
    path('get', views.get_message, name='get_message'),
    path('post_time', views.post_time, name='post_time'),
    path('get_time', views.get_time, name='get_time'),
    path('google/login/', views.custom_google_login, name='custom_google_login'),
    path('google/login/callback/',views.custom_google_callback, name='custom_google_callback'),
    path("", include("allauth.urls")), #most important
]
