from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
   return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def detail(request):
    return render(request, 'detail.html')

def shop(request):
    return render(request, 'shop.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')

# Create your views here.
