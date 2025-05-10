from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'html/home.html', {})

def products(request):
    products = Product.objects.all()
    return render(request, 'html/products.html', {'products': products})

def login(request):
    return render(request, 'html/login.html', {})