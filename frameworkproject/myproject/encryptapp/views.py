import hashlib

from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import RegisterSerializer, loginSerializer
from .models import Register

class encrypt(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        a = Register()
        a.username = request.POST.get("username")
        password = request.POST.get("password")
        saltpassword = hashlib.md5(password.encode())
        ser = saltpassword.hexdigest()
        a.password = ser
        a.contact = request.POST.get("contact")
        a.save()
        return Response(RegisterSerializer(a).data)

class loginEncrypt(generics.GenericAPIView):
    serializer_class = loginSerializer

    def post(self, request):
        u = request.data.get("username")
        print(u)
        pwd = request.data.get("password")
        saltpassword = hashlib.md5(pwd.encode())
        ser = saltpassword.hexdigest()
        a = Register.objects.get(username=u)
        
        print(a.password)
        if a.password == ser:
            return Response(loginSerializer(a).data)
        else:
            return HttpResponse('wrong details')
