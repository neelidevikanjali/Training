from django.urls import path
from .views import *

urlpatterns = [
    path('date/', dob.as_view())
]
