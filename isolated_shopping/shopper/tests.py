from django.test import TestCase
from shopper import models
# from django.contrib.auth import authenticate


# Create your tests here.
class ModelTestCase(TestCase):
    def setUp(self):
        self.shopper = models.ShopperDB.objects.create(shopperEmail='test@test.com', shopperPassword='test123',
                                                       shopperName='testName', shopperPhone='0741526541',
                                                       shopperAddress='Test Rd, Test, UK')

    def test_model(self):
        self.assertEqual(self.shopper.__str__(), 'testName')
        self.assertEqual(self.shopper.shopperId, 1)
        self.assertEqual(self.shopper.shopperAddress, 'Test Rd, Test, UK')

    # def test_password(self):
    #     user = authenticate(username=self.shopper.shopperEmail, password=self.shopper.shopperPassword)
    #     self.assertTrue(user.check_password('test123'))
