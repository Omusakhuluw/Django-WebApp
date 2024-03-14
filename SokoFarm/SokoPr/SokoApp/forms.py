from django import forms
from .models import Product, Category, Order, Exports


class ProductForm(forms.ModelForm):
    CATEGORY_CHOICES = [
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
    
    category = forms.ModelChoiceField(queryset=Category.objects.all())  # Use ModelChoiceField for category

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


class ExportsForm(forms.ModelForm):
    class Meta:
        model = Exports
        fields = ['name', 'category', 'subcategory', 'image1', 'image2', 'image3', 'price', 'quantity', 'ready_for_purchase', 'purchase_timeframe',
                  'location', 'description', 'additional_info', 'contacts',]
        exclude = ['created_at']