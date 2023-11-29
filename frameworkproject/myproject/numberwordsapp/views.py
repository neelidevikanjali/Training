from django.shortcuts import render
from .models import numtowords
from .serializers import numtowprdsSerilaizer
from rest_framework import generics
from rest_framework.response import Response
from datetime import datetime

class words(generics.GenericAPIView):
    serializer_class = numtowprdsSerilaizer

    def post(self, request):
        var = numtowprdsSerilaizer(data=request.data)
        var.is_valid()
        h = var.save()
        return Response(numtowprdsSerilaizer(h).data)

