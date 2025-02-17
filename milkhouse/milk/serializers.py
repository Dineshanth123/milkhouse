from rest_framework import serializers
from .models import Seller, Buyer, Transaction

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['id', 'name', 'mobile', 'address']


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ['id', 'name', 'mobile', 'address']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'name','mobile','seller', 'buyer', 'date', 'litres', 'transaction_type','payment','status']
