from django.urls import path
from . views import *

urlpatterns = [
    path('two/', song.as_view()),
    path('song/', song1.as_view()),
]
