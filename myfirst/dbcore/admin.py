from django.contrib import admin

from dbcore.models import Type, Database, Port, Server_type, Server, Database_server
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


@admin.register(Server_type)
class CustomAdminClass(ModelAdmin):
    pass


@admin.register(Server)
class CustomAdminClass(ModelAdmin):
    pass


@admin.register(Database_server)
class CustomAdminClass(ModelAdmin):
    pass
