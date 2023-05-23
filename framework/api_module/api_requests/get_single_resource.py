import json
import allure
from .base_request_get import BaseRequestGet


class GetSingleResource(BaseRequestGet):

    @allure.step('Send request with selected resource id.')
    def send_request_with_selected_resource_id(self, request, resource_id: int) -> None:
        request.method_api = self.method_api + str(resource_id)
        request.send()

    @allure.step('Get requests response.')
    def get_response(self) -> dict:
        response = self.response.json()
        return response

    @allure.step('Get total number of users from request.')
    def get_total_number_of_resources(self) -> int:
        total_number_of_resources = self.response.json()['total']
        return total_number_of_resources

    @allure.step('Get total number of pages from request.')
    def get_total_number_of_pages(self) -> int:
        total_pages_with_data = self.response.json()['total_pages']
        return total_pages_with_data

    @allure.step('Check resource id in response.')
    def should_be_correct_resource_id(self, resource_id_request: int) -> None:
        resource_id_response = self.response.json()['data']['id']
        assert resource_id_request == resource_id_response, \
            f'Id in request: {resource_id_request=},\n' \
            f' should be equal to: {resource_id_response=}'
