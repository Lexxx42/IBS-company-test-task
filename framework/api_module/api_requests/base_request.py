import allure
from ..api_expected_results import BaseRequestResultsExpected as ebr


class BaseRequest:
    def __init__(self, method_api, url='https://reqres.in/api/', **kwargs):
        self.method_api = method_api
        self.url = url
        self.response = None
        self.params = {key: value for key, value in kwargs.items()}

    @allure.step('Get requests response.')
    def get_response(self) -> dict:
        response = self.response.json()
        return response

    @allure.step('Check status code 200.')
    def should_be_status_code_200(self):
        assert self.response.status_code == ebr.STATUS_CODE, \
            f'Response status code with method {self.method_api} should be {ebr.STATUS_CODE},' \
            f'\n but got {self.response.status_code}'

    @allure.step('Check status code 201.')
    def should_be_status_code_201(self):
        assert self.response.status_code == ebr.STATUS_CODE_CREATED, \
            f'Response status code with method {self.method_api} should be {ebr.STATUS_CODE_CREATED},' \
            f'\n but got {self.response.status_code}'

    @allure.step('Check status code 404.')
    def should_be_status_code_404(self):
        assert self.response.status_code == ebr.STATUS_CODE_NOT_FOUND, \
            f'Response status code with method {self.method_api} ' \
            f'\nshould be {ebr.STATUS_CODE_NOT_FOUND},' \
            f' \nbut got {self.response.status_code}'

    @allure.step('Check status code 400.')
    def should_be_status_code_400(self):
        assert self.response.status_code == ebr.STATUS_CODE_MISSING, \
            f'Response status code with method {self.method_api} ' \
            f'\nshould be {ebr.STATUS_CODE_MISSING},' \
            f' \nbut got {self.response.status_code}'

    @allure.step('Check result of request.')
    def should_be_result_of_request_in_response(self):
        assert self.is_result_of_request_in_response() is True, \
            'Should be result of request but got nothing'

    @allure.step('Check if response can be a dict.')
    def is_result_of_request_in_response(self):
        try:
            self.response.json()
        except KeyError:
            return False
        return True
