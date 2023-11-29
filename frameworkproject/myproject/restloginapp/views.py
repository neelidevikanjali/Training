from django.http import HttpResponse
from rest_framework import generics
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import register

@api_view(['GET'])

def get(request):
    task = register.objects.all()
    serializer = registerSerializer(task, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def registerpage(request):
    serializer = registerSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

class login(generics.GenericAPIView):
    serializer_class = loginserializer

    def post(self, request):
        print('5822')
        u = request.data.get("username")
        print(u)
        pwd = request.data.get("password")
        b = register.objects.get(username=u)
        print(b.password)
        if b.password == pwd:
            return Response(loginserializer(b).data)
        else:
            return HttpResponse('fail')



