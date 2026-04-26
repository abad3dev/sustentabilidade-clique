from django.contrib import admin

from .models import Estado, Cidade, Local, Residuo, Residuo_Local

admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Local)
admin.site.register(Residuo)
admin.site.register(Residuo_Local)
