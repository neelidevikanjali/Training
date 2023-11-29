from rest_framework import serializers
from .models import dobtoage
from datetime import date
import datetime

# def calculatedate(age):
#     today = date.today()
#     y = today.year - int(age)
#     dob = f'{y}-{today.month}-{today.day}'
#     #print(type(dob))
#     d = datetime.datetime.now().strptime(dob, "%Y-%m-%d").date()
#     #print(type(d))
#     #print(d)
#     return d

class dobtoageSerializer(serializers.ModelSerializer):

    class Meta:
        model = dobtoage
        fields = ['dob']
    # def create(self, validated_data):
    #     dob = validated_data['age']
    #     print(type(dob))
    #     convert = calculatedate(dob)
    #     r = dobtoage.objects.create(age=validated_data['age'], dob=convert)
    #     #print(r)
    #     r.save()
    #     return r



