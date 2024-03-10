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

#def home(request):
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
            category_name = form.cleaned_data['category']
            product = form.save()

            print("Product uploaded successfully!:", product.name)

            for image in request.FILES.getlist('images'):
                product.images.create(image=image)
            return redirect('shop')
    else:
        form = ProductForm()
    return render(request, 'upload_product.html', {'form':form})

#def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            category_name = form.cleaned_data['category']
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

def farm_machinery(request):
    farmmachinery_category = get_object_or_404(Category, name='Farm Machinery')
    farmmachinery_products = Product.objects.filter(category=farmmachinery_category)
    return render(request, 'farm_machinery.html', {'products': farmmachinery_products})

def farm_inputs(request):
    farminputs_category = get_object_or_404(Category, name='Farm Inputs')
    farminputs_products = Product.objects.filter(category=farminputs_category)
    return render(request, 'farm_inputs.html', {'products': farminputs_products})

def animals(request):
    animals_category = get_object_or_404(Category, name='Animals')
    animals_products = Product.objects.filter(category=animals_category)
    return render(request, 'animals.html', {'products': animals_products})

def birds(request):
    # Retrieve all Category objects with the name 'Birds'
    birds_categories = Category.objects.filter(name='Birds')
    
    # Check if any Category objects are found
    if birds_categories.exists():
        # Choose one of the Category objects (e.g., the first one)
        birds_category = birds_categories.first()
        
        # Retrieve all Product objects associated with the chosen category
        birds_products = Product.objects.filter(category=birds_category)
        
        return render(request, 'birds.html', {'products': birds_products})
    else:
        # Handle the case where no Category objects are found
        return HttpResponse("Birds category not found")
    
    
def cereals(request):
    cereals_category = get_object_or_404(Category, name='Cereals')
    cereals_products = Product.objects.filter(category=cereals_category)
    return render(request, 'cereals.html', {'products': cereals_products})

def featured_products(request):
    return render(request, 'featured_products.html')

def fruits(request):
    fruits_category = get_object_or_404(Category, name='Fruits')
    fruits_products = Product.objects.filter(category=fruits_category)
    return render(request, 'fruits.html', {'products': fruits_products})

def onions(request):
    onions_category = get_object_or_404(Category, name='Onions')
    onions_products = Product.objects.filter(category=onions_category)
    return render(request, 'onions.html', {'products': onions_products})

def potatoes(request):
    potatoes_category = get_object_or_404(Category, name='Potatoes')
    potatoes_products = Product.objects.filter(category=potatoes_category)
    return render(request, 'potatoes.html', {'products': potatoes_products})

def seedlings(request):
    seedlings_category = get_object_or_404(Category, name='Seedlings')
    seedlings_products = Product.objects.filter(category=seedlings_category)
    return render(request, 'seedlings.html', {'products': seedlings_products})

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
