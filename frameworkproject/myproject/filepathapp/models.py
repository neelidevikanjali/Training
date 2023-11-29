from django.db import models

class filepath(models.Model):
    name = models.CharField(max_length=50)
    newimage = models.ImageField()
    date = models.DateTimeField(auto_now=True)
    #dt = models.DateTimeField()
    objects = models.Manager


