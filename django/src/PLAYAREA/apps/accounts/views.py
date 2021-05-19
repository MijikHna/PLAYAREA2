from django.shortcuts import render

# Create your views here.


def dashboard(request):
    return render(request, 'dashboard.html', {'title': 'Register'})


def register(request):
    return render(request, 'register.html', {'title': 'Register'})


def login(request):
    return render(request, 'login.html', {'title': 'Register'})
