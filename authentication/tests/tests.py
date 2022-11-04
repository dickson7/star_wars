from rest_framework.test import APITestCase
from authentication.models import User

class TestModel(APITestCase):
    
    def test_creates_user(self):
        user = User.objects.create_user('d1','d1@d1.com','q1w2e3r4')
        self.assertIsInstance(user,User)
        self.assertEqual(user.email,'d1@d1.com')