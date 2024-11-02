from django import forms
from .models import Seller, Buyer

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['name', 'mobile', 'address']

class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['name', 'mobile', 'address']
