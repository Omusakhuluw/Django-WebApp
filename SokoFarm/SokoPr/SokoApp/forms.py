from django import forms
from .models import Product
import re

"""class ProductForm(forms.ModelForm):
    contacts = forms.CharField(max_length=15)

    def clean_contacts(delf):
        phone = self.cleaned_data['contacts']

        if not re.match(r'^\d{3}-\d{4}$', phone):
            raise forms.ValidationError("Invalid phone number format. Please use XXX-XXX-XXX format."""
        

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'subcategory', 'image', 'image2', 'image3', 'county', 'price', 'quantity', 'description',
                   'location', 'ready_for_purchase', 'purchase_timeframe', 'contacts']



        