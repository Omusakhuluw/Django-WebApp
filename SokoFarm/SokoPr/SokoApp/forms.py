from django import forms
from .models import Product, Category, Order, Offer, Export, CustomUser, Contact
from .models import ContactMessage
import re



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
                  'location', 'description', 'additional_info', 'contacts']
        exclude = ['created_at']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price:
            # Remove commas
            price = re.sub(r',', '', str(price))
            try:
                # Convert to float
                price = float(price)
            except (ValueError, TypeError):
                raise forms.ValidationError("Invalid price format")
        return price


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'category', 'variety', 'quantity', 'price_range', 'location', 'timeframe', 'description', 'additional_info', 'contact1', 'contact2']
        exclude = ['created_at']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price:
            # Remove commas
            price = re.sub(r',', '', str(price))
            try:
                # Convert to float
                price = float(price)
            except (ValueError, TypeError):
                raise forms.ValidationError("Invalid price format")
        return price


class ExportForm(forms.ModelForm):
    class Meta:
        model = Export
        fields = ['name', 'category', 'subcategory', 'image1', 'image2', 'image3', 'price', 'quantity', 'ready_for_purchase', 'purchase_timeframe',
                  'location', 'description', 'additional_info', 'contacts',]
        exclude = ['created_at']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price:
            # Remove commas
            price = re.sub(r',', '', str(price))
            try:
                # Convert to float
                price = float(price)
            except (ValueError, TypeError):
                raise forms.ValidationError("Invalid price format")
        return price

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['name', 'category', 'subcategory', 'image1', 'image2', 'image3', 'quantity', 'initial_price', 'current_price', 'purchase_timeframe',
                  'location', 'description', 'additional_info', 'contacts',]
        exclude = ['created_at']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price:
            # Remove commas
            price = re.sub(r',', '', str(price))
            try:
                # Convert to float
                price = float(price)
            except (ValueError, TypeError):
                raise forms.ValidationError("Invalid price format")
            
            # Ensure the price is within a reasonable range
            if price <= 0 or price > 100000000:  # You can adjust the upper limit as needed
                raise forms.ValidationError("Price must be between 1 and 100,000,000")
        return price

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

"""class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']"""


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'location', 'subject', 'message', ]