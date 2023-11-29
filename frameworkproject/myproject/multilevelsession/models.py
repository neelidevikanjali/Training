from django.db import models

# Create your models here.
class multilevel(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=80)
    email = models.EmailField()
    objects = models.Manager
