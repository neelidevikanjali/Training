from .views import *
from django.urls import path
from . import *
urlpatterns = [
    path('get/', get),
    path('page/', registerpage),
    path('login/', login.as_view())
]
