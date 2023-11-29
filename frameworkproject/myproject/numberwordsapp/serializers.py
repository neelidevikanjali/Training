from num2words import num2words
from rest_framework import serializers
from .models import numtowords

def converstion(a):
    user = num2words(a)
    return user

class numtowprdsSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = numtowords
        fields = '__all__'
    def create(self, validated_data):
        currency = validated_data['currency']
        convert = converstion(currency)
        print(convert)
        var = numtowords.objects.create(currency=currency, convert_words=convert)
        var.save()
        return var

