from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Bmimodel
from .serializers import bmiserializer


class service(generics.GenericAPIView):
    serializer_class = bmiserializer

    def post(self, request):
        s = bmiserializer(data=request.data)
        s.is_valid()
        a = s.save()
        print(a)
        return Response(bmiserializer(a).data)


        # weight = request.data.get('weight')
        # height = request.data.get('height')
        # weight = int(weight)
        # height = int(height)
        # bmi = weight / (height / 100) ** 2
        # print(bmi)
        # round_bmi = round(bmi, 2)
        # n = Bmimodel()
        # n.height = height
        # n.weight = weight
        # n.bmi = round_bmi
        # n.save()
        # return Response(valueserializer(n).data)
