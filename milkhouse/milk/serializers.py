from rest_framework import serializers
from .models import Seller, Buyer, Transaction

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['id', 'user', 'mobile_number']

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ['id', 'user', 'mobile_number']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'user', 'transaction_type', 'date', 'quantity_litres', 'cost']
