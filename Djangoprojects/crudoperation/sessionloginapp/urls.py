from . import views
from django.urls import path

urlpatterns = [
    path('set/', views.setsession),
    path('get/', views.getsession),
]

