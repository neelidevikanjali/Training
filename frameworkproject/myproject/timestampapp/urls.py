from django.urls import path
from .views import currenttime

urlpatterns = [
    path('time/', currenttime.as_view()),
]
