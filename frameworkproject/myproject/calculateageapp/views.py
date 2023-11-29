from datetime import date
from .serializers import dobtoageSerializer
from .models import dobtoage
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
import datetime

class Dob(generics.GenericAPIView):
    serializer_class = dobtoageSerializer

    def post(self, request):
        today = date.today()
        dob = request.data.get('dob')
        dob = datetime.datetime.strptime(str(dob), '%Y-%m-%d').date()
        age = today.year-dob.year
        return Response({
            "result": age
        })


# class Dob(generics.GenericAPIView):
#     serializer_class = dobtoageSerializer
#
#     def post(self, request):
#         s = dobtoageSerializer(data=request.data)
#         s.is_valid()
#         user = s.save()
#         return Response(dobtoageSerializer(user).data)