from django.urls import path
from .views import *

urlpatterns = [
    path('zone/', zone.as_view()),
]
