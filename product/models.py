from statistics import mode
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=25,db_index=True)
    description = models.TextField()
    price = models.IntegerField()
    # image = models.ImageField( upload_to='image/%Y/%m/%d',blank=True) 
    created_date = models.DateField(auto_now=True)
    rating = models.IntegerField()
    

class Customer(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    comment = models.CharField(max_length=500)
    address = models.CharField(max_length=100)
    number = models.CharField(max_length=12)
