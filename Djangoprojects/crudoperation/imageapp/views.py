from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import result
from datetime import datetime


def upload(request):
    if request.method == 'POST':
        b = result()
        b.name = request.POST.get("name")
        b.image = request.FILES['image']
        b.dt = datetime.now()
        print(b.image)
        b.save()
        return HttpResponse('success')
    return render(request, 'imagenature.html')
