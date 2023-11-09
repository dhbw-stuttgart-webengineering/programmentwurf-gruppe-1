"""Admin Confirguration for the Data Endpoint App."""
from django.contrib import admin

# Register your models here.
from .models import Grades, Courses

admin.site.register(Grades)
admin.site.register(Courses)
