from rest_framework import serializers
from .models import album, album_company


class albumSerializer(serializers.ModelSerializer):
    class Meta:
       model = album
       fields = 'name', 'address'

class albumcompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = album_company
        fields = 'Album', 'contact', 'email'


