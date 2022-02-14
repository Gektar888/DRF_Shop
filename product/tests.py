from http import client
from itertools import product
from urllib import response
from django.urls import path, reverse, include, resolve
from django.test import SimpleTestCase
from .models import Customer
from product.models import Customer
from .views import ProductView
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.views import APIView


class ApiUrlsTests(SimpleTestCase):

    def test_get_product_is_resolved(self):
        url = reverse('product')
        self.assertEquals(resolve(url).func.view_class, ProductView)


class ProductAPIViewTests(APITestCase):
    product = reverse("product")

    def setUp(self):
        self.user = User.objects.create_user(
            username='admin', password='admin')
        self.token = Token.objects.create(user=self.user)
        #self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_customers_authenticated(self):
        response = self.client.get(self.product)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_customers_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.product)
        self.assertEquals(response.status_code, 401)

    

class ProductDetailAPIViewTests(APITestCase):
    product_url = reverse('product-detail', args=[1])
    products_url = reverse("product")

    def setUp(self):
        self.user = User.objects.create_user(
            username='admin', password='admin')
        self.token = Token.objects.create(user=self.user)
        #self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Saving customer
        data = {
        "id": 2,
        "name": "test5",
        "description": "test",
        "price": 15,
        "created_date": "2022-02-11",
        "rating": 5
    }
        self.client.post(
            self.products_url, data, format='json')

    def test_get_customer_autheticated(self):
        response = self.client.get(self.product_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'test5')

    def test_get_customer_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.product_url)
        self.assertEqual(response.status_code, 401)

    def test_delete_customer_authenticated(self):
        response = self.client.delete(self.product_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



## Customer tests




class TestView(APITestCase):

    def test_get_all_customers(self):
        response = self.client.get(reverse('customer'))
        self.assertEqual(response.status_code,200)

    def test_get_detail_customer(self):
        Customer.objects.create(
            id=1,
            name='test',
            age=25,
            comment='test_comment',
            address='badaxshan',
            number='+999429232')
        response = self.client.get(reverse('customer_detail',args='1'))
        self.assertEqual(response.status_code,200)
    def test_post_customer(self):
        customer_data = {
            'name' :'test',
            'age' : 25,
            'comment' :'test_comment',
            'address' :'badaxshan',
            'number' : '+999429232'
        }
        response = self.client.post(reverse('customer'),customer_data)
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.data['name'],'test')

    def test_put_customer(self):
        Customer.objects.create(
            id=6,
            name='test',
            age=25,
            comment='test_comment',
            address='badaxshan',
            number='+999429232')
        customer_data = {
            'name' :'test_put',
            'age' : 25,
            'comment' :'test_comment',
            'address' :'badaxshan',
            'number' : '+999429232'
        }
        response = self.client.put(reverse('customer_detail',args='6'),customer_data)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data['name'],'test_put')


        


        

