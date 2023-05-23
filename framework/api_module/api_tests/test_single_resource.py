"""
API tests for SingleResource method.
"""

import pytest
import allure
from ..api_requests import GetSingleResource
from .test_list_resourse import get_total_resources_list_resource


@allure.step('Get response body for ui test')
def get_received_response_body_for_ui_single_resource(search_type='found') -> dict:
    if search_type == 'found':
        request = GetSingleResource('unknown/')
        request.send_request_with_selected_resource_id(request, resource_id=2)
    elif search_type == 'not found':
        request = GetSingleResource('unknown/')
        request.send_request_with_selected_resource_id(request, resource_id=23)
    return request.get_response()


@allure.step('Get request URL')
def get_request_url_for_ui_single_resource(search_type='found') -> str:
    if search_type == 'found':
        request = GetSingleResource('unknown/')
        request.send_request_with_selected_resource_id(request, resource_id=2)
    elif search_type == 'not found':
        request = GetSingleResource('unknown/')
        request.send_request_with_selected_resource_id(request, resource_id=23)
    return '/api/' + request.method_api


@allure.step('Get request URL single user not found')
def get_request_url_for_ui_single_resource_not_found() -> str:
    request = GetSingleResource('unknown/')
    request.send_request_with_selected_resource_id(request, resource_id=23)
    return '/api/' + request.method_api


@allure.suite('GetListUsers API method')
@pytest.mark.getlistusers
class TestGetSingleResource:
    total_number_of_resources = get_total_resources_list_resource()

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        global request
        request = GetSingleResource('unknown/')

    @allure.title('Test should_return_status_code_200.')
    @pytest.mark.parametrize('resource_id', range(1, total_number_of_resources + 1))
    def test_get_single_user_should_return_correct_user_id(self, resource_id: int):
        request.send_request_with_selected_resource_id(request, resource_id)
        request.should_be_correct_resource_id(resource_id)

    @allure.title('No data for resource out of number.')
    @pytest.mark.parametrize('resource_id', range(total_number_of_resources + 1, total_number_of_resources + 3))
    def test_get_single_user_should_not_return_data_for_users_out_of_available_ids(self, resource_id: int):
        request.send_request_with_selected_resource_id(request, resource_id)
        request.should_not_be_data_with_id()

    @allure.title('No data for resource out of number of resources. Negative numbers.')
    @pytest.mark.parametrize('resource_id', range(-2, 0))
    def test_get_single_user_should_not_return_data_for_users_with_negative_ids(self, resource_id: int):
        request.send_request_with_selected_resource_id(request, resource_id)
        request.should_not_be_data_with_id()

    @allure.title('Test should_return_status_code_404 when resource not found.')
    @pytest.mark.parametrize('resource_id', range(-2, 0))
    def test_get_single_user_should_return_status_code_404(self, resource_id: int):
        request.send_request_with_selected_resource_id(request, resource_id)
        request.should_be_status_code_404()
