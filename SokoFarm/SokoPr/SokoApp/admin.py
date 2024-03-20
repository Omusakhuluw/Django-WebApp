from django.contrib import admin
from .models import Product, Category, Offer, Exports

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Offer)
admin.site.register(Exports)

# Register your models here.
