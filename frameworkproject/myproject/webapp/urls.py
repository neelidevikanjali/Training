from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('list/', employeeCreateApi.as_view()),
    path('post/', employeeApi.as_view()),
    path('update/<int:pk>', employeeUpdateApi.as_view()),
    path('delete/<int:pk>', employeeDeleteApi.as_view()),

]
