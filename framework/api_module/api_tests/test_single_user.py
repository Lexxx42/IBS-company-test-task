"""
API tests for GetSingleUser method.
"""

import pytest
import allure
from ..api_requests import GetSingleUser
from .test_get_list_users import get_total_users


@allure.step('Get response body for ui test')
def get_received_response_body_for_ui_single_user(search_type='found') -> dict:
    if search_type == 'found':
        request = GetSingleUser('users/')
        request.send_request_with_selected_user_id(request, user_id=2)
    elif search_type == 'not found':
        request = GetSingleUser('users/')
        request.send_request_with_selected_user_id(request, user_id=23)
    return request.get_response()


@allure.step('Get request URL')
def get_request_url_for_ui_single_user() -> str:
    request = GetSingleUser('users/')
    request.send_request_with_selected_user_id(request, user_id=2)
    return '/api/' + request.method_api


@allure.step('Get request URL single user not found')
def get_request_url_for_ui_single_user_not_found() -> str:
    request = GetSingleUser('users/')
    request.send_request_with_selected_user_id(request, user_id=23)
    return '/api/' + request.method_api


@allure.suite('SingleUser API method')
class TestGetSingleUserMethod:
    total_number_of_users = get_total_users()

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        global request
        request = GetSingleUser('users/')

    @allure.title('Test should_return_status_code_200.')
    @pytest.mark.parametrize('user_id', range(1, total_number_of_users + 1))
    def test_get_single_user_should_return_status_code_200(self, user_id: int):
        request.send_request_with_selected_user_id(request, user_id)
        request.should_be_status_code_200()

    @allure.title('Test should_return_status_code_200.')
    @pytest.mark.parametrize('user_id', range(1, total_number_of_users + 1))
    def test_get_single_user_should_return_correct_user_id(self, user_id: int):
        request.send_request_with_selected_user_id(request, user_id)
        request.should_be_correct_user_id(user_id)

    @allure.title('No data for users out of number of users.')
    @pytest.mark.parametrize('user_id', range(total_number_of_users + 1, total_number_of_users + 3))
    def test_get_single_user_should_not_return_data_for_users_out_of_available_ids(self, user_id: int):
        request.send_request_with_selected_user_id(request, user_id)
        request.should_not_be_data_with_id()

    @allure.title('No data for users out of number of users. Negative numbers.')
    @pytest.mark.parametrize('user_id', range(-2, 0))
    def test_get_single_user_should_not_return_data_for_users_with_negative_ids(self, user_id: int):
        request.send_request_with_selected_user_id(request, user_id)
        request.should_not_be_data_with_id()

    @allure.title('Test should_return_status_code_404 when user not found.')
    @pytest.mark.parametrize('user_id', range(-2, 0))
    def test_get_single_user_should_return_status_code_404(self, user_id: int):
        request.send_request_with_selected_user_id(request, user_id)
        request.should_be_status_code_404()
