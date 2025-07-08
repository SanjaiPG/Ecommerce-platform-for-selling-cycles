from django.shortcuts import render, redirect
from .models import Product, Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .froms import SignUpForm, UpdateUserForm, UpdatePasswordForm, UserInfoForm
from payment.forms import ShippingAddressForm
from payment.models import ShippingAddress, Order, OrderItem
import json
import random
from cart.cart import Cart


def home(request):
    products = list(Product.objects.all())
    random.shuffle(products)
    return render(request, 'html/home.html', {'products': products[:8]})

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

            current_user = Profile.objects.get(user__id=request.user.id)

            saver_cart = current_user.old_cart

            if saver_cart:
                converted = json.loads(saver_cart)
                cart = Cart(request)

                for key, value in converted.items():
                    cart.db_add(product=key, quantity=value)

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
            form = UpdatePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your password has been updated successfully login again')
                return redirect('home')

            else:
                messages.error(request, 'There was an error updating your password')
                return redirect('home')
            
        else:
            form = UpdatePasswordForm(user=current_user)
            return render(request, 'html/update_password.html', {'form': form})

    else:
        messages.success(request, 'You need to be logged in to update your password')
        return redirect('home')
    
def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        
        # Safely get or create shipping address
        shipping_user = ShippingAddress.objects.filter(user=request.user).first()
        if not shipping_user:
            shipping_user = ShippingAddress.objects.create(user=request.user)

        info_form = UserInfoForm(request.POST or None, instance=current_user)
        shipping_form = ShippingAddressForm(request.POST or None, instance=shipping_user)

        if info_form.is_valid() or shipping_form.is_valid():
            info_form.save()  
            shipping_form.save()
            messages.success(request, 'Your Info has been updated successfully')
            return redirect('home')
        
        return render(request, 'html/update_info.html', {
            'info_form': info_form,
            'shipping_form': shipping_form
        })
    
    else:
        messages.success(request, 'You need to be logged in to update your profile')
        return redirect('home')
    
def products(request):
    query = request.GET.get('q', '')
    
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    
    return render(request, 'html/products.html', {'products': products, 'query': query})

def user_order(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user)
        order_items = OrderItem.objects.filter(order__in=orders)
        return render(request, 'html/user_order.html', {'orders': orders, 'order_items': order_items})

    else:
        messages.success(request, 'You need to be logged in to view your orders')
        return redirect('home')
    
def home_order_views(request, pk):
    if request.user.is_authenticated:
        order = Order.objects.get(id=pk)
        order_items = OrderItem.objects.filter(order=order)

        for item in order_items:
            item.total = item.quantity * item.price

        return render(request, 'html/home_order_views.html', {
            'order': order,
            'order_items': order_items
        })