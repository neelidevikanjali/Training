from django.db import models

# Create your models here.
class dobtoage(models.Model):
    dob = models.DateField()
    age = models.IntegerField()
    objects = models.Manager

