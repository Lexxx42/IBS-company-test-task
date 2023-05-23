"""
API tests for DelayedResponse method.
"""

import pytest
import allure
from ..api_requests import GetDelayedResponse


@allure.step('Get response body for ui test')
def get_received_response_body_for_ui_delayed_response(delay=3) -> dict:
    request = GetDelayedResponse('users?delay=/')
    request.send_request_with_selected_delay(request, delay=delay)
    return request.get_response()


@allure.step('Get request URL')
def get_request_url_for_ui_delayed_response(delay=3) -> str:
    request = GetDelayedResponse('users?delay=')
    request.send_request_with_selected_delay(request, delay=delay)
    return '/api/' + request.method_api


@allure.suite('GetListUsers API method')
class TestGetDelayedResponse:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        global request
        request = GetDelayedResponse('users?delay=')

    @allure.title('Test should_return_status_code_200.')
    def test_get_delayed_response_should_return_status_code_200(self):
        request.send_request_with_selected_delay(request, delay=0)
        request.should_be_status_code_200()

    @allure.title('Test should_return_response.')
    def test_get_delayed_response_should_return_response(self):
        request.send_request_with_selected_delay(request, delay=0)
        request.should_be_result_of_request_in_response()
