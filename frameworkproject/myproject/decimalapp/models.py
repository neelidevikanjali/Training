from django.db import models

class Decimalvalue(models.Model):
    numbers = models.FloatField()
    decimal_field = models.IntegerField()
    converted_value = models.CharField(max_length=200)
    objects = models.Manager
