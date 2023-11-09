from django.contrib import admin

# Register your models here.
from .models import Grade, Module, Unit

admin.site.register(Grade)
admin.site.register(Unit)
admin.site.register(Module)
