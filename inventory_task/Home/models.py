from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    product_id=models.CharField(max_length=100, primary_key=True)
    product_name=models.CharField(max_length=100)
    product_price=models.IntegerField()

    class Meta:
        managed = True
        db_table = 'Product'

class Location(models.Model):
    location_id = models.CharField(max_length=100, primary_key=True)
    location_name = models.CharField(max_length=100)
    product_balance = models.IntegerField(default=0)
    class Meta:
        managed = True
        db_table = 'Location'

class Product_movement(models.Model):
    movement_id=models.AutoField(primary_key=True)
    timestamp=models.DateTimeField(default=timezone.now)
    from_location=models.CharField(max_length=100, null=True)
    to_location=models.CharField(max_length=100, null=True)
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    class Meta:
        managed = True
        db_table = 'Product_movement'



