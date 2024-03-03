from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.template import loader
from .forms import ProductForm
from .models import Product

def home(request):
    latest_products = Product.objects.order_by('-created_at')[:12]
    return render(request, 'home.html', {'latest_products': latest_products})

def about(request):
    return render(request, 'about.html')

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'detail.html', {'product': product})

def shop(request, page=1):
    all_products = Product.objects.all()
    print("Total number of items:", all_products.count())
    
    paginator = Paginator(all_products, 15)  # Display 15 products per page

    try:
        products = paginator.page(page)
        print("Number of items on current page:", len(products))
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

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
