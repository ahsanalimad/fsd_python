from django import http
from django.shortcuts import render
from website.models import Products
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import redirect

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        print("User Logged In")
    else:
        print("Not Logged In")
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request, 'website/index.html', context)

def search(request):

    data = {
        'title': "Welcome to Our E-commerce Search Website",
        'description': "Search for your favorite products here."
    }
    return render(request, 'website/index.html', data)


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect('home')
    return render(request, 'website/login.html')

def logout(request):
    return render(request, 'website/logout.html')




