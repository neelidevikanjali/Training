from .views import *
from django.urls import path

urlpatterns = [
    path('hello/', INDEX),
    path('getall/', getall),
    path('delete/<int:id>', delete),
    path('update/<int:id>', update),
]
