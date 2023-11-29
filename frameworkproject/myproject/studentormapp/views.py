from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response


# Create your views here.
class page(generics.GenericAPIView):
    serializer_class = StudentSerializer

    def post(self, request):
        s = StudentSerializer(data=request.data)
        s.is_valid()
        user = s.save()
        return Response(StudentSerializer(user).data)

class page1(generics.GenericAPIView):
    serializer_class = detailsSerializer

    def post(self, request):
        b = detailsSerializer(data=request.data)
        b.is_valid(raise_exception=True)
        c = b.save()
        return Response(detailsSerializer(c).data)

class page2(generics.GenericAPIView):
    serializer_class = informationSerializer

    def post(self, request):
        b = informationSerializer(data=request.data)
        b.is_valid(raise_exception=True)
        c = b.save()
        return Response(informationSerializer(c).data)





