from django.contrib import admin

from dbcore.models import Type, Database, Port
from unfold.admin import ModelAdmin


@admin.register(Type)
class CustomAdminClass(ModelAdmin):
    pass


@admin.register(Database)
class CustomAdminClass(ModelAdmin):
    pass


@admin.register(Port)
class CustomAdminClass(ModelAdmin):
    pass
