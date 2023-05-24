"""
API tests for DeleteDelete method.
"""

import pytest
import allure
from ..api_requests import DeleteDelete


@allure.step('Get response body for ui test')
def get_received_response_body_for_ui_delete_delete() -> dict:
    request = DeleteDelete('users/')
    request.send_request_with_selected_user_id(request, user_id=2)
    return request.get_response()


@allure.step('Get request URL')
def get_request_url_for_ui_delete_delete() -> str:
    request = DeleteDelete('users/')
    request.send_request_with_selected_user_id(request, user_id=2)
    return '/api/' + request.method_api


@allure.suite('Delete API method')
class TestDeleteDeleteMethod:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        global request
        request = DeleteDelete('users/')

    @allure.title('Test should_return_status_code_204.')
    @pytest.mark.parametrize('user_id', range(1, 11))
    def test_delete_delete_should_return_status_code_204(self, user_id: int):
        request.send_request_with_selected_user_id(request, user_id)
        request.should_be_status_code_204()

    @allure.title('Test response should return empty result.')
    @pytest.mark.parametrize('user_id', range(1, 11))
    def test_delete_delete_should_not_return_json_object(self, user_id: int):
        request.send_request_with_selected_user_id(request, user_id)
        is_contain_json = request.is_contain_json()
        assert is_contain_json is False, \
            'Expected response to not contain json object.' \
            f'\n Got {is_contain_json=}'
