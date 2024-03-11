from django import forms
from .models import Product, Category


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
