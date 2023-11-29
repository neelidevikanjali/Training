from rest_framework import serializers
from .models import twodates

class twodatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = twodates
        fields = '__all__'
