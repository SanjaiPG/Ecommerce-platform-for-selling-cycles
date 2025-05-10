from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
