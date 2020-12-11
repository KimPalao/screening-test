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
        self.assertEqual(response.json()["message"], "Text must not be empty")

    def test_value_insert_missing_params(self):
        response = self.client.put("/api/values", {}, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["message"], "Text is required")

    def test_value_insert_duplicate(self):
        response = self.client.put("/api/values", {"text": values[0]}, format="json")
        self.assertEqual(response.status_code, 409)
        self.assertEqual(
            response.json()["message"], "A Value with this text already exists"
        )

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
        self.assertEqual(response.json()["message"], "Value not found")

    def test_value_update(self):
        value_id = 4
        text = "sample text"
        response = self.client.patch(
            f"/api/values/{value_id}", {"text": text}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.get(f"/api/values/{value_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["data"]["text"], text)

    def test_value_update_no_change(self):
        value_id = 4
        text = values[value_id - 1]
        response = self.client.patch(
            f"/api/values/{value_id}", {"text": text}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.get(f"/api/values/{value_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["data"]["text"], text)

    def test_value_update_failed(self):
        value_id = 3
        text = values[0]
        response = self.client.patch(
            f"/api/values/{value_id}", {"text": text}, format="json"
        )
        self.assertEqual(response.status_code, 409)
        self.assertEqual(
            response.json()["message"], "A Value with this text already exists"
        )

    def test_value_update_not_found(self):
        value_id = 5
        text = "sample text"
        response = self.client.patch(
            f"/api/values/{value_id}", {"text": text}, format="json"
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["message"], "Value not found")

    def test_value_update_blank_text(self):
        value_id = 4
        text = ""
        response = self.client.patch(
            f"/api/values/{value_id}", {"text": text}, format="json"
        )
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json()["message"], "Text must not be empty")

    def test_value_update_no_text(self):
        value_id = 4
        response = self.client.patch(f"/api/values/{value_id}", {}, format="json")
        self.assertEqual(response.status_code, 200)

    def test_value_delete(self):
        value_id = 4
        response = self.client.delete(f"/api/values/{value_id}")
        self.assertEqual(response.status_code, 200)
        response = self.client.get(f"/api/values/{value_id}")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["message"], "Value not found")

    def test_value_delete_not_found(self):
        value_id = 5
        response = self.client.delete(f"/api/values/{value_id}")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["message"], "Value not found")


principles = [
    "Customer satisfaction through early and continuous software delivery",
    "Accommodate changing requirements throughout the development process",
    "Frequent delivery of working software",
    "Collaboration between the business stakeholders and developers throughout the project",
    "Support, trust, and motivate the people involved",
    "Enable face-to-face interactions",
    "Working software is the primary measure of progress",
    "Agile processes to support a consistent development pace",
    "Attention to technical detail and design enhances agility",
    "Simplicity",
    "Self-organizing teams encourage great architectures, requirements, and designs",
    "Regular reflections on how to become more effective",
]


class PrincipleTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_principle_insert(self):
        response = self.client.put(
            "/api/principles", {"text": "This is a test"}, format="json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["id"], 13)

    def test_principle_insert_blank_text(self):
        response = self.client.put("/api/principles", {"text": ""}, format="json")
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json()["message"], "Text must not be empty")

    def test_principle_insert_missing_params(self):
        response = self.client.put("/api/principles", {}, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["message"], "Text is required")

    def test_principle_insert_duplicate(self):
        response = self.client.put(
            "/api/principles", {"text": principles[0]}, format="json"
        )
        self.assertEqual(response.status_code, 409)
        self.assertEqual(
            response.json()["message"], "A Principle with this text already exists"
        )

    def test_principle_get(self):
        response = self.client.get("/api/principles")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["data"]), 10)

    def test_principle_get_more(self):
        response = self.client.get("/api/principles", {"per_page": 20})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["data"]), 12)

    def test_principle_get_filter(self):
        response = self.client.get("/api/principles", {"text_contains": "software"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["data"]), 3)

        response = self.client.get("/api/principles", {"text_contains": "and"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["data"]), 5)

    def test_principle_get_single(self):
        principle_id = 5
        response = self.client.get(f"/api/principles/{principle_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["data"]["text"], principles[principle_id - 1])

    def test_principle_get_single_not_found(self):
        principle_id = 13
        response = self.client.get(f"/api/principles/{principle_id}")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["message"], "Principle not found")

    def test_principle_update(self):
        principle_id = 4
        text = "sample text"
        response = self.client.patch(
            f"/api/principles/{principle_id}", {"text": text}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.get(f"/api/principles/{principle_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["data"]["text"], text)

    def test_principle_update_no_change(self):
        principle_id = 4
        text = principles[principle_id - 1]
        response = self.client.patch(
            f"/api/principles/{principle_id}", {"text": text}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.get(f"/api/principles/{principle_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["data"]["text"], text)

    def test_principle_update_failed(self):
        principle_id = 3
        text = principles[0]
        response = self.client.patch(
            f"/api/principles/{principle_id}", {"text": text}, format="json"
        )
        self.assertEqual(response.status_code, 409)
        self.assertEqual(
            response.json()["message"], "A Principle with this text already exists"
        )

    def test_principle_update_not_found(self):
        principle_id = 13
        text = "sample text"
        response = self.client.patch(
            f"/api/principles/{principle_id}", {"text": text}, format="json"
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["message"], "Principle not found")

    def test_principle_update_blank_text(self):
        principle_id = 4
        text = ""
        response = self.client.patch(
            f"/api/principles/{principle_id}", {"text": text}, format="json"
        )
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json()["message"], "Text must not be empty")

    def test_principle_update_no_text(self):
        principle_id = 4
        response = self.client.patch(
            f"/api/principles/{principle_id}", {}, format="json"
        )
        self.assertEqual(response.status_code, 200)

    def test_principle_delete(self):
        principle_id = 4
        response = self.client.delete(f"/api/principles/{principle_id}")
        self.assertEqual(response.status_code, 200)
        response = self.client.get(f"/api/principles/{principle_id}")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["message"], "Principle not found")

    def test_principle_delete_not_found(self):
        principle_id = 13
        response = self.client.delete(f"/api/principles/{principle_id}")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["message"], "Principle not found")
