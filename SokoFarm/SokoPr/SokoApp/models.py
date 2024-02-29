from django.db import models

class MyModel(models.Model):
    image = models.ImageField(upload_to='img/')

class Category(models.Model):
    name = models.CharField(max_length=100)

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Product(models.Model): 
    name = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/')
    image3 = models.ImageField(upload_to='products/')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    county = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    ready_for_purchase = models.BooleanField()
    purchase_timeframe = models.PositiveIntegerField()
    contacts = models.CharField(max_length=15)


# Create your models here.
