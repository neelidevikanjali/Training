from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Register
from .serializers import RegisterSerializer



class valid(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        r = RegisterSerializer(data=request.data)
        r.is_valid()
        user = r.save()
        return Response(RegisterSerializer(user).data)


