from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, studentSerializer
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer


class group(generics.GenericAPIView):
    serializer_class = studentSerializer

    def post(self, request):
        a = studentSerializer(data=request.data)
        a.is_valid()
        page = a.save()
        return Response({
            "user": studentSerializer(page, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(page)[1]
        })

# class loginview(generics.GenericAPIView):
#     serializer_class = UserSerializer
#
#     def post(self, request):
#         serializer = AuthTokenSerializer(data=request.data)
#         ser=serializer.is_valid(raise_exception=True)
#         login(request, ser)
#         return Response(UserSerializer(ser).data)



class loginview(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(UserSerializer(user).data)







