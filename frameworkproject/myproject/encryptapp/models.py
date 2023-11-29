from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    contact = models.CharField(max_length=80)
    objects = models.Manager

