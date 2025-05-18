from django.shortcuts import render, get_object_or_404
from .cart import Cart
from skyraptor.models import Product
from django.http import JsonResponse

# Create your views here.

def cart_summary(request):
    return render(request, 'html/cart_summary.html', {})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        Product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=Product_id)

        cart.add(product=product)
        response = JsonResponse({'Product Name: ': product.name})
        return response

def cart_remove(request):
    return render(request, 'html/cart_remove.html', {})

def cart_update(request):
    return render(request, 'html/cart_update.html', {})