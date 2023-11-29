from django.db import models

class timestamp(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    phno = models.CharField(max_length=100)
    present_time = models.CharField(max_length=100)
    #cuurent_time = models.CharField(max_length=100)
    objects = models.Manager

