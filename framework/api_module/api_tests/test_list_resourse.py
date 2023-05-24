"""
API tests for ListResource method.
"""

import pytest
import allure
from ..api_requests import GetListResource


@allure.step('Get response body for ui test')
def get_received_response_body_for_ui_list_resource(search_type='unknown') -> dict:
    if search_type == 'unknown':
        request = GetListResource('unknown')
        request.send_request_list_resource(request)
    return request.get_response()


@allure.step('Get request URL')
def get_request_url_for_ui_list_resource() -> str:
    request = GetListResource('unknown')
    request.send_request_list_resource(request)
    return '/api/' + request.method_api


@allure.step('Get total resources')
def get_total_resources_list_resource() -> int:
    request = GetListResource('unknown')
    request.send_request_list_resource(request)
    number_of_resources = request.get_total_number_of_resources()
    return number_of_resources


@allure.step('Get total pages')
def get_total_pages_number_list_resource() -> int:
    request = GetListResource('unknown')
    request.send_request_list_resource(request)
    number_of_pages = request.get_total_number_of_pages()
    return number_of_pages


@allure.suite('ListResource API method')
class TestGetListResource:
    total_number_of_resources = get_total_resources_list_resource()
    total_number_of_pages = get_total_pages_number_list_resource()

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        global request
        request = GetListResource('unknown')

    @allure.title('Test should_return_status_code_200.')
    def test_get_list_resource_should_return_status_code_200(self):
        request.send_request_list_resource(request)
        request.should_be_status_code_200()

    @allure.title('Test got_6_items_as_default.')
    def test_get_list_resource_got_6_items_as_default(self):
        request.send_request_list_resource(request)
        request.should_be_six_resources()

    @allure.title('Test resource_total_pages.')
    def test_get_list_resource_total_pages(self):
        request.send_request_list_resource(request)
        request.should_be_correct_number_of_total_pages()
