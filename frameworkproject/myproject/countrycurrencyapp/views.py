from django.shortcuts import render
from .models import Currency_symbol
from .serializers import *
from rest_framework import generics
from countryinfo import CountryInfo
from datetime import datetime
from django.http import HttpResponse
from currency_symbols import CurrencySymbols
from rest_framework.response import Response

def currency(name):
    name = CountryInfo(name)
    name1 = name.currencies()
    result = name1[0]
    return result


def symbol(symbol):
    name3 = CurrencySymbols.get_symbol(symbol)
    return name3


class countries(generics.GenericAPIView):
    serializer_class = symbolSerializer

    def post(self, request):
        date1 = datetime.now()
        cr_name = request.data.get('country_currency')
        con_cur = currency(cr_name)
        page = symbol(con_cur)
        y = Currency_symbol()
        y.country = cr_name
        y.currency = con_cur
        y.currency_symbol = page
        y.time = date1.strftime("%y-%m-%d")
        y.save()
        return Response(getSerializer(y).data)

