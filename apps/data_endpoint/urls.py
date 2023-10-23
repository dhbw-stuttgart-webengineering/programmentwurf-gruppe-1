from django.urls import path
from .views import load_data

urlpatterns = [
    path('background/load_data', load_data, name="load_data"),
]
