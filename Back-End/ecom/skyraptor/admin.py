from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Category, Product, Customer, Order, Profile

# Register models normally
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Profile)

# Inline for Profile model
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

# Extend default UserAdmin and include Profile inline
class CustomUserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

# Unregister default User admin and register customized one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
