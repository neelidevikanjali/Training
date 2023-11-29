from django.db import models

# Create your models here.
class agetoyear(models.Model):
    age = models.IntegerField()
    objects = models.Manager

