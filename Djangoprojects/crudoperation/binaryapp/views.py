from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import photo
from datetime import datetime
from .convert import im
def upgrade(request):
    if request.method == 'POST':
        b = photo()
        b.name = request.POST.get("name")
        img = request.FILES['image']
        b.image = im(img)
        b.dt = datetime.now()
        print(b.image)
        b.save()
        return HttpResponse('success')
    return render(request, 'binary.html')



