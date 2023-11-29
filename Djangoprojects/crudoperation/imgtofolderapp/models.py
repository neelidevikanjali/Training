from django.db import models


class folder(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField('/image')
    objects = models.Manager

