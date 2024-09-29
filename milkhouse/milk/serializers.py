from rest_framework import serializers
from .models import Seller, Buyer

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['id', 'user', 'mobile_number', 'date_of_selling', 'quantity_litres', 'cost']

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ['id', 'user', 'mobile_number', 'date_of_buying', 'quantity_litres', 'cost']
