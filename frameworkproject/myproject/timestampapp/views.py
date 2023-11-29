from django.shortcuts import render
from .models import timestamp
from .serializers import timestampSerializer
from rest_framework import generics
from rest_framework.response import Response

class currenttime(generics.GenericAPIView):
    serializer_class = timestampSerializer

    def post(self, request):
        m = timestampSerializer(data=request.data)
        m.is_valid()
        m.save()
        return Response(timestampSerializer(m).data)
