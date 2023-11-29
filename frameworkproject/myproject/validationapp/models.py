from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=100)
    Password = RegexValidator(regex=r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$",
                              message="password "
                                      "must contain 8 letters and a captITAL letter and a special character ")
    password = models.CharField(validators=[Password], max_length=30)
    contact = models.CharField(max_length=80)
    objects = models.Manager

