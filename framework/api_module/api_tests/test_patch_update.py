"""
API tests for PatchUpdate method.
"""
import pytest
import allure
from ..api_requests import PatchUpdate
from .. import generated_person


@allure.step('Get response body for ui test')
def get_received_response_body_for_ui_patch_update(name_to_send, job_to_send, user_id=2) -> dict:
    request = PatchUpdate('users/', name='', job='')
    request.send_request_with_name_job_and_id(request, name_to_send, job_to_send, user_id)
    return request.get_response()


@allure.step('Get request URL')
def get_request_url_for_ui_patch_update(user_id=2) -> str:
    request = PatchUpdate('users/', name='', job='')
    request.send_request_with_name_job_and_id(
        request, name_to_send='morpheus', job_to_send='zion resident', user_id=user_id)
    return '/api/' + request.method_api


@allure.suite('PutUpdate API method')
class TestPutUpdate:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        global request
        request = PatchUpdate('users/', name='', job='')

    @allure.title('Test should_return_status_code_200.')
    @pytest.mark.parametrize('user_id', range(1, 6))
    @pytest.mark.parametrize('name_to_send, job_to_send', [('', '')] * 2)
    def test_patch_update_should_return_status_code_201(self, name_to_send, job_to_send, user_id):
        person = next(generated_person())
        name_to_send = person.name
        job_to_send = person.job
        request.send_request_with_name_job_and_id(request, name_to_send, job_to_send, user_id)
        request.should_be_status_code_200()

    @allure.title('Test sent data must be in response.')
    @pytest.mark.parametrize('user_id', range(1, 6))
    @pytest.mark.parametrize('name_to_send, job_to_send', [('', '')] * 2)
    def test_patch_update_sent_data_must_be_in_response(self, name_to_send, job_to_send, user_id):
        person = next(generated_person())
        name_to_send = person.name
        job_to_send = person.job
        sent_name, sent_job = \
            request.send_request_with_name_job_and_id(request, name_to_send, job_to_send, user_id)
        request.check_job_and_name_in_response(sent_name, sent_job)

    @allure.title('Test response must have all data.')
    @pytest.mark.parametrize('user_id', range(1, 6))
    @pytest.mark.parametrize('name_to_send, job_to_send', [('', '')] * 2)
    def test_patch_update_have_all_data_in_response(self, name_to_send, job_to_send, user_id):
        person = next(generated_person())
        name_to_send = person.name
        job_to_send = person.job
        request.send_request_with_name_job_and_id(request, name_to_send, job_to_send, user_id)
        request.check_data_in_response()

    @allure.title('Test response must have all data.')
    @pytest.mark.parametrize('user_id', range(1, 2))
    @pytest.mark.parametrize('job_to_send', [''] * 2)
    def test_patch_update_returns_400_when_no_name_provided(self, job_to_send, user_id):
        person = next(generated_person())
        job_to_send = person.job
        request.send_request_without_name(job_to_send, user_id)
        request.should_be_status_code_400()
