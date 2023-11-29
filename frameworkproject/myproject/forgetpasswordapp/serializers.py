from django.contrib.auth.models import User
from .models import forgetmodel
from rest_framework import serializers


class registerserializer(serializers.ModelSerializer):
    class Meta:
        model = forgetmodel
        fields = '__all__'


class resetserializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=10)
    new_password = serializers.CharField(max_length=10)
    class Meta:
        model = forgetmodel
        fields = 'username', 'email', 'new_password', 'confirm_password'
    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        new_password = validated_data['new_password']
        confirm_password = validated_data['confirm_password']
        em = forgetmodel.objects.get(email=email)
        if new_password == confirm_password:
            em.password = new_password

        user = forgetmodel.objects.create(username=username, email=email, password=new_password)
        user.save()
        print(user)
        return user

class loginserializer(serializers.ModelSerializer):
    class Meta:
        model = forgetmodel
        fields = 'username', 'password'
