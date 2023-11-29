from django.db import models

# Create your models here.
class program(models.Model):
    name = models.CharField(max_length=20)
    password = models.IntegerField()
    email = models.EmailField()

