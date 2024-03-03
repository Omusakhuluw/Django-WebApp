from django.db import models
from django.utils import timezone
from django import forms

class MyModel(models.Model):
    image = models.ImageField(upload_to='img/')

class Category(models.Model):
    name = models.CharField(max_length=100)

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Product(models.Model): 
    category_choices = (
        ('electronics', 'Electronics'),
        ('clothing', 'Clothing'),
        # Add more category choices as needed
    )
    subcategory_choices = (
        ('phone', 'Phone'),
        ('laptop', 'Laptop'),
        # Add more sub-category choices as needed
    )
    county_choices = (
        ('nairobi', 'Nairobi'),
        ('mombasa', 'Mombasa'),
        # Add more county choices as needed
    )
    country_choices = (
        ('kenya', 'Kenya'),
        ('uganda', 'Uganda'),
        # Add more country choices as needed
    )

    name = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/')
    image3 = models.ImageField(upload_to='products/')
    description = models.TextField(default='')
    additional_info = models.TextField(default='')
    subcategory = models.CharField(max_length=100)
    category = forms.ChoiceField(choices=category_choices)
    location = models.CharField(max_length=100)
    county = forms.ChoiceField(choices=county_choices)
    country = forms.ChoiceField(choices=country_choices)
    price = models.CharField(max_length=10)
    quantity = models.CharField(max_length=50)
    ready_for_purchase = models.BooleanField()
    purchase_timeframe = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)  # Automatically set to the current date and time on creation
    contacts = models.CharField(max_length=15)

def __str__(self):
    return self.name


# Create your models here.
