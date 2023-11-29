from django.shortcuts import render
from rest_framework import generics
from .serializers import twodatesSerializer
from .models import twodates
from rest_framework.response import Response
from datetime import date
import datetime

class dates(generics.GenericAPIView):
    serializer_class = twodatesSerializer

    def post(self, request):
        today = date.today()
        date1 = request.data.get('date1')
        date2 = request.data.get('date2')
        #dob = request.data.get('date2')
        date1 = datetime.datetime.strptime(str(date1), '%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(str(date2), '%Y-%m-%d').date()
        #print(dob2)
        age = date1.year-date2.year
        return Response({
            "result": age
        })



