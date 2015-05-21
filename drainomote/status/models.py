from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.


class Realserver(models.Model):
    ip = models.CharField(max_length=15)
    name = models.CharField(max_length=100, default="Unnamed")

    def __str__(self):
        return self.ip


class Realserver_Group_Permissions(models.Model):
    realserver = models.ForeignKey('Realserver')
    group = models.ForeignKey(Group)
    allow_drain = models.BooleanField(default=True)
