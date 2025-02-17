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
    TRANSACTION_TYPES = [
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,default=None,null=True,blank=True)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE,default=None,null=True,blank=True)
    date = models.DateField()
    litres = models.DecimalField(max_digits=5, decimal_places=2,default=0)  
    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPES)
    payment = models.DecimalField(max_digits=10, decimal_places=2,default=0)  
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')  

    def __str__(self):
        return f"Transaction {self.id} - {self.transaction_type} - {self.payment} - {self.status}"
