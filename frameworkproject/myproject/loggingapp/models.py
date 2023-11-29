from django.db import models

# Create your models here.
class register(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=80)
    objects = models.Manager


