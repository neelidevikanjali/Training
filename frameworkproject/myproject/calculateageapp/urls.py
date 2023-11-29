from django.urls import path
from .views import *

urlpatterns = [
    path('age/', Dob.as_view()),
]
