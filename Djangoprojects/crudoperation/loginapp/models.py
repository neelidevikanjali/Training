from django.db import models

# Create your models here.
class Person(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=60)
    email = models.EmailField(max_length=50)
    contact = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    objects = models.Manager
