"""Homework_27"""


import uuid
import requests
from jsonschema import validate
import pytest


BASE_URL = "https://alexqa.netlify.app/.netlify"
AUTH_TOKEN = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIxMTU0NTMwMTY1NTEwMDM2NDU3NT"
              "giLCJpYXQiOjE3MjM3Njk1ODUsImV4cCI6MTcyMzc3MzE4NX0."
              "nCZl_zjV-su_IJKa2Js3YD2Ff5OaUciGvn2h1co2ews")

user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "age": {"type": "number"},
        "phoneNumber": {"type": "string"},
        "address": {"type": "string"},
        "role": {"type": "string"},
        "referralCode": {"type": ["string", "null"]},
        "status": {"type": "string"},
        "createdAt": {"type": "string"},
        "createdBy": {"type": "string"}
    },
    "required": ["id", "name", "email", "age",
                 "phoneNumber", "address", "role"]
}


@pytest.fixture
def test_user_id():
    url = f"{BASE_URL}/functions/createUser"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AUTH_TOKEN}"
    }
    unique_email = f"testuser_{uuid.uuid4()}@example.com"
    payload = {
        "name": "John Doe",
        "email": unique_email,
        "age": 30,
        "phoneNumber": "+12345678901",
        "address": "123 Main St",
        "role": "user",
        "referralCode": "ABCDEFGH"
    }

    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 200

    data = response.json()
    validate(instance=data, schema=user_schema)

    return data['id']


def test_get_user(test_user_id):
    url = f"{BASE_URL}/functions/getUser/{test_user_id}"
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    assert response.status_code == 200

    data = response.json()
    validate(instance=data, schema=user_schema)
    assert data['id'] == test_user_id


def test_update_user(test_user_id):
    url = f"{BASE_URL}/functions/updateUser/{test_user_id}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AUTH_TOKEN}"
    }
    payload = {
        "name": "John Smith",
        "email": f"johnsmith_{uuid.uuid4()}@example.com",
        "age": 31,
        "phoneNumber": "+1234567890",
        "address": "456 Elm Stanciya Zavodskaya",
        "role": "user"
    }

    response = requests.put(url, json=payload, headers=headers)
    assert response.status_code == 200

    data = response.json()
    validate(instance=data, schema=user_schema)
    assert data['name'] == "John Smith"
    assert data['id'] == test_user_id


def test_check_user_status(test_user_id):
    url = f"{BASE_URL}/functions/checkUserStatus/{test_user_id}"
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    assert response.status_code == 200, (f"Failed to check user status. "
                                         f"Status code: {response.status_code}")

    data = response.json()
    assert data["id"] == test_user_id, "User ID does not match"
    assert data["status"] == "created", "User status is not 'created'"


def test_delete_user(test_user_id):
    url = f"{BASE_URL}/functions/deleteUser/{test_user_id}"
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}"
    }

    response = requests.delete(url, headers=headers)
    assert response.status_code == 200

    data = response.json()
    assert data['status'] == 'deleted'
    assert data['id'] == test_user_id


def test_get_users():
    url = f"{BASE_URL}/functions/getUsers"
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}"
    }

    params = {
        "page": 1,
        "limit": 10
    }

    response = requests.get(url, headers=headers, params=params)
    assert response.status_code == 200, (f"Failed to get users. "
                                         f"Status code: {response.status_code}")

    data = response.json()
    assert "users" in data, "Response does not contain 'users' field"
    assert isinstance(data["users"], list), "'users' is not a list"
    assert len(data["users"]) > 0, "Users list is empty"
    assert "totalPages" in data, "Response does not contain 'totalPages' field"


def test_delete_nonexistent_user():
    user_id = "nonexistent_user_id"
    url = f"{BASE_URL}/functions/deleteUser/{user_id}"
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}"
    }

    response = requests.delete(url, headers=headers)
    assert response.status_code == 400

    data = response.json()
    assert 'error' in data


def test_create_user_invalid_data():
    url = f"{BASE_URL}/functions/createUser"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AUTH_TOKEN}"
    }
    payload = {
        "name": "JD",
        "email": "invalidemail",
        "age": 17,
        "phoneNumber": "1234567",
        "address": "Short",
        "role": "invalid_role",
        "referralCode": "short"
    }

    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 400

    data = response.json()
    assert 'error' in data


def test_get_nonexistent_user():
    non_existent_user_id = "11a2cf334a56789c10d1ccf2"
    url = f"{BASE_URL}/functions/getUser/{non_existent_user_id}"
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    assert response.status_code == 404, (f"Expected status code 404, "
                                         f"but got {response.status_code}")

    data = response.json()
    assert "error" in data, "Response does not contain 'error' field"
    assert data["error"] == "User not found", "Unexpected error message"
