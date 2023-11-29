from django.urls import path
from .views import *

urlpatterns = [
    path('post/', page.as_view()),
    path('one/', page1.as_view()),
    path('many/', page2.as_view()),
]
