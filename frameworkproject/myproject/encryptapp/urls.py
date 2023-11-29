from django.urls import path
from . views import *

urlpatterns = [
    path('post/', encrypt.as_view()),
    path('login/', loginEncrypt.as_view()),
]

