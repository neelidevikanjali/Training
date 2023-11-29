from django.shortcuts import render, redirect
from .models import program
from django.contrib import messages
from django.http import HttpResponse
from .models import *

def INDEX(request):
    if request.method == "POST":
        if request.POST.get("name") and request.POST.get("password") and request.POST.get("email"):
            a = program()
            a.name = request.POST.get("name")
            a.password = request.POST.get("password")
            a.email = request.POST.get("email")
            a.save()
        return HttpResponse('success')

    else:
        HttpResponse()
        return render(request, 'index.html')

def getall(request):
    student = program.objects.all()
    return render(request, 'my.html', {'program': student})

def delete(request, id):
    b = program.objects.get(id=id)
    b.delete()
    return redirect(getall)

def update(request, id):
    d = program.objects.get(id=id)
    d.name = request.POST.get("name")
    d.email = request.POST.get("email")
    d.password = request.POST.get('password')
    d.save()
    return render(request, 'first.html', {'program': d})


