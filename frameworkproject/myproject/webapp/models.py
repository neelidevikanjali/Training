from django.db import models

# Create your models here.

class employee(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=20)
    emp_id = models.IntegerField()
    objects = models.Manager





