import json
import allure
from .base_request_get import BaseRequestGet
from ..api_expected_results import GetListUsersExpected, BaseRequestResultsExpected


class GetListUsers(BaseRequestGet):

    @allure.step('Send request with chosen page number.')
    def send_request_with_selected_page(self, request, page: int) -> None:
        separator = self.method_api.find('=')
        self.method_api = self.method_api[:separator + 1]
        request.method_api = self.method_api + str(page)
        request.send()

    @allure.step('Get requests response.')
    def get_response(self) -> dict:
        response = self.response.json()
        return response

    @allure.step('Get total number of users from request.')
    def get_total_number_of_users(self) -> int:
        total_number_of_users = self.response.json()['total']
        return total_number_of_users

    @allure.step('Get total number of pages from request.')
    def get_total_number_of_pages(self) -> int:
        total_pages_with_data = self.response.json()['total_pages']
        return total_pages_with_data

    @allure.step('Get support url from request.')
    def get_support_url(self) -> str:
        support_url = self.response.json()['support']['url']
        return support_url

    @allure.step('Get support text from request.')
    def get_support_text(self) -> str:
        support_text = self.response.json()['support']['text']
        return support_text

    @allure.step('Check number of page in request.')
    def should_be_correct_number_of_current_page(self, page_sent_to_request: int) -> None:
        page_in_request_body = self.response.json()['page']
        assert page_in_request_body == page_sent_to_request, \
            f'Page number in response should be {page_sent_to_request},\n' \
            f' but got {page_in_request_body}'

    @allure.step('Check number of users in request.')
    def should_be_six_users_in_list(self) -> None:
        per_page_default = GetListUsersExpected.PER_PAGE
        per_page_actual = self.response.json()['per_page']
        assert per_page_default == per_page_actual, \
            f'Expected {per_page_default=} to be equal to {per_page_actual=}'
        number_of_users = len(self.response.json()['data'])
        assert per_page_default == number_of_users, \
            f'Expected {per_page_default=} to be equal to ' \
            f'\nactual number of users represented: {number_of_users}'

    @allure.step('Check data absens.')
    def should_be_no_data_if_out_of_page_number(self, request) -> None:
        self.send_request_with_selected_page(request, page=1)
        total_pages_with_data = self.get_total_number_of_pages()
        self.send_request_with_selected_page(request, page=total_pages_with_data + 1)
        data_content = self.response.json()['data']
        assert len(data_content) == 0, \
            f'Expected no data at page {total_pages_with_data + 1}.\n' \
            f'But got {data_content=}'

    @allure.step('Check total number of users.')
    def should_be_correct_number_of_users(self, request) -> None:
        self.send_request_with_selected_page(request, page=1)
        total_number_of_users = self.get_total_number_of_users()
        total_pages_with_data = self.get_total_number_of_pages()
        number_of_users_data = 0
        for i in range(total_pages_with_data):
            self.send_request_with_selected_page(request, page=i + 1)
            number_of_users_data += len(self.response.json()['data'])
        assert total_number_of_users == number_of_users_data, \
            f'Expected number of users {total_number_of_users} to' \
            f'\nbe equal to {number_of_users_data=} in response.'

    @allure.step('Check id for all users.')
    def should_be_ids_for_all_users(self, request) -> None:
        self.send_request_with_selected_page(request, page=1)
        total_number_of_users = self.get_total_number_of_users()
        total_pages_with_data = self.get_total_number_of_pages()
        users_with_email, report = self.check_users_to_have_email(request, total_pages_with_data)
        assert total_number_of_users == users_with_email, \
            f'Expected all users= {total_number_of_users} to have email\'s.\n' \
            f'Got {users_with_email}.\n' \
            f'Report: {report}'

    @allure.step('Check email for all users.')
    def should_be_emails_for_all_users(self, request) -> None:
        self.send_request_with_selected_page(request, page=1)
        total_number_of_users = self.get_total_number_of_users()
        total_pages_with_data = self.get_total_number_of_pages()
        users_with_id, report = self.check_users_to_have_ids(request, total_pages_with_data)
        assert total_number_of_users == users_with_id, \
            f'Expected all users= {total_number_of_users} to have id\'s.\n' \
            f'Got {users_with_id}.\n' \
            f'Report: {report}'

    @allure.step('Check first_name for all users.')
    def should_be_first_name_for_all_users(self, request) -> None:
        self.send_request_with_selected_page(request, page=1)
        total_number_of_users = self.get_total_number_of_users()
        total_pages_with_data = self.get_total_number_of_pages()
        users_with_first_name, report = self.check_users_to_have_first_name(request, total_pages_with_data)
        assert total_number_of_users == users_with_first_name, \
            f'Expected all users= {total_number_of_users} to have first name\'s.\n' \
            f'Got {users_with_first_name}.\n' \
            f'Report: {report}'

    @allure.step('Check last_name for all users.')
    def should_be_last_name_for_all_users(self, request) -> None:
        self.send_request_with_selected_page(request, page=1)
        total_number_of_users = self.get_total_number_of_users()
        total_pages_with_data = self.get_total_number_of_pages()
        users_with_last_name, report = self.check_users_to_have_last_name(request, total_pages_with_data)
        assert total_number_of_users == users_with_last_name, \
            f'Expected all users= {total_number_of_users} to have last name\'s.\n' \
            f'Got {users_with_last_name}.\n' \
            f'Report: {report}'

    @allure.step('Check avatar for all users.')
    def should_be_avatar_for_all_users(self, request) -> None:
        self.send_request_with_selected_page(request, page=1)
        total_number_of_users = self.get_total_number_of_users()
        total_pages_with_data = self.get_total_number_of_pages()
        users_with_avatar, report = self.check_users_to_have_avatar(request, total_pages_with_data)
        assert total_number_of_users == users_with_avatar, \
            f'Expected all users= {total_number_of_users} to have avatar\'s.\n' \
            f'Got {users_with_avatar}.\n' \
            f'Report: {report}'

    @allure.step('Check users on page to have id.')
    def check_users_to_have_ids(self, request, total_pages: int) -> tuple[int, str]:
        users_with_id = 0
        report = ''
        for i in range(total_pages):
            self.send_request_with_selected_page(request, page=i + 1)
            for user in self.response.json()['data']:
                try:
                    user['id']
                    users_with_id += 1
                except KeyError:
                    report += f'No id for {user=}\n'
                    break
        return users_with_id, report

    @allure.step('Check users on page to have email.')
    def check_users_to_have_email(self, request, total_pages: int) -> tuple[int, str]:
        users_with_email = 0
        report = ''
        for i in range(total_pages):
            self.send_request_with_selected_page(request, page=i + 1)
            for user in self.response.json()['data']:
                try:
                    user['email']
                    users_with_email += 1
                except KeyError:
                    report += f'No email for {user=}\n'
                    break
        return users_with_email, report

    @allure.step('Check users on page to have first_name.')
    def check_users_to_have_first_name(self, request, total_pages: int) -> tuple[int, str]:
        users_with_first_name = 0
        report = ''
        for i in range(total_pages):
            self.send_request_with_selected_page(request, page=i + 1)
            for user in self.response.json()['data']:
                try:
                    user['first_name']
                    users_with_first_name += 1
                except KeyError:
                    report += f'No first_name for {user=}\n'
                    break
        return users_with_first_name, report

    @allure.step('Check users on page to have last_name.')
    def check_users_to_have_last_name(self, request, total_pages: int) -> tuple[int, str]:
        users_with_last_name = 0
        report = ''
        for i in range(total_pages):
            self.send_request_with_selected_page(request, page=i + 1)
            for user in self.response.json()['data']:
                try:
                    user['last_name']
                    users_with_last_name += 1
                except KeyError:
                    report += f'No last_name for {user=}\n'
                    break
        return users_with_last_name, report

    @allure.step('Check users on page to have avatar.')
    def check_users_to_have_avatar(self, request, total_pages: int) -> tuple[int, str]:
        users_with_avatar = 0
        report = ''
        for i in range(total_pages):
            self.send_request_with_selected_page(request, page=i + 1)
            for user in self.response.json()['data']:
                try:
                    user['avatar']
                    users_with_avatar += 1
                except KeyError:
                    report += f'No avatar for {user=}\n'
                    break
        return users_with_avatar, report

    @allure.step('Check support_url in response.')
    def should_be_correct_support_url(self) -> None:
        expected_support_url = BaseRequestResultsExpected.SUPPORT_URL
        actual_support_url = self.get_support_url()
        assert expected_support_url == actual_support_url, \
            f'Expected {expected_support_url=} to be equal to {actual_support_url}'

    @allure.step('Check support_text in response.')
    def should_be_correct_support_text(self) -> None:
        expected_support_text = BaseRequestResultsExpected.SUPPORT_TEXT
        actual_support_text = self.get_support_text()
        assert expected_support_text == actual_support_text, \
            f'Expected {expected_support_text=} to be equal to {actual_support_text}'
