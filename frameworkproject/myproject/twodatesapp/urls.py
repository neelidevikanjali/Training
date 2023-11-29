from django.urls import path
from .views import *

urlpatterns = [
    path('two/', dates.as_view()),
]
