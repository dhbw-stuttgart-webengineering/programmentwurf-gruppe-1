from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    # Django admin route
    path('admin/', admin.site.urls),

    path("", include("apps.data_endpoint.urls")),

    # Auth routes - login / register
    path("", include("apps.authentication.urls")),

    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls")),
    
    
    ]
