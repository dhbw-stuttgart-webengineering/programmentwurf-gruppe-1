from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    # Django admin route
    path('admin/', admin.site.urls),
    # Auth routes - login / register
    path("", include("apps.authentication.urls")),

    # ADD NEW Routes HERE

    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls"))]
