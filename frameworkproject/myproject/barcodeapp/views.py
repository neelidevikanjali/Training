from django.shortcuts import render
from rest_framework.response import Response

from .models import folderapp, barimage
from .serializers import folderappSerializer, barimageSerializer
from rest_framework import generics

class book(generics.GenericAPIView):
    serializer_class = folderappSerializer

    def post(self, request):
        c = folderappSerializer(data=request.data)
        c.is_valid(raise_exception=True)
        b = c.save()
        return Response(folderappSerializer(b).data)

class book1(generics.GenericAPIView):
    serializer_class = barimageSerializer

    def post(self, request):
        a = barimage()
        a.name = request.POST.get("name")
        a.image = request.FILES['image']
        print(a.image)
        a.save()
        return Response(barimageSerializer(a).data)
