from django.shortcuts import render
from django.http import HttpResponse
from .models import folder
# Create your views here.

def read(request):
    if request.method == 'POST':
        a = folder()
        a.name = request.POST.get('name')
        a.image = request.FILES['image']
        print(a.image)
        a.save()
        return HttpResponse('complete')
    return render(request, 'imagefolder.html')

def get(request):
    get_image = folder.objects.all()
    context={'get_image':get_image}
    return render(request, 'folder.html', {'image': get_image})









