from rest_framework import generics
from django.apps import apps
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .models import multilevel

def home(request):
    if request.method == "POST":
        a = multilevel()
        a.username = request.POST.get("username")
        a.password = request.POST.get("password")
        a.email = request.POST.get("email")
        a.save()
        request.session = ['name']
        return HttpResponse('success')

    return render(request, 'base.html')

def set(request):
    if request.method == 'POST':
        uname = request.POST.get("username")
        pwd = request.POST.get("password")
        # program = apps.get_model('loginsessionapp', 'result')
        u = multilevel.objects.get(username=uname)
        print(u)
        request.session['name'] = u.username
        request.session.set_expiry(30)
        if u.password == pwd:
            return HttpResponse('successfully login')
        else:
            return HttpResponse('invalid login')
    return render(request, 'login.html')

def get(request):
    if 'name' in request.session:
       name = request.session['name']
       return render(request, 'getsession.html', {'name': name})
    else:
      return HttpResponse("Your Session is expired")

def set1(request):
    if request.method == 'POST':
        uname = request.POST.get("username")
        pwd = request.POST.get("password")
        # program = apps.get_model('loginsessionapp', 'result')
        u = multilevel.objects.get(username=uname)
        print(u)
        request.session['name'] = u.username
        request.session.set_expiry(40)
        if u.password == pwd:
            return HttpResponse('successfully login')
        else:
            return HttpResponse('invalid login')
    return render(request, 'login.html')

def get1(request):
    if 'name' in request.session:
       name = request.session['name']
       return render(request, 'getsession.html', {'name': name})
    else:
      return HttpResponse("Your Session is expired")

def set2(request):
    if request.method == 'POST':
        uname = request.POST.get("username")
        pwd = request.POST.get("password")
        # program = apps.get_model('loginsessionapp', 'result')
        u = multilevel.objects.get(username=uname)
        print(u)
        request.session['name'] = u.username
        request.session.set_expiry(25)
        if u.password == pwd:
            return HttpResponse('successfully login')
        else:
            return HttpResponse('invalid login')
    return render(request, 'login.html')

def get2(request):
    if 'name' in request.session:
       name = request.session['name']
       return render(request, 'getsession.html', {'name': name})
    else:
      return HttpResponse("Your Session is expired")
