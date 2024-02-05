# backend/api/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('get', views.is_auth, name='is_auth'),
    path('post_time', views.post_time, name='post_time'),
    path('get_time', views.get_time, name='get_time'),
    # path('google/login/', views.custom_google_login, name='custom-google-login'),
    path("", include("allauth.urls")),
    path('absolute_uri', views.get_absolute_uri, name='get_absolute_uri')
]
