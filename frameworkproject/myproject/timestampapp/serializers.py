import datetime

from rest_framework import serializers
from .models import timestamp

class timestampSerializer(serializers.ModelSerializer):
    class Meta:
        model = timestamp
        fields = ('name', 'age', 'phno', 'present_time')
    def create(self, validated_data):
        time = datetime.datetime.now()
        print(time)
        page = timestamp.objects.create(name=validated_data['name'], age=validated_data['age'], phno=validated_data['phno'], present_time=time)
        page.save()
        return page
