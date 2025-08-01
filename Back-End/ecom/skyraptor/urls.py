from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_user/', views.update_user, name='update_user'),
    path('update_info/', views.update_info, name='update_info'),
    path('update_password/', views.update_password, name='update_password'),
    path('product_view/<int:pk>/', views.product_view, name='product_view'),
    path('category/<str:foo>', views.category, name='category'),
    path('user_order/', views.user_order, name='user_order'),
    path('home_order_views/<int:pk>', views.home_order_views, name='home_order_views'),
]
