from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
    )
    username = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password1 = forms.CharField(
        label="", 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        label="", 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        # Removing the help texts
        self.fields['username'].help_text = None
        self.fields['email'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None


class UpdateUserForm(UserChangeForm):
    email = forms.EmailField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
    )
    first_name = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), required=False
    )
    last_name = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), required=False
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        
        # Removing the help texts
        self.fields['first_name'].help_text = None
        self.fields['last_name'].help_text = None
        self.fields['email'].help_text = None

class UpdatePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="", 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'})
    )
    new_password2 = forms.CharField(
        label="", 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = User
        fields = ('new_password1', 'new_password2')
    
class UserInfoForm(forms.ModelForm):
    phone = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'})
    )
    Address = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'})
    )
    city = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'})
    )
    state = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'})
    )
    pin_code = forms.CharField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pin Code'})
    )

    class Meta:
        model = Profile
        fields = ('phone', 'Address', 'city', 'state', 'pin_code')