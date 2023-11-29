from django.db import models

class numtowords(models.Model):
    currency = models.IntegerField()
    convert_words = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    objects = models.Manager
