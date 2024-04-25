from django.db import models

from dbcore.models import Database, Port


class Server_type(models.Model):
    server_type = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return f"{self.server_type}"


class Server(models.Model):
    server = models.CharField(max_length=256, blank=False)
    type = models.ForeignKey(Server_type, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.server}"


class Database_server(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    database = models.ForeignKey(Database, on_delete=models.CASCADE)
    port = models.ForeignKey(Port, on_delete=models.CASCADE)
