from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import BasketDB, BasketItem
from shopper.models import ShopperDB
from product.models import ProductDB


# Create your tests here.
class BasketTestCase(APITestCase, TestCase):
    def setUp(self):
        self.shopper_1 = ShopperDB.objects.create(shopperEmail='test_1@test.com', shopperPassword='test123',
                                                  shopperName='Test_1', shopperPhone='09876352671',
                                                  shopperAddress='Test_1 Rd, Test')
        self.shopper_2 = ShopperDB.objects.create(shopperEmail='test_2@test.com', shopperPassword='test123',
                                                  shopperName='Test_2', shopperPhone='01762536789',
                                                  shopperAddress='Test_2 Rd, Test')
        self.basket_1 = BasketDB.objects.create(shopperId=1, totalPrice=0, isEmpty=False)
        self.basket_1_item_1 = BasketItem.objects.create(basketId=1, productId=1, quantity=1)
        self.basket_1_item_2 = BasketItem.objects.create(basketId=1, productId=2, quantity=2)
        self.product_1 = ProductDB.objects.create(name='Test_Product_1', price=1, stock=2, retailer='TestR_1', views=0)
        self.product_2 = ProductDB.objects.create(name='Test_Product_2', price=2, stock=3, retailer='TestR_2', views=0)
        self.product_3 = ProductDB.objects.create(name='Test_Product_3', price=3, stock=4, retailer='TestR_1', views=0)

    def testModelValue(self):
        self.assertEqual(self.basket_1.basketId, 1)
        self.assertEqual(self.basket_1.isEmpty, False)
        self.assertEqual(self.basket_1_item_2.basketItemId, 2)
        self.assertEqual(self.basket_1_item_1.quantity, 1)

    def testViewGet(self):
        url_0 = reverse('basket_process', args='2')
        response_0 = self.client.get(url_0, format='json')
        self.assertEqual(response_0.status_code, status.HTTP_404_NOT_FOUND)

        url_1 = reverse('basket_process', args='1')
        response_1 = self.client.get(url_1, format='json')
        self.assertEqual(response_1.data['shopper'][0]['shopperId'], 1)
        self.assertEqual(response_1.data['totalPrice'], 0)
        self.assertEqual(response_1.data['items'][0]['product']['productId'], 1)
        self.assertEqual(response_1.data['items'][1]['quantity'], 2)

    def testViewPut(self):
        # Update a shopper that is not existed
        url_0 = reverse('basket_process', args='3')
        response_0 = self.client.put(url_0, format='json')
        self.assertEqual(response_0.status_code, status.HTTP_404_NOT_FOUND)

        # Update a existed shopper already having a basket
        url_1 = reverse('basket_process', args='1')
        data = {"items": [{"product": {"productId": 1}, "quantity": 2}, {"product": {"productId": 3}, "quantity": 1}]}
        response_1 = self.client.put(url_1, data, format='json')
        self.assertEqual(response_1.data['shopper'][0]['shopperId'], 1)
        self.assertEqual(response_1.data['totalPrice'], 5)
        self.assertNotEqual(BasketDB.objects.get(basketId=1).totalPrice, 0)
        self.assertEqual(response_1.data['items'][1]['product']['productId'], 3)
        self.assertEqual(response_1.data['items'][1]['quantity'], 1)
        self.assertEqual(list(BasketItem.objects.filter(basketItemId=1)), [])
        self.assertEqual(ProductDB.objects.get(productId=1).views, 1)

        # Update a existed shopper who has not a basket
        url_2 = reverse('basket_process', args='2')
        response_2 = self.client.put(url_2, data, format='json')
        self.assertEqual(response_2.data['shopper'][0]['shopperId'], 2)
        self.assertFalse(BasketDB.objects.get(basketId=2).isEmpty)
        self.assertTrue(BasketDB.objects.get(basketId=2).totalPrice, 5)
        self.assertEqual(ProductDB.objects.get(productId=3).views, 2)

    def testDeleteView(self):
        url_0 = reverse('basket_process', args='2')
        response_0 = self.client.delete(url_0, format='json')
        self.assertEqual(response_0.status_code, status.HTTP_404_NOT_FOUND)

        url_1 = reverse('basket_process', args='1')
        response_1 = self.client.delete(url_1, format='json')
        self.assertEqual(response_1.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(list(BasketItem.objects.filter(basketItemId=1)), [])
        self.assertTrue(BasketDB.objects.get(basketId=1).isEmpty)
        self.assertEqual(BasketDB.objects.get(basketId=1).totalPrice, 0)
