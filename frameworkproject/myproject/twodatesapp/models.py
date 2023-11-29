from django.db import models

class twodates(models.Model):
    #age = models.IntegerField()
    date1 = models.DateField()
    date2 = models.DateField()
    objects = models.Manager
