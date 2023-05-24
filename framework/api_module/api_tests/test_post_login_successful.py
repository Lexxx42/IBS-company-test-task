"""
API tests for LoginSuccessful and LoginUnsuccessful method.
"""

import pytest
import allure
from ..api_requests import LoginSuccessful
from .. import generated_person


@allure.step('Get response body for ui test')
def get_received_response_body_for_ui_login_successful(
        email_to_send, password_to_send) -> dict:
    request = LoginSuccessful('login', email='', password='')
    request.send_request_with_email_and_password_login(request, email_to_send, password_to_send)
    return request.get_response()


@allure.step('Get response body for ui test')
def get_received_response_body_for_ui_login_unsuccessful(
        email_to_send) -> dict:
    request = LoginSuccessful('login', email='')
    request.params['email'] = email_to_send
    request.send()
    return request.get_response()


@allure.step('Get request URL')
def get_request_url_for_ui_login_successful() -> str:
    request = LoginSuccessful('login', email='', password='')
    request.send_request_with_email_and_password_login(request)
    return '/api/' + request.method_api


@allure.suite('LoginSuccessful and LoginUnsuccessful API method')
class TestPostLoginSuccessful:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        global request
        request = LoginSuccessful('login', email='', password='')

    @allure.title('Test should_return_status_code_200.')
    @pytest.mark.login_successful
    def test_post_login_successful_should_return_status_code_200(self):
        request.send_request_with_email_and_password_login(request)
        request.should_be_status_code_200()

    @allure.title('Test successful login returns token.')
    @pytest.mark.login_successful
    @pytest.mark.parametrize('email, password', [('', '')] * 2)
    def test_post_login_successful_sent_data_must_be_in_response(self, email, password):
        request.send_request_with_email_and_password_login(request)
        request.check_token_in_response()

    @allure.title('Test unsuccessful login with missing email.')
    @pytest.mark.login_unsuccessful
    @pytest.mark.parametrize('password_to_send', ['1', '2'])
    def test_post_login_unsuccessful_should_return_status_code_400(self, password_to_send: str):
        request = LoginSuccessful('login', password='')
        person = next(generated_person())
        password_to_send = person.password
        request.send_request_with_password_only_login(request, password_to_send)
        request.should_be_status_code_400()

    @allure.title('Test unsuccessful login with missing password.')
    @pytest.mark.login_unsuccessful
    @pytest.mark.parametrize('email_to_send', ['1', '2'])
    def test_post_login_unsuccessful_should_return_status_code_400(self, email_to_send: str):
        request = LoginSuccessful('login', email='')
        email_to_send = 'peter@klaven'
        request.send_request_with_email_only_login(request, email_to_send)
        request.should_be_status_code_400()

    @allure.title('Test unsuccessful login with incorrect email.')
    @pytest.mark.login_unsuccessful
    @pytest.mark.parametrize('password_to_send, email_to_send', [('', '')] * 2)
    def test_post_login_unsuccessful_should_return_status_code_400(
            self, password_to_send: str, email_to_send: str):
        person = next(generated_person())
        password_to_send = person.password
        email_to_send = person.email
        request.send_request_with_email_and_password_login(request, email_to_send, password_to_send)
        request.should_be_status_code_400()
