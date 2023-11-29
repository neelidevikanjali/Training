from django.http import HttpResponse

from .models import forgetmodel
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import resetserializer, registerserializer, loginserializer


class forget(generics.CreateAPIView):
    serializer_class = registerserializer
    queryset = forgetmodel.objects.all()

class resetpassword(generics.UpdateAPIView):
    serializer_class = resetserializer

    def post(self, request):
        ser =resetserializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        #print(ser)
        return Response({'message': 'Password change success',
                         'result': ser.data})


class login(generics.GenericAPIView):
    serializer_class = loginserializer

    def post(self, request):
        u = request.data.get("username")
        print(u)
        pwd = request.data.get("password")
        b = forgetmodel.objects.get(username=u)
        print(b.password)
        if b.password == pwd:
            return Response(loginserializer(b).data)
        else:
            return HttpResponse('invalid username or password')

        # ser = loginserializer(data=request.data)
        # ser.is_valid(raise_exception=True)
        # ser.save()
        # return Response('invalid username or password')

