from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group as AuthGroup  
from django.contrib.auth.models import Permission as AuthPermission 
from django.contrib.auth.models import User


class ContactMessage(models.Model):
    SUBJECT_CHOICES = [
        ('Enquiry', 'Enquiry'),
        ('Complaint', 'Complaint'),
        ('Complement', 'Complement'),
        ('Refund', 'Refund'),
        
    ]
     
    def __str__(self):
        return self.name

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.message[:20]}'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.subject

class CustomUser(AbstractUser):
    is_farmer = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    is_guest = models.BooleanField(default=False)
    groups = models.ManyToManyField(AuthGroup, related_name='customuser_set', blank=True)  
    user_permissions = models.ManyToManyField(AuthPermission, related_name='customuser_set', blank=True)  
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Category(models.Model):
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

class Order(models.Model):
    CATEGORY_CHOICES = [
        ('Fisheries', 'Fisheries'),
        ('Cereals & Grains', 'Cereals & Grains'),
        ('Vegetables', 'Vegetables'),
        ('Fruits', 'Fruits'),
        ('Potatoes', 'Potatoes'),
        ('Onions', 'Onions'),
        ('Spices', 'Spices'),
        ('Birds & Products', 'Birds & Products'),
        ('Animals & Products', 'Animals & Products'),
        ('Seedlings', 'Seedlings'),
        ('Farm Inputs', 'Farm Inputs'),
        ('Farm Machinery', 'Farm Machinery'),
    ]

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    variety = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    price_range = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    timeframe = models.CharField(max_length=100)
    description = models.TextField()
    additional_info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    contact1 = models.CharField(max_length=15)
    contact2 = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.quantity} {self.category} - {self.location}"

class Export(models.Model):
    CATEGORY_CHOICES = [
        ('Fisheries', 'Fisheries'),
        ('Cereals & Grains', 'Cereals & Grains'),
        ('Vegetables', 'Vegetables'),
        ('Fruits', 'Fruits'),
        ('Potatoes', 'Potatoes'),
        ('Onions', 'Onions'),
        ('Spices', 'Spices'),
        ('Birds & Products', 'Birds & Products'),
        ('Animals & Products', 'Animals & Products'),
        ('Seedlings', 'Seedlings'),
        ('Farm Inputs', 'Farm Inputs'),
        ('Farm Machinery', 'Farm Machinery'),
    ]

    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='exports')  
    image1 = models.ImageField(upload_to='exports/', null=True)
    image2 = models.ImageField(upload_to='exports/', null=True)
    image3 = models.ImageField(upload_to='exports/', null=True)
    subcategory = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.CharField(max_length=15)
    quantity = models.CharField(max_length=20)
    ready_for_purchase = models.BooleanField()
    purchase_timeframe = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    contacts = models.CharField(max_length=15)
    additional_info = models.TextField()
    #category_products = models.ForeignKey('Product', related_name='export_category_products', on_delete=models.CASCADE) 

    def __str__(self):
        return self.name
    

class Offer(models.Model):
    CATEGORY_CHOICES = [
        ('Fisheries', 'Fisheries'),
        ('Cereals & Grains', 'Cereals & Grains'),
        ('Vegetables', 'Vegetables'),
        ('Fruits', 'Fruits'),
        ('Potatoes', 'Potatoes'),
        ('Onions', 'Onions'),
        ('Spices', 'Spices'),
        ('Birds & Products', 'Birds & Products'),
        ('Animals & Products', 'Animals & Products'),
        ('Seedlings', 'Seedlings'),
        ('Farm Inputs', 'Farm Inputs'),
        ('Farm Machinery', 'Farm Machinery'),
    ]

    name = models.CharField(max_length=50)
    description = models.TextField()
    initial_price = models.CharField(max_length=20)
    current_price = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='offers')
    image1 = models.ImageField(upload_to='offers/', null=True)
    image2 = models.ImageField(upload_to='offers/', null=True)
    image3 = models.ImageField(upload_to='offers/', null=True)
    subcategory = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    quantity = models.CharField(max_length=20)
    purchase_timeframe = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    contacts = models.CharField(max_length=15)
    additional_info = models.TextField()

    def __str__(self):
        return self.name