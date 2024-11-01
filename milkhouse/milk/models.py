

from django.db import models

class Seller(models.Model):
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name} ({self.mobile})" 


class Buyer(models.Model):
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name} ({self.mobile})"


class Transaction(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True, blank=True)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    litres = models.FloatField(default=0.0)

    transaction_type = models.CharField(max_length=10)  
    def __str__(self):
        return f"Transaction on {self.date} - {self.transaction_type}"
