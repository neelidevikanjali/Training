from rest_framework import serializers
from .models import Currency_symbol

class symbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency_symbol
        fields = ['country']


class getSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency_symbol
        fields = ['currency', 'currency_symbol', 'country']
