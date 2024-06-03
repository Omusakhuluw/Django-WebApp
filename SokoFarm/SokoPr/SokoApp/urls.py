from django.contrib import admin
from django.urls import path, include
from . import views
from .views import upload_product, fetch_products, fisheries, vegetables, fruits, potatoes, onions, spices, cereals, birds, feeds, animals, upload_offers, user_login
from .views import contact_view, contact_success_view, delete_from_cart


urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', upload_product, name='upload_product'),
    path('shop/', views.shop, name='shop'),
    path('product/<int:product_id>/', views.detail, name='product_detail'),
    path('product/<int:product_id>/', views.detail, name='detail'),
    path('shop/<int:page>/', views.shop, name='shop_with_page'),
    path('fetch-products/', fetch_products, name='fetch_products'),
    path('category/<str:category>/', views.category_view, name='category_view'),

    path('search/', views.search_products, name='search_products'),
    
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add-to-favorites/<int:product_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('sync-product/<int:product_id>/', views.sync_product, name='sync_product'),
    path('category/vegetables/', views.vegetables, name='vegetables'),
    path('category/fruits/', views.fruits, name='fruits'),
    path('category/potatoes/', views.potatoes, name='potatoes'),
    path('category/cereals/', views.cereals, name='cereals'),
    path('category/onions/', views.onions, name='onions'),
    path('category/spices/', views.spices, name='spices'),
    path('category/birds/', views.birds, name='birds'),
    path('category/animals/', views.animals, name='animals'),
    path('category/feeds/', views.feeds, name='feeds'),
    path('category/seedlings/', views.seedlings, name='seedlings'),
    path('category/farm_inputs/', views.farm_inputs, name='farm_inputs'),
    path('category/farm_machinery/', views.farm_machinery, name='farm_machinery'),
    path('create_order/', views.create_order, name='create_order'),
    path('orders/', views.orders, name='orders'),
    path('upload_exports/', views.upload_exports, name='upload_exports'),
    path('exports/<int:export_id>/', views.exports, name='exports'),
    path('export_order/', views.export_order, name='export_order'),
    path('offers/', views.offers, name='offers'),  # Updated path
    path('upload_offers/', views.upload_offers, name='upload_offers'),
    path('offers/<int:offer_id>/', views.offer_detail, name='offer_detail'),
    path('farmer/', views.farmer_dashboard, name='farmer_dashboard'),
    path('buyer/', views.buyer_dashboard, name='buyer_dashboard'),
    path('guest/', views.guest_dashboard, name='guest_dashboard'),
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', user_login, name='user_login'),
    path('category/fisheries/', views.fisheries, name='fisheries'),
    path('contact/', contact_view, name='contact'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', views.contact_success_view, name='success'),
    path('delete-from-cart/', delete_from_cart, name='delete_from_cart'),
]