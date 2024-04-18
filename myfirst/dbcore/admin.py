from django.contrib import admin

from dbcore.models import Type, Database, Port, Server_type, Server, Database_server

admin.site.register(Type)
admin.site.register(Database)
admin.site.register(Port)
admin.site.register(Server_type)
admin.site.register(Server)
admin.site.register(Database_server)