from django.urls import path
from .views import *

urlpatterns = [
    path('code1/', book.as_view()),
    path('code3/', book1.as_view()),
]
