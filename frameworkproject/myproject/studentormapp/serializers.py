from rest_framework import serializers
from .models import Student, details, information


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
       model = Student
       fields = '__all__'

class detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = details
        fields = '__all__'

class informationSerializer(serializers.ModelSerializer):
    class Meta:
        model = information
        fields = '__all__'

