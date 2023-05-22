'''
API tests for getMe method
\nCommand to start getMe tests: pytest . -m getme
'''

import pytest
from ..api_requests import GetListUsers


@pytest.mark.getme
class TestGetListUsersMethod:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        global request
        request = GetListUsers('users?')
        request.send()

    @pytest.mark.parametrize('page', range(1, 13))
    def test_get_list_users_request_should_return_status_code_200(self, page):
        request.method_api = request.method_api + 'page=' + str(page)
        print(request.method_api)
        request.should_be_status_code_200()
