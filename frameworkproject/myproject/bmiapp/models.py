from django.db import models

# Create your models here.
class Bmimodel(models.Model):
    weight = models.IntegerField()
    height = models.IntegerField()
    calculatedbmi = models.IntegerField()
    objects = models.Manager
