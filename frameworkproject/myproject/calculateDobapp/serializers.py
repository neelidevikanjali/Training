

from rest_framework import serializers
from .models import agetoyear

class agetoyearserializer(serializers.ModelSerializer):
    class Meta:
        model = agetoyear
        fields = '__all__'



