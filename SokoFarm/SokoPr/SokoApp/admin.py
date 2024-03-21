from django.contrib import admin
from .models import Product, Category, Offer, Export

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Offer)
admin.site.register(Export)

# Register your models here.
