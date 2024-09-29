from django.contrib import admin
from .models import Seller, Buyer

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'mobile_number', 'date_of_selling', 'quantity_litres', 'cost')

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'mobile_number', 'date_of_buying', 'quantity_litres', 'cost')
