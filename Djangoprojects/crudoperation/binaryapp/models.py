from django.db import models

# Create your models here.
class photo(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    #dt = models.DateTimeField()
