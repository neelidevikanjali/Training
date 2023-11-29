from django.shortcuts import render
from django.http import HttpResponse
import logging
from rest_framework import generics
from .serializers import registerSerializer

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class my_view(generics.GenericAPIView):
    serializer_class = registerSerializer

    def post(self, request):
        b = registerSerializer(data=request.data)
        b.is_valid()
        b.save()
        return HttpResponse("django logging example")

