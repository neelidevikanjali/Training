from django.urls import path
from .views import *

urlpatterns = [
    path('country/', currency.as_view())
]
