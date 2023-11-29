from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        paa = validated_data['password']
        user = User.objects.create_user(username=validated_data['username'], password=make_password(paa),
                                        email=validated_data['email'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
