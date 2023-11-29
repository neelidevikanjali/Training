from django.urls import path
from .views import *

urlpatterns = [
    path('num/', forget.as_view()),
    path('one/', resetpassword.as_view()),
    path('two/', login.as_view()),
]
