import json

from django.contrib.auth.models import User

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

        

# class RegistrationTestCase(APITestCase):

#     def test_registration(self):
#         data = {"username": "TotoBriac", "email": "toto@gmail.com",
#                 "password1": "strongPsw", "password2": "strongPsw"}
#         response = self.client.post("/api/rest-auth/registration/", data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
