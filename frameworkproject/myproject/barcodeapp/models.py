from django.db import models

class folderapp(models.Model):
    book_name = models.CharField(max_length=100)
    book_address = models.CharField(max_length=100)
    book_field = models.CharField(max_length=80)
    book_code = models.BinaryField(max_length=150)
    objects = models.Manager

class barimage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
