from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.template import loader
from .forms import ProductForm
from .models import Product, Category
from django.http import JsonResponse
from django.urls import reverse


def home(request):
    latest_products = Product.objects.order_by('-created_at')[:12]
    return render(request, 'home.html', {'latest_products': latest_products})

def home(request):
    categories = ['Vegetables', 'Fruits', 'Potatotes', 'Cereals', 'Onions', 'Spices', 'Birds', 'Animals', 'Feeds', 'Seedlings', 'Farm Inputs', 'Farm Machinery' ]
    context = {
        'categories': categories,
    }
    return render(request, 'home.html', context)

def category_view(request, category):
    products = Product.objects.filter(category=category)
    context = {
        'products': products,
        'category': category,
    }
    return render(request, 'category_view.html', context)

# def shop(request):
    latest_products = Product.objects.order_by('-created_at')[:20]
    return render(request, 'shop.html', {'latest_products': latest_products})

def about(request):
    return render(request, 'about.html')

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'detail.html', {'product': product})

def shop(request, page=1):
    all_products = Product.objects.all()
    print("Total number of items:", all_products.count())
    
    paginator = Paginator(all_products, 20)  # Display 20 products per page

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

            print("Product uploaded successfully!:", product.name)

            
            for image in request.FILES.getlist('images'):
                product.images.create(image=image)
            return redirect('shop')
        
            category_pages = ['home', 'shop', 'vegetables', 'fruits', 'potatoes', 'cereals', 'onions', 'spices', 'birds', 'animals', 'feeds', 'seedlings', 'farm_inputs', 'farm_machinery']

            for page in category_pages:
                redirect_url = reverse(page)
                print("Redirecting to:", redirect_url)
                return redirect(redirect_url)
    else:
        form = ProductForm()
    return render(request, 'upload_product.html', {'form':form})

def offers(request):
    return render(request, 'offers.html')

def animals(request):
    products = Product.objects.filter(category='animals')
    return render(request, 'animals.html', {'products': products})

def birds(request):
    products = Product.objects.filter(category='birds')
    return render(request, 'birds.html', {'products': products})

def cereals(request):
    products = Product.objects.filter(category='cereals')
    return render(request, 'cereals.html', {'products': products})

def farm_inputs(request):
    products = Product.objects.filter(category='farm_input')
    return render(request, 'farm_input.html', {'products': products})

def farm_machinery(request):
    products = Product.objects.filter(category='farm_machinery')
    return render(request, 'farm_machinery.html', {'products': products})

def featured_products(request):
    return render(request, 'featured_products.html')

def fruits(request):
    products = Product.objects.filter(category='fruits')
    return render(request, 'fruits.html', {'products': products})

def onions(request):
    products = Product.objects.filter(category='onions')
    return render(request, 'onions.html', {'products': products})

def potatoes(request):
    products = Product.objects.filter(category='potatoes')
    return render(request, 'potatoes.html', {'products': products})

def seedlings(request):
    products = Product.objects.filter(category='seedlings')
    return render(request, 'seedlings.html', {'products': products})

def spices(request):
    spices_category = get_object_or_404(Category, name='Spices')
    spices_products = Product.objects.filter(category=spices_category)
    return render(request, 'spices.html', {'products': spices_products})

def vegetables(request):
    vegetables_category = get_object_or_404(Category, name='Vegetables')
    vegetables_products = Product.objects.filter(category=vegetables_category)
    return render(request, 'vegetables.html', {'products': vegetables_products})

def feeds(request):
    feeds_category = get_object_or_404(Category, name='Feeds')
    feeds_products = Product.objects.filter(category=feeds_category)
    return render(request, 'feeds.html', {'products': feeds_products})

def recent_products(request):
    return render(request, 'recent_products.html')



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

def fetch_products(request):
    categories = request.GET.getlist('categories[]')
    products = Product.objects.filter(category__in=categories).values('name')
    return JsonResponse({'products': list(products)})

# def fruits_view(request):
    vegetables = Product.objects.filter(category='vegetables')
    return render(request, 'vegetables.html', {'vegetables': vegetables})

# def potatoes_view(request):
    vegetables = Product.objects.filter(category='vegetables')
    return render(request, 'vegetables.html', {'vegetables': vegetables})

# def cereals_view(request):
    vegetables = Product.objects.filter(category='vegetables')
    return render(request, 'vegetables.html', {'vegetables': vegetables})

# def onions_view(request):
    vegetables = Product.objects.filter(category='vegetables')
    return render(request, 'vegetables.html', {'vegetables': vegetables})

# def spices_view(request):
    vegetables = Product.objects.filter(category='vegetables')
    return render(request, 'vegetables.html', {'vegetables': vegetables})

# def birds_view(request):
    vegetables = Product.objects.filter(category='vegetables')
    return render(request, 'vegetables.html', {'vegetables': vegetables})

# def animals_view(request):
    vegetables = Product.objects.filter(category='vegetables')
    return render(request, 'vegetables.html', {'vegetables': vegetables})

# def feeds_view(request):
    vegetables = Product.objects.filter(category='vegetables')
    return render(request, 'vegetables.html', {'vegetables': vegetables})

# def sugarcane_view(request):
    vegetables = Product.objects.filter(category='vegetables')
    return render(request, 'vegetables.html', {'vegetables': vegetables})

# def seedlings_view(request):
    vegetables = Product.objects.filter(category='vegetables')
    return render(request, 'vegetables.html', {'vegetables': vegetables})

# def chicks_view(request):
    vegetables = Product.objects.filter(category='chicks')
    return render(request, 'chicks.html', {'chicks': chicks})


# Create your views here.
