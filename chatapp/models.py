from django.db import models
from datetime import datetime

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=1000)
    def __str__(self):
        return self.name
    

class Message(models.Model):
    value = models.CharField(max_length=10000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    datetime_built_in = models.DateTimeField(auto_now=True, auto_now_add=False)
    room = models.CharField(max_length=10000000)
    user = models.CharField(max_length=10000000)
    def __str__(self):
        return self.user