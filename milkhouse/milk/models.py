from django.db import models

class Seller(models.Model):
    user = models.CharField(max_length=25)  # This will store a username or other identifier
    mobile_number = models.CharField(max_length=15)  # Field for mobile number
    date_of_selling = models.DateField()
    quantity_litres = models.DecimalField(max_digits=5, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Seller: {self.user}, Mobile: {self.mobile_number}, Date: {self.date_of_selling}"

class Buyer(models.Model):
    user = models.CharField(max_length=25)  # This will store a username or other identifier
    mobile_number = models.CharField(max_length=15)  # Field for mobile number
    date_of_buying = models.DateField()
    quantity_litres = models.DecimalField(max_digits=5, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Buyer: {self.user}, Mobile: {self.mobile_number}, Date: {self.date_of_buying}"
