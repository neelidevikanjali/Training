from django.db import models


class forgetmodel(models.Model):
    username = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    objects = models.Manager








# from django.db import models
#
# class forgetmodel(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     email = models.EmailField()
#     new_password = models.CharField(max_length=100)
#     confirm_password = models.CharField(max_length=100)
#     objects = models.Manager

