import json
import allure
from .base_request_post import BaseRequestPost


class LoginSuccessful(BaseRequestPost):

    @allure.step('Send request with user\'s email and password.')
    def send_request_with_email_and_password_login(
            self, request, email='eve.holt@reqres.in', password='cityslicka') -> tuple[str, str]:
        request.params['email'] = email
        request.params['password'] = password
        request.send()
        return password, email

    @allure.step('Send request with only password.')
    def send_request_with_password_only_login(self, request, password):
        request.params['password'] = password
        request.send()

    @allure.step('Send request with only email.')
    def send_request_with_email_only_login(self, request, email):
        request.params['email'] = email
        request.send()

    @allure.step('Get requests response.')
    def get_response(self) -> dict:
        response = self.response.json()
        return response

    @allure.step('Get id and token from response.')
    def get_token_login(self) -> tuple[str, str]:
        response = self.get_response()
        token = response['token']
        return token

    @allure.step('Check response to have id and token.')
    def check_token_in_response(self):
        token = self.get_token_login()
        assert token is not None, \
            f'Expected response to have token. Got: {token}'
