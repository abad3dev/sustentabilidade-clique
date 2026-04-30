from django.contrib import admin

# Register your models here.
from .models import Residuo, Residuo_Local


admin.site.register(Residuo)
admin.site.register(Residuo_Local)