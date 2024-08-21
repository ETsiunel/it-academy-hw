"""Fixtures"""


import pytest
from api_model import UserAPI
from test_data import get_unique_email


@pytest.fixture(scope="function")
def user_api():
    return UserAPI()


@pytest.fixture(scope="function")
def test_user_id(user_api):
    user_data = {
        "name": "John Doe",
        "email": get_unique_email(),
        "age": 30,
        "phoneNumber": "+12345678901",
        "address": "123 Main St",
        "role": "user",
        "referralCode": "ABCDEFGH"
    }
    user = user_api.create_user(user_data)
    return user['id']
