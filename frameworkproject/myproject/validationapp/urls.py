from django.urls import path
from . views import *

urlpatterns = [
    path('post/', valid.as_view()),
]


