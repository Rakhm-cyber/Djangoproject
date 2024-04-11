from django.contrib import admin

from Djangoproject.myfirst.dbcore.models import DBTypes, Element

admin.site.register(DBTypes)
admin.site.register(Element)