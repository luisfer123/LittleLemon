from django.test import TestCase
from restaurant.models import *

class MenuTest(TestCase):
    
    def test_get_menu_item(self):
        item = Menu.objects.create(title='IceCream', price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")