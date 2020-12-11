from django.test import TestCase, Client
from rest_framework.test import APIClient

from .models import Value, Principle


# Create your tests here.

values = [
    "Individuals and Interactions Over Processes and Tools",
    "Working Software Over Comprehensive Documentation",
    "Customer Collaboration Over Contract Negotiation",
    "Responding to Change Over Following a Plan",
]


class ValueTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_value_insert(self):
        response = self.client.put(
            "/api/values", {"text": "This is a test"}, format="json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["id"], 5)

    def test_value_insert_blank_text(self):
        response = self.client.put("/api/values", {"text": ""}, format="json")
        self.assertEqual(response.status_code, 422)

    def test_value_insert_missing_params(self):
        response = self.client.put("/api/values", {}, format="json")
        self.assertEqual(response.status_code, 400)

    def test_value_insert_duplicate(self):
        response = self.client.put("/api/values", {"text": values[0]}, format="json")
        self.assertEqual(response.status_code, 409)

    def test_value_get(self):
        response = self.client.get("/api/values")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["data"]), 4)

    def test_value_get_filter(self):
        response = self.client.get("/api/values", {"text_contains": "over"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["data"]), 4)

        response = self.client.get("/api/values", {"text_contains": "and"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["data"]), 1)

    def test_value_get_single(self):
        value_id = 2
        response = self.client.get(f"/api/values/{value_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["data"]["text"], values[value_id - 1])

    def test_value_get_single_not_found(self):
        value_id = 10
        response = self.client.get(f"/api/values/{value_id}")
        self.assertEqual(response.status_code, 404)