from rest_framework import serializers
from .models import Bmimodel

def calculate(h,w):
    BMI = w/(h/100)** 2
    return BMI

class bmiserializer(serializers.ModelSerializer):
    class Meta:
        model = Bmimodel
        fields = 'weight', 'height'

    def create(self, validated_data):
        height = validated_data['height']
        weight = validated_data['weight']
        calculatebmi = calculate(height,weight)
        print(calculatebmi)
        user = Bmimodel.objects.create(height=validated_data['height'], weight=validated_data['weight'], calculatedbmi=calculatebmi)
        user.save()
        return user

# class valueserializer(serializers.ModelSerializer):
#     class Meta:
#         model = Bmimodel
#         fields = '__all__'




