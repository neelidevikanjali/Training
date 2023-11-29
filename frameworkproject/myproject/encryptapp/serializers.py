from rest_framework import serializers
from .models import Register

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('username', 'password', 'contact')

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('username', 'password')
