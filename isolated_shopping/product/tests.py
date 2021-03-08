from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from product import models


# Create your tests here.
class ModelTestCase(TestCase):
    def setUp(self):
        self.product_1 = models.ProductDB.objects.create(name="testProduct", image="testURl", price=100.00,
                                                         stock=100, retailer="TestRetailer", views=1)
        self.product_2 = models.ProductDB.objects.create(name="testProductParaLess", price=90.5,
                                                         retailer="TestRetailer_2")

    def test_str(self):
        self.assertEqual(self.product_1.__str__(), self.product_1.name)

    def test_value(self):
        self.assertEqual(self.product_1.image, "testURl")
        self.assertEqual(self.product_1.price, 100)
        self.assertEqual(self.product_1.stock, 100)
        self.assertEqual(self.product_1.retailer, "TestRetailer")
        self.assertIsNone(self.product_2.image)
        self.assertEqual(self.product_2.stock, 1)
        self.assertEqual(self.product_2.views, 0)


class ViewTestCase(APITestCase):
    def setUp(self):
        self.product_1 = models.ProductDB.objects.create(name="testProduct1", image="testURl1", price=100.00,
                                                         stock=10, retailer="TestRetailer1", views=2)
        self.product_2 = models.ProductDB.objects.create(name="testProduct2", image="testURl2", price=200.00,
                                                         stock=20, retailer="TestRetailer2", views=4)
        self.product_3 = models.ProductDB.objects.create(name="testProduct3", image="testURl3", price=300.00,
                                                         stock=30, retailer="TestRetailer1", views=2)

    def test_wrong_parameter(self):
        url = reverse('product_process')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get(self):
        url = reverse('product_process')
        data_0 = {'query': '1'}
        response_0 = self.client.get(url, data_0, format='json')
        self.assertEqual(response_0.data[0],
                         {'productId': 1, 'name': "testProduct1", 'image': "testURl1", 'price': 100.00,
                          'stock': 10, 'retailer': "TestRetailer1", 'views': 2})
        data_1 = {'query': 'test'}
        response_1 = self.client.get(url, data_1, format='json')
        self.assertEqual(response_1.data[0], {'productId': 2, 'name': "testProduct2", 'image': "testURl2",
                                              'price': 200.00, 'stock': 20, 'retailer': "TestRetailer2", 'views': 4})
        data_2 = {'retailer': 'TestRetailer1'}
        response_2 = self.client.get(url, data_2, format='json')
        self.assertEqual(len(response_2.data), 2)
        data_3 = {'retailer': 'TestRetailer1', 'limit': 1}
        response_3 = self.client.get(url, data_3, format='json')
        self.assertEqual(len(response_3.data), 1)
        data_4 = {'query': 'test', 'retailer': '1'}
        response_4 = self.client.get(url, data_4, format='json')
        self.assertEqual(len(response_4.data), 2)
        data_5 = {'query': 'test', 'limit': '1'}
        response_5 = self.client.get(url, data_5, format='json')
        self.assertEqual(len(response_5.data), 1)
        data_6 = {'query': 'test', 'retailer': 'test', 'limit': 2}
        response_6 = self.client.get(url, data_6, format='json')
        self.assertEqual(len(response_6.data), 2)

    def test_ranking(self):
        url = reverse('product_process')
        data = {'query': 'test'}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.data[0]['name'], 'testProduct2')
        self.assertEqual(response.data[1]['name'], 'testProduct1')
        self.assertEqual(response.data[2]['name'], 'testProduct3')

