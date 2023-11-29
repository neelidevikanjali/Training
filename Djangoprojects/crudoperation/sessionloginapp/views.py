from django.http import HttpResponse
from django.shortcuts import render

def setsession(request):
    request.session['name'] = 'riya'
    return render(request, 'setsession.html')

def getsession(request):
    if 'name' in request.session:
       name = request.session['name']
       return render(request, 'getsession.html', {'name': name})
    else:
      return HttpResponse("Your Session is expired")




# def logsession(request):
#     if request.method == "POST":
#         uname = request.POST.get('uname')
#         pwd = request.POST.get('pwd')
#         check_user = User.objects.filter(username=uname, password=pwd)
#         if check_user:
#             request.session['user'] = uname
#             return HttpResponse('home')
#         else:
#             return HttpResponse('enter valid Username or Password')
#     return render(request, 'getsession.html')



