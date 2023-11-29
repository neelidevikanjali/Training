from django.shortcuts import render
from rest_framework import generics
from .models import Timezone
from .serializers import TimezoneSerializer
from rest_framework.response import Response

class zone(generics.GenericAPIView):
    serializer_class = TimezoneSerializer
    def post(self, request):
        a = TimezoneSerializer(data=request.data)
        a.is_valid()
        s = a.save()
        return Response(TimezoneSerializer(s).data)
