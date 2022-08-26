from app.modules.user.models import User
from flask import url_for

from test_flask_base import TestFlaskBase

class TestUserCreate(TestFlaskBase):
    def test_create_success(self):
        request_data = {
            "username": "test",
            "password": "123456",
        }

        response = self.client.post(url_for("bp_v1.bp_user.create"), json=request_data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["username"], request_data["username"])

    def test_create_missing_field_failure(self):
        request_data = {"username": "test"}

        expected_response = {
            "message": "ValidationError",
            "errors": {"password": ["Missing data for required field."]},
        }

        response = self.client.post(url_for("bp_v1.bp_user.create"), json=request_data)

        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json, expected_response)

    def test_create_blank_field_failure(self):
        request_data = {
            "username": "",
            "password": "123456",
        }

        expected_response = {
            "message": "ValidationError",
            "errors": {"username": "Field is blank."},
        }

        response = self.client.post(url_for("bp_v1.bp_user.create"), json=request_data)

        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json, expected_response)

    def test_create_empty_failure(self):
        request_data = {}

        expected_response = {
            "message": "ValidationError",
            "errors": {
                "username": ["Missing data for required field."],
                "password": ["Missing data for required field."],
            },
        }

        response = self.client.post(url_for("bp_v1.bp_user.create"), json=request_data)

        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json, expected_response)

    def test_create_id_unknown_field_failure(self):
        request_data = {
            "id": 1,
            "username": "test",
            "password": "123456",
        }

        expected_response = {
            "message": "ValidationError",
            "errors": {"id": ["Unknown field."]},
        }

        response = self.client.post(url_for("bp_v1.bp_user.create"), json=request_data)

        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json, expected_response)

    def test_create_non_unique_username_failure(self):
        request_data = {
            "username": "test",
            "password": "123456",
        }

        expected_response = {
            "message": "ValidationError",
            "errors": {"username": ["Username already exists."]},
        }

        self.client.post(url_for("bp_v1.bp_user.create"), json=request_data)
        response = self.client.post(url_for("bp_v1.bp_user.create"), json=request_data)

        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json, expected_response)
