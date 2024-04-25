from django.contrib import admin
from unfold.admin import ModelAdmin

from servers.models import Server_type, Server, Database_server


@admin.register(Server_type)
class CustomAdminClass(ModelAdmin):
    pass


@admin.register(Server)
class CustomAdminClass(ModelAdmin):
    pass


@admin.register(Database_server)
class CustomAdminClass(ModelAdmin):
    pass
