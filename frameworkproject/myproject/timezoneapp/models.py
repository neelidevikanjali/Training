from django.db import models
import zoneinfo
import calendar

# class Article(models.Model):
#     description = models.TextField()
#     publish_date = models.DateTimeField()
class Timezone(models.Model):
    TIMEZONE_CHOICES = ((x, x) for x in sorted(zoneinfo.available_timezones(), key=str.lower))
    DateTime = models.DateTimeField(auto_now_add=True)
    timezone = models.CharField("Timezone", choices=TIMEZONE_CHOICES, max_length=250, default='Etc/GMT+2')
    objects = models.Manager
