from django.urls import path
from . import views

urlpatterns = [
    path('payment_success', views.payment_success, name='payment_success'),
    path('checkout', views.checkout, name='checkout'),
    path('order_summary', views.order_summary, name='order_summary'),
    path('dash', views.dash, name='dash'),
]
