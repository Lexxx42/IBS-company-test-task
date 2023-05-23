"""
API tests for SingleResource method.
"""
import json
import pytest
import allure
from ..api_requests import PostCreate
from .. import generated_person


@allure.step('Get response body for ui test')
def get_received_response_body_for_ui_post_create(name_to_send, job_to_send) -> dict:
    request = PostCreate('users', name='', job='')
    request.send_request_with_name_and_job(request, name_to_send, job_to_send)
    return request.get_response()


@allure.step('Get request URL')
def get_request_url_for_ui_post_create() -> str:
    request = PostCreate('users', name='', job='')
    person = next(generated_person())
    name_to_send = person.name
    job_to_send = person.job
    request.send_request_with_name_and_job(request, name_to_send, job_to_send)
    return '/api/' + request.method_api


@allure.suite('PostCreate API method')
class TestPostCreate:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        global request
        request = PostCreate('users', name='', job='')

    @allure.title('Test should_return_status_code_200.')
    @pytest.mark.parametrize('name, job', [('', '')] * 2)
    def test_post_create_should_return_status_code_201(self, name, job):
        person = next(generated_person())
        name_to_send = person.name
        job_to_send = person.job
        request.send_request_with_name_and_job(request, name_to_send, job_to_send)
        request.should_be_status_code_201()

    @allure.title('Test sent data must be in response.')
    @pytest.mark.parametrize('name, job', [('', '')] * 2)
    def test_post_create_should_return_status_code_201(self, name, job):
        person = next(generated_person())
        name_to_send = person.name
        job_to_send = person.job
        sent_name, sent_job = \
            request.send_request_with_name_and_job(request, name_to_send, job_to_send)
        request.check_job_and_name_in_response(sent_name, sent_job)
