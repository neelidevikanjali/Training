from django.db import models
from django_countries.fields import CountryField
from datetime import datetime
country = ['India', 'newyork', 'america']
class Currency_symbol(models.Model):
    country = CountryField(blank_label={'select country_currency'})
    currency = models.CharField(max_length=50)
    currency_symbol = models.CharField(max_length=60)
    time = models.DateTimeField(auto_now=True)
    objects = models.Manager


