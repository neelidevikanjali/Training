from django.urls import path
from .views import words

urlpatterns = [
    path('word/', words.as_view()),
]
