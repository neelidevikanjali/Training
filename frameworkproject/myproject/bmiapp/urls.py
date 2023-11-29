from django.urls import path
from .views import *

urlpatterns = [
    path('bmi/', service.as_view()),
]

