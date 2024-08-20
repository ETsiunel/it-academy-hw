"""User API model"""


import json
import requests
from jsonschema import validate
from test_data import (BASE_URL, USER_SCHEMA,
                       CREATE_USER_URL, GET_USER_URL,
                       UPDATE_USER_URL, DELETE_USER_URL,
                       CHECK_USER_STATUS_URL, GET_USERS_URL)


def load_auth_token():
    with open('config.json') as config_file:
        config = json.load(config_file)
    return config['auth_token']


class BaseAPI:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url
        self.auth_token = load_auth_token()
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.auth_token}"
        }

    def _send_request(self, method, endpoint, data=None, params=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, headers=self.headers,
                                    json=data, params=params)
        response.raise_for_status()
        return response

    def validate_response(self, response, expected_schema=None):
        if 200 <= response.status_code < 300:
            if expected_schema:
                validate(instance=response.json(), schema=expected_schema)
            return True
        return False


class UserAPI(BaseAPI):
    def create_user(self, user_data):
        response = self._send_request('POST', CREATE_USER_URL,
                                      data=user_data)
        self.validate_response(response, expected_schema=USER_SCHEMA)
        return response.json()

    def get_user(self, user_id):
        response = self._send_request('GET',
                                      f"{GET_USER_URL}/{user_id}")
        self.validate_response(response, expected_schema=USER_SCHEMA)
        return response.json()

    def update_user(self, user_id, update_data):
        response = self._send_request('PUT',
                                      f"{UPDATE_USER_URL}/{user_id}",
                                      data=update_data)
        self.validate_response(response, expected_schema=USER_SCHEMA)
        return response.json()

    def check_user_status(self, user_id):
        response = self._send_request('GET',
                                      f"{CHECK_USER_STATUS_URL}/{user_id}")
        self.validate_response(response)
        return response.json()

    def delete_user(self, user_id):
        try:
            response = self._send_request('DELETE',
                                          f"{DELETE_USER_URL}/{user_id}")
            self.validate_response(response)
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 400:
                return e.response.json()
            else:
                raise

    def get_users(self, page=1, limit=10):
        params = {"page": page, "limit": limit}
        response = self._send_request('GET', GET_USERS_URL,
                                      params=params)
        self.validate_response(response)
        return response.json()
