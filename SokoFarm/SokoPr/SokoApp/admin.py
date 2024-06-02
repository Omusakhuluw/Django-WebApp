from django.contrib import admin
from .models import Product, Category, Offer, Export, Order, CustomUser, ContactMessage

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Offer)
admin.site.register(Export)
admin.site.register(Order)
admin.site.register(CustomUser)
admin.site.register(ContactMessage)

# Register your models here.
