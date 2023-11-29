from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('set/', views.setsession),
    path('get/', views.getsession),
    #path('logout/', views.logout),
    #path('signup/', views.signup),
]
