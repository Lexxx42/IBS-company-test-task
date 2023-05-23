from ..api_expected_results import BaseRequestResultsExpected as ebr


class BaseRequest:
    def __init__(self, method_api, url='https://reqres.in/api/', **kwargs):
        self.method_api = method_api
        self.url = url
        self.response = None
        self.params = {key: value for key, value in kwargs.items()}

    def should_be_status_code_200(self):
        assert self.response.status_code == ebr.STATUS_CODE, \
            f'Response status code with method {self.method_api} should be {ebr.STATUS_CODE},' \
            f'\n but got {self.response.status_code}'

    def should_be_status_code_404(self):
        assert self.response.status_code == ebr.STATUS_CODE_NOT_FOUND, \
            f'Response status code with method {self.method_api} ' \
            f'\nshould be {ebr.STATUS_CODE_NOT_FOUND},' \
            f' \nbut got {self.response.status_code}'

    def should_be_result_of_request_in_response(self):
        assert self.is_result_of_request_in_response() is True, \
            'Should be result of request but got nothing'

    def is_result_of_request_in_response(self):
        try:
            self.response.json()
        except KeyError:
            return False
        return True
