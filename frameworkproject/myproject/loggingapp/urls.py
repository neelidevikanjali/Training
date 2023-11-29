from django.urls import path
from . views import *

urlpatterns = [
    path('post/', my_view.as_view()),

]
