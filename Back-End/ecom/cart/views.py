from django.shortcuts import render, get_object_or_404
from .cart import Cart
from skyraptor.models import Product
from django.http import JsonResponse

# Create your views here.

def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    return render(request, 'html/cart_summary.html', {"cart_products": cart_products})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        Product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=Product_id)

        cart.add(product=product)

        cart_quantity = cart.__len__()

        # response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty': cart_quantity})
        return response

def cart_remove(request):
    return render(request, 'html/cart_remove.html', {})

def cart_update(request):
    return render(request, 'html/cart_update.html', {})