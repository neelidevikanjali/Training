from django.db import models

# Create your models here.
class result(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    date = models.DateTimeField(auto_now=True)
    #dt = models.DateTimeField()


