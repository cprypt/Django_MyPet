from django.contrib import admin
from .models import BaseInfo


class BaseInfoAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(BaseInfo, BaseInfoAdmin)

# Register your models here.
