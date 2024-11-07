from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user_email = models.EmailField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('shipped', 'Shipped')])

    def __str__(self):
        return f"Order {self.id} - {self.status}"

