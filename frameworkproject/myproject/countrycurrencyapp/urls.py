from django.urls import path
from .views import *

urlpatterns = [
    path('symbol/', countries.as_view())
]
