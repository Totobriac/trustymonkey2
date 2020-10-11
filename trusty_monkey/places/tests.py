import json

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.test import Client, TestCase
from django.urls import reverse

class CreateReviewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="TotoBriac",
                                            password="verystrongpsw")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
    
    def test_create_review(self):
        data = {"id": 1, "restaurant_name": "Les délices de Toto",
                "restaurant_adress": "21 Grande Rue, 77630 Barbizon, France",
                "created_at": "18 October, 2020", "maps": "ChIJd230zfzz5UcRz8XVIZjiVzY",
                "review_author": "TotoBriac"}
        response = self.client.post("/api/restaurant_review/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


      

