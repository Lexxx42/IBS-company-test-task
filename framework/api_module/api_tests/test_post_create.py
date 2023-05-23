"""
API tests for SingleResource method.
"""
import json
import pytest
import allure
from ..api_requests import PostCreate
from ..api_tests import generated_person


@allure.step('Get response body for ui test')
def get_received_response_body_for_ui_single_resource(search_type='found') -> dict:
    return request.get_response()


@allure.step('Get request URL')
def get_request_url_for_ui_single_resource() -> str:
    return '/api/' + request.method_api


@allure.step('Get request URL single user not found')
def get_request_url_for_ui_single_resource_not_found() -> str:
    return '/api/' + request.method_api


@allure.suite('PostCreate API method')
class TestPostCreate:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        global request
        person = next(generated_person())
        request = PostCreate('users', name='', job='')

    @allure.title('Test should_return_status_code_200.')
    @pytest.mark.parametrize('name, job', [('vasia', 'lesnik')] * 2)
    def test_post_create_should_return_status_code_201(self, name, job):
        # request.send_request_with_name_and_job(request, )
        #request.params['name'] = name
        #request.params['job'] = job
        #request.send()
        # request.should_be_status_code_201()

        print(request.response.json())
