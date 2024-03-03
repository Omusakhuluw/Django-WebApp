from django.contrib import admin
from django.urls import path, include
from . import views
from .views import upload_product

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', upload_product, name='upload_product'),
    path('shop/', views.shop, name='shop'),
    path('product/<int:product_id>/', views.detail, name='detail'),
    path('shop/<int:page>/', views.shop, name='shop_with_page'),
      
]