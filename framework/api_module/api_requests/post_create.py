import json
import allure
from .base_request_post import BaseRequestPost


class PostCreate(BaseRequestPost):

    @allure.step('Send request with user\'s name and job.')
    def send_request_with_name_and_job(self, request, name: str, job: str) -> None:
        request.method_api = self.method_api
        request.send()

    @allure.step('Get requests response.')
    def get_response(self) -> dict:
        response = self.response.json()
        return response

    @allure.step('Check id user id in response.')
    def should_be_correct_user_id(self, user_id_request: int) -> None:
        user_id_response = self.response.json()['data']['id']
        assert user_id_request == user_id_response, \
            f'User id in request: {user_id_request},\n' \
            f' should be equal to user id in response: {user_id_response}'

    @allure.step('Check data with incorrect user id.')
    def should_not_be_data_with_id(self) -> None:
        data = self.response.json()
        number_of_data_items = len(data.items())
        assert number_of_data_items == 0, \
            f'Should be no data. But got: {data}'
