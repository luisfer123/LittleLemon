from django.test import TestCase, Client
from restaurant.models import *
from restaurant.serializers import *
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status

class MenuViewTest(TestCase):
    
    def setup(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(
            username = "testUser",
            password = "password"
        )
        
        self.pizza = Menu.objects.create(title='Pizza', price=12.5, inventory=12)
        self.hamburger = Menu.objects.create(title='Hamburger', price=9.33, inventory=21)
        self.tacos = Menu.objects.create(title='Tacos', price=21.9, inventory=99)
        
        
    def test_getall(self) -> None:
        self.client.login(username = "testUser", password = "password")
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many = True)
        self.assertEqual(response.data, serializer.data)