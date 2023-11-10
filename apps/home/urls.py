"""URL-Config for home app."""
from django.urls import path, re_path
from apps.home import views
from . import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

    path('', views.own_grades_view, name='own_grades_view'),

]
