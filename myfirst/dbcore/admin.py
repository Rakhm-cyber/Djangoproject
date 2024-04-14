from django.contrib import admin

from dbcore.models import DBTypes, Element

admin.site.register(DBTypes)
admin.site.register(Element)