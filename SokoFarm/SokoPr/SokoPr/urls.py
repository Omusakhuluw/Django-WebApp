"""
URL configuration for SokoPr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from SokoApp import views


urlpatterns = [
    path('', include('SokoApp.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'),
    path('detail/', views.detail, name='detail'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('upload_product/', views.upload_product, name='upload_product'),
    path('success/', views.success, name='success'),
    path('exports/', views.exports, name='exports'),
    path('orders/', views.orders, name='orders'),
    path('product/<int:product_id>/', views.detail, name='detail'),
    path('offers/', views.offers, name='offers'),
    path('featured_products/', views.featured_products, name='featured_products'),
    path('vegetables/', views.vegetables, name='vegetables'),
    path('fruits/', views.fruits, name='fruits'),
    path('potatoes/', views.potatoes, name='potatoes'),
    path('spices/', views.spices, name='spices'),
    path('onions/', views.onions, name='onions'),
    path('seedlings/', views.seedlings, name='seedlings'),
    path('animals/', views.animals, name='animals'),
    path('birds/', views.birds, name='birds'),
    path('cereals/', views.cereals, name='cereals'),
    path('farm_machinery/', views.farm_machinery, name='farm_machinery'),
    path('farm_inputs/', views.farm_inputs, name='farm_inputs'),
    path('feeds/', views.feeds, name='feeds'),
    path('recent_products/', views.recent_products, name='recent_products'),
    path('category_view/', views.category_view, name='category_view'),
    path('orders/', views.orders, name='orders'),
    path('create_order/', views.create_order, name='create_order'),
    path('upload_exports/', views.upload_exports, name='upload_exports'),
    path('exports/<int:export_id>/', views.exports, name='exports'),
    #path('export_order/', export_order, name='export_order'),
    path('upload_offers/', views.upload_offers, name='upload_offers'),
    path('offers/<int:export_id>/', views.offers, name='offers'),
    path('offers/<int:offer_id>/', views.offers, name='offers'),
    path('offers/<int:offer_id>/', views.offer_detail, name='offer_detail'),
    path('farmer/', views.farmer_dashboard, name='farmer_dashboard'),
    path('buyer/', views.buyer_dashboard, name='buyer_dashboard'),
    path('guest/', views.guest_dashboard, name='guest_dashboard'),
    
    
    

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)