"""
API tests for LoginSuccessful and asd method.
"""
import json
import pytest
import allure
from ..api_requests import LoginSuccessful
from .. import generated_person


@allure.step('Get response body for ui test')
def get_received_response_body_for_ui_login_successful(
        email_to_send, password_to_send, type_of_registration='success') -> dict:
    if type_of_registration == 'success':
        request = LoginSuccessful('login', email='', password='')
        request.send_request_with_email_and_password_login(request, email_to_send, password_to_send)
    elif type_of_registration == 'unsuccessful':
        request = LoginSuccessful('login', email='', password='')
        request.params['email'] = email_to_send
        request.send()
    return request.get_response()


@allure.step('Get request URL')
def get_request_url_for_ui_login_successful() -> str:
    request = LoginSuccessful('login', email='', password='')
    request.send_request_with_email_and_password_login(request)
    return '/api/' + request.method_api


@allure.suite('LoginSuccessful API method')
class TestPostLoginSuccessful:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        global request
        request = LoginSuccessful('login', email='', password='')

    @allure.title('Test should_return_status_code_200.')
    def test_post_login_successful_should_return_status_code_200(self):
        request.send_request_with_email_and_password_login(request)
        request.should_be_status_code_200()

    @allure.title('Test succsessful login returns token.')
    def test_post_login_successful_sent_data_must_be_in_response(self):
        request.send_request_with_email_and_password_login(request)
        request.check_token_in_response()

    @allure.title('Test unsuccesseful login with missing email.')
    def test_post_login_unsuccessful_should_return_status_code_400(self):
        request = LoginSuccessful('login', password='')
        person = next(generated_person())
        password_to_send = person.password
        request.send_request_with_password_only_login(request, password_to_send)
        request.should_be_status_code_400()

    @allure.title('Test unsuccesseful login with missing password.')
    def test_post_login_unsuccessful_should_return_status_code_400(self):
        request = LoginSuccessful('login', email='')
        email_to_send = 'sydney@fife'
        request.send_request_with_email_only_login(request, email_to_send)
        request.should_be_status_code_400()

    @allure.title('Test unsuccesseful login with incorrect email.')
    def test_post_login_unsuccessful_should_return_status_code_400(self):
        person = next(generated_person())
        password_to_send = person.password
        email_to_send = person.email
        request.send_request_with_email_and_password_login(request, email_to_send, password_to_send)
        request.should_be_status_code_400()
