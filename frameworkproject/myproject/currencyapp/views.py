from django.shortcuts import render
from rest_framework.response import Response
from .models import customer
from .serializers import customerSerializer
from rest_framework import generics
from num2words import num2words

class currency(generics.GenericAPIView):
    serializer_class = customerSerializer

    def post(self, request):
        Currency = request.data.get('currency')
        conversion = num2words(Currency)
        s = customer()
        s.currency = Currency
        s.currency_word = conversion
        s.save()
        return Response(customerSerializer(s).data)
