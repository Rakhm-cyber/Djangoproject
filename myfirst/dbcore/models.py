from django.db import models


class DBTypes(models.Model):
    Char = models.CharField(max_length=256, blank=False)


class Element(models.Model):
    name = models.CharField(max_length=256, blank=False)
    description = models.CharField(max_length=256, blank=False)
    address = models.CharField(max_length=256, blank=False)
    port = models.CharField(max_length=256, blank=False)
    type = models.ForeignKey(DBTypes, on_delete=models.CASCADE)



