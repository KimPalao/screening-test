from django.test import TestCase, Client
from .models import Value, Principle

# Create your tests here.


class ValueTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_value_insert(self):
        response = self.client.put("/api/values", {"text": "This is a test"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["id"], 5)
