from django.db import models

# Create your models here.

class register(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    objects = models.Manager



