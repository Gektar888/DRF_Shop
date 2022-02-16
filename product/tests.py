import email
from email.policy import HTTP
from unicodedata import category, name
from urllib import response
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Category,Comment
class ProductTesting(APITestCase):

    def test_get_product(self):
        response = self.client.get('http://127.0.0.1:8000/api/v1/product/')
        self.assertEqual(response.status_code,200)

    def test_post_product(self):
        Category.objects.create(id=1,name='test',slug='test')
        Comment.objects.create(id =1 ,username='c0mrade',email='test@gmail.com',text = 'test')
        product_data = {
            'category' : {
                'id' : 1,
                'name' : 'test',
                'slug' : 'test_1'
            },
            'title' : 'test',
            'slug' : 'test',
            'comment' : 1,
            'likes' : 1,
            'views' : 1,
            'description' : 'test',
            'price' : 1000
        }
        response = self.client.post('http://127.0.0.1:8000/api/v1/product/',product_data,format='json')
        print(response.data)
        self.assertEqual(response.status_code,201)

