import json
import allure
from .base_request_get import BaseRequestGet


class GetListResource(BaseRequestGet):

    @allure.step('Send request with selected user id.')
    def send_request_list_resource(self, request) -> None:
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

    @allure.step('Check number of resources from request in list.')
    def should_be_six_resources(self):
        per_page = self.response.json()['per_page']
        number_of_resources = len(self.response.json()['data'])
        assert per_page == number_of_resources, \
            f'Expected {number_of_resources=} to be equal to ' \
            f'\nper page number of resources: {per_page}'

    @allure.step('Check number of total pages.')
    def should_be_correct_number_of_total_pages(self):
        total_resources = self.get_total_number_of_resources()
        per_page = self.response.json()['per_page']
        total_pages = self.get_total_number_of_pages()
        expected_total_pages = int(total_resources) / int(per_page)
        assert int(total_pages) == int(expected_total_pages), \
            f'Expected {expected_total_pages=} to be ' \
            f'\n equal to {total_pages}'
