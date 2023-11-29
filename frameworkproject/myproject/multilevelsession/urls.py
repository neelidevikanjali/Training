from django.urls import path
from . import views

urlpatterns = [
    path('one/', views.home),
    path('set/', views.set),
    path('get/', views.get),
    path('set1/', views.set1),
    path('get1/', views.get1),
    path('set2/', views.set2),
    path('get2/', views.get2),
]
