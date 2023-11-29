from .views import *
from django.urls import path

urlpatterns = [
    path('photo/', read),
    path('getimage/', get),
]
