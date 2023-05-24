"""
API tests for RegisterSuccessful and RegisterUnsuccessful method.
"""

import pytest
import allure
from ..api_requests import RegisterSuccessful
from .. import generated_person


@allure.step('Get response body for ui test')
def get_received_response_body_for_ui_register_successful(
        password_to_send, email_to_send) -> dict:
    request = RegisterSuccessful('register', password='', email='')
    request.send_request_with_email_and_password(request, password_to_send, email_to_send)
    return request.get_response()


@allure.step('Get response body for ui test')
def get_received_response_body_for_ui_register_unsuccessful(email_to_send) -> dict:
    request = RegisterSuccessful('register', email='')
    request.params['email'] = email_to_send
    request.send()
    return request.get_response()


@allure.step('Get request URL')
def get_request_url_for_ui_register_successful() -> str:
    request = RegisterSuccessful('register', password='', email='')
    person = next(generated_person())
    password_to_send = person.password
    request.send_request_with_email_and_password(request, password_to_send)
    return '/api/' + request.method_api


@allure.suite('RegisterSuccessful and RegisterUnsuccessful API method')
class TestPostRegisterSuccessful:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        global request
        request = RegisterSuccessful('register', password='', email='')

    @allure.title('Test should_return_status_code_200.')
    @pytest.mark.register_successful
    @pytest.mark.parametrize('password, email', [('', '')] * 2)
    def test_post_register_successful_should_return_status_code_200(self, password, email):
        person = next(generated_person())
        password_to_send = person.password
        request.send_request_with_email_and_password(request, password_to_send)
        request.should_be_status_code_200()

    @allure.title('Test successful registration returns id and token.')
    @pytest.mark.register_successful
    @pytest.mark.parametrize('password, email', [('', '')] * 2)
    def test_post_register_successful_sent_data_must_be_in_response(self, password, email):
        person = next(generated_person())
        password_to_send = person.password
        request.send_request_with_email_and_password(request, password_to_send)
        request.check_id_and_token_in_response()

    @allure.title('Test unsuccessful registration with missing email.')
    @pytest.mark.register_unsuccessful
    @pytest.mark.parametrize('password_to_send', ['1', '2'])
    def test_post_register_unsuccessful_should_return_status_code_400(self, password_to_send: str):
        request = RegisterSuccessful('register', password='')
        person = next(generated_person())
        password_to_send = person.password
        request.send_request_with_password_only(request, password_to_send)
        request.should_be_status_code_400()

    @allure.title('Test unsuccessful registration with missing password.')
    @pytest.mark.register_unsuccessful
    @pytest.mark.parametrize('email_to_send', ['1', '2'])
    def test_post_register_unsuccessful_should_return_status_code_400(self, email_to_send: str):
        request = RegisterSuccessful('register', email='')
        email_to_send = 'sydney@fife'
        request.send_request_with_email_only(request, email_to_send)
        request.should_be_status_code_400()

    @allure.title('Test unsuccessful registration with incorrect email.')
    @pytest.mark.register_unsuccessful
    @pytest.mark.parametrize('password_to_send, email_to_send', [('', '')] * 2)
    def test_post_register_unsuccessful_should_return_status_code_400(
            self, password_to_send: str, email_to_send: str):
        person = next(generated_person())
        password_to_send = person.password
        email_to_send = person.email
        request.send_request_with_email_and_password(request, password_to_send, email_to_send)
        request.should_be_status_code_400()
