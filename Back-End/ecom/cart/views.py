from django.shortcuts import render, get_object_or_404
from .cart import Cart
from skyraptor.models import Product
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.

def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    total = cart.get_total()
    return render(request, 'html/cart_summary.html', {"cart_products": cart_products, "quantities": quantities, "total": total})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        Product_id = int(request.POST.get('product_id'))
        Product_qty = int(request.POST.get('product_qty'))

        product = get_object_or_404(Product, id=Product_id)

        cart.add(product=product, quantity = Product_qty)

        cart_quantity = cart.__len__()

        # response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, 'Product added to cart successfully!')
        return response

def cart_remove(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        Product_id = int(request.POST.get('product_id'))

        cart.remove(product = Product_id)

        response = JsonResponse({'product': Product_id})
        messages.success(request, 'Product removed from cart successfully!')
        return response

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        Product_id = int(request.POST.get('product_id'))
        Product_qty = int(request.POST.get('product_qty'))

        cart.update(product=Product_id, quantity=Product_qty)

        response = JsonResponse({'qty': Product_qty})
        messages.success(request, 'Cart updated successfully!')
        return response
