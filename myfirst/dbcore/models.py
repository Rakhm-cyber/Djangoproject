from django.db import models


class Type(models.Model):
    title = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return f"{self.title}"


class Database(models.Model):
    title = models.CharField(max_length=256, blank=False)
    description = models.CharField(max_length=256, blank=False)
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)
    server_id = models.IntegerField(blank=False)


class Port(models.Model):
    port = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return f"{self.port}"
