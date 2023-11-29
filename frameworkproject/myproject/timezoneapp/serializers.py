from rest_framework import serializers
from .models import *
import pytz
from pytz import country_timezones
import datetime


class TimezoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timezone
        fields = ['timezone','DateTime']

    def create(self, validated_data):
        timezone = validated_data['timezone']
        zone_time = datetime.datetime.now(pytz.timezone(timezone))
        print(zone_time)

        data =Timezone.objects.create(timezone=timezone, DateTime=zone_time)
        data.save()
        return data
