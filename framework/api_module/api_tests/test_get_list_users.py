"""
API tests for GetListUsers method.
"""

import pytest
import allure
from ..api_requests import GetListUsers


@allure.suite('GetListUsers API method')
@pytest.mark.getlistusers
class TestGetListUsersMethod:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        global request
        request = GetListUsers('users?page=')

    @allure.title('Test should_return_status_code_200.')
    @pytest.mark.parametrize('page', range(1, 13))
    def test_get_list_users_should_return_status_code_200(self, page):
        request.send_request_with_selected_page(request, page)
        request.should_be_status_code_200()

    @allure.title('Test should_return_response.')
    @pytest.mark.parametrize('page', range(1, 13))
    def test_get_list_users_should_return_response(self, page):
        request.send_request_with_selected_page(request, page)
        request.should_be_result_of_request_in_response()

    @allure.title('Test should_return_correct_page_number.')
    @pytest.mark.parametrize('page', range(1, 4))
    def test_get_list_users_should_return_correct_page_number(self, page):
        request.send_request_with_selected_page(request, page)
        request.should_be_correct_number_of_current_page(page)

    @allure.title('Test first_page_got_6_items_as_default.')
    @pytest.mark.parametrize('page', range(1, 2))
    def test_get_list_users_first_page_got_6_items_as_default(self, page):
        request.send_request_with_selected_page(request, page)
        request.should_be_six_users_in_list()

    @allure.title('Test returns_empty_data_if_out_of_pages.')
    def test_get_list_users_returns_empty_data_if_out_of_pages(self):
        request.should_be_no_data_if_out_of_page_number(request)

    @allure.title('Test returns_total_number_of_users.')
    def test_get_list_users_total_number_of_users(self):
        request.should_be_correct_number_of_users(request)

    @allure.title('Test all_users_have_ids.')
    def test_get_list_users_all_users_have_ids(self):
        request.should_be_ids_for_all_users(request)

    @allure.title('Test all_users_have_emails.')
    def test_get_list_users_all_users_have_emails(self):
        request.should_be_emails_for_all_users(request)

    @allure.title('Test all_users_have_first_name.')
    def test_get_list_users_all_users_have_first_name(self):
        request.should_be_first_name_for_all_users(request)

    @allure.title('Test all_users_have_last_name.')
    def test_get_list_users_all_users_have_last_name(self):
        request.should_be_last_name_for_all_users(request)

    @allure.title('Test all_users_have_avatar.')
    def test_get_list_users_all_users_have_avatar(self):
        request.should_be_avatar_for_all_users(request)

    @allure.title('Test should_return_correct_support_url.')
    @pytest.mark.parametrize('page', range(1, 2))
    def test_get_list_users_should_return_correct_support_url(self, page):
        request.send_request_with_selected_page(request, page)
        request.should_be_correct_support_url()

    @allure.title('Test should_return_correct_support_text.')
    @pytest.mark.parametrize('page', range(1, 2))
    def test_get_list_users_should_return_correct_support_text(self, page):
        request.send_request_with_selected_page(request, page)
        request.should_be_correct_support_text()