from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse
from .forms import ProductForm
from .models import Product, Category


def home(request):
    latest_products = Product.objects.order_by('-created_at')[:12]
    categories = Category.objects.all()  # Fetch all categories
    return render(request, 'home.html', {'latest_products': latest_products, 'categories': categories})


def category_view(request, category):
    category_instance = get_object_or_404(Category, name=category)
    products = Product.objects.filter(category=category_instance)
    context = {
        'products': products,
        'category': category_instance,
    }
    return render(request, 'category_view.html', context)


def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})


def about(request):
    return render(request, 'about.html')


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'detail.html', {'product': product})


def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            category_name = form.cleaned_data['category']
            category_instance = Category.objects.get(name=category_name)
            product.category = category_instance
            product.save()
            return redirect('shop')
    else:
        form = ProductForm()
    return render(request, 'upload_product.html', {'form': form})


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


def offers(request):
    return render(request, 'offers.html')


def farm_machinery(request):
    farmmachinery_category = get_object_or_404(Category, name='Farm Machinery')
    farmmachinery_products = Product.objects.filter(category=farmmachinery_category)
    return render(request, 'farm_machinery.html', {'products': farmmachinery_products})


def farm_inputs(request):
    farminputs_category = get_object_or_404(Category, name='Farm Inputs')
    farminputs_products = Product.objects.filter(category=farminputs_category)
    return render(request, 'farm_inputs.html', {'products': farminputs_products})

def vegetables(request):
    vegetables_category = get_object_or_404(Category, name='Vegetables')
    vegetables_products = Product.objects.filter(category=vegetables_category)
    return render(request, 'vegetables.html', {'products': vegetables_products})

def fruits(request):
    fruits_category = get_object_or_404(Category, name='Fruits')
    fruits_products = Product.objects.filter(category=fruits_category)
    return render(request, 'fruits.html', {'products': fruits_products})

def potatoes(request):
    potatoes_category = get_object_or_404(Category, name='Potatoes')
    potatoes_products = Product.objects.filter(category=potatoes_category)
    return render(request, 'potatoes.html', {'products': potatoes_products})

def cereals(request):
    cereals_category = get_object_or_404(Category, name='Cereals')
    cereals_products = Product.objects.filter(category=cereals_category)
    return render(request, 'cereals.html', {'products': cereals_products})

def onions(request):
    onions_category = get_object_or_404(Category, name='Onions')
    onions_products = Product.objects.filter(category=onions_category)
    return render(request, 'onions.html', {'products': onions_products})

def spices(request):
    spices_category = get_object_or_404(Category, name='Spices')
    spices_products = Product.objects.filter(category=spices_category)
    return render(request, 'spices.html', {'products': spices_products})

def birds(request):
    birds_category = get_object_or_404(Category, name='Birds')
    birds_products = Product.objects.filter(category=birds_category)
    return render(request, 'birds.html', {'products': birds_products})

def animals(request):
    animals_category = get_object_or_404(Category, name='Animals')
    animals_products = Product.objects.filter(category=animals_category)
    return render(request, 'animals.html', {'products': animals_products})

def feeds(request):
    feeds_category = get_object_or_404(Category, name='Feeds')
    feeds_products = Product.objects.filter(category=feeds_category)
    return render(request, 'feeds.html', {'products': feeds_products})

def seedlings(request):
    seedlings_category = get_object_or_404(Category, name='Seedlings')
    seedlings_products = Product.objects.filter(category=seedlings_category)
    return render(request, 'seedlings.html', {'products': seedlings_products})



def fetch_products(request):
    categories = request.GET.getlist('categories[]')
    products = Product.objects.filter(category__in=categories).values('name')
    return JsonResponse({'products': list(products)})


def recent_products(request):
    return render(request, 'recent_products.html')

def featured_products(request):
    return render(request, 'featured_products.html')


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



def birds(request):
    birds_categories = Category.objects.filter(name='Birds')
    if birds_categories.exists():
        birds_category = birds_categories.first()
        birds_products = Product.objects.filter(category=birds_category)
        return render(request, 'birds.html', {'products': birds_products})
    else:
        return HttpResponse("Birds category not found")


def feeds(request):
    feeds_category = get_object_or_404(Category, name='Feeds')
    feeds_products = Product.objects.filter(category=feeds_category)
    return render(request, 'feeds.html', {'products': feeds_products})


def seedlings(request):
    seedlings_category = get_object_or_404(Category, name='Seedlings')
    seedlings_products = Product.objects.filter(category=seedlings_category)
    return render(request, 'seedlings.html', {'products': seedlings_products})


def recent_products(request):
    return render(request, 'recent_products.html')

