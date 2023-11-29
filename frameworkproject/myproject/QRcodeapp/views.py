from django.http import HttpResponse
from django.shortcuts import render
from pyqrcode import *
from rest_framework.response import Response

from .models import folder, qrimage
from .serializers import folderSerializer
from rest_framework import generics

class home(generics.GenericAPIView):
    serializer_class = folderSerializer

    def post(self, request):
        c = folderSerializer(data=request.data)
        c.is_valid(raise_exception=True)
        b = c.save()
        return Response(folderSerializer(b).data)

def upload(request):
    if request.method == 'POST':
        b = qrimage()
        b.name = request.POST.get("name")
        b.image = request.FILES['image']
        print(b.image)
        b.save()
        return HttpResponse('success')
    return render(request, 'codeimage.html')
