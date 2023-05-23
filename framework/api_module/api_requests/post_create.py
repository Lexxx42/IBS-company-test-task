import json
import allure
from .base_request_post import BaseRequestPost


class PostCreate(BaseRequestPost):

    @allure.step('Send request with user\'s name and job.')
    def send_request_with_name_and_job(self, request, name_to_send, job_to_send) -> tuple[str, str]:
        request.params['name'] = name_to_send
        request.params['job'] = job_to_send
        request.send()
        return name_to_send, job_to_send

    @allure.step('Get requests response.')
    def get_response(self) -> dict:
        response = self.response.json()
        return response

    @allure.step('Check response to have sent name and job.')
    def check_job_and_name_in_response(self, sent_name, sent_job):
        response = self.get_response()
        assert response['name'] == sent_name, \
            f'Expected response to have {sent_name=}.' \
            f'\n Got: {response["name"]}'
        assert response['job'] == sent_job, \
            f'Expected response to have {sent_job=}.' \
            f'\n Got: {response["job"]}'
