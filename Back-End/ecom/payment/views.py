from django.shortcuts import render, redirect
from cart.cart import Cart
from payment.forms import ShippingAddressForm
from payment.models import ShippingAddress
from django.contrib import messages
from django.forms.models import model_to_dict



# Create your views here.

def payment_success(request):
    return render(request, 'payment/payment_success.html', {})

def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    total = cart.get_total()

    if total == 0:
        messages.success(request, 'Your cart is empty, please add products to your cart before checking out.')
        return redirect('home')

    if request.user.is_authenticated:
        shipping_user = ShippingAddress.objects.get(user=request.user)
        shipping_form = ShippingAddressForm(request.POST or None, instance=shipping_user)

        request.session['my_shipping'] = model_to_dict(shipping_user)

        if not shipping_user.shipping_name or not shipping_user.shipping_name.strip():
            messages.success(request, 'Please complete your shipping information before checking out.')
            return redirect('home')

        return render(request, 'payment/checkout.html', {"cart_products": cart_products, "quantities": quantities, "total": total, "shipping_form": shipping_form})
    else:
        messages.success(request, 'You need to be logged in to checkout')
        return redirect('home')

def order_summary(request):
    my_shipping = request.session.get('my_shipping')
    print(my_shipping)

    shipping_address = f"{my_shipping['shipping_address']}\n{my_shipping['shipping_city']}, {my_shipping['shipping_state']} - {my_shipping['shipping_pin_code']}\n"
    print(shipping_address)


    messages.success(request, 'Your order has been placed successfully!')
    return redirect('home')