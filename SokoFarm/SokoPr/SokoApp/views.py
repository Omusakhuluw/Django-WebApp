from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse
from .forms import ProductForm, OrderForm, Order, ExportForm, OfferForm, Offer, Export
from .models import Product, Category, Offer
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Ensure user is not None before calling login()
            return redirect('home')  # Redirect to the homepage after successful login
        else:
            # Invalid login
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('login')  # Redirect back to the login page with error message
    else:
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def farmer_dashboard(request):
    if not request.user.is_farmer:
        return HttpResponseForbidden("You don't have permission to access this page.")
    # Render farmer dashboard

@login_required
def buyer_dashboard(request):
    if not request.user.is_buyer:
        return HttpResponseForbidden("You don't have permission to access this page.")
    # Render buyer dashboard

def guest_dashboard(request):
    if request.user.is_authenticated:
        return HttpResponseForbidden("You are already logged in.")
    # Render guest dashboard



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


def search_products(request):
    query = request.GET.get('q')
    if query:
        # Perform the search query on the Product model
        search_results = Product.objects.filter(name__icontains=query)
    else:
        search_results = None
    
    return render(request, 'shop.html', {'search_results': search_results, 'query': query})

def add_to_cart(request):
    product_id = request.POST.get('product_id')
    # Logic to add product to cart
    return JsonResponse({'message': 'Product added to cart'})

def add_to_favorites(request):
    product_id = request.POST.get('product_id')
    # Logic to add product to favorites
    return JsonResponse({'message': 'Product added to favorites'})

def sync_product(request):
    product_id = request.POST.get('product_id')
    # Logic to sync product
    return JsonResponse({'message': 'Product synced'})

def shop(request):
    latest_products = Product.objects.order_by('-created_at')  # Order products by created_at in descending order
    return render(request, 'shop.html', {'latest_products': latest_products})


#def offers(request):
    latest_offers = Offer.objects.order_by('-created_at')
    return render(request, 'offers.html', {'latest_offers': latest_offers})

def offers(request):
    latest_offers = Offer.objects.order_by('-created_at')  # Order offers by created_at in descending order
    return render(request, 'offers.html', {'latest_offers': latest_offers})

def upload_offers(request):
    if request.method == 'POST':
        form = OfferForm(request.POST, request.FILES)
        if form.is_valid():
            new_offer = form.save(commit=False)
            new_offer.user = request.user  # Associate the logged-in user with the offer
            new_offer.save()
            return redirect('offers')  # Redirect to the offers page after successful upload
    else:
        form = OfferForm()
    return render(request, 'upload_offers.html', {'form': form})

def upload_exports(request):
    if request.method == 'POST':
        form = ExportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('exports')  
    else:
        form = ExportForm()
    return render(request, 'upload_exports.html', {'form': form})


def offer_detail(request, offer_id):
    # Retrieve the offer object by its ID
    offer = get_object_or_404(Offer, pk=offer_id)
    return render(request, 'offer_detail.html', {'offer': offer})


def export_detail(request, export_id):
    # Retrieve the offer object by its ID
    export = get_object_or_404(Offer, pk=export_id)
    return render(request, 'export_detail.html', {'export': export})


def about(request):
    return render(request, 'about.html')


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'detail.html', {'product': product})


def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.user = request.user  # Associate the logged-in user with the product
            new_product.save()
            return redirect('product_detail', product_id=new_product.id)  
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


def orders(request):
    return render(request, 'orders.html')



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


#def recent_products(request):
    recent_products = Product.objects.order_by('-created_at')[:12]  # Get the latest 12 products
    return render(request, 'recent_products.html', {'recent_products': recent_products})

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


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')  # Redirect to the orders page after successful submission
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})


def orders(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})

def export_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('export_order')  # Redirect to the orders page after successful submission
    else:
        form = OrderForm()
    return render(request, 'export_order.html', {'form': form})

#def upload_exports(request):
    if request.method == 'POST':
        form = ExportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exports')  
    else:
        form = ExportForm()
    return render(request, 'upload_exports.html', {'form': form})


def exports(request):
    latest_exports = Export.objects.order_by('-created_at')  
    return render(request, 'exports.html', {'latest_exports': latest_exports})


#def upload_exports(request):
    #if request.method == 'POST':
        #form = ExportsForm(request.POST, request.FILES)
        #if form.is_valid():
            #new_product = form.save(commit=False)
            #new_product.user = request.user  # Associate the logged-in user with the product
            #new_product.save()
            #return redirect('exports', product_id=new_product.id)  


#def upload_exports(request):
    #if request.method == 'POST':
        #form = ExportsForm(request.POST, request.FILES)
        #if form.is_valid():
            #new_product = form.save(commit=False)
            #new_product.user = request.user  # Associate the logged-in user with the product
            #new_product.save()
            #return redirect('exports', product_id=new_product.id)  

#def exports(request):
    exports = Order.objects.all()
    return render(request, 'exports.html', {'exports': exports})
