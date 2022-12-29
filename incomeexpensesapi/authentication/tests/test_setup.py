from django.urls import reverse
from rest_framework.test import APITestCase
from faker import Faker

class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.fake = Faker()

        self.user_data = {
            'email': self.fake.email(),
            'username':self.fake.last_name(),
            'password':self.fake.password(),
        }
        import pdb
        pdb.set_trace()
        return  super().setUp()

    def tearDown(self):
        return super().tearDown()

  