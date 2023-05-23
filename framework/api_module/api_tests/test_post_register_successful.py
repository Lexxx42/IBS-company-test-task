"""
API tests for RegisterSuccessful method.
"""
import json
import pytest
import allure
from ..api_requests import RegisterSuccessful
from .. import generated_person


@allure.step('Get response body for ui test')
def get_received_response_body_for_ui_register_successful(password_to_send, email_to_send) -> dict:
    request = RegisterSuccessful('register', password='', email='')
    request.send_request_with_email_and_password(request, password_to_send, email_to_send)
    return request.get_response()


@allure.step('Get request URL')
def get_request_url_for_ui_register_successful() -> str:
    request = RegisterSuccessful('register', password='', email='')
    person = next(generated_person())
    password_to_send = person.password
    request.send_request_with_email_and_password(request, password_to_send)
    return '/api/' + request.method_api


@allure.suite('RegisterSuccessful API method')
class TestPostRegisterSuccessful:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        global request
        request = RegisterSuccessful('register', password='', email='')

    @allure.title('Test should_return_status_code_200.')
    @pytest.mark.parametrize('password, email', [('', '')] * 2)
    def test_post_register_successful_should_return_status_code_200(self, password, email):
        person = next(generated_person())
        password_to_send = person.password
        request.send_request_with_email_and_password(request, password_to_send)
        request.should_be_status_code_200()

    @allure.title('Test succsessful registration returns id and token.')
    @pytest.mark.parametrize('password, email', [('', '')] * 2)
    def test_post_register_successful_sent_data_must_be_in_response(self, password, email):
        person = next(generated_person())
        password_to_send = person.password
        request.send_request_with_email_and_password(request, password_to_send)
        request.check_id_and_token_in_response()
