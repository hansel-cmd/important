from django.test import TestCase, Client

class TestView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_page(self):
        response = self.client.get('http://127.0.0.1:8000')
        self.assertEqual(response.status_code, 200)

