from django import forms
from .models import ShippingAddress

class ShippingAddressForm(forms.ModelForm):
    shipping_name = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}), required=True
    )
    shipping_email = forms.EmailField(
        label="", 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}), required=True
    )
    shipping_address = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}), required=True
    )
    shipping_phone = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}), required=True
    )
    shipping_city = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}), required=True
    )
    shipping_state = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}), required=True
    )
    shipping_pin_code = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pin Code'}), required=True
    )

    class Meta:
        model = ShippingAddress
        fields = [
            'shipping_name', 
            'shipping_email', 
            'shipping_address', 
            'shipping_phone', 
            'shipping_city', 
            'shipping_state', 
            'shipping_pin_code'
        ]
        exclude = ['user',]