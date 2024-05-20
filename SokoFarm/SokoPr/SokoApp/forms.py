from django import forms
from .models import Product, Category, Order, Offer, Export, CustomUser


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'is_farmer']


class ProductForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('Fisheries', 'Fisheries'),
        ('Vegetables', 'Vegetables'),
        ('Fruits', 'Fruits'),
        ('Potatoes', 'Potatoes'),
        ('Cereals', 'Cereals'),
        ('Onions', 'Onions'),
        ('Spices', 'Spices'),
        ('Birds', 'Birds & Products'),
        ('Animals', 'Animals & Products'),
        ('Feeds', 'Feeds'),
        ('Seedlings', 'Seedlings'),
        ('Farm Inputs', 'Farm Inputs'),
        ('Farm Machinery', 'Farm Machinery'),
    ]
    
    category = forms.ModelChoiceField(queryset=Category.objects.all())  

    class Meta:
        model = Product
        fields = ['name', 'category', 'subcategory', 'image1', 'image2', 'image3', 'price', 'quantity', 'ready_for_purchase', 'purchase_timeframe',
                  'location', 'description', 'additional_info', 'contacts',]
        exclude = ['created_at']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'category', 'variety', 'quantity', 'price_range', 'location', 'timeframe', 'description', 'additional_info', 'contact1', 'contact2']
        exclude = ['created_at']


class ExportForm(forms.ModelForm):
    class Meta:
        model = Export
        fields = ['name', 'category', 'subcategory', 'image1', 'image2', 'image3', 'price', 'quantity', 'ready_for_purchase', 'purchase_timeframe',
                  'location', 'description', 'additional_info', 'contacts',]
        exclude = ['created_at']

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['name', 'category', 'subcategory', 'image1', 'image2', 'image3', 'quantity', 'initial_price', 'current_price', 'purchase_timeframe',
                  'location', 'description', 'additional_info', 'contacts',]
        exclude = ['created_at']
