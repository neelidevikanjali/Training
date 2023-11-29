from .views import *
from django.urls import path

urlpatterns = [
    path('first/', INDEX),
    path('login/', login),
]
