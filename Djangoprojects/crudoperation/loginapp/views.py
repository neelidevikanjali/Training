from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from .models import Person

def INDEX(request):
    if request.method == "POST":
        if request.POST.get("username") and request.POST.get("branch") and request.POST.get("password") and request.POST.get("email") and request.POST.get("contact"):
            a = Person()
            a.username = request.POST.get("username")
            a.branch = request.POST.get("branch")
            a.password = request.POST.get("password")
            a.email = request.POST.get("email")
            a.contact = request.POST.get("contact")
            a.save()

        return HttpResponse('success')

    else:
        return render(request, 'second.html')

def login(request):
    if request.method == "POST":
        u = request.POST.get("username")
        pwd = request.POST.get("password")
        b = Person.objects.get(username=u)
        print(b)

        if b.password == pwd:
            return HttpResponse('success')
        else:
            return HttpResponse('please check')
    return render(request, 'third.html')
