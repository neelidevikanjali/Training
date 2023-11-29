from django.urls import path
from .views import *

urlpatterns = [
    path('app/', value.as_view()),
]
