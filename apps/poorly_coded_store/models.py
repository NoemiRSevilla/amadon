from django.db import models

class Product(models.Model):
    description = models.CharField(max_length=45)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"id: {self.id}, description: {self.description}, price: {self.price}, created_at: {self.created_at}, updated_at: {self.updated_at}"

class Order(models.Model):
    quantity_ordered = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"id: {self.id}, quantity_ordered: {self.quantity_ordered}, total_price: {self.total_price}, created_at: {self.created_at}, updated_at: {self.updated_at}"