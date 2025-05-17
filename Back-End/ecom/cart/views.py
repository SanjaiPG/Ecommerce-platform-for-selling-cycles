from django.shortcuts import render

# Create your views here.

def cart_summary(request):
    return render(request, 'html/cart_summary.html', {})

def cart_add(request):
    return render(request, 'html/cart_add.html', {})

def cart_remove(request):
    return render(request, 'html/cart_remove.html', {})

def cart_update(request):
    return render(request, 'html/cart_update.html', {})