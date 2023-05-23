import json
import allure
from .base_request_post import BaseRequestPost


class RegisterSuccessful(BaseRequestPost):

    @allure.step('Send request with user\'s email and password.')
    def send_request_with_email_and_password(self, request, password='', email='eve.holt@reqres.in') -> tuple[str, str]:
        request.params['password'] = password
        request.params['email'] = email
        request.send()
        return password, email

    @allure.step('Send request with only password.')
    def send_request_with_password_only(self, request, password):
        request.params['password'] = password
        request.send()

    @allure.step('Send request with only email.')
    def send_request_with_email_only(self, request, email):
        request.params['email'] = email
        request.send()

    @allure.step('Get requests response.')
    def get_response(self) -> dict:
        response = self.response.json()
        return response

    @allure.step('Get id and token from response.')
    def get_id_and_token_registration(self) -> tuple[str, str]:
        response = self.get_response()
        id = response['id']
        token = response['token']
        return id, token

    @allure.step('Check response to have id and token.')
    def check_id_and_token_in_response(self):
        id, token = self.get_id_and_token_registration()
        assert id is not None, \
            f'Expected response to have id. Got: {id}'
        assert token is not None, \
            f'Expected response to have token. Got: {token}'
