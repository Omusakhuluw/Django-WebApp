from django.contrib import admin
from django.urls import path, include
from . import views
from .views import upload_product

urlpatterns = [
    path('', views.home, name='home'),
    path('upload_product/', upload_product, name='upload_product'),
      
]