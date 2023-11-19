from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='post':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        my_user=User.object.create_user(uname,email,password)
        my_user.save()
        return HttpResponse("User has been created sucessfully!!!")
        print(uname,email,password)

    return render (request,'signup.html')

def LoginPage(request):
    return render (request,'login.html')
