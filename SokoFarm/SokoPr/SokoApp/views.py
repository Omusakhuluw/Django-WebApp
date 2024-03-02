from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import ProductForm
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def about(request):
    return render(request, 'about.html')

def detail(request):
    return render(request, 'detail.html')

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def success(request):
    return render(request, 'success.html')

def exports(request):
    return render(request, 'exports.html')

def orders(request):
    return render(request, 'orders.html')

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})

def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            for image in request.FILES.getlist('images'):
                product.images.create(image=image)
            return redirect('shop') #Redirect to a shop's website' 
    else:
        form = ProductForm()
    return render(request, 'upload_product.html', {'form':form})

def my_view(request):
    Facebook = "https://www.facebook.com/sharer/sharer.php?u"  # Replace with your actual URL
    return render(request, 'home.html', 'about.html', 'detail.html', 'shop.html', 'cart.html', 'checkout.html', 'contact.html', {'https://www.facebook.com/sharer/sharer.php?u': Facebook})

def my_view(request):
    Twitter = "https://twitter.com/intent/tweet?url"  # Replace with your actual URL
    return render(request, 'home.html', 'about.html', 'detail.html', 'shop.html', 'cart.html', 'checkout.html', 'contact.html', {'https://twitter.com/intent/tweet?url': Twitter})

def my_view(request):
    LinkedIn = "https://www.linkedin.com/sharing/share-offsite/?url"  # Replace with your actual URL
    return render(request, 'home.html', 'about.html', 'detail.html', 'shop.html', 'cart.html', 'checkout.html', 'contact.html', {'https://www.linkedin.com/sharing/share-offsite/?url': LinkedIn})

def my_view(request):
    Instagram = "https://www.instagram.com/your_username"  # Replace with your actual URL
    return render(request, 'home.html', 'about.html', 'detail.html', 'shop.html', 'cart.html', 'checkout.html', 'contact.html', {'https://www.instagram.com/your_username': Instagram})




# Create your views here.
