from django.urls import path
from . views import *

urlpatterns = [
    path('post1/', group.as_view()),
    path('login/', loginview.as_view()),
]

