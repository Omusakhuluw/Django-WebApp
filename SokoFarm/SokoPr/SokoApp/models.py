from django.db import models
from django.utils import timezone


class Category(models.Model):
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
    name = models.CharField(max_length=50)
     
    def __str__(self):
        return self.name
    

class Product(models.Model): 
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')   
    image1 = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/')
    image3 = models.ImageField(upload_to='products/')
    subcategory = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.CharField(max_length=15)
    quantity = models.CharField(max_length=20)
    ready_for_purchase = models.BooleanField()
    purchase_timeframe = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    contacts = models.CharField(max_length=15)
    additional_info = models.TextField()

    def __str__(self):
        return self.name
