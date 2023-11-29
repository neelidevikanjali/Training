from django.db import models

# Create your models here.

class customer(models.Model):
    currency = models.IntegerField()
    currency_word = models.CharField(max_length=80)
    objects = models.Manager

