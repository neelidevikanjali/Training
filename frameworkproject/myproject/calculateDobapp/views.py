from datetime import date

from django.shortcuts import render
from rest_framework.response import Response
from .serializers import agetoyearserializer
from .models import agetoyear
from rest_framework import generics

class dob(generics.GenericAPIView):
    serializer_class = agetoyearserializer

    def post(self, request):
        today = date.today()
        year = today.year
        print(type(year))
        age = request.data.get('age')
        print(type(age))
        calculate = int(age) - year
        return Response({
            "result": calculate
        })









