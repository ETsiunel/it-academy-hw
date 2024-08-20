"""Tests User API"""


import pytest
import requests
from test_data import get_unique_email


def test_create_user(user_api):
    user_data = {
        "name": "John Doe",
        "email": get_unique_email(),
        "age": 30,
        "phoneNumber": "+12345678901",
        "address": "123 Main St",
        "role": "user",
        "referralCode": "ABCDEFGH"
    }
    response = user_api.create_user(user_data)
    assert response["name"] == user_data["name"]
    assert response["email"] == user_data["email"]


def test_get_user(user_api, test_user_id):
    user = user_api.get_user(test_user_id)
    assert user['id'] == test_user_id


def test_update_user(user_api, test_user_id):
    update_data = {
        "name": "John Smith",
        "email": get_unique_email(),
        "age": 31,
        "phoneNumber": "+1234567890",
        "address": "456 Elm St",
        "role": "user"
    }
    updated_user = user_api.update_user(test_user_id, update_data)
    assert updated_user['name'] == "John Smith"
    assert updated_user['id'] == test_user_id


def test_check_user_status(user_api, test_user_id):
    status_response = user_api.check_user_status(test_user_id)
    assert status_response["id"] == test_user_id
    assert status_response["status"] == "created"


def test_delete_user(user_api, test_user_id):
    delete_response = user_api.delete_user(test_user_id)
    assert delete_response['status'] == 'deleted'
    assert delete_response['id'] == test_user_id


def test_get_users(user_api):
    users_response = user_api.get_users(page=1, limit=10)
    assert "users" in users_response
    assert len(users_response["users"]) > 0


def test_delete_nonexistent_user(user_api):
    non_existent_user_id = "nonexistent_user_id"
    response = user_api.delete_user(non_existent_user_id)

    assert 'error' in response
    assert response['error'] == "Invalid Order ID format"


def test_create_user_invalid_data(user_api):
    invalid_user_data = {
        "name": "JD",
        "email": "invalidemail",
        "age": 17,
        "phoneNumber": "1234567",
        "address": "Short",
        "role": "invalid_role",
        "referralCode": "short"
    }
    with pytest.raises(requests.exceptions.HTTPError):
        user_api.create_user(invalid_user_data)


def test_get_nonexistent_user(user_api):
    non_existent_user_id = "11a2cf334a56789c10d1ccf2"
    with pytest.raises(requests.exceptions.HTTPError):
        user_api.get_user(non_existent_user_id)
