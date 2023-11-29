from django.http import HttpResponse
from django.shortcuts import render
from .models import result

def home(request):
    if request.method == "POST":
        a = result()
        a.username = request.POST.get("username")
        a.password = request.POST.get("password")
        a.email = request.POST.get("email")
        a.save()
        request.session = ['name']
        return HttpResponse('success')
    return render(request, 'base.html')

def setsession(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        u = result.objects.get(username=uname)
        print(u)
        request.session['name'] = u.username
        if u.password == pwd:
           return HttpResponse('completed login')
        else:
           return HttpResponse('invalid password')
    return render(request, 'login.html')



def getsession(request):
    if 'name' in request.session:
       name = request.session['name']
       return render(request, 'getsession.html', {'name': name})
    else:
      return HttpResponse("Your Session is expired")


# def signup(request):
#     if request.method == 'POST':
#         uname = request.POST.get('username')
#         pwd = request.POST.get('password')
#         if result.objects.filter(username=uname):
#             return HttpResponse('username already exists')
#         else:
#             u = result(username=uname, password=pwd)
#             u.save()
#     else:
#         return render(request, 'signup.html')

# def logout(request):
#     try:
#         del request.session['user']
#     except:
#         return redirect('login')
#     return redirect('base.html')

