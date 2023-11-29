from django.shortcuts import render
from .models import Decimalvalue
from .serializers import decimalvalueSerializer
from rest_framework import generics
from rest_framework.response import Response

class value(generics.GenericAPIView):
    serializer_class = decimalvalueSerializer
    def post(self, request):
        d = decimalvalueSerializer(data=request.data)
        d.is_valid()
        a = d.save()
        return Response(decimalvalueSerializer(a).data)
