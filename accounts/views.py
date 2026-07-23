from django.shortcuts import render

# Create your views here.
def register(request):
    context={}
    return render(request,"accounts/register.html",context)

def login(request):
    context={}
    return render(request,"accounts/login.html",context)

def logout(request):
    context={}
    return render(request,"accounts/logout.html",context)

def dashboard(request):
    context={}
    return render(request,"accounts/dashboard.html",context)
