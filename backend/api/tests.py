from django.test import TestCase, Client
from rest_framework.test import APIClient

from .models import Value, Principle


# Create your tests here.


class ValueTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_value_insert(self):
        response = self.client.put(
            "/api/values", {"text": "This is a test"}, format="json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["id"], 5)

    def test_value_get(self):
        response = self.client.get("/api/values")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["data"]), 4)
