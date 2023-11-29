from django.urls import path
from .views import fileupload

urlpatterns = [
    path('file/', fileupload),
]
