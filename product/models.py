from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=25,db_index=True)
    description = models.TextField()
    price = models.IntegerField()
    # image = models.ImageField( upload_to='image/%Y/%m/%d',blank=True) 
    created_date = models.DateField(auto_now=True)
    rating = models.IntegerField()
    
