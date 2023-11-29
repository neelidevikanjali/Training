from django.db import models

# Create your models here.
class album(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=80)

class album_company(models.Model):
    Album = models.ForeignKey(
        album,
        on_delete=models.CASCADE,
        related_name='company'
    )
    contact = models.CharField(max_length=50)
    email = models.CharField(max_length=60)







