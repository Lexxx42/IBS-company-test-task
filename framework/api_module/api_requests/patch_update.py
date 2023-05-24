import allure
from .base_request_patch import BaseRequestPatch


class PatchUpdate(BaseRequestPatch):

    @allure.step('Send request with user\'s name and job.')
    def send_request_with_name_job_and_id(
            self, request, name_to_send='morpheus', job_to_send='zion resident', user_id='') -> tuple[str, str]:
        request.method_api = self.method_api + str(user_id)
        request.params['name'] = name_to_send
        request.params['job'] = job_to_send
        request.send()
        return name_to_send, job_to_send

    @allure.step('Send PutUpdate without user id.')
    def send_request_without_name(self, job_to_send, user_id=''):
        request = PatchUpdate('users/', job='')
        request.method_api = self.method_api + str(user_id)
        request.params['job'] = job_to_send
        request.send()

    @allure.step('Check response to have sent name and job.')
    def check_job_and_name_in_response(self, sent_name, sent_job):
        response = self.get_response()
        assert response['name'] == sent_name, \
            f'Expected response to have {sent_name=}.' \
            f'\n Got: {response["name"]}'
        assert response['job'] == sent_job, \
            f'Expected response to have {sent_job=}.' \
            f'\n Got: {response["job"]}'

    @allure.step('Check response to have all data.')
    def check_data_in_response(self):
        response = self.get_response()
        assert response['name'] is not None, \
            'Expected response to have name data.' \
            '\n Got nothing.'
        assert response['job'] is not None, \
            'Expected response to have job data.' \
            '\n Got nothing.'
        assert response['updatedAt'] is not None, \
            'Expected response to have updatedAt data.' \
            '\n Got nothing.'
