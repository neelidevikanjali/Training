from django.shortcuts import render
from rest_framework.response import Response
from .models import album, album_company
from .serializers import albumSerializer, albumcompanySerializer
from rest_framework import generics

# Create your views here.
class song(generics.GenericAPIView):
    serializer_class = albumSerializer
    def post(self, request):
        a = albumSerializer(data=request.data)
        a.is_valid()
        page = a.save()
        return Response(albumSerializer(page).data)

class song1(generics.GenericAPIView):
    serializer_class = albumcompanySerializer
    def post(self, request):
        a = albumcompanySerializer(data=request.data)
        a.is_valid(raise_exception=True)
        a.save()
        return Response(albumcompanySerializer(a).data)




