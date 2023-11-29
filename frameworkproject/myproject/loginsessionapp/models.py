from django.db import models

# Create your models here.
class result(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    objects = models.Manager

