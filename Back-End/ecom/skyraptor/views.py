from django.shortcuts import render
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    products = Product.objects.all()
    return render(request, 'html/home.html', {})

def products(request):
    products = Product.objects.all()
    return render(request, 'html/products.html', {'products': products})

def login_user(request):
    return render(request, 'html/login.html', {})

def logout_user(request):
    return render(request, 'html/home.html', {})