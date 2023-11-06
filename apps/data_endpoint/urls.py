"""URL Configuration for data_endpoint app."""
from django.urls import path
from .views import refresh_data

urlpatterns = [
    path('api/refresh_data', refresh_data, name="load_data"),
]
