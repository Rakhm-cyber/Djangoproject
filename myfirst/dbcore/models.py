import random
from django.db import models
from django.db.models import Q


def generate_key():
    a = "qwrtyuiopadfghjlzcvbnm"
    b = "QWERTYUIOPASDFGHJKLZXCVBNM"
    c = "0123456789"
    d = a + b + c
    return "".join(random.sample(d, 8))


class Type(models.Model):
    title = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return f"{self.title}"


class Database(models.Model):
    title = models.CharField(max_length=256, blank=False)
    description = models.CharField(max_length=256, blank=False)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='databases')
    server_id = models.IntegerField(blank=False)
    key = models.CharField(max_length=256, default=generate_key, unique=True)

    def save(self, *args, **kwargs):
        while not self.pk or Database.objects.filter(key=self.key).exists():
            self.key = generate_key()
        super().save(*args, **kwargs)


class Port(models.Model):
    port = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return f"{self.port}"
