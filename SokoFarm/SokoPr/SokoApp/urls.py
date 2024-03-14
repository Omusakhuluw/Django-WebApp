from django.contrib import admin
from django.urls import path, include
from . import views
from .views import upload_product, fetch_products, vegetables, fruits, potatoes, onions, spices, cereals, birds, feeds, animals


urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', upload_product, name='upload_product'),
    path('shop/', views.shop, name='shop'),
    path('product/<int:product_id>/', views.detail, name='product_detail'),
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
    path('exports/', views.exports, name='exports'),
    path('export_order/', views.export_order, name='export_order'),
    
]