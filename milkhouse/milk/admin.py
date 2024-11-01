

from django.contrib import admin
from .models import Seller, Buyer, Transaction

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'address')
    search_fields = ('name', 'mobile')
    list_filter = ('name',)

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'address')
    search_fields = ('name', 'mobile')
    list_filter = ('name',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'seller', 'buyer', 'litres', 'transaction_type')
    search_fields = ('seller__name', 'buyer__name')
    list_filter = ('transaction_type', 'date')
