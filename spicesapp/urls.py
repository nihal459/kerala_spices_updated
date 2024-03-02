from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('user_reg', views.user_reg, name='user_reg'),
    path('user_log', views.user_log, name='user_log'),
    path('spices_login', views.spices_login, name='spices_login'),
    path('SignOut', views.SignOut, name='SignOut'),
    path('spices_home', views.spices_home, name='spices_home'),
    path('SignOut2', views.SignOut2, name='SignOut2'),
    path('spices_category', views.spices_category, name='spices_category'),
    path('delete_category/<int:pk>/', views.delete_category, name='delete_category'),
    path('edit_category/<int:pk>/', views.edit_category, name='edit_category'),
    path('spices_product', views.spices_product, name='spices_product'),
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
    path('shop', views.shop, name='shop'),
    path('single_product/<int:pk>/', views.single_product, name='single_product'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart', views.cart, name='cart'),
    path('product_remove_cart/<int:pk>/', views.product_remove_cart, name='product_remove_cart'),
    path('about_us', views.about_us, name='about_us'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('update_cart_quantity', views.update_cart_quantity, name='update_cart_quantity'),
    path('checkout', views.checkout, name='checkout'),
    path('order_placed', views.order_placed, name='order_placed'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('user_orders', views.user_orders, name='user_orders'),
    path('view_products/<int:pk>/', views.view_products, name='view_products'),
    path('add_to_cart2', views.add_to_cart2, name='add_to_cart2'),
    path('view_order_products/<int:pk>/', views.view_order_products, name='view_order_products'),
    path('spices_orders', views.spices_orders, name='spices_orders'),
    path('update_order/<int:pk>/', views.update_order, name='update_order'),
    path('delete_order/<int:pk>/', views.delete_order, name='delete_order'),
    path('customer_details', views.customer_details, name='customer_details'),
    path('delete_order2/<int:pk>/', views.delete_order2, name='delete_order2'),
    path('category_products/<int:pk>/', views.category_products, name='category_products'),
    path('contact_forms', views.contact_forms, name='contact_forms'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),




]