from django.shortcuts import render
from .models import filepath
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def fileupload(request):
    if request.method == 'POST':
        b = filepath()
        b.name = request.POST.get("name")
        b.newimage = request.FILES['newimage']
        b.dt = datetime.now()
        print(b.newimage)
        b.save()
        return HttpResponse('success')
    return render(request, 'fileimage.html')
