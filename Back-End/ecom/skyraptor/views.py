from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .froms import SignUpForm, UpdateUserForm, UpdatePasswordForm


def home(request):
    products = Product.objects.all()
    return render(request, 'html/home.html', {})

def products(request):
    products = Product.objects.all()
    return render(request, 'html/products.html', {'products': products})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in')
            return redirect('home')
        else:
            # messages.success(request, 'There was an error logging in')
            return redirect('login')
    
    return render(request, 'html/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have registered succesfully')
            return redirect('home')

        else:
            # messages.success(request, 'There was an error registering')
            return redirect('register')

    return render(request, 'html/login.html', {'form': form})

def product_view(request, pk):
    product_view = Product.objects.get(id=pk)
    category = product_view.Category

    related_products = Product.objects.filter(Category=category).exclude(id=pk)[:10]
    
    return render(request, 'html/product_view.html', {'product_view': product_view, 'category': category, 'related_products': related_products})

def category(request, foo):

    foo = foo.replace('-', ' ')

    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(Category=category)
        return render(request, 'html/category.html', {'products': products})
        
    except:
        messages.success(request, 'That category does not exist')
        return redirect('home')
    
def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, 'Your profile has been updated successfully')
            return redirect('home')
        return render(request, 'html/update_user.html', {'user_form': user_form})
    
    else:
        messages.success(request, 'You need to be logged in to update your profile')
        return redirect('home')
    
def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            pass
        else:
            form = UpdatePasswordForm(user=current_user)
            return render(request, 'html/update_password.html', {'form': form})

    else:
        messages.success(request, 'You need to be logged in to update your password')
        return redirect('home')