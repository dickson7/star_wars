from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class TestPeople(APITestCase):
    
    def authenticate(self):
        self.client.post(reverse("register"), {
            'username':"username", "email": "email@gmail.com", "password":"q1w2e3r4"
        })
        response = self.client.post(reverse('login'), {
            "username":"username", "password":"q1w2e3r4"
        })
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['token']}")
    
    def test_should_not_consult_without_authorization(self):
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_should_consult_people(self):
        self.authenticate()
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
