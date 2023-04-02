from django.db import models

# Create your models here.

class Product(models.Model):
    name_of_product = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    details = models.TextField()
    manufactured_by= models.TextField()
    quantity_left_in_stock = models.IntegerField()
    quantity_sold = models.IntegerField()
    product_reviews = models.CharField(max_length=200, null=True)
    image = models.CharField(max_length=5000, null=True, blank=True)