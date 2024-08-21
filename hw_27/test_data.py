"""Test data"""


import uuid

BASE_URL = "https://alexqa.netlify.app/.netlify"

CREATE_USER_URL = "/functions/createUser"
GET_USER_URL = "/functions/getUser"
UPDATE_USER_URL = "/functions/updateUser"
DELETE_USER_URL = "/functions/deleteUser"
CHECK_USER_STATUS_URL = "/functions/checkUserStatus"
GET_USERS_URL = "/functions/getUsers"

USER_SCHEMA = {
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


def get_unique_email():
    return f"testuser_{uuid.uuid4()}@example.com"
